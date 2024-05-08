import pytz
import logging
from flask import Flask, jsonify, request
from datetime import datetime

from helpers.logging import timed_rotating_log_helper
from helpers.parameters import process_parameters
from helpers.responder import json_message

timed_rotating_log_helper("./logs/time_localiser.log")
logging.info("Started Flask Timezone Localiser by Marc Falconer.")

app = Flask(__name__)

# Main entry point
@app.route('/', methods=['GET'])
def convet_time():
    # Check parameters are ok.
    processed_parameters = process_parameters(
        request.args,
        required=["datetime", "from_tz", "to_tz"],
        optional=["datetime_format"]
    )
    if not processed_parameters.ok:
        logging.error(" Bailing due to parameters.")
        return json_message(processed_parameters.errors, 422)

    # Next step we need to check if the timezone exists.  Bail if they fail.
    timezones = {
        "from_tz": processed_parameters.values.from_tz,
        "to_tz": processed_parameters.values.to_tz
    }
    failed_timezones = [
        {tz_key: tv_value} for tz_key, tv_value in timezones.items()
        if tv_value not in pytz.all_timezones
    ]
    if failed_timezones:
        failed_timezones_msg = {"Invalid timezone(s)": failed_timezones}
        logging.error(failed_timezones_msg)
        return json_message(failed_timezones_msg, 422)
    
    # Look for the format else fail back.
    datetime_format = getattr(
        processed_parameters.values, "datetime_format", "%Y-%m-%d %H:%M:%S"
    )
    logging.info(f"  Datetime format set: {datetime_format}")
    
    try:
        from_datetime_obj = datetime.strptime(
            processed_parameters.values.datetime, datetime_format
        )
        logging.info(f"  From datetime object created: {from_datetime_obj}")
    except ValueError:
        logging.error(f"  Datetime format invalid: {datetime_format}")
        return json_message({"Invalid datetime format": datetime_format}, 422)
    
    # Now we do the conversion
    from_pytz = pytz.timezone(timezones["from_tz"])
    to_pytz = pytz.timezone(timezones["to_tz"])
    
    to_datetime_obj = from_pytz.localize(from_datetime_obj).astimezone(to_pytz)
    converted_datetime = to_datetime_obj.strftime(datetime_format)
    
    logging.info(f"  To datetime object created: {converted_datetime}")
    return json_message(
        {
            "localised_datetime": converted_datetime,
            "datetime_format": datetime_format,
            **processed_parameters.dict
        }, 200
    )

# Get available timezones.
@app.route('/timezones', methods=['GET'])
def timezone_list():
    logging.info("Returning list of timezones.")
    return json_message(
        {
            "available_timezones": pytz.all_timezones,
            "total_number": len(pytz.all_timezones)
        }, 200
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

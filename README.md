# Flask Timezone Localiser

This Flask application provides a simple API for localising date and time to various timezones. Users can easily convert a date and time to a different timezone using this application.

## Usage
To use the API, send a GET request to the endpoint root with the following parameters:

### Required parameters:
-**datetime:** String format of the timestamp in the from_tz timezone. Example: '2024-05-08 15:30:00'
-**from_tz:** String name of the timezone the datetime parameter is from. Example: 'Pacific/Auckland'
-**to_tz:** String name of the timezone to localize the datetime to. Example: 'America/New_York'

### Optional parameters:
-**datetime_format:** String to specify the format of datetime. The returned value is also in this format. If not specified, the default format is '%Y-%m-%d %H:%M:%S'.

## Received list of available timezones:
To received list of available timezones, send a GET request to the endpoint *'/timezones'*

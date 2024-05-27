# Flask Timezone Localiser

This Flask application provides a simple API for localising date and time to various timezones. Users can easily convert a date and time to a different timezone using this application.

By default this Flask runs on port *5001*. You can also mount the log directory to your filesystem. The log path in the container is '/app/logs'.

## Docker Image

This repository is available as a docker image: [View on Docker Hub](https://hub.docker.com/repository/docker/marcfalconer/flask-timezone-localiser/general).

By default this Flask runs on port *5001*. You can also mount the log directory to your filesystem. The log path in the container is '/app/logs'.

```console
docker pull marcfalconer/flask-timezone-localiser
docker run -v /var/log/projects:/app/logs -p 5001:5001 marcfalconer/flask-timezone-localiser
```

## Test Server

You can check out this API using my test server at folloing url: [https://projects.falconerdigital.co.nz/localise_timezone](https://projects.falconerdigital.co.nz/localise_timezone) 


## Postman collection

Postman collection available: [Postman Collection](https://www.postman.com/interstellar-rocket-53991/workspace/projects/request/19905884-486361f4-a008-4bf5-b1bf-9f7a6ee62b59)

## API Usage

### Localise timezones:
To use the API, send a GET request to the endpoint root with the following parameters:

Try it out on the test setver the curl command below.
```console
curl -X GET "https://projects.falconerdigital.co.nz/localise_timezone?datetime=2024-05-08%2012:30:45&from_tz=Pacific/Auckland&to_tz=America/New_York"
```

#### Required parameters:
**datetime:** String format of the timestamp in the from_tz timezone. Example: '2024-05-08 15:30:00'\
**from_tz:** String name of the timezone the datetime parameter is from. Example: 'Pacific/Auckland'\
**to_tz:** String name of the timezone to localize the datetime to. Example: 'America/New_York'

#### Optional parameters:
**datetime_format:** String to specify the format of datetime. The returned value is also in this format. If not specified, the default format is '%Y-%m-%d %H:%M:%S'.

#### Response:
The API endpoint with response with a an appropriate status code. The body will includ a JSON message with the localised time or any validion errors encounted.

##### Successful Example:
```jsonc
{
    "data": {
        "converted_datetime": "2024-05-07 23:30:00",
        "datetime": "2024-05-08 15:30:00",
        "datetime_format": "%Y-%m-%d %H:%M:%S",
        "from_tz": "Pacific/Auckland",
        "to_tz": "America/New_York"
    },
    "error": false,
    "status_code": 200
}
```

##### Failed Vaildation  Example:
```jsonc
{
    "data": {
        "Missing required parameter(s)": [
            "datetime",
            "from_tz",
            "to_tz"
        ]
    },
    "error": true,
    "status_code": 422
}
```

### Received list of available timezones:
To received list of available timezones, send a GET request to the endpoint *'/timezones'*

Try it out on the test setver the curl command below.
```console
curl -X GET "https://projects.falconerdigital.co.nz/localise_timezone/timezones"
```

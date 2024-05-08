import logging
from flask import jsonify

def json_message(data, status, **kargs):
    if "error" in kargs:
        error = kargs["error"]
    elif 200 <= status <= 299:
        error = False
    else:
        error = True
    
    msg = jsonify(
            error=error,
            data=data,
            status_code=status
        ), status
    
    return msg
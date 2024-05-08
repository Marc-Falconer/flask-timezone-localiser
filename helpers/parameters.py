import logging

# Lets make this a class because it's going on GitHub.
class processed_parameters:
    def __init__(self, parameters, parameter_errors):
        self.values = type("parameters", (), parameters)
        self.dict = parameters
        self.errors = parameter_errors
        self.ok = True if not parameter_errors else False


def process_parameters(request_args, required=[], optional=[]):
    logging.info("  Processing parameters")
    all_pramas = required + optional
    unknown_pramas = []
    parameters = {}

    for key, value in request_args.items():
        parameters[key] = value
        if key in required:
            required.remove(key)
        if key not in all_pramas:
            unknown_pramas.append(key)

    error_dict = {}
    if required:
        error_dict["Missing required parameter(s)"] = required
        logging.warning("  Missing required parameter(s): " + " ".join(required))
    if unknown_pramas:
        error_dict["Unexpected parameter(s)"] = unknown_pramas
        logging.warning("  Unexpected parameter(s): " + " ".join(unknown_pramas))
    
    pp = processed_parameters(parameters, error_dict)
    logging.info(f"    OK: {pp.ok}")
    return pp
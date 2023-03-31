from flask_server.errors.errors import InvalidParameters


def validate_parameters(rules, params: dict):
    if params is None:
        raise InvalidParameters("Missing root object for rules: {}".format(rules))

    failed_rules = []
    for rule in rules:
        parts = rule.split(".")
        obj = params
        for p in parts:
            if p not in obj:
                failed_rules.append(rule)
                break
            obj = obj[p]

    if len(failed_rules) > 0:
        raise InvalidParameters("Missing params: " + ", ".join(failed_rules))

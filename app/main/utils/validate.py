class Validates: 
    def validate_response(validator, response):
        r = True
        for v in validator:
            if v not in response:
                r = False
        return r
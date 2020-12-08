class Response:
    def format_response(sts, msg, data = None):
        errs = ['500', '501', '502', '503', '504', '505', '506']
        response = {
                    "status": 400,
                    "message": msg,
                    "data": data
                }
        for e in errs:
            if e in sts:
                return response 

        if(sts is not '200'):
            response['status'] = int(sts)
        else:
            response["status"] = 200
            
        return response
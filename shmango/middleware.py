class ExtractIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
        if ip:
            request.ip = ip.split(", ")[0]
        else:
            request.ip = request.META.get("REMOTE_ADDR")
        
        return self.get_response(request)

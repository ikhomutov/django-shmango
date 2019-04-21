class BaseURLMiddleware:
    def process_request(self, request):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
        if ip:
            request.ip = ip.split(", ")[0]
        else:
            request.ip = request.META.get("REMOTE_ADDR")

from django.utils.deprecation import MiddlewareMixin
from django.http.multipartparser import MultiPartParser


class RestfulMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST':
            request.params = request.POST
        elif request.method != 'GET':
            params = MultiPartParser(request.META, request,
                                     request.upload_handlers).parse()
            request.params = params[0]

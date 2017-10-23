from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin
 

class NavigationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if (request.method == 'GET'):
            request.nxt = request.GET.get('next', '')

    def process_template_response(self, request, response):
        response.context_data['next'] = request.nxt
        return response

from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin
 

class NavigationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        req_next = request.GET.get('next', '')
        if req_next: 
            request.nxt = req_next

    def process_template_response(self, request, response):
            if hasattr(request, 'nxt'):
                response.context_data['next'] = request.nxt
            return response

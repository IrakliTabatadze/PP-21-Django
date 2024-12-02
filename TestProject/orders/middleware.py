from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)

class SimpleMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f'Start Processing Request: {request.path}')

        response = self.get_response(request)

        # print(response.content)

        logger.info(f'Finished Processing Request: {request.path}')

        return response

    def process_exception(self, request, exception):
        logger.error(f'Exception occurred while processing request: {request.path} - {exception}')

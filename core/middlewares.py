import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class RequestLogMiddleware(MiddlewareMixin):
    """
    middleware para LOGar todas as requisicoes.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"{request.method} {request.path}")
        response = self.get_response(request)
        return response

    def process_request(self, request):
        logger.info(
            f'{request.method} {request.path} - User: {request.user if request.user.is_authenticated else "Anonymous"}'
        )


class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error(f"Exception in request {request.path}: {exception}")

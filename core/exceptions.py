from rest_framework.exceptions import APIException


class ServiceUnavailabreException(APIException):
    status_code = 503
    default_detail = "Servvice temporaruly unavailable"
    default_code = "service_unavailable"


class ValidationException(APIException):
    status_code = 400
    default_detail = "Validation error"
    default_code = "validation_error"

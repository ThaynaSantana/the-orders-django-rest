from functools import wraps

from rest_framework import status
from rest_framework.response import Response


def validate_json(keys: list[str]):
    """
    decorator para garantir que o JSON tenha as chaves necessarias
    """

    def decorator(func):
        @wraps(func)
        def wrapped(self, request, *args, **kwargs):
            data = request.data
            missing = [k for k in keys if k not in data]
            if missing:
                return Response(
                    {"error": f"Campo faltando: {missing}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return func(self, request, *args, **kwargs)

        return wrapped

    return decorator

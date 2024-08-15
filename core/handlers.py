from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    if isinstance(exc, NotAuthenticated):
        return Response({"message": "인증에 실패했습니다."}, status=401)

    return exception_handler(exc, context)
from rest_framework.views import exception_handler
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import json


def error_checks(func):
    def inner(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
        except ObjectDoesNotExist:
            response = HttpResponse("Data not found in the database with the provided values")
            response.status_code = 450
        except Exception as e:
            response = exception_handler(e, context=func)

        if response is None:
            response = HttpResponse(json.dumps(
                "The required key or value has not been supplied. Refer example in documentation for the accepted key"
                "value pairs"))
            response.status_code = 412
        return response
    return inner

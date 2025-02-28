from functools import wraps

from django.http import HttpRequest
from django.shortcuts import render


def require_POST_params(POST_params: list[str]):

    def decorator(func):

        @wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            for POST_param in POST_params:
                if POST_param not in request.POST:
                    return render(request, 'scoreboard/bad_request.html', status=400)

            return func(request, *args, **kwargs)
        
        return wrapper
        
    return decorator

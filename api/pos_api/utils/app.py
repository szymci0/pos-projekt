import logging

from starlette.requests import Request
from starlette.responses import Response

log = logging.getLogger(__name__)

def get_token(headers):
    token = headers['Authorization']
    token = token.replace('Bearer', '')
    token = token.replace('JWT', '')
    return token


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        log.exception(e)
        return Response("Internal server error", status_code=500)


async def security_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Frame-Options"] = "deny"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1"
    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains"  # noqa
    return response


async def jwt_middleware(request: Request, call_next):
    if 'Authorization' not in request.headers or 'auth' in str(request.url.path):
        return await call_next(request)
    token = get_token(request.headers)
    from pos_api.models.blacklisted_tokens import BlacklistedTokens
    if BlacklistedTokens.objects(token=token).first():
        return Response("JWT Token Invalid", status_code=401)
    return await call_next(request)
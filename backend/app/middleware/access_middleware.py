#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from backend.app.common.log import log
from backend.app.utils.timezone import timezone_utils


class AccessMiddleware(BaseHTTPMiddleware):
    """记录请求日志中间件"""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = timezone_utils.get_timezone_datetime()
        response = await call_next(request)
        end_time = timezone_utils.get_timezone_datetime()
        log.info(f'{response.status_code} {request.client.host} {request.method} {request.url} {end_time - start_time}')
        return response

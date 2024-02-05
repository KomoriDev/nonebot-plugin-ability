import httpx
import nonebot

from httpx import Response
from httpx._types import (
    CookieTypes,
    HeaderTypes,
    ProxiesTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestFiles,
    TimeoutTypes,
    URLTypes,
    VerifyTypes,
)

from typing import Any, Literal

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from .utils import add_user_agent

config = nonebot.get_driver().config


class Requests:
    """
    httpx 异步请求封装
    """

    @classmethod
    async def get(
        cls,
        url: URLTypes,
        *,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> Response:
        """
        发起 GET 请求
        :param url: 请求地址
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 尝试时间，单位：秒
        :param verify: 是否显示 SSL 整数
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return: `httpx.Response` 对象
        """

        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            **kwargs,
        ) as client:
            return await client.get(
                url,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            )

    @classmethod
    async def post(
        cls,
        url: URLTypes,
        *,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        json: RequestContent | None = None,
        files: RequestFiles | None = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> Response:
        """
        发起 POST 请求。
        :param url: 请求地址
        :param content: 请求内容
        :param data: 请求数据
        :param json: 请求 JSON
        :param files: 请求文件
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 超时时间，单位: 秒
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return:`httpx.Response` 对象
        """
        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            **kwargs,
        ) as client:
            return await client.post(
                url,
                content=content,
                data=data,
                files=files,
                json=json,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            )

    @classmethod
    async def put(
        cls,
        url: URLTypes,
        *,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: Any = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> Response:
        """
        发起 PUT 请求。

        :param url: 请求地址
        :param content: 请求内容
        :param data: 请求数据
        :param files: 请求文件
        :param json: 请求 JSON
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 超时时间，单位: 秒
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return: `httpx.Response` 对象
        """
        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            **kwargs,
        ) as client:
            return await client.put(
                url,
                content=content,
                data=data,
                files=files,
                json=json,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            )

    @classmethod
    async def delete(
        cls,
        url: URLTypes,
        *,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> Response:
        """
        发起 DELETE 请求。

        :param url: 请求地址
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 超时时间，单位: 秒
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return: `httpx.Response` 对象
        """
        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            **kwargs,
        ) as client:
            return await client.delete(
                url,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            )

    @classmethod
    async def patch(
        cls,
        url: URLTypes,
        *,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: Any = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> Response:
        """
        发起 PATCH 请求。

        :param url: 请求地址
        :param content: 请求内容
        :param data: 请求数据
        :param files: 请求文件
        :param json: 请求 JSON
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 超时时间，单位: 秒
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return: `httpx.Response` 对象
        """
        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            **kwargs,
        ) as client:
            return await client.patch(
                url,
                content=content,
                data=data,
                files=files,
                json=json,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            )

    @classmethod
    async def head(
        cls,
        url: URLTypes,
        *,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> Response:
        """
        发起 HEAD 请求。

        :param url: 请求地址
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 超时时间，单位: 秒
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return: `httpx.Response` 对象
        """
        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            **kwargs,
        ) as client:
            return await client.head(
                url,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            )

    @classmethod
    async def options(
        cls,
        url: URLTypes,
        *,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> Response:
        """
        发起 OPTIONS 请求。

        :param url: 请求地址
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 超时时间，单位: 秒
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return: `httpx.Response` 对象
        """
        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            **kwargs,
        ) as client:
            return await client.options(
                url,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            )

    @classmethod
    async def request(
        cls,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
        url: URLTypes,
        *,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: Any = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> Response:
        """
        发起请求。

        :param method: 请求方法
        :param url: 请求地址
        :param content: 请求内容
        :param data: 请求数据
        :param files: 请求文件
        :param json: 请求 JSON
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 超时时间，单位: 秒
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return: `httpx.Response` 对象
        """
        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            **kwargs,
        ) as client:
            return await client.request(
                method,
                url,
                content=content,
                data=data,
                files=files,
                json=json,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            )

    @classmethod
    @asynccontextmanager
    async def stream(
        cls,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
        url: URLTypes,
        *,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: Any = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        follow_redirects: bool = True,
        timeout: TimeoutTypes | None = None,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        **kwargs,
    ) -> AsyncGenerator[Response, None]:
        """
        发起流式请求。

        :param method: 请求方法
        :param url: 请求地址
        :param content: 请求内容
        :param data: 请求数据
        :param files: 请求文件
        :param json: 请求 JSON
        :param params: 请求参数
        :param headers: 请求头
        :param cookies: 请求 Cookie
        :param follow_redirects: 是否跟随重定向
        :param timeout: 超时时间，单位: 秒
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 代理地址
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数

        :return: `httpx.Response` 对象
        """
        async with (
            httpx.AsyncClient(
                verify=verify,
                http2=http2,
                proxies=proxies or config.proxy_url,  # type: ignore
                **kwargs,
            ) as client,
            client.stream(
                method,
                url,
                content=content,
                data=data,
                files=files,
                json=json,
                params=params,
                headers=add_user_agent(headers),
                cookies=cookies,
                follow_redirects=follow_redirects,
                timeout=timeout if timeout is not None else config.http_timeout,
            ) as response,
        ):
            yield response

    @classmethod
    @asynccontextmanager
    async def client_session(
        cls,
        verify: VerifyTypes = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        follow_redirects: bool = True,
        **kwargs,
    ) -> AsyncGenerator[httpx.AsyncClient, None]:
        """
        创建 `httpx.AsyncClient` 会话。
        :param verify: 是否验证 SSL 证书
        :param http2: 是否使用 HTTP/2
        :param proxies: 地址
        :param follow_redirects: 是否跟随重定向
        :param kwargs: 传递给 `httpx.AsyncClient` 的其他参数
        :return: `httpx.AsyncClient` 对象
        """
        async with httpx.AsyncClient(
            verify=verify,
            http2=http2,
            proxies=proxies or config.proxy_url,  # type: ignore
            follow_redirects=follow_redirects,
            **kwargs,
        ) as client:
            yield client

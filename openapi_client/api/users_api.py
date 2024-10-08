# coding: utf-8

"""
    Open Food Facts open-prices REST API

    Open Prices API allows you to add product prices

    The version of the OpenAPI document: 0.0.0 (api)
    Contact: contact@openfoodfacts.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_client.models.paginated_user_list import PaginatedUserList

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class UsersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def users_list(
        self,
        order_by: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        price_count: Optional[StrictInt] = None,
        price_count__gte: Optional[StrictInt] = None,
        price_count__lte: Optional[StrictInt] = None,
        size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PaginatedUserList:
        """users_list


        :param order_by: Which field to use when ordering the results.
        :type order_by: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param price_count:
        :type price_count: int
        :param price_count__gte:
        :type price_count__gte: int
        :param price_count__lte:
        :type price_count__lte: int
        :param size: Number of results to return per page.
        :type size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._users_list_serialize(
            order_by=order_by,
            page=page,
            price_count=price_count,
            price_count__gte=price_count__gte,
            price_count__lte=price_count__lte,
            size=size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedUserList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def users_list_with_http_info(
        self,
        order_by: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        price_count: Optional[StrictInt] = None,
        price_count__gte: Optional[StrictInt] = None,
        price_count__lte: Optional[StrictInt] = None,
        size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PaginatedUserList]:
        """users_list


        :param order_by: Which field to use when ordering the results.
        :type order_by: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param price_count:
        :type price_count: int
        :param price_count__gte:
        :type price_count__gte: int
        :param price_count__lte:
        :type price_count__lte: int
        :param size: Number of results to return per page.
        :type size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._users_list_serialize(
            order_by=order_by,
            page=page,
            price_count=price_count,
            price_count__gte=price_count__gte,
            price_count__lte=price_count__lte,
            size=size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedUserList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def users_list_without_preload_content(
        self,
        order_by: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        price_count: Optional[StrictInt] = None,
        price_count__gte: Optional[StrictInt] = None,
        price_count__lte: Optional[StrictInt] = None,
        size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """users_list


        :param order_by: Which field to use when ordering the results.
        :type order_by: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param price_count:
        :type price_count: int
        :param price_count__gte:
        :type price_count__gte: int
        :param price_count__lte:
        :type price_count__lte: int
        :param size: Number of results to return per page.
        :type size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._users_list_serialize(
            order_by=order_by,
            page=page,
            price_count=price_count,
            price_count__gte=price_count__gte,
            price_count__lte=price_count__lte,
            size=size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedUserList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _users_list_serialize(
        self,
        order_by,
        page,
        price_count,
        price_count__gte,
        price_count__lte,
        size,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if order_by is not None:
            
            _query_params.append(('order_by', order_by))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if price_count is not None:
            
            _query_params.append(('price_count', price_count))
            
        if price_count__gte is not None:
            
            _query_params.append(('price_count__gte', price_count__gte))
            
        if price_count__lte is not None:
            
            _query_params.append(('price_count__lte', price_count__lte))
            
        if size is not None:
            
            _query_params.append(('size', size))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'basicAuth', 
            'cookieAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/users',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )



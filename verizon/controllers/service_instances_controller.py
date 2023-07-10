# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.http.api_response import ApiResponse
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from verizon.models.service_instances_result_set_item import ServiceInstancesResultSetItem
from verizon.models.service_instances_result import ServiceInstancesResult
from verizon.exceptions.edge_service_launch_result_exception import EdgeServiceLaunchResultException


class ServiceInstancesController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ServiceInstancesController, self).__init__(config)

    def retrieve_service_instance(self,
                                  service_instance_id,
                                  account_name,
                                  cluster=False):
        """Does a GET request to /v1/service/instances/{serviceInstanceId}.

        Retrieve information of a service instance.

        Args:
            service_instance_id (string): Unique Id of the service instance.
            account_name (string): User account name.
            cluster (bool, optional): TODO: type description here. Example:
                false

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A service
                instance.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/service/instances/{serviceInstanceId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('serviceInstanceId')
                            .value(service_instance_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .query_param(Parameter()
                         .key('cluster')
                         .value(cluster))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceInstancesResultSetItem.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceLaunchResultException)
            .local_error('401', 'Unauthorized.', EdgeServiceLaunchResultException)
            .local_error('403', 'Forbidden.', EdgeServiceLaunchResultException)
            .local_error('404', 'Not found.', EdgeServiceLaunchResultException)
            .local_error('415', 'Unsupported media type.', EdgeServiceLaunchResultException)
            .local_error('429', 'Too many requests.', EdgeServiceLaunchResultException)
            .local_error('500', 'Internal Server Error.', EdgeServiceLaunchResultException)
            .local_error('default', 'Unexpected error.', EdgeServiceLaunchResultException)
        ).execute()

    def list_services_instances(self,
                                account_name,
                                offset=None,
                                state=None,
                                limit=None,
                                searchbyname=None,
                                listofstate=None):
        """Does a GET request to /v1/service/instances.

        Retrieve all instances for all services.

        Args:
            account_name (string): User account name.
            offset (string, optional): TODO: type description here.
            state (string, optional): TODO: type description here.
            limit (string, optional): TODO: type description here.
            searchbyname (string, optional): TODO: type description here.
            listofstate (list of string, optional): TODO: type description
                here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Service
                instances.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/service/instances')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .query_param(Parameter()
                         .key('state')
                         .value(state))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('searchbyname')
                         .value(searchbyname))
            .query_param(Parameter()
                         .key('listofstate')
                         .value(listofstate))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceInstancesResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceLaunchResultException)
            .local_error('401', 'Unauthorized.', EdgeServiceLaunchResultException)
            .local_error('403', 'Forbidden.', EdgeServiceLaunchResultException)
            .local_error('404', 'Not found.', EdgeServiceLaunchResultException)
            .local_error('415', 'Unsupported media type.', EdgeServiceLaunchResultException)
            .local_error('429', 'Too many requests.', EdgeServiceLaunchResultException)
            .local_error('500', 'Internal Server Error.', EdgeServiceLaunchResultException)
            .local_error('default', 'Unexpected error.', EdgeServiceLaunchResultException)
        ).execute()

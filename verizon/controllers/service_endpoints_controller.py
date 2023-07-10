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
from verizon.models.list_optimal_service_endpoints_result import ListOptimalServiceEndpointsResult
from verizon.models.register_service_endpoint_result import RegisterServiceEndpointResult
from verizon.models.list_all_service_endpoints_result import ListAllServiceEndpointsResult
from verizon.models.resources_edge_hosted_service_with_profile_id import ResourcesEdgeHostedServiceWithProfileId
from verizon.models.update_service_endpoint_result import UpdateServiceEndpointResult
from verizon.models.deregister_service_endpoint_result import DeregisterServiceEndpointResult
from verizon.exceptions.edge_discovery_result_exception import EdgeDiscoveryResultException


class ServiceEndpointsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ServiceEndpointsController, self).__init__(config)

    def list_optimal_service_endpoints(self,
                                       region=None,
                                       subscriber_density=None,
                                       ue_identity_type=None,
                                       ue_identity=None,
                                       service_endpoints_ids=None):
        """Does a GET request to /serviceendpoints.

        Returns a list of optimal Service Endpoints that client devices can
        connect to. **Note:** If a query is sent with all of the parameters,
        it will fail with a "400" error. You can search based on the following
        parameter combinations - Region plus Service Endpoints IDs and
        Subscriber density (density is optional but recommended), Region plus
        Service Endpoints IDs and UEIdentity(Including UEIdentity Type) and
        Service Endpoints IDs plus UEIdentity(Including UEIdentity Type).

        Args:
            region (string, optional): MEC region name. Current valid values
                are US_WEST_2 and US_EAST_1.
            subscriber_density (int, optional): Minimum number of 4G/5G
                subscribers per square kilometer.
            ue_identity_type (UserEquipmentIdentityTypeEnum, optional): Type
                of User Equipment identifier used in `UEIdentity`.
            ue_identity (string, optional): The identifier value for User
                Equipment. The type of identifier is defined by the
                'UEIdentityType' parameter. The`IPAddress`format can be IPv4
                or IPv6.
            service_endpoints_ids (string, optional): A system-defined string
                identifier representing one or more registered Service
                Endpoints.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. An array
                of optimal Service Endpoint IDs for clients to connect to.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceendpoints')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('region')
                         .value(region))
            .query_param(Parameter()
                         .key('subscriberDensity')
                         .value(subscriber_density))
            .query_param(Parameter()
                         .key('UEIdentityType')
                         .value(ue_identity_type))
            .query_param(Parameter()
                         .key('UEIdentity')
                         .value(ue_identity))
            .query_param(Parameter()
                         .key('serviceEndpointsIds')
                         .value(service_endpoints_ids))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListOptimalServiceEndpointsResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def register_service_endpoints(self,
                                   body):
        """Does a POST request to /serviceendpoints.

        Register Service Endpoints of a deployed application to specified MEC
        Platforms.

        Args:
            body (list of ResourcesEdgeHostedServiceWithProfileId): An array
                of Service Endpoint data for a deployed application. The
                request body passes all of the needed parameters to create a
                service endpoint. Parameters will be edited here rather than
                the **Parameters** section above. The
                `ern`,`applicationServerProviderId`, `applicationId` and
                `serviceProfileID` parameters are required. **Note:**
                Currently, the only valid value for
                `applicationServerProviderId`is **AWS**. Also, if you do not
                know one of the optional values (i.e. URI), you can erase the
                line from the query by back-spacing over it.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Returns a
                service endpoints Id.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceendpoints')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RegisterServiceEndpointResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def list_all_service_endpoints(self):
        """Does a GET request to /serviceendpointsall.

        Returns a list of all registered service endpoints.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Returns a
                comma delimited list of all registered service endpoints.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceendpointsall')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListAllServiceEndpointsResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def get_service_endpoint(self,
                             service_endpoints_id):
        """Does a GET request to /serviceendpoints/{serviceEndpointsId}.

        Returns endpoint information for all Service Endpoints registered to a
        specified serviceEndpointId.

        Args:
            service_endpoints_id (string): A system-defined string identifier
                representing one or more registered Service Endpoints.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Registered service endpoint information for a 5G Edge
                service.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceendpoints/{serviceEndpointsId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('serviceEndpointsId')
                            .value(service_endpoints_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ResourcesEdgeHostedServiceWithProfileId.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def update_service_endpoint(self,
                                service_endpoints_id,
                                body):
        """Does a PUT request to /serviceendpoints/{serviceEndpointsId}.

        Update registered Service Endpoint information.

        Args:
            service_endpoints_id (string): A system-defined string identifier
                representing one or more registered Service Endpoints.
            body (list of ResourcesEdgeHostedServiceWithProfileId): Data
                needed for Service Endpoint information. The request body
                passes the rest of the needed parameters to create a service
                endpoint. Parameters other than `serviceEndpointsId` will be
                edited here rather than the **Parameters** section above. The
                `ern`,`applicationServerProviderId` and `applicationId`
                parameters are required. **Note:** Currently, the only valid
                value for `applicationServerProviderId`is **AWS**.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Update
                registered Service Endpoint information.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceendpoints/{serviceEndpointsId}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('serviceEndpointsId')
                            .value(service_endpoints_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UpdateServiceEndpointResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def deregister_service_endpoint(self,
                                    service_endpoints_id):
        """Does a DELETE request to /serviceendpoints/{serviceEndpointsId}.

        Deregister an application's Service Endpoint from the MEC
        Platform(s).

        Args:
            service_endpoints_id (string): A system-defined string identifier
                representing one or more registered Service Endpoints.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Service
                endpoint deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceendpoints/{serviceEndpointsId}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('serviceEndpointsId')
                            .value(service_endpoints_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeregisterServiceEndpointResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

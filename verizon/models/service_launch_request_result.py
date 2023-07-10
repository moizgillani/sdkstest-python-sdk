# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.config_file_item import ConfigFileItem
from verizon.models.linked_service_instance import LinkedServiceInstance


class ServiceLaunchRequestResult(object):

    """Implementation of the 'ServiceLaunchRequestResult' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): Unique service profile ID.
        name (string): Service request name.
        service_name (string): Service being deployed.
        state (ServiceLaunchStateEnum): TODO: type description here.
        service_version (string): Service version being deployed.
        service_id (string): TODO: type description here.
        service_profile_id (string): The service profile ID that is created
            during the post-service API.
        csp_profile_id (string): TODO: type description here.
        config_files (list of ConfigFileItem): TODO: type description here.
        linked_service_instances (list of LinkedServiceInstance): TODO: type
            description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        updated_by (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "service_name": 'serviceName',
        "state": 'state',
        "service_version": 'serviceVersion',
        "service_id": 'serviceId',
        "service_profile_id": 'serviceProfileId',
        "csp_profile_id": 'cspProfileId',
        "config_files": 'configFiles',
        "linked_service_instances": 'linkedServiceInstances',
        "created_at": 'createdAt',
        "updated_at": 'updatedAt',
        "updated_by": 'updatedBy'
    }

    _optionals = [
        'id',
        'name',
        'service_name',
        'state',
        'service_version',
        'service_id',
        'service_profile_id',
        'csp_profile_id',
        'config_files',
        'linked_service_instances',
        'created_at',
        'updated_at',
        'updated_by',
    ]

    _nullables = [
        'linked_service_instances',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 service_name=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 service_version=APIHelper.SKIP,
                 service_id=APIHelper.SKIP,
                 service_profile_id=APIHelper.SKIP,
                 csp_profile_id=APIHelper.SKIP,
                 config_files=APIHelper.SKIP,
                 linked_service_instances=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 updated_by=APIHelper.SKIP):
        """Constructor for the ServiceLaunchRequestResult class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if service_name is not APIHelper.SKIP:
            self.service_name = service_name 
        if state is not APIHelper.SKIP:
            self.state = state 
        if service_version is not APIHelper.SKIP:
            self.service_version = service_version 
        if service_id is not APIHelper.SKIP:
            self.service_id = service_id 
        if service_profile_id is not APIHelper.SKIP:
            self.service_profile_id = service_profile_id 
        if csp_profile_id is not APIHelper.SKIP:
            self.csp_profile_id = csp_profile_id 
        if config_files is not APIHelper.SKIP:
            self.config_files = config_files 
        if linked_service_instances is not APIHelper.SKIP:
            self.linked_service_instances = linked_service_instances 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None 
        if updated_by is not APIHelper.SKIP:
            self.updated_by = updated_by 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        service_version = dictionary.get("serviceVersion") if dictionary.get("serviceVersion") else APIHelper.SKIP
        service_id = dictionary.get("serviceId") if dictionary.get("serviceId") else APIHelper.SKIP
        service_profile_id = dictionary.get("serviceProfileId") if dictionary.get("serviceProfileId") else APIHelper.SKIP
        csp_profile_id = dictionary.get("cspProfileId") if dictionary.get("cspProfileId") else APIHelper.SKIP
        config_files = None
        if dictionary.get('configFiles') is not None:
            config_files = [ConfigFileItem.from_dictionary(x) for x in dictionary.get('configFiles')]
        else:
            config_files = APIHelper.SKIP
        if 'linkedServiceInstances' in dictionary.keys():
            linked_service_instances = [LinkedServiceInstance.from_dictionary(x) for x in dictionary.get('linkedServiceInstances')] if dictionary.get('linkedServiceInstances') else None
        else:
            linked_service_instances = APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdAt")).datetime if dictionary.get("createdAt") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updatedAt")).datetime if dictionary.get("updatedAt") else APIHelper.SKIP
        updated_by = dictionary.get("updatedBy") if dictionary.get("updatedBy") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   service_name,
                   state,
                   service_version,
                   service_id,
                   service_profile_id,
                   csp_profile_id,
                   config_files,
                   linked_service_instances,
                   created_at,
                   updated_at,
                   updated_by)

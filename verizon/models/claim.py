# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class Claim(object):

    """Implementation of the 'Claim' model.

    Users would provide CSP compatibility during service creation, which are
    nothing but declaring service compatibility with different cloud service
    providers like AWS or Azure. This API would help users to fetch all
    service claims using which user can initiate sandbox testing of the
    service.

    Attributes:
        id (string): Auto-generated Id.
        name (string): Name of the claim.
        claim_status (ClaimStatusEnum): Current status of the claim can have
            only two values eg: VERIFIED/UNVERIFIED.
        sand_box_state (SandBoxStateEnum): State of sandbox can have value
            like - STARTED, NOT_STARTED, STOPPED, PAUSED, COMPLETED, DELETED,
            STOP_IN_PROGRESS, PAUSE_IN_PROGRESS, TEST_IN_PROGRESS,
            MARK_FOR_DELETEION.
        sand_box_status (SandBoxStatusEnum): Status of sandbox can have value
            like - NA, INPROGRESS, SUCCESS, FAILED.
        environment (string): Claim environment in which it is deployed eg:
            AWS Public Cloud.
        claim_type (ClaimTypeEnum): Claim type can have values like -
            PUBLIC_MEC, PRIVATE_MEC.
        start_time_stamp (datetime): Start time when the claim got
            introduced.
        service_instance_id (string): Auto-generated Id of the service
            instance.
        csp_profile_id (string): CSP Profile ID in which service will be
            deployed.
        service_id (string): Auto-generated Id of the service which is to be
            deployed.
        end_time_stamp (datetime): End time when the claim got introduced.
        created_date (datetime): Auto-derived time of creation. Part of
            response only.
        last_modified_date (datetime): Last modified time. Part of response
            only.
        created_by (string): User who created the dropDown. Part of response
            only.
        last_modified_by (string): User who last modified the dropDown. Part
            of response only.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "claim_status": 'claimStatus',
        "sand_box_state": 'sandBoxState',
        "sand_box_status": 'sandBoxStatus',
        "environment": 'environment',
        "claim_type": 'claimType',
        "start_time_stamp": 'startTimeStamp',
        "service_instance_id": 'serviceInstanceId',
        "csp_profile_id": 'cspProfileId',
        "service_id": 'serviceId',
        "end_time_stamp": 'endTimeStamp',
        "created_date": 'createdDate',
        "last_modified_date": 'lastModifiedDate',
        "created_by": 'createdBy',
        "last_modified_by": 'lastModifiedBy'
    }

    _optionals = [
        'id',
        'name',
        'claim_status',
        'sand_box_state',
        'sand_box_status',
        'environment',
        'claim_type',
        'start_time_stamp',
        'service_instance_id',
        'csp_profile_id',
        'service_id',
        'end_time_stamp',
        'created_date',
        'last_modified_date',
        'created_by',
        'last_modified_by',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 claim_status=APIHelper.SKIP,
                 sand_box_state=APIHelper.SKIP,
                 sand_box_status=APIHelper.SKIP,
                 environment=APIHelper.SKIP,
                 claim_type=APIHelper.SKIP,
                 start_time_stamp=APIHelper.SKIP,
                 service_instance_id=APIHelper.SKIP,
                 csp_profile_id=APIHelper.SKIP,
                 service_id=APIHelper.SKIP,
                 end_time_stamp=APIHelper.SKIP,
                 created_date=APIHelper.SKIP,
                 last_modified_date=APIHelper.SKIP,
                 created_by=APIHelper.SKIP,
                 last_modified_by=APIHelper.SKIP):
        """Constructor for the Claim class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if claim_status is not APIHelper.SKIP:
            self.claim_status = claim_status 
        if sand_box_state is not APIHelper.SKIP:
            self.sand_box_state = sand_box_state 
        if sand_box_status is not APIHelper.SKIP:
            self.sand_box_status = sand_box_status 
        if environment is not APIHelper.SKIP:
            self.environment = environment 
        if claim_type is not APIHelper.SKIP:
            self.claim_type = claim_type 
        if start_time_stamp is not APIHelper.SKIP:
            self.start_time_stamp = APIHelper.RFC3339DateTime(start_time_stamp) if start_time_stamp else None 
        if service_instance_id is not APIHelper.SKIP:
            self.service_instance_id = service_instance_id 
        if csp_profile_id is not APIHelper.SKIP:
            self.csp_profile_id = csp_profile_id 
        if service_id is not APIHelper.SKIP:
            self.service_id = service_id 
        if end_time_stamp is not APIHelper.SKIP:
            self.end_time_stamp = APIHelper.RFC3339DateTime(end_time_stamp) if end_time_stamp else None 
        if created_date is not APIHelper.SKIP:
            self.created_date = APIHelper.RFC3339DateTime(created_date) if created_date else None 
        if last_modified_date is not APIHelper.SKIP:
            self.last_modified_date = APIHelper.RFC3339DateTime(last_modified_date) if last_modified_date else None 
        if created_by is not APIHelper.SKIP:
            self.created_by = created_by 
        if last_modified_by is not APIHelper.SKIP:
            self.last_modified_by = last_modified_by 

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
        claim_status = dictionary.get("claimStatus") if dictionary.get("claimStatus") else APIHelper.SKIP
        sand_box_state = dictionary.get("sandBoxState") if dictionary.get("sandBoxState") else APIHelper.SKIP
        sand_box_status = dictionary.get("sandBoxStatus") if dictionary.get("sandBoxStatus") else APIHelper.SKIP
        environment = dictionary.get("environment") if dictionary.get("environment") else APIHelper.SKIP
        claim_type = dictionary.get("claimType") if dictionary.get("claimType") else APIHelper.SKIP
        start_time_stamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("startTimeStamp")).datetime if dictionary.get("startTimeStamp") else APIHelper.SKIP
        service_instance_id = dictionary.get("serviceInstanceId") if dictionary.get("serviceInstanceId") else APIHelper.SKIP
        csp_profile_id = dictionary.get("cspProfileId") if dictionary.get("cspProfileId") else APIHelper.SKIP
        service_id = dictionary.get("serviceId") if dictionary.get("serviceId") else APIHelper.SKIP
        end_time_stamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("endTimeStamp")).datetime if dictionary.get("endTimeStamp") else APIHelper.SKIP
        created_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdDate")).datetime if dictionary.get("createdDate") else APIHelper.SKIP
        last_modified_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastModifiedDate")).datetime if dictionary.get("lastModifiedDate") else APIHelper.SKIP
        created_by = dictionary.get("createdBy") if dictionary.get("createdBy") else APIHelper.SKIP
        last_modified_by = dictionary.get("lastModifiedBy") if dictionary.get("lastModifiedBy") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   claim_status,
                   sand_box_state,
                   sand_box_status,
                   environment,
                   claim_type,
                   start_time_stamp,
                   service_instance_id,
                   csp_profile_id,
                   service_id,
                   end_time_stamp,
                   created_date,
                   last_modified_date,
                   created_by,
                   last_modified_by)

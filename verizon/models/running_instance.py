# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class RunningInstance(object):

    """Implementation of the 'RunningInstance' model.

    Running instance of a service.

    Attributes:
        instance_name (string): Service instance name.
        instance_id (string): Service instance ID.
        csp (string): Cloud Service Provider.
        status (ServiceStatusEnum): Can have any value as - DRAFT_INPROGRESS,
            DRAFT_COMPLETE, DESIGN_INPROGRESS, DESIGN_FAILED,
            DESIGN_COMPLETED, VALIDATION_INPROGRESS,  VALIDATION_FAILED,
            VALIDATION_COMPLETED, TESTING_INPROGRESS, TESTING_FAILED,
            TESTING_COMPLETED, READY_TO_USE_INPROGRESS, READY_TO_USE_FAILED,
            READY_TO_USE_COMPLETED, READY_TO_PRIVATE_USE_INPROGRESS,
            READY_TO_PRIVATE_USE_FAILED, READY_TO_PRIVATE_USE_COMPLETED, 
            PUBLISH_INPROGRESS,  PUBLISH_FAILED,  PUBLISH_COMPLETED, 
            CERTIFY_INPROGRESS,  CERTIFY_FAILED, CERTIFY_COMPLETED,
            DEPRECATE_INPROGRESS,  DEPRECATE_FAILED, DEPRECATE_COMPLETED,
            MARKDELETE_INPROGRESS, MARKDELETE_FAILED, MARKDELETE_COMPLETED.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "instance_name": 'instanceName',
        "instance_id": 'instanceID',
        "csp": 'CSP',
        "status": 'status'
    }

    _optionals = [
        'instance_name',
        'instance_id',
        'csp',
        'status',
    ]

    def __init__(self,
                 instance_name=APIHelper.SKIP,
                 instance_id=APIHelper.SKIP,
                 csp=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the RunningInstance class"""

        # Initialize members of the class
        if instance_name is not APIHelper.SKIP:
            self.instance_name = instance_name 
        if instance_id is not APIHelper.SKIP:
            self.instance_id = instance_id 
        if csp is not APIHelper.SKIP:
            self.csp = csp 
        if status is not APIHelper.SKIP:
            self.status = status 

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

        instance_name = dictionary.get("instanceName") if dictionary.get("instanceName") else APIHelper.SKIP
        instance_id = dictionary.get("instanceID") if dictionary.get("instanceID") else APIHelper.SKIP
        csp = dictionary.get("CSP") if dictionary.get("CSP") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(instance_name,
                   instance_id,
                   csp,
                   status)

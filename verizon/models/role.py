# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class Role(object):

    """Implementation of the 'Role' model.

    Role of the user calling API.

    Attributes:
        account_id (string): Account ID of the role.
        external_id (string): External ID of the role.
        role_arn (string): Role ARN of the role.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'accountId',
        "external_id": 'externalId',
        "role_arn": 'roleARN'
    }

    _optionals = [
        'account_id',
        'external_id',
        'role_arn',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 external_id=APIHelper.SKIP,
                 role_arn=APIHelper.SKIP):
        """Constructor for the Role class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if external_id is not APIHelper.SKIP:
            self.external_id = external_id 
        if role_arn is not APIHelper.SKIP:
            self.role_arn = role_arn 

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

        account_id = dictionary.get("accountId") if dictionary.get("accountId") else APIHelper.SKIP
        external_id = dictionary.get("externalId") if dictionary.get("externalId") else APIHelper.SKIP
        role_arn = dictionary.get("roleARN") if dictionary.get("roleARN") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   external_id,
                   role_arn)

# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ServiceSwaggerSpecId(object):

    """Implementation of the 'ServiceSwaggerSpecId' model.

    Auto-generated Id of service handler Swagger specification file uploaded.

    Attributes:
        id (string): Auto-generated id of the service handler Swagger
            specification file uploaded.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id'
    }

    _optionals = [
        'id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP):
        """Constructor for the ServiceSwaggerSpecId class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 

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
        # Return an object of this model
        return cls(id)

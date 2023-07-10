# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ListAllServiceEndpointsResult(object):

    """Implementation of the 'ListAllServiceEndpointsResult' model.

    Response on successful retrieval of all registered service endpoints.

    Attributes:
        status (string): HTTP status code.
        data (list of string): A comma delimited list of all registered
            service endpoints.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "data": 'data'
    }

    _optionals = [
        'status',
        'data',
    ]

    def __init__(self,
                 status='success',
                 data=APIHelper.SKIP):
        """Constructor for the ListAllServiceEndpointsResult class"""

        # Initialize members of the class
        self.status = status 
        if data is not APIHelper.SKIP:
            self.data = data 

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

        status = dictionary.get("status") if dictionary.get("status") else 'success'
        data = dictionary.get("data") if dictionary.get("data") else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   data)

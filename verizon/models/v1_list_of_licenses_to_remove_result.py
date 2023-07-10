# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class V1ListOfLicensesToRemoveResult(object):

    """Implementation of the 'V1ListOfLicensesToRemoveResult' model.

    List of licenses assigned.

    Attributes:
        count (int): The total number of devices on the cancellation candidate
            list.
        device_list (list of string): The IMEIs of the devices.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "device_list": 'deviceList'
    }

    _optionals = [
        'count',
        'device_list',
    ]

    def __init__(self,
                 count=APIHelper.SKIP,
                 device_list=APIHelper.SKIP):
        """Constructor for the V1ListOfLicensesToRemoveResult class"""

        # Initialize members of the class
        if count is not APIHelper.SKIP:
            self.count = count 
        if device_list is not APIHelper.SKIP:
            self.device_list = device_list 

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

        count = dictionary.get("count") if dictionary.get("count") else APIHelper.SKIP
        device_list = dictionary.get("deviceList") if dictionary.get("deviceList") else APIHelper.SKIP
        # Return an object of this model
        return cls(count,
                   device_list)
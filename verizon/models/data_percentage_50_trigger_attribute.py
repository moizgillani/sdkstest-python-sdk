# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class DataPercentage50TriggerAttribute(object):

    """Implementation of the 'DataPercentage50TriggerAttribute' model.

    Trigger attribute for when data percentage is over 50% used.

    Attributes:
        key (string): Key data percentage 50.
        value (bool): DataPercentage50<br />True - Trigger on Data percentage
            is over 50% used<br />False - Do not trigger when over 50% used.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "value": 'value'
    }

    _optionals = [
        'key',
        'value',
    ]

    def __init__(self,
                 key=APIHelper.SKIP,
                 value=APIHelper.SKIP):
        """Constructor for the DataPercentage50TriggerAttribute class"""

        # Initialize members of the class
        if key is not APIHelper.SKIP:
            self.key = key 
        if value is not APIHelper.SKIP:
            self.value = value 

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

        key = dictionary.get("key") if dictionary.get("key") else APIHelper.SKIP
        value = dictionary.get("value") if "value" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(key,
                   value)

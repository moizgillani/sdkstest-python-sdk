# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ResourceBase(object):

    """Implementation of the 'ResourceBase' model.

    Resource Base of the service.

    Attributes:
        unit (string): Resource unit ex :MB.
        value (long|int): Resource value e.g. 200MB.
        max (long|int): Resource max value e.g. 400MB.
        min (long|int): Resource min value e.g. 10MB.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "unit": 'unit',
        "value": 'value',
        "max": 'max',
        "min": 'min'
    }

    _optionals = [
        'unit',
        'value',
        'max',
        'min',
    ]

    def __init__(self,
                 unit=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 max=APIHelper.SKIP,
                 min=APIHelper.SKIP):
        """Constructor for the ResourceBase class"""

        # Initialize members of the class
        if unit is not APIHelper.SKIP:
            self.unit = unit 
        if value is not APIHelper.SKIP:
            self.value = value 
        if max is not APIHelper.SKIP:
            self.max = max 
        if min is not APIHelper.SKIP:
            self.min = min 

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

        unit = dictionary.get("unit") if dictionary.get("unit") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        max = dictionary.get("max") if dictionary.get("max") else APIHelper.SKIP
        min = dictionary.get("min") if dictionary.get("min") else APIHelper.SKIP
        # Return an object of this model
        return cls(unit,
                   value,
                   max,
                   min)

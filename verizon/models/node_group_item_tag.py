# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class NodeGroupItemTag(object):

    """Implementation of the 'NodeGroupItemTag' model.

    TODO: type model description here.

    Attributes:
        associate_carrier_ip (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "associate_carrier_ip": 'associate-carrier-ip'
    }

    _optionals = [
        'associate_carrier_ip',
    ]

    def __init__(self,
                 associate_carrier_ip=APIHelper.SKIP):
        """Constructor for the NodeGroupItemTag class"""

        # Initialize members of the class
        if associate_carrier_ip is not APIHelper.SKIP:
            self.associate_carrier_ip = associate_carrier_ip 

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

        associate_carrier_ip = dictionary.get("associate-carrier-ip") if dictionary.get("associate-carrier-ip") else APIHelper.SKIP
        # Return an object of this model
        return cls(associate_carrier_ip)

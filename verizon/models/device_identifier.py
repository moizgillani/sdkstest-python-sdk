# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class DeviceIdentifier(object):

    """Implementation of the 'DeviceIdentifier' model.

    TODO: type model description here.

    Attributes:
        kind (string): TODO: type description here.
        id (string): TODO: type description here.
        mdn (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kind": 'kind',
        "id": 'id',
        "mdn": 'mdn'
    }

    _optionals = [
        'mdn',
    ]

    def __init__(self,
                 kind=None,
                 id=None,
                 mdn=APIHelper.SKIP):
        """Constructor for the DeviceIdentifier class"""

        # Initialize members of the class
        self.kind = kind 
        self.id = id 
        if mdn is not APIHelper.SKIP:
            self.mdn = mdn 

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

        kind = dictionary.get("kind") if dictionary.get("kind") else None
        id = dictionary.get("id") if dictionary.get("id") else None
        mdn = dictionary.get("mdn") if dictionary.get("mdn") else APIHelper.SKIP
        # Return an object of this model
        return cls(kind,
                   id,
                   mdn)

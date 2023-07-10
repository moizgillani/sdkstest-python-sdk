# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.models.locationscoord import Locationscoord
from verizon.models.network_type import NetworkType


class GetWirelessCoverageRequest(object):

    """Implementation of the 'GetWirelessCoverageRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (string): TODO: type description here.
        request_type (string): TODO: type description here.
        location_type (string): TODO: type description here.
        locations (Locationscoord): TODO: type description here.
        network_types_list (list of NetworkType): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "request_type": 'requestType',
        "location_type": 'locationType',
        "locations": 'locations',
        "network_types_list": 'networkTypesList'
    }

    def __init__(self,
                 account_name=None,
                 request_type=None,
                 location_type=None,
                 locations=None,
                 network_types_list=None):
        """Constructor for the GetWirelessCoverageRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.request_type = request_type 
        self.location_type = location_type 
        self.locations = locations 
        self.network_types_list = network_types_list 

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

        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        request_type = dictionary.get("requestType") if dictionary.get("requestType") else None
        location_type = dictionary.get("locationType") if dictionary.get("locationType") else None
        locations = Locationscoord.from_dictionary(dictionary.get('locations')) if dictionary.get('locations') else None
        network_types_list = None
        if dictionary.get('networkTypesList') is not None:
            network_types_list = [NetworkType.from_dictionary(x) for x in dictionary.get('networkTypesList')]
        # Return an object of this model
        return cls(account_name,
                   request_type,
                   location_type,
                   locations,
                   network_types_list)

# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.daily_usage_item import DailyUsageItem


class SessionReport(object):

    """Implementation of the 'SessionReport' model.

    Session report for a device.

    Attributes:
        sessions (list of DailyUsageItem): An object containing the start and
            end time of the session with the amount of data transferred.
        id (string): The 10-digit ID of the device.
        txid (string): A unique string that associates the request with the
            location report information that is sent in asynchronous callback
            message.ThingSpace will send a separate callback message for each
            device that was in the request. All of the callback messages will
            have the same txid.
        example (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "txid": 'txid',
        "sessions": 'sessions',
        "example": 'example'
    }

    _optionals = [
        'sessions',
        'example',
    ]

    _nullables = [
        'txid',
    ]

    def __init__(self,
                 id=None,
                 txid=None,
                 sessions=APIHelper.SKIP,
                 example=APIHelper.SKIP):
        """Constructor for the SessionReport class"""

        # Initialize members of the class
        if sessions is not APIHelper.SKIP:
            self.sessions = sessions 
        self.id = id 
        self.txid = txid 
        if example is not APIHelper.SKIP:
            self.example = example 

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

        id = dictionary.get("id") if dictionary.get("id") else None
        txid = dictionary.get("txid") if dictionary.get("txid") else None
        sessions = None
        if dictionary.get('sessions') is not None:
            sessions = [DailyUsageItem.from_dictionary(x) for x in dictionary.get('sessions')]
        else:
            sessions = APIHelper.SKIP
        example = dictionary.get("example") if dictionary.get("example") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   txid,
                   sessions,
                   example)

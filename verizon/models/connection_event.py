# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.custom_fields import CustomFields


class ConnectionEvent(object):

    """Implementation of the 'ConnectionEvent' model.

    Network connection events for a device during a specified time period.

    Attributes:
        connection_event_attributes (list of CustomFields): The attributes
            that describe the connection event.
        extended_attributes (list of CustomFields): Currently not used.
        occurred_at (string): The date and time when the connection event
            occured.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "connection_event_attributes": 'connectionEventAttributes',
        "extended_attributes": 'extendedAttributes',
        "occurred_at": 'occurredAt'
    }

    _optionals = [
        'connection_event_attributes',
        'extended_attributes',
        'occurred_at',
    ]

    def __init__(self,
                 connection_event_attributes=APIHelper.SKIP,
                 extended_attributes=APIHelper.SKIP,
                 occurred_at=APIHelper.SKIP):
        """Constructor for the ConnectionEvent class"""

        # Initialize members of the class
        if connection_event_attributes is not APIHelper.SKIP:
            self.connection_event_attributes = connection_event_attributes 
        if extended_attributes is not APIHelper.SKIP:
            self.extended_attributes = extended_attributes 
        if occurred_at is not APIHelper.SKIP:
            self.occurred_at = occurred_at 

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

        connection_event_attributes = None
        if dictionary.get('connectionEventAttributes') is not None:
            connection_event_attributes = [CustomFields.from_dictionary(x) for x in dictionary.get('connectionEventAttributes')]
        else:
            connection_event_attributes = APIHelper.SKIP
        extended_attributes = None
        if dictionary.get('extendedAttributes') is not None:
            extended_attributes = [CustomFields.from_dictionary(x) for x in dictionary.get('extendedAttributes')]
        else:
            extended_attributes = APIHelper.SKIP
        occurred_at = dictionary.get("occurredAt") if dictionary.get("occurredAt") else APIHelper.SKIP
        # Return an object of this model
        return cls(connection_event_attributes,
                   extended_attributes,
                   occurred_at)

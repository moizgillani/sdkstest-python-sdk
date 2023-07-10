# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class RegisteredCallbacks(object):

    """Implementation of the 'RegisteredCallbacks' model.

    List of registered callback endpoints.

    Attributes:
        aname (string): The name of the billing account for which callback
            messages will be sent.
        name (string): The name of the callback service, which identifies the
            type and format of messages that will be sent to the registered
            URL. This will be 'Fota' for the Software Management Services
            callback.
        url (string): The address to which callback messages will be sent.
        username (string): The user name that ThingSpace will return in the
            callback messages.
        password (string): The password that ThingSpace will return in the
            callback messages.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aname": 'aname',
        "name": 'name',
        "url": 'url',
        "username": 'username',
        "password": 'password'
    }

    _optionals = [
        'aname',
        'name',
        'url',
        'username',
        'password',
    ]

    def __init__(self,
                 aname=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 username=APIHelper.SKIP,
                 password=APIHelper.SKIP):
        """Constructor for the RegisteredCallbacks class"""

        # Initialize members of the class
        if aname is not APIHelper.SKIP:
            self.aname = aname 
        if name is not APIHelper.SKIP:
            self.name = name 
        if url is not APIHelper.SKIP:
            self.url = url 
        if username is not APIHelper.SKIP:
            self.username = username 
        if password is not APIHelper.SKIP:
            self.password = password 

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

        aname = dictionary.get("aname") if dictionary.get("aname") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        username = dictionary.get("username") if dictionary.get("username") else APIHelper.SKIP
        password = dictionary.get("password") if dictionary.get("password") else APIHelper.SKIP
        # Return an object of this model
        return cls(aname,
                   name,
                   url,
                   username,
                   password)
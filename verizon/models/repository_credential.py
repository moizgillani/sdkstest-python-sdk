# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class RepositoryCredential(object):

    """Implementation of the 'RepositoryCredential' model.

    Credentials of a repository.

    Attributes:
        name (string): User name to connect to the repository.
        password (string): Account password to connect to user provided
            repository.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "password": 'password'
    }

    _optionals = [
        'name',
        'password',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 password=APIHelper.SKIP):
        """Constructor for the RepositoryCredential class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        password = dictionary.get("password") if dictionary.get("password") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   password)

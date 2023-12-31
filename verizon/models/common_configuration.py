# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.blueprint import Blueprint
from verizon.models.cloud_credential import CloudCredential


class CommonConfiguration(object):

    """Implementation of the 'CommonConfiguration' model.

    TODO: type model description here.

    Attributes:
        cloud_credentials (CloudCredential): TODO: type description here.
        k_8_s_version (K8sVersionEnum): Version of K8s platform.
        blueprint (Blueprint): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_credentials": 'cloudCredentials',
        "k_8_s_version": 'k8sVersion',
        "blueprint": 'blueprint'
    }

    _optionals = [
        'cloud_credentials',
        'k_8_s_version',
        'blueprint',
    ]

    def __init__(self,
                 cloud_credentials=APIHelper.SKIP,
                 k_8_s_version='1.18',
                 blueprint=APIHelper.SKIP):
        """Constructor for the CommonConfiguration class"""

        # Initialize members of the class
        if cloud_credentials is not APIHelper.SKIP:
            self.cloud_credentials = cloud_credentials 
        self.k_8_s_version = k_8_s_version 
        if blueprint is not APIHelper.SKIP:
            self.blueprint = blueprint 

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

        cloud_credentials = CloudCredential.from_dictionary(dictionary.get('cloudCredentials')) if 'cloudCredentials' in dictionary.keys() else APIHelper.SKIP
        k_8_s_version = dictionary.get("k8sVersion") if dictionary.get("k8sVersion") else '1.18'
        blueprint = Blueprint.from_dictionary(dictionary.get('blueprint')) if 'blueprint' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(cloud_credentials,
                   k_8_s_version,
                   blueprint)

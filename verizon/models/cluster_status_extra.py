# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.service_launch_cluster_additional_params import ServiceLaunchClusterAdditionalParams


class ClusterStatusExtra(object):

    """Implementation of the 'ClusterStatusExtra' model.

    TODO: type model description here.

    Attributes:
        vault_integration (ServiceLaunchClusterAdditionalParams): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vault_integration": 'vaultIntegration'
    }

    _optionals = [
        'vault_integration',
    ]

    def __init__(self,
                 vault_integration=APIHelper.SKIP):
        """Constructor for the ClusterStatusExtra class"""

        # Initialize members of the class
        if vault_integration is not APIHelper.SKIP:
            self.vault_integration = vault_integration 

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

        vault_integration = ServiceLaunchClusterAdditionalParams.from_dictionary(dictionary.get('vaultIntegration')) if 'vaultIntegration' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(vault_integration)

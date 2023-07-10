# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ServiceLaunchHelmRepo(object):

    """Implementation of the 'ServiceLaunchHelmRepo' model.

    TODO: type model description here.

    Attributes:
        helm_chart_name (string): TODO: type description here.
        helm_chart_version (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "helm_chart_name": 'helmChartName',
        "helm_chart_version": 'helmChartVersion'
    }

    _optionals = [
        'helm_chart_name',
        'helm_chart_version',
    ]

    def __init__(self,
                 helm_chart_name=APIHelper.SKIP,
                 helm_chart_version=APIHelper.SKIP):
        """Constructor for the ServiceLaunchHelmRepo class"""

        # Initialize members of the class
        if helm_chart_name is not APIHelper.SKIP:
            self.helm_chart_name = helm_chart_name 
        if helm_chart_version is not APIHelper.SKIP:
            self.helm_chart_version = helm_chart_version 

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

        helm_chart_name = dictionary.get("helmChartName") if dictionary.get("helmChartName") else APIHelper.SKIP
        helm_chart_version = dictionary.get("helmChartVersion") if dictionary.get("helmChartVersion") else APIHelper.SKIP
        # Return an object of this model
        return cls(helm_chart_name,
                   helm_chart_version)

# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class NodeStatusCapacity(object):

    """Implementation of the 'NodeStatusCapacity' model.

    TODO: type model description here.

    Attributes:
        cpu_count (int): TODO: type description here.
        ephemeral_storage_kb (long|int): TODO: type description here.
        memory_kb (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cpu_count": 'cpuCount',
        "ephemeral_storage_kb": 'ephemeralStorageKB',
        "memory_kb": 'memoryKB'
    }

    _optionals = [
        'cpu_count',
        'ephemeral_storage_kb',
        'memory_kb',
    ]

    def __init__(self,
                 cpu_count=APIHelper.SKIP,
                 ephemeral_storage_kb=APIHelper.SKIP,
                 memory_kb=APIHelper.SKIP):
        """Constructor for the NodeStatusCapacity class"""

        # Initialize members of the class
        if cpu_count is not APIHelper.SKIP:
            self.cpu_count = cpu_count 
        if ephemeral_storage_kb is not APIHelper.SKIP:
            self.ephemeral_storage_kb = ephemeral_storage_kb 
        if memory_kb is not APIHelper.SKIP:
            self.memory_kb = memory_kb 

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

        cpu_count = dictionary.get("cpuCount") if dictionary.get("cpuCount") else APIHelper.SKIP
        ephemeral_storage_kb = dictionary.get("ephemeralStorageKB") if dictionary.get("ephemeralStorageKB") else APIHelper.SKIP
        memory_kb = dictionary.get("memoryKB") if dictionary.get("memoryKB") else APIHelper.SKIP
        # Return an object of this model
        return cls(cpu_count,
                   ephemeral_storage_kb,
                   memory_kb)

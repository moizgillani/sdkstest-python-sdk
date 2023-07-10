# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class Node(object):

    """Implementation of the 'Node' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        created_at (string): TODO: type description here.
        modified_at (string): TODO: type description here.
        node_id (string): TODO: type description here.
        private_ip (string): TODO: type description here.
        num_cores (int): TODO: type description here.
        total_memory (int): TODO: type description here.
        cluster_id (string): TODO: type description here.
        roles (list of string): TODO: type description here.
        id (string): TODO: type description here.
        approved (bool): TODO: type description here.
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "created_at": 'created_at',
        "modified_at": 'modified_at',
        "node_id": 'node_id',
        "private_ip": 'private_ip',
        "num_cores": 'num_cores',
        "total_memory": 'total_memory',
        "cluster_id": 'cluster_id',
        "roles": 'roles',
        "id": 'id',
        "approved": 'approved',
        "status": 'status'
    }

    _optionals = [
        'name',
        'created_at',
        'modified_at',
        'node_id',
        'private_ip',
        'num_cores',
        'total_memory',
        'cluster_id',
        'roles',
        'id',
        'approved',
        'status',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 modified_at=APIHelper.SKIP,
                 node_id=APIHelper.SKIP,
                 private_ip=APIHelper.SKIP,
                 num_cores=APIHelper.SKIP,
                 total_memory=APIHelper.SKIP,
                 cluster_id=APIHelper.SKIP,
                 roles=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 approved=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the Node class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if modified_at is not APIHelper.SKIP:
            self.modified_at = modified_at 
        if node_id is not APIHelper.SKIP:
            self.node_id = node_id 
        if private_ip is not APIHelper.SKIP:
            self.private_ip = private_ip 
        if num_cores is not APIHelper.SKIP:
            self.num_cores = num_cores 
        if total_memory is not APIHelper.SKIP:
            self.total_memory = total_memory 
        if cluster_id is not APIHelper.SKIP:
            self.cluster_id = cluster_id 
        if roles is not APIHelper.SKIP:
            self.roles = roles 
        if id is not APIHelper.SKIP:
            self.id = id 
        if approved is not APIHelper.SKIP:
            self.approved = approved 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        modified_at = dictionary.get("modified_at") if dictionary.get("modified_at") else APIHelper.SKIP
        node_id = dictionary.get("node_id") if dictionary.get("node_id") else APIHelper.SKIP
        private_ip = dictionary.get("private_ip") if dictionary.get("private_ip") else APIHelper.SKIP
        num_cores = dictionary.get("num_cores") if dictionary.get("num_cores") else APIHelper.SKIP
        total_memory = dictionary.get("total_memory") if dictionary.get("total_memory") else APIHelper.SKIP
        cluster_id = dictionary.get("cluster_id") if dictionary.get("cluster_id") else APIHelper.SKIP
        roles = dictionary.get("roles") if dictionary.get("roles") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        approved = dictionary.get("approved") if "approved" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   created_at,
                   modified_at,
                   node_id,
                   private_ip,
                   num_cores,
                   total_memory,
                   cluster_id,
                   roles,
                   id,
                   approved,
                   status)
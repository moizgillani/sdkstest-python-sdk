# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.id_list import IdList
from verizon.models.node_configuration_label import NodeConfigurationLabel
from verizon.models.node_configuration_tag import NodeConfigurationTag


class NodeConfiguration(object):

    """Implementation of the 'NodeConfiguration' model.

    TODO: type model description here.

    Attributes:
        name (string): Name of the nodeGroup.
        is_wavelength_zone (bool): TODO: type description here.
        is_managed_node_group (bool): TODO: type description here.
        is_spot_instance_needed (bool): TODO: type description here.
        end_point_access_type (EndPointAccessTypeEnum): TODO: type description
            here.
        instance_type (string): TODO: type description here.
        nodes (int): TODO: type description here.
        nodes_min (int): TODO: type description here.
        nodes_max (int): TODO: type description here.
        node_volume_type (string): TODO: type description here.
        subnet_cidr_block (string): TODO: type description here.
        node_ami_family (string): TODO: type description here.
        node_volume_size (int): TODO: type description here.
        key_name (string): TODO: type description here.
        max_pod_per_node (int): TODO: type description here.
        use_volume_encryption (bool): TODO: type description here.
        node_private_networking (bool): TODO: type description here.
        instance_profile_arn (string): TODO: type description here.
        instance_role_arn (string): TODO: type description here.
        instance_role_permission_boundary (string): TODO: type description
            here.
        security_group_ids (list of IdList): TODO: type description here.
        availability_zone_ids (list of IdList): TODO: type description here.
        labels (NodeConfigurationLabel): TODO: type description here.
        tags (NodeConfigurationTag): TODO: type description here.
        auto_create_service_roles (bool): TODO: type description here.
        enable_full_access_to_ecr (bool): TODO: type description here.
        enable_asg_access (bool): TODO: type description here.
        enable_dns_access (bool): TODO: type description here.
        enable_app_mesh_access (bool): TODO: type description here.
        enable_alb_access (bool): TODO: type description here.
        enable_efs_access (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "is_wavelength_zone": 'isWavelengthZone',
        "is_managed_node_group": 'isManagedNodeGroup',
        "is_spot_instance_needed": 'isSpotInstanceNeeded',
        "end_point_access_type": 'endPointAccessType',
        "instance_type": 'instanceType',
        "nodes": 'nodes',
        "nodes_min": 'nodesMin',
        "nodes_max": 'nodesMax',
        "node_volume_type": 'nodeVolumeType',
        "subnet_cidr_block": 'subnetCidrBlock',
        "node_ami_family": 'nodeAmiFamily',
        "node_volume_size": 'nodeVolumeSize',
        "key_name": 'keyName',
        "max_pod_per_node": 'maxPodPerNode',
        "use_volume_encryption": 'useVolumeEncryption',
        "node_private_networking": 'nodePrivateNetworking',
        "instance_profile_arn": 'instanceProfileArn',
        "instance_role_arn": 'instanceRoleArn',
        "instance_role_permission_boundary": 'instanceRolePermissionBoundary',
        "security_group_ids": 'securityGroupIds',
        "availability_zone_ids": 'availabilityZoneIds',
        "labels": 'labels',
        "tags": 'tags',
        "auto_create_service_roles": 'autoCreateServiceRoles',
        "enable_full_access_to_ecr": 'enableFullAccessToEcr',
        "enable_asg_access": 'enableAsgAccess',
        "enable_dns_access": 'enableDnsAccess',
        "enable_app_mesh_access": 'enableAppMeshAccess',
        "enable_alb_access": 'enableAlbAccess',
        "enable_efs_access": 'enableEfsAccess'
    }

    _optionals = [
        'name',
        'is_wavelength_zone',
        'is_managed_node_group',
        'is_spot_instance_needed',
        'end_point_access_type',
        'instance_type',
        'nodes',
        'nodes_min',
        'nodes_max',
        'node_volume_type',
        'subnet_cidr_block',
        'node_ami_family',
        'node_volume_size',
        'key_name',
        'max_pod_per_node',
        'use_volume_encryption',
        'node_private_networking',
        'instance_profile_arn',
        'instance_role_arn',
        'instance_role_permission_boundary',
        'security_group_ids',
        'availability_zone_ids',
        'labels',
        'tags',
        'auto_create_service_roles',
        'enable_full_access_to_ecr',
        'enable_asg_access',
        'enable_dns_access',
        'enable_app_mesh_access',
        'enable_alb_access',
        'enable_efs_access',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 is_wavelength_zone=False,
                 is_managed_node_group=False,
                 is_spot_instance_needed=False,
                 end_point_access_type='private',
                 instance_type='m5.xlarge',
                 nodes=2,
                 nodes_min=APIHelper.SKIP,
                 nodes_max=APIHelper.SKIP,
                 node_volume_type=APIHelper.SKIP,
                 subnet_cidr_block=APIHelper.SKIP,
                 node_ami_family='AmazonLinux2',
                 node_volume_size=APIHelper.SKIP,
                 key_name=APIHelper.SKIP,
                 max_pod_per_node=APIHelper.SKIP,
                 use_volume_encryption=True,
                 node_private_networking=False,
                 instance_profile_arn=APIHelper.SKIP,
                 instance_role_arn=APIHelper.SKIP,
                 instance_role_permission_boundary=APIHelper.SKIP,
                 security_group_ids=APIHelper.SKIP,
                 availability_zone_ids=APIHelper.SKIP,
                 labels=APIHelper.SKIP,
                 tags=APIHelper.SKIP,
                 auto_create_service_roles=True,
                 enable_full_access_to_ecr=APIHelper.SKIP,
                 enable_asg_access=APIHelper.SKIP,
                 enable_dns_access=APIHelper.SKIP,
                 enable_app_mesh_access=APIHelper.SKIP,
                 enable_alb_access=APIHelper.SKIP,
                 enable_efs_access=APIHelper.SKIP):
        """Constructor for the NodeConfiguration class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        self.is_wavelength_zone = is_wavelength_zone 
        self.is_managed_node_group = is_managed_node_group 
        self.is_spot_instance_needed = is_spot_instance_needed 
        self.end_point_access_type = end_point_access_type 
        self.instance_type = instance_type 
        self.nodes = nodes 
        if nodes_min is not APIHelper.SKIP:
            self.nodes_min = nodes_min 
        if nodes_max is not APIHelper.SKIP:
            self.nodes_max = nodes_max 
        if node_volume_type is not APIHelper.SKIP:
            self.node_volume_type = node_volume_type 
        if subnet_cidr_block is not APIHelper.SKIP:
            self.subnet_cidr_block = subnet_cidr_block 
        self.node_ami_family = node_ami_family 
        if node_volume_size is not APIHelper.SKIP:
            self.node_volume_size = node_volume_size 
        if key_name is not APIHelper.SKIP:
            self.key_name = key_name 
        if max_pod_per_node is not APIHelper.SKIP:
            self.max_pod_per_node = max_pod_per_node 
        self.use_volume_encryption = use_volume_encryption 
        self.node_private_networking = node_private_networking 
        if instance_profile_arn is not APIHelper.SKIP:
            self.instance_profile_arn = instance_profile_arn 
        if instance_role_arn is not APIHelper.SKIP:
            self.instance_role_arn = instance_role_arn 
        if instance_role_permission_boundary is not APIHelper.SKIP:
            self.instance_role_permission_boundary = instance_role_permission_boundary 
        if security_group_ids is not APIHelper.SKIP:
            self.security_group_ids = security_group_ids 
        if availability_zone_ids is not APIHelper.SKIP:
            self.availability_zone_ids = availability_zone_ids 
        if labels is not APIHelper.SKIP:
            self.labels = labels 
        if tags is not APIHelper.SKIP:
            self.tags = tags 
        self.auto_create_service_roles = auto_create_service_roles 
        if enable_full_access_to_ecr is not APIHelper.SKIP:
            self.enable_full_access_to_ecr = enable_full_access_to_ecr 
        if enable_asg_access is not APIHelper.SKIP:
            self.enable_asg_access = enable_asg_access 
        if enable_dns_access is not APIHelper.SKIP:
            self.enable_dns_access = enable_dns_access 
        if enable_app_mesh_access is not APIHelper.SKIP:
            self.enable_app_mesh_access = enable_app_mesh_access 
        if enable_alb_access is not APIHelper.SKIP:
            self.enable_alb_access = enable_alb_access 
        if enable_efs_access is not APIHelper.SKIP:
            self.enable_efs_access = enable_efs_access 

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
        is_wavelength_zone = dictionary.get("isWavelengthZone") if dictionary.get("isWavelengthZone") else False
        is_managed_node_group = dictionary.get("isManagedNodeGroup") if dictionary.get("isManagedNodeGroup") else False
        is_spot_instance_needed = dictionary.get("isSpotInstanceNeeded") if dictionary.get("isSpotInstanceNeeded") else False
        end_point_access_type = dictionary.get("endPointAccessType") if dictionary.get("endPointAccessType") else 'private'
        instance_type = dictionary.get("instanceType") if dictionary.get("instanceType") else 'm5.xlarge'
        nodes = dictionary.get("nodes") if dictionary.get("nodes") else 2
        nodes_min = dictionary.get("nodesMin") if dictionary.get("nodesMin") else APIHelper.SKIP
        nodes_max = dictionary.get("nodesMax") if dictionary.get("nodesMax") else APIHelper.SKIP
        node_volume_type = dictionary.get("nodeVolumeType") if dictionary.get("nodeVolumeType") else APIHelper.SKIP
        subnet_cidr_block = dictionary.get("subnetCidrBlock") if dictionary.get("subnetCidrBlock") else APIHelper.SKIP
        node_ami_family = dictionary.get("nodeAmiFamily") if dictionary.get("nodeAmiFamily") else 'AmazonLinux2'
        node_volume_size = dictionary.get("nodeVolumeSize") if dictionary.get("nodeVolumeSize") else APIHelper.SKIP
        key_name = dictionary.get("keyName") if dictionary.get("keyName") else APIHelper.SKIP
        max_pod_per_node = dictionary.get("maxPodPerNode") if dictionary.get("maxPodPerNode") else APIHelper.SKIP
        use_volume_encryption = dictionary.get("useVolumeEncryption") if dictionary.get("useVolumeEncryption") else True
        node_private_networking = dictionary.get("nodePrivateNetworking") if dictionary.get("nodePrivateNetworking") else False
        instance_profile_arn = dictionary.get("instanceProfileArn") if dictionary.get("instanceProfileArn") else APIHelper.SKIP
        instance_role_arn = dictionary.get("instanceRoleArn") if dictionary.get("instanceRoleArn") else APIHelper.SKIP
        instance_role_permission_boundary = dictionary.get("instanceRolePermissionBoundary") if dictionary.get("instanceRolePermissionBoundary") else APIHelper.SKIP
        security_group_ids = None
        if dictionary.get('securityGroupIds') is not None:
            security_group_ids = [IdList.from_dictionary(x) for x in dictionary.get('securityGroupIds')]
        else:
            security_group_ids = APIHelper.SKIP
        availability_zone_ids = None
        if dictionary.get('availabilityZoneIds') is not None:
            availability_zone_ids = [IdList.from_dictionary(x) for x in dictionary.get('availabilityZoneIds')]
        else:
            availability_zone_ids = APIHelper.SKIP
        labels = NodeConfigurationLabel.from_dictionary(dictionary.get('labels')) if 'labels' in dictionary.keys() else APIHelper.SKIP
        tags = NodeConfigurationTag.from_dictionary(dictionary.get('tags')) if 'tags' in dictionary.keys() else APIHelper.SKIP
        auto_create_service_roles = dictionary.get("autoCreateServiceRoles") if dictionary.get("autoCreateServiceRoles") else True
        enable_full_access_to_ecr = dictionary.get("enableFullAccessToEcr") if "enableFullAccessToEcr" in dictionary.keys() else APIHelper.SKIP
        enable_asg_access = dictionary.get("enableAsgAccess") if "enableAsgAccess" in dictionary.keys() else APIHelper.SKIP
        enable_dns_access = dictionary.get("enableDnsAccess") if "enableDnsAccess" in dictionary.keys() else APIHelper.SKIP
        enable_app_mesh_access = dictionary.get("enableAppMeshAccess") if "enableAppMeshAccess" in dictionary.keys() else APIHelper.SKIP
        enable_alb_access = dictionary.get("enableAlbAccess") if "enableAlbAccess" in dictionary.keys() else APIHelper.SKIP
        enable_efs_access = dictionary.get("enableEfsAccess") if "enableEfsAccess" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   is_wavelength_zone,
                   is_managed_node_group,
                   is_spot_instance_needed,
                   end_point_access_type,
                   instance_type,
                   nodes,
                   nodes_min,
                   nodes_max,
                   node_volume_type,
                   subnet_cidr_block,
                   node_ami_family,
                   node_volume_size,
                   key_name,
                   max_pod_per_node,
                   use_volume_encryption,
                   node_private_networking,
                   instance_profile_arn,
                   instance_role_arn,
                   instance_role_permission_boundary,
                   security_group_ids,
                   availability_zone_ids,
                   labels,
                   tags,
                   auto_create_service_roles,
                   enable_full_access_to_ecr,
                   enable_asg_access,
                   enable_dns_access,
                   enable_app_mesh_access,
                   enable_alb_access,
                   enable_efs_access)

# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.repository import Repository


class CustomWf(object):

    """Implementation of the 'CustomWf' model.

    `customWf` attribute of a service.

    Attributes:
        event_name (string): Custom event being created for a workflow.
        upload_type (UploadTypeEnum): Allowed values are: GIT files
            (PULL_FROM_REPO), MANUAL_UPLOAD.
        repository_id (string): Repository ID for an existing repository.
        repository (Repository): Users can create a repository to maintain
            service artifacts. Repository would be either a Git or HELM
            repository.
        source_code_type (SourceCodeTypeEnum): Source code type can be JAVA or
            GO.
        revision_type (WorkloadRevisionTypeEnum): Revision type can be a
            BRANCH or TAG.
        name (string): Branch or tag name.
        path (string): The workflow path.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "event_name": 'eventName',
        "upload_type": 'uploadType',
        "repository_id": 'repositoryId',
        "repository": 'repository',
        "source_code_type": 'sourceCodeType',
        "revision_type": 'revisionType',
        "name": 'name',
        "path": 'path'
    }

    _optionals = [
        'event_name',
        'upload_type',
        'repository_id',
        'repository',
        'source_code_type',
        'revision_type',
        'name',
        'path',
    ]

    def __init__(self,
                 event_name=APIHelper.SKIP,
                 upload_type=APIHelper.SKIP,
                 repository_id=APIHelper.SKIP,
                 repository=APIHelper.SKIP,
                 source_code_type=APIHelper.SKIP,
                 revision_type=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 path=APIHelper.SKIP):
        """Constructor for the CustomWf class"""

        # Initialize members of the class
        if event_name is not APIHelper.SKIP:
            self.event_name = event_name 
        if upload_type is not APIHelper.SKIP:
            self.upload_type = upload_type 
        if repository_id is not APIHelper.SKIP:
            self.repository_id = repository_id 
        if repository is not APIHelper.SKIP:
            self.repository = repository 
        if source_code_type is not APIHelper.SKIP:
            self.source_code_type = source_code_type 
        if revision_type is not APIHelper.SKIP:
            self.revision_type = revision_type 
        if name is not APIHelper.SKIP:
            self.name = name 
        if path is not APIHelper.SKIP:
            self.path = path 

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

        event_name = dictionary.get("eventName") if dictionary.get("eventName") else APIHelper.SKIP
        upload_type = dictionary.get("uploadType") if dictionary.get("uploadType") else APIHelper.SKIP
        repository_id = dictionary.get("repositoryId") if dictionary.get("repositoryId") else APIHelper.SKIP
        repository = Repository.from_dictionary(dictionary.get('repository')) if 'repository' in dictionary.keys() else APIHelper.SKIP
        source_code_type = dictionary.get("sourceCodeType") if dictionary.get("sourceCodeType") else APIHelper.SKIP
        revision_type = dictionary.get("revisionType") if dictionary.get("revisionType") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        path = dictionary.get("path") if dictionary.get("path") else APIHelper.SKIP
        # Return an object of this model
        return cls(event_name,
                   upload_type,
                   repository_id,
                   repository,
                   source_code_type,
                   revision_type,
                   name,
                   path)

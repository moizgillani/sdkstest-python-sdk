# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.custom_wf import CustomWf
from verizon.models.installation_wf import InstallationWf
from verizon.models.operations_wf import OperationsWf


class Workflow(object):

    """Implementation of the 'Workflow' model.

    Workflow attribute of a service.

    Attributes:
        name (string): The service version workflow name.
        version (string): The service version workflow value.
        id (string): Auto-generated UUID for each workdflow triggered.
        mtype (WorkflowTypeEnum): Service type e.g. Installation, Operations,
            Custom.
        installation_wf (InstallationWf): `installationWf` attribute of a
            service.
        operations_wf (OperationsWf): `operationsWf` attribute of a service.
        custom_wf (CustomWf): `customWf` attribute of a service.
        files (list of string): Files which are being generated.
        status (string): Status of the workflow.
        created_date (datetime): The date on which the workflow is created.
        last_modified_date (datetime): The date when the created workflow was
            last modified.
        created_by (string): Identity of the user who created the workflow.
        updated_by (string): Identity of the user who updated the workflow.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "version": 'version',
        "id": 'id',
        "mtype": 'type',
        "installation_wf": 'installationWf',
        "operations_wf": 'operationsWf',
        "custom_wf": 'customWf',
        "files": 'files',
        "status": 'status',
        "created_date": 'createdDate',
        "last_modified_date": 'lastModifiedDate',
        "created_by": 'createdBy',
        "updated_by": 'updatedBy'
    }

    _optionals = [
        'id',
        'mtype',
        'installation_wf',
        'operations_wf',
        'custom_wf',
        'files',
        'status',
        'created_date',
        'last_modified_date',
        'created_by',
        'updated_by',
    ]

    def __init__(self,
                 name=None,
                 version=None,
                 id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 installation_wf=APIHelper.SKIP,
                 operations_wf=APIHelper.SKIP,
                 custom_wf=APIHelper.SKIP,
                 files=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_date=APIHelper.SKIP,
                 last_modified_date=APIHelper.SKIP,
                 created_by=APIHelper.SKIP,
                 updated_by=APIHelper.SKIP):
        """Constructor for the Workflow class"""

        # Initialize members of the class
        self.name = name 
        self.version = version 
        if id is not APIHelper.SKIP:
            self.id = id 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if installation_wf is not APIHelper.SKIP:
            self.installation_wf = installation_wf 
        if operations_wf is not APIHelper.SKIP:
            self.operations_wf = operations_wf 
        if custom_wf is not APIHelper.SKIP:
            self.custom_wf = custom_wf 
        if files is not APIHelper.SKIP:
            self.files = files 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_date is not APIHelper.SKIP:
            self.created_date = APIHelper.RFC3339DateTime(created_date) if created_date else None 
        if last_modified_date is not APIHelper.SKIP:
            self.last_modified_date = APIHelper.RFC3339DateTime(last_modified_date) if last_modified_date else None 
        if created_by is not APIHelper.SKIP:
            self.created_by = created_by 
        if updated_by is not APIHelper.SKIP:
            self.updated_by = updated_by 

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

        name = dictionary.get("name") if dictionary.get("name") else None
        version = dictionary.get("version") if dictionary.get("version") else None
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        installation_wf = InstallationWf.from_dictionary(dictionary.get('installationWf')) if 'installationWf' in dictionary.keys() else APIHelper.SKIP
        operations_wf = OperationsWf.from_dictionary(dictionary.get('operationsWf')) if 'operationsWf' in dictionary.keys() else APIHelper.SKIP
        custom_wf = CustomWf.from_dictionary(dictionary.get('customWf')) if 'customWf' in dictionary.keys() else APIHelper.SKIP
        files = dictionary.get("files") if dictionary.get("files") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        created_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdDate")).datetime if dictionary.get("createdDate") else APIHelper.SKIP
        last_modified_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastModifiedDate")).datetime if dictionary.get("lastModifiedDate") else APIHelper.SKIP
        created_by = dictionary.get("createdBy") if dictionary.get("createdBy") else APIHelper.SKIP
        updated_by = dictionary.get("updatedBy") if dictionary.get("updatedBy") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   version,
                   id,
                   mtype,
                   installation_wf,
                   operations_wf,
                   custom_wf,
                   files,
                   status,
                   created_date,
                   last_modified_date,
                   created_by,
                   updated_by)

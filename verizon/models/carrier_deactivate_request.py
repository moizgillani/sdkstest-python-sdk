# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.custom_fields import CustomFields


class CarrierDeactivateRequest(object):

    """Implementation of the 'CarrierDeactivateRequest' model.

    Request to deactivate a carrier.

    Attributes:
        account_name (string): The name of a billing account.
        custom_fields (list of CustomFields): Custom field names and values,
            if you want to only include devices that have matching values.
        devices (list of AccountDeviceList): The devices for which you want to
            deactivate service, specified by device identifier.
        etf_waiver (bool): Fees may be assessed for deactivating Verizon
            Wireless devices, depending on the account contract. The etfWaiver
            parameter waives the Early Termination Fee (ETF), if applicable.
        group_name (string): The name of a device group, if you want to
            deactivate all devices in that group.
        reason_code (string): Code identifying the reason for the
            deactivation. Currently the only valid reason code is “FF”, which
            corresponds to General Admin/Maintenance.
        service_plan (string): The name of a service plan, if you want to only
            include devices that have that service plan.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "custom_fields": 'customFields',
        "devices": 'devices',
        "etf_waiver": 'etfWaiver',
        "group_name": 'groupName',
        "reason_code": 'reasonCode',
        "service_plan": 'servicePlan'
    }

    _optionals = [
        'account_name',
        'custom_fields',
        'devices',
        'etf_waiver',
        'group_name',
        'reason_code',
        'service_plan',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 devices=APIHelper.SKIP,
                 etf_waiver=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 reason_code=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP):
        """Constructor for the CarrierDeactivateRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if etf_waiver is not APIHelper.SKIP:
            self.etf_waiver = etf_waiver 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if reason_code is not APIHelper.SKIP:
            self.reason_code = reason_code 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 

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

        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [CustomFields.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        devices = None
        if dictionary.get('devices') is not None:
            devices = [AccountDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        etf_waiver = dictionary.get("etfWaiver") if "etfWaiver" in dictionary.keys() else APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        reason_code = dictionary.get("reasonCode") if dictionary.get("reasonCode") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   custom_fields,
                   devices,
                   etf_waiver,
                   group_name,
                   reason_code,
                   service_plan)

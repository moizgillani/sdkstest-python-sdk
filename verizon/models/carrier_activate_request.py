# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.custom_fields import CustomFields
from verizon.models.place_of_use import PlaceOfUse


class CarrierActivateRequest(object):

    """Implementation of the 'CarrierActivateRequest' model.

    Request for carrier activation.

    Attributes:
        account_name (string): The name of a billing account.
        carrier_ip_pool_name (string): The private IP pool (Carrier Group
            Name) from which your device IP addresses will be derived.
        carrier_name (string): The carrier that will perform the activation.
        cost_center_code (string): A string to identify the cost center that
            the device is associated with.
        custom_fields (list of CustomFields): A user-defined descriptive
            field, limited to 50 characters.
        devices (list of AccountDeviceList): Up to 10,000 devices for which
            you want to activate service, specified by device identifier.
        group_name (string): If you specify devices by ID in the devices
            parameters, this is the name of a device group that the devices
            should be added to.If you don't specify individual devices with
            the devices parameter, you can provide the name of a device group
            to activate all devices in that group.
        lead_id (string): The ID of a “Qualified” or “Closed - Won” VPP
            customer lead, which is used with other values to determine MDN
            assignment, taxation, and compensation.
        mdn_zip_code (string): The Zip code of the location where the line of
            service will primarily be used, or a Zip code that you have been
            told to use with these devices. For accounts that are configured
            for geographic numbering, this is the ZIP code from which the MDN
            will be derived.
        primary_place_of_use (PlaceOfUse): The customer name and the address
            of the device's primary place of use. Leave these fields empty to
            use the account profile address as the primary place of use. These
            values will be applied to all devices in the request.If the
            account is enabled for non-geographic MDNs and the device supports
            it, the primaryPlaceOfUse address will also be used to derive the
            MDN for the device.
        public_ip_restriction (string): For devices with static IP addresses
            on the public network, this specifies whether the devices have
            general access to the Internet.
        service_plan (string): The service plan code that you want to assign
            to all specified devices.
        sku_number (string): The Stock Keeping Unit (SKU) of a 4G device type
            can be used with ICCID device identifiers in lieu of an IMEI when
            activating 4G devices. The SkuNumber will be used with all devices
            in the request, so all devices must be of the same type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "carrier_ip_pool_name": 'carrierIpPoolName',
        "carrier_name": 'carrierName',
        "cost_center_code": 'costCenterCode',
        "custom_fields": 'customFields',
        "devices": 'devices',
        "group_name": 'groupName',
        "lead_id": 'leadId',
        "mdn_zip_code": 'mdnZipCode',
        "primary_place_of_use": 'primaryPlaceOfUse',
        "public_ip_restriction": 'publicIpRestriction',
        "service_plan": 'servicePlan',
        "sku_number": 'skuNumber'
    }

    _optionals = [
        'account_name',
        'carrier_ip_pool_name',
        'carrier_name',
        'cost_center_code',
        'custom_fields',
        'devices',
        'group_name',
        'lead_id',
        'mdn_zip_code',
        'primary_place_of_use',
        'public_ip_restriction',
        'service_plan',
        'sku_number',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 carrier_ip_pool_name=APIHelper.SKIP,
                 carrier_name=APIHelper.SKIP,
                 cost_center_code=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 devices=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 lead_id=APIHelper.SKIP,
                 mdn_zip_code=APIHelper.SKIP,
                 primary_place_of_use=APIHelper.SKIP,
                 public_ip_restriction=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 sku_number=APIHelper.SKIP):
        """Constructor for the CarrierActivateRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if carrier_ip_pool_name is not APIHelper.SKIP:
            self.carrier_ip_pool_name = carrier_ip_pool_name 
        if carrier_name is not APIHelper.SKIP:
            self.carrier_name = carrier_name 
        if cost_center_code is not APIHelper.SKIP:
            self.cost_center_code = cost_center_code 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if lead_id is not APIHelper.SKIP:
            self.lead_id = lead_id 
        if mdn_zip_code is not APIHelper.SKIP:
            self.mdn_zip_code = mdn_zip_code 
        if primary_place_of_use is not APIHelper.SKIP:
            self.primary_place_of_use = primary_place_of_use 
        if public_ip_restriction is not APIHelper.SKIP:
            self.public_ip_restriction = public_ip_restriction 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
        if sku_number is not APIHelper.SKIP:
            self.sku_number = sku_number 

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
        carrier_ip_pool_name = dictionary.get("carrierIpPoolName") if dictionary.get("carrierIpPoolName") else APIHelper.SKIP
        carrier_name = dictionary.get("carrierName") if dictionary.get("carrierName") else APIHelper.SKIP
        cost_center_code = dictionary.get("costCenterCode") if dictionary.get("costCenterCode") else APIHelper.SKIP
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
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        lead_id = dictionary.get("leadId") if dictionary.get("leadId") else APIHelper.SKIP
        mdn_zip_code = dictionary.get("mdnZipCode") if dictionary.get("mdnZipCode") else APIHelper.SKIP
        primary_place_of_use = PlaceOfUse.from_dictionary(dictionary.get('primaryPlaceOfUse')) if 'primaryPlaceOfUse' in dictionary.keys() else APIHelper.SKIP
        public_ip_restriction = dictionary.get("publicIpRestriction") if dictionary.get("publicIpRestriction") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        sku_number = dictionary.get("skuNumber") if dictionary.get("skuNumber") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   carrier_ip_pool_name,
                   carrier_name,
                   cost_center_code,
                   custom_fields,
                   devices,
                   group_name,
                   lead_id,
                   mdn_zip_code,
                   primary_place_of_use,
                   public_ip_restriction,
                   service_plan,
                   sku_number)

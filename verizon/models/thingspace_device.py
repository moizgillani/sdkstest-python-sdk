# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.carrier_information import CarrierInformation
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId


class ThingspaceDevice(object):

    """Implementation of the 'ThingspaceDevice' model.

    Device that exist in Verizon Mobile Device Management (MDM).

    Attributes:
        account_name (string): The billing account that the device is
            associated with.
        billing_cycle_end_date (string): The date that the device's current
            billing cycle ends.
        carrier_informations (list of CarrierInformation): The carrier
            information associated with the device.
        connected (bool): True if the device is connected; false if it is
            not.
        created_at (string): The date and time that the device was added to
            the system.
        custom_fields (list of CustomFields): The custom fields and values
            that have been set for the device.
        device_ids (list of DeviceId): All identifiers for the device.
        extended_attributes (list of CustomFields): Any extended attributes
            for the device, as Key and Value pairs. The pairs listed below are
            returned as part of the response for a single device, but are not
            included if the request was for information about multiple
            devices.
        group_names (list of string): The device groups that the device
            belongs to.
        ip_address (string): The IP address of the device.
        last_activation_by (string): The user who last activated the device.
        last_activation_date (string): The date and time that the device was
            last activated.
        last_connection_date (string): The most recent connection date and
            time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "billing_cycle_end_date": 'billingCycleEndDate',
        "carrier_informations": 'carrierInformations',
        "connected": 'connected',
        "created_at": 'createdAt',
        "custom_fields": 'customFields',
        "device_ids": 'deviceIds',
        "extended_attributes": 'extendedAttributes',
        "group_names": 'groupNames',
        "ip_address": 'ipAddress',
        "last_activation_by": 'lastActivationBy',
        "last_activation_date": 'lastActivationDate',
        "last_connection_date": 'lastConnectionDate'
    }

    _optionals = [
        'account_name',
        'billing_cycle_end_date',
        'carrier_informations',
        'connected',
        'created_at',
        'custom_fields',
        'device_ids',
        'extended_attributes',
        'group_names',
        'ip_address',
        'last_activation_by',
        'last_activation_date',
        'last_connection_date',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 billing_cycle_end_date=APIHelper.SKIP,
                 carrier_informations=APIHelper.SKIP,
                 connected=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 device_ids=APIHelper.SKIP,
                 extended_attributes=APIHelper.SKIP,
                 group_names=APIHelper.SKIP,
                 ip_address=APIHelper.SKIP,
                 last_activation_by=APIHelper.SKIP,
                 last_activation_date=APIHelper.SKIP,
                 last_connection_date=APIHelper.SKIP):
        """Constructor for the ThingspaceDevice class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if billing_cycle_end_date is not APIHelper.SKIP:
            self.billing_cycle_end_date = billing_cycle_end_date 
        if carrier_informations is not APIHelper.SKIP:
            self.carrier_informations = carrier_informations 
        if connected is not APIHelper.SKIP:
            self.connected = connected 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if device_ids is not APIHelper.SKIP:
            self.device_ids = device_ids 
        if extended_attributes is not APIHelper.SKIP:
            self.extended_attributes = extended_attributes 
        if group_names is not APIHelper.SKIP:
            self.group_names = group_names 
        if ip_address is not APIHelper.SKIP:
            self.ip_address = ip_address 
        if last_activation_by is not APIHelper.SKIP:
            self.last_activation_by = last_activation_by 
        if last_activation_date is not APIHelper.SKIP:
            self.last_activation_date = last_activation_date 
        if last_connection_date is not APIHelper.SKIP:
            self.last_connection_date = last_connection_date 

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
        billing_cycle_end_date = dictionary.get("billingCycleEndDate") if dictionary.get("billingCycleEndDate") else APIHelper.SKIP
        carrier_informations = None
        if dictionary.get('carrierInformations') is not None:
            carrier_informations = [CarrierInformation.from_dictionary(x) for x in dictionary.get('carrierInformations')]
        else:
            carrier_informations = APIHelper.SKIP
        connected = dictionary.get("connected") if "connected" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("createdAt") if dictionary.get("createdAt") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [CustomFields.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        device_ids = None
        if dictionary.get('deviceIds') is not None:
            device_ids = [DeviceId.from_dictionary(x) for x in dictionary.get('deviceIds')]
        else:
            device_ids = APIHelper.SKIP
        extended_attributes = None
        if dictionary.get('extendedAttributes') is not None:
            extended_attributes = [CustomFields.from_dictionary(x) for x in dictionary.get('extendedAttributes')]
        else:
            extended_attributes = APIHelper.SKIP
        group_names = dictionary.get("groupNames") if dictionary.get("groupNames") else APIHelper.SKIP
        ip_address = dictionary.get("ipAddress") if dictionary.get("ipAddress") else APIHelper.SKIP
        last_activation_by = dictionary.get("lastActivationBy") if dictionary.get("lastActivationBy") else APIHelper.SKIP
        last_activation_date = dictionary.get("lastActivationDate") if dictionary.get("lastActivationDate") else APIHelper.SKIP
        last_connection_date = dictionary.get("lastConnectionDate") if dictionary.get("lastConnectionDate") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   billing_cycle_end_date,
                   carrier_informations,
                   connected,
                   created_at,
                   custom_fields,
                   device_ids,
                   extended_attributes,
                   group_names,
                   ip_address,
                   last_activation_by,
                   last_activation_date,
                   last_connection_date)

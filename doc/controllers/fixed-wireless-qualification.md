# Fixed Wireless Qualification

```python
fixed_wireless_qualification_controller = client.fixed_wireless_qualification
```

## Class Name

`FixedWirelessQualificationController`


# Domestic 4 G and 5G Fixed Wireless Qualification

Use this query for Fixed Wireless Qualification of an address. Network types include: LTE, C-BAND and MMWAVE.

```python
def domestic_4_g_and_5g_fixed_wireless_qualification(self,
                                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetWirelessCoverageRequestFWA`](../../doc/models/get-wireless-coverage-request-fwa.md) | Body, Required | Request for network coverage details. |

## Response Type

[`WNPRequestResponse`](../../doc/models/wnp-request-response.md)

## Example Usage

```python
body = GetWirelessCoverageRequestFWA(
    account_name='0000123456-00001',
    request_type='FWA',
    location_type='ADDRESS',
    locations=Locations(),
    network_types_list=[
        NetworkType(
            network_type='LTE'
        )
    ]
)

result = fixed_wireless_qualification_controller.domestic_4_g_and_5g_fixed_wireless_qualification(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`WNPRestErrorResponseException`](../../doc/models/wnp-rest-error-response-exception.md) |


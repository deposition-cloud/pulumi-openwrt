# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetWirelessWifiDeviceResult',
    'AwaitableGetWirelessWifiDeviceResult',
    'get_wireless_wifi_device',
    'get_wireless_wifi_device_output',
]

@pulumi.output_type
class GetWirelessWifiDeviceResult:
    """
    A collection of values returned by getWirelessWifiDevice.
    """
    def __init__(__self__, band=None, cell_density=None, channel=None, country=None, htmode=None, id=None, path=None, type=None):
        if band and not isinstance(band, str):
            raise TypeError("Expected argument 'band' to be a str")
        pulumi.set(__self__, "band", band)
        if cell_density and not isinstance(cell_density, int):
            raise TypeError("Expected argument 'cell_density' to be a int")
        pulumi.set(__self__, "cell_density", cell_density)
        if channel and not isinstance(channel, str):
            raise TypeError("Expected argument 'channel' to be a str")
        pulumi.set(__self__, "channel", channel)
        if country and not isinstance(country, str):
            raise TypeError("Expected argument 'country' to be a str")
        pulumi.set(__self__, "country", country)
        if htmode and not isinstance(htmode, str):
            raise TypeError("Expected argument 'htmode' to be a str")
        pulumi.set(__self__, "htmode", htmode)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def band(self) -> str:
        """
        Channel width. Must be one of: "2g", "5g", "6g".
        """
        return pulumi.get(self, "band")

    @property
    @pulumi.getter(name="cellDensity")
    def cell_density(self) -> int:
        """
        Configures data rates based on the coverage cell density. Must be one of 0, 1, 2, 3.
        """
        return pulumi.get(self, "cell_density")

    @property
    @pulumi.getter
    def channel(self) -> str:
        """
        The wireless channel. Currently, only "auto" is supported.
        """
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter
    def country(self) -> str:
        """
        Two-digit country code. E.g. "US".
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def htmode(self) -> str:
        """
        Channel width. Must be one of: "HE20", "HE40", "HE80", "HE160", "HT20", "HT40", "HT40-", "HT40+", "NONE", "VHT20", "VHT40", "VHT80", "VHT160".
        """
        return pulumi.get(self, "htmode")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Name of the section. This name is only used when interacting with UCI directly.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path of the device in `/sys/devices`.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of device. Currently only "mac80211" is supported.
        """
        return pulumi.get(self, "type")


class AwaitableGetWirelessWifiDeviceResult(GetWirelessWifiDeviceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWirelessWifiDeviceResult(
            band=self.band,
            cell_density=self.cell_density,
            channel=self.channel,
            country=self.country,
            htmode=self.htmode,
            id=self.id,
            path=self.path,
            type=self.type)


def get_wireless_wifi_device(id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWirelessWifiDeviceResult:
    """
    The physical radio device.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    testing = openwrt.get_wireless_wifi_device(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('openwrt:index/getWirelessWifiDevice:getWirelessWifiDevice', __args__, opts=opts, typ=GetWirelessWifiDeviceResult).value

    return AwaitableGetWirelessWifiDeviceResult(
        band=pulumi.get(__ret__, 'band'),
        cell_density=pulumi.get(__ret__, 'cell_density'),
        channel=pulumi.get(__ret__, 'channel'),
        country=pulumi.get(__ret__, 'country'),
        htmode=pulumi.get(__ret__, 'htmode'),
        id=pulumi.get(__ret__, 'id'),
        path=pulumi.get(__ret__, 'path'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_wireless_wifi_device)
def get_wireless_wifi_device_output(id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWirelessWifiDeviceResult]:
    """
    The physical radio device.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    testing = openwrt.get_wireless_wifi_device(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    ...

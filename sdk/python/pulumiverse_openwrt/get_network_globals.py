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
    'GetNetworkGlobalsResult',
    'AwaitableGetNetworkGlobalsResult',
    'get_network_globals',
    'get_network_globals_output',
]

@pulumi.output_type
class GetNetworkGlobalsResult:
    """
    A collection of values returned by getNetworkGlobals.
    """
    def __init__(__self__, id=None, packet_steering=None, ula_prefix=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if packet_steering and not isinstance(packet_steering, bool):
            raise TypeError("Expected argument 'packet_steering' to be a bool")
        pulumi.set(__self__, "packet_steering", packet_steering)
        if ula_prefix and not isinstance(ula_prefix, str):
            raise TypeError("Expected argument 'ula_prefix' to be a str")
        pulumi.set(__self__, "ula_prefix", ula_prefix)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Name of the section. This name is only used when interacting with UCI directly.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="packetSteering")
    def packet_steering(self) -> bool:
        """
        Use every CPU to handle packet traffic.
        """
        return pulumi.get(self, "packet_steering")

    @property
    @pulumi.getter(name="ulaPrefix")
    def ula_prefix(self) -> str:
        """
        IPv6 ULA prefix for this device.
        """
        return pulumi.get(self, "ula_prefix")


class AwaitableGetNetworkGlobalsResult(GetNetworkGlobalsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkGlobalsResult(
            id=self.id,
            packet_steering=self.packet_steering,
            ula_prefix=self.ula_prefix)


def get_network_globals(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkGlobalsResult:
    """
    Contains interface-independent options affecting the network configuration in general.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    this = openwrt.get_network_globals(id="globals")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('openwrt:index/getNetworkGlobals:getNetworkGlobals', __args__, opts=opts, typ=GetNetworkGlobalsResult).value

    return AwaitableGetNetworkGlobalsResult(
        id=pulumi.get(__ret__, 'id'),
        packet_steering=pulumi.get(__ret__, 'packet_steering'),
        ula_prefix=pulumi.get(__ret__, 'ula_prefix'))


@_utilities.lift_output_func(get_network_globals)
def get_network_globals_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkGlobalsResult]:
    """
    Contains interface-independent options affecting the network configuration in general.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    this = openwrt.get_network_globals(id="globals")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    ...
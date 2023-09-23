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
    'GetNetworkInterfaceResult',
    'AwaitableGetNetworkInterfaceResult',
    'get_network_interface',
    'get_network_interface_output',
]

@pulumi.output_type
class GetNetworkInterfaceResult:
    """
    A collection of values returned by getNetworkInterface.
    """
    def __init__(__self__, auto=None, device=None, disabled=None, dns=None, gateway=None, id=None, ip6assign=None, ipaddr=None, macaddr=None, mtu=None, netmask=None, peerdns=None, proto=None, reqaddress=None, reqprefix=None):
        if auto and not isinstance(auto, bool):
            raise TypeError("Expected argument 'auto' to be a bool")
        pulumi.set(__self__, "auto", auto)
        if device and not isinstance(device, str):
            raise TypeError("Expected argument 'device' to be a str")
        pulumi.set(__self__, "device", device)
        if disabled and not isinstance(disabled, bool):
            raise TypeError("Expected argument 'disabled' to be a bool")
        pulumi.set(__self__, "disabled", disabled)
        if dns and not isinstance(dns, list):
            raise TypeError("Expected argument 'dns' to be a list")
        pulumi.set(__self__, "dns", dns)
        if gateway and not isinstance(gateway, str):
            raise TypeError("Expected argument 'gateway' to be a str")
        pulumi.set(__self__, "gateway", gateway)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip6assign and not isinstance(ip6assign, int):
            raise TypeError("Expected argument 'ip6assign' to be a int")
        pulumi.set(__self__, "ip6assign", ip6assign)
        if ipaddr and not isinstance(ipaddr, str):
            raise TypeError("Expected argument 'ipaddr' to be a str")
        pulumi.set(__self__, "ipaddr", ipaddr)
        if macaddr and not isinstance(macaddr, str):
            raise TypeError("Expected argument 'macaddr' to be a str")
        pulumi.set(__self__, "macaddr", macaddr)
        if mtu and not isinstance(mtu, int):
            raise TypeError("Expected argument 'mtu' to be a int")
        pulumi.set(__self__, "mtu", mtu)
        if netmask and not isinstance(netmask, str):
            raise TypeError("Expected argument 'netmask' to be a str")
        pulumi.set(__self__, "netmask", netmask)
        if peerdns and not isinstance(peerdns, bool):
            raise TypeError("Expected argument 'peerdns' to be a bool")
        pulumi.set(__self__, "peerdns", peerdns)
        if proto and not isinstance(proto, str):
            raise TypeError("Expected argument 'proto' to be a str")
        pulumi.set(__self__, "proto", proto)
        if reqaddress and not isinstance(reqaddress, str):
            raise TypeError("Expected argument 'reqaddress' to be a str")
        pulumi.set(__self__, "reqaddress", reqaddress)
        if reqprefix and not isinstance(reqprefix, str):
            raise TypeError("Expected argument 'reqprefix' to be a str")
        pulumi.set(__self__, "reqprefix", reqprefix)

    @property
    @pulumi.getter
    def auto(self) -> bool:
        """
        Specifies whether to bring up this interface on boot.
        """
        return pulumi.get(self, "auto")

    @property
    @pulumi.getter
    def device(self) -> str:
        return pulumi.get(self, "device")

    @property
    @pulumi.getter
    def disabled(self) -> bool:
        """
        Disables this interface.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def dns(self) -> Sequence[str]:
        """
        DNS servers
        """
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter
    def gateway(self) -> str:
        """
        Gateway of the interface
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Name of the section. This name is only used when interacting with UCI directly.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip6assign(self) -> int:
        """
        Delegate a prefix of given length to this interface
        """
        return pulumi.get(self, "ip6assign")

    @property
    @pulumi.getter
    def ipaddr(self) -> str:
        """
        IP address of the interface
        """
        return pulumi.get(self, "ipaddr")

    @property
    @pulumi.getter
    def macaddr(self) -> str:
        """
        Override the MAC Address of this interface.
        """
        return pulumi.get(self, "macaddr")

    @property
    @pulumi.getter
    def mtu(self) -> int:
        """
        Override the default MTU on this interface.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def netmask(self) -> str:
        """
        Netmask of the interface
        """
        return pulumi.get(self, "netmask")

    @property
    @pulumi.getter
    def peerdns(self) -> bool:
        """
        Use DHCP-provided DNS servers.
        """
        return pulumi.get(self, "peerdns")

    @property
    @pulumi.getter
    def proto(self) -> str:
        """
        The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
        """
        return pulumi.get(self, "proto")

    @property
    @pulumi.getter
    def reqaddress(self) -> str:
        """
        Behavior for requesting address. Can only be one of "force", "try", or "none".
        """
        return pulumi.get(self, "reqaddress")

    @property
    @pulumi.getter
    def reqprefix(self) -> str:
        """
        Behavior for requesting prefixes. Currently, only "auto" is supported.
        """
        return pulumi.get(self, "reqprefix")


class AwaitableGetNetworkInterfaceResult(GetNetworkInterfaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInterfaceResult(
            auto=self.auto,
            device=self.device,
            disabled=self.disabled,
            dns=self.dns,
            gateway=self.gateway,
            id=self.id,
            ip6assign=self.ip6assign,
            ipaddr=self.ipaddr,
            macaddr=self.macaddr,
            mtu=self.mtu,
            netmask=self.netmask,
            peerdns=self.peerdns,
            proto=self.proto,
            reqaddress=self.reqaddress,
            reqprefix=self.reqprefix)


def get_network_interface(id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInterfaceResult:
    """
    A logic network.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    br_testing = openwrt.get_network_interface(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('openwrt:index/getNetworkInterface:getNetworkInterface', __args__, opts=opts, typ=GetNetworkInterfaceResult).value

    return AwaitableGetNetworkInterfaceResult(
        auto=pulumi.get(__ret__, 'auto'),
        device=pulumi.get(__ret__, 'device'),
        disabled=pulumi.get(__ret__, 'disabled'),
        dns=pulumi.get(__ret__, 'dns'),
        gateway=pulumi.get(__ret__, 'gateway'),
        id=pulumi.get(__ret__, 'id'),
        ip6assign=pulumi.get(__ret__, 'ip6assign'),
        ipaddr=pulumi.get(__ret__, 'ipaddr'),
        macaddr=pulumi.get(__ret__, 'macaddr'),
        mtu=pulumi.get(__ret__, 'mtu'),
        netmask=pulumi.get(__ret__, 'netmask'),
        peerdns=pulumi.get(__ret__, 'peerdns'),
        proto=pulumi.get(__ret__, 'proto'),
        reqaddress=pulumi.get(__ret__, 'reqaddress'),
        reqprefix=pulumi.get(__ret__, 'reqprefix'))


@_utilities.lift_output_func(get_network_interface)
def get_network_interface_output(id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkInterfaceResult]:
    """
    A logic network.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    br_testing = openwrt.get_network_interface(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    ...

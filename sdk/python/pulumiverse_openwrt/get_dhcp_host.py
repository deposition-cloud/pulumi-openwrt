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
    'GetDhcpHostResult',
    'AwaitableGetDhcpHostResult',
    'get_dhcp_host',
    'get_dhcp_host_output',
]

@pulumi.output_type
class GetDhcpHostResult:
    """
    A collection of values returned by getDhcpHost.
    """
    def __init__(__self__, dns=None, id=None, ip=None, mac=None, name=None):
        if dns and not isinstance(dns, bool):
            raise TypeError("Expected argument 'dns' to be a bool")
        pulumi.set(__self__, "dns", dns)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, str):
            raise TypeError("Expected argument 'ip' to be a str")
        pulumi.set(__self__, "ip", ip)
        if mac and not isinstance(mac, str):
            raise TypeError("Expected argument 'mac' to be a str")
        pulumi.set(__self__, "mac", mac)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def dns(self) -> bool:
        """
        Add static forward and reverse DNS entries for this host.
        """
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Name of the section. This name is only used when interacting with UCI directly.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> str:
        """
        The IP address to be used for this host, or `ignore` to ignore any DHCP request from this host.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def mac(self) -> str:
        """
        The hardware address(es) of this host, separated by spaces.
        """
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Hostname to assign.
        """
        return pulumi.get(self, "name")


class AwaitableGetDhcpHostResult(GetDhcpHostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDhcpHostResult(
            dns=self.dns,
            id=self.id,
            ip=self.ip,
            mac=self.mac,
            name=self.name)


def get_dhcp_host(id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDhcpHostResult:
    """
    Assign a fixed IP address to hosts.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    testing = openwrt.get_dhcp_host(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('openwrt:index/getDhcpHost:getDhcpHost', __args__, opts=opts, typ=GetDhcpHostResult).value

    return AwaitableGetDhcpHostResult(
        dns=pulumi.get(__ret__, 'dns'),
        id=pulumi.get(__ret__, 'id'),
        ip=pulumi.get(__ret__, 'ip'),
        mac=pulumi.get(__ret__, 'mac'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_dhcp_host)
def get_dhcp_host_output(id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDhcpHostResult]:
    """
    Assign a fixed IP address to hosts.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    testing = openwrt.get_dhcp_host(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    ...

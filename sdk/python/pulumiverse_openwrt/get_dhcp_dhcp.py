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
    'GetDhcpDhcpResult',
    'AwaitableGetDhcpDhcpResult',
    'get_dhcp_dhcp',
    'get_dhcp_dhcp_output',
]

@pulumi.output_type
class GetDhcpDhcpResult:
    """
    A collection of values returned by getDhcpDhcp.
    """
    def __init__(__self__, dhcpv4=None, dhcpv6=None, force=None, id=None, ignore=None, interface=None, leasetime=None, limit=None, ra=None, ra_flags=None, start=None):
        if dhcpv4 and not isinstance(dhcpv4, str):
            raise TypeError("Expected argument 'dhcpv4' to be a str")
        pulumi.set(__self__, "dhcpv4", dhcpv4)
        if dhcpv6 and not isinstance(dhcpv6, str):
            raise TypeError("Expected argument 'dhcpv6' to be a str")
        pulumi.set(__self__, "dhcpv6", dhcpv6)
        if force and not isinstance(force, bool):
            raise TypeError("Expected argument 'force' to be a bool")
        pulumi.set(__self__, "force", force)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ignore and not isinstance(ignore, bool):
            raise TypeError("Expected argument 'ignore' to be a bool")
        pulumi.set(__self__, "ignore", ignore)
        if interface and not isinstance(interface, str):
            raise TypeError("Expected argument 'interface' to be a str")
        pulumi.set(__self__, "interface", interface)
        if leasetime and not isinstance(leasetime, str):
            raise TypeError("Expected argument 'leasetime' to be a str")
        pulumi.set(__self__, "leasetime", leasetime)
        if limit and not isinstance(limit, int):
            raise TypeError("Expected argument 'limit' to be a int")
        pulumi.set(__self__, "limit", limit)
        if ra and not isinstance(ra, str):
            raise TypeError("Expected argument 'ra' to be a str")
        pulumi.set(__self__, "ra", ra)
        if ra_flags and not isinstance(ra_flags, list):
            raise TypeError("Expected argument 'ra_flags' to be a list")
        pulumi.set(__self__, "ra_flags", ra_flags)
        if start and not isinstance(start, int):
            raise TypeError("Expected argument 'start' to be a int")
        pulumi.set(__self__, "start", start)

    @property
    @pulumi.getter
    def dhcpv4(self) -> str:
        """
        The mode of the DHCPv4 server. Must be one of: "disabled", "server".
        """
        return pulumi.get(self, "dhcpv4")

    @property
    @pulumi.getter
    def dhcpv6(self) -> str:
        """
        The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
        """
        return pulumi.get(self, "dhcpv6")

    @property
    @pulumi.getter
    def force(self) -> bool:
        """
        Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
        """
        return pulumi.get(self, "force")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Name of the section. This name is only used when interacting with UCI directly.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ignore(self) -> bool:
        """
        Specifies whether dnsmasq should ignore this pool.
        """
        return pulumi.get(self, "ignore")

    @property
    @pulumi.getter
    def interface(self) -> str:
        return pulumi.get(self, "interface")

    @property
    @pulumi.getter
    def leasetime(self) -> str:
        """
        The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "leasetime")

    @property
    @pulumi.getter
    def limit(self) -> int:
        """
        Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter
    def ra(self) -> str:
        """
        The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
        """
        return pulumi.get(self, "ra")

    @property
    @pulumi.getter(name="raFlags")
    def ra_flags(self) -> Sequence[str]:
        """
        Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
        """
        return pulumi.get(self, "ra_flags")

    @property
    @pulumi.getter
    def start(self) -> int:
        """
        Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "start")


class AwaitableGetDhcpDhcpResult(GetDhcpDhcpResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDhcpDhcpResult(
            dhcpv4=self.dhcpv4,
            dhcpv6=self.dhcpv6,
            force=self.force,
            id=self.id,
            ignore=self.ignore,
            interface=self.interface,
            leasetime=self.leasetime,
            limit=self.limit,
            ra=self.ra,
            ra_flags=self.ra_flags,
            start=self.start)


def get_dhcp_dhcp(id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDhcpDhcpResult:
    """
    Per interface lease pools and settings for serving DHCP requests.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    testing = openwrt.get_dhcp_dhcp(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('openwrt:index/getDhcpDhcp:getDhcpDhcp', __args__, opts=opts, typ=GetDhcpDhcpResult).value

    return AwaitableGetDhcpDhcpResult(
        dhcpv4=pulumi.get(__ret__, 'dhcpv4'),
        dhcpv6=pulumi.get(__ret__, 'dhcpv6'),
        force=pulumi.get(__ret__, 'force'),
        id=pulumi.get(__ret__, 'id'),
        ignore=pulumi.get(__ret__, 'ignore'),
        interface=pulumi.get(__ret__, 'interface'),
        leasetime=pulumi.get(__ret__, 'leasetime'),
        limit=pulumi.get(__ret__, 'limit'),
        ra=pulumi.get(__ret__, 'ra'),
        ra_flags=pulumi.get(__ret__, 'ra_flags'),
        start=pulumi.get(__ret__, 'start'))


@_utilities.lift_output_func(get_dhcp_dhcp)
def get_dhcp_dhcp_output(id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDhcpDhcpResult]:
    """
    Per interface lease pools and settings for serving DHCP requests.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    testing = openwrt.get_dhcp_dhcp(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    ...
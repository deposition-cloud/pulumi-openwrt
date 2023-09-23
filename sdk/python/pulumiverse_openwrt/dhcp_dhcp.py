# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DhcpDhcpArgs', 'DhcpDhcp']

@pulumi.input_type
class DhcpDhcpArgs:
    def __init__(__self__, *,
                 dhcpv4: Optional[pulumi.Input[str]] = None,
                 dhcpv6: Optional[pulumi.Input[str]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 ignore: Optional[pulumi.Input[bool]] = None,
                 interface: Optional[pulumi.Input[str]] = None,
                 leasetime: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 ra: Optional[pulumi.Input[str]] = None,
                 ra_flags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 start: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a DhcpDhcp resource.
        :param pulumi.Input[str] dhcpv4: The mode of the DHCPv4 server. Must be one of: "disabled", "server".
        :param pulumi.Input[str] dhcpv6: The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
        :param pulumi.Input[bool] force: Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
        :param pulumi.Input[bool] ignore: Specifies whether dnsmasq should ignore this pool.
        :param pulumi.Input[str] interface: The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
               field in Terraform. Required if `ignore` is not `true`.
        :param pulumi.Input[str] leasetime: The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
        :param pulumi.Input[int] limit: Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
        :param pulumi.Input[str] ra: The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ra_flags: Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
        :param pulumi.Input[int] start: Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
        """
        if dhcpv4 is not None:
            pulumi.set(__self__, "dhcpv4", dhcpv4)
        if dhcpv6 is not None:
            pulumi.set(__self__, "dhcpv6", dhcpv6)
        if force is not None:
            pulumi.set(__self__, "force", force)
        if ignore is not None:
            pulumi.set(__self__, "ignore", ignore)
        if interface is not None:
            pulumi.set(__self__, "interface", interface)
        if leasetime is not None:
            pulumi.set(__self__, "leasetime", leasetime)
        if limit is not None:
            pulumi.set(__self__, "limit", limit)
        if ra is not None:
            pulumi.set(__self__, "ra", ra)
        if ra_flags is not None:
            pulumi.set(__self__, "ra_flags", ra_flags)
        if start is not None:
            pulumi.set(__self__, "start", start)

    @property
    @pulumi.getter
    def dhcpv4(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of the DHCPv4 server. Must be one of: "disabled", "server".
        """
        return pulumi.get(self, "dhcpv4")

    @dhcpv4.setter
    def dhcpv4(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dhcpv4", value)

    @property
    @pulumi.getter
    def dhcpv6(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
        """
        return pulumi.get(self, "dhcpv6")

    @dhcpv6.setter
    def dhcpv6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dhcpv6", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter
    def ignore(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether dnsmasq should ignore this pool.
        """
        return pulumi.get(self, "ignore")

    @ignore.setter
    def ignore(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore", value)

    @property
    @pulumi.getter
    def interface(self) -> Optional[pulumi.Input[str]]:
        """
        The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
        field in Terraform. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "interface")

    @interface.setter
    def interface(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface", value)

    @property
    @pulumi.getter
    def leasetime(self) -> Optional[pulumi.Input[str]]:
        """
        The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "leasetime")

    @leasetime.setter
    def leasetime(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "leasetime", value)

    @property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "limit", value)

    @property
    @pulumi.getter
    def ra(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
        """
        return pulumi.get(self, "ra")

    @ra.setter
    def ra(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ra", value)

    @property
    @pulumi.getter(name="raFlags")
    def ra_flags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
        """
        return pulumi.get(self, "ra_flags")

    @ra_flags.setter
    def ra_flags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ra_flags", value)

    @property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "start")

    @start.setter
    def start(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "start", value)


@pulumi.input_type
class _DhcpDhcpState:
    def __init__(__self__, *,
                 dhcpv4: Optional[pulumi.Input[str]] = None,
                 dhcpv6: Optional[pulumi.Input[str]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 ignore: Optional[pulumi.Input[bool]] = None,
                 interface: Optional[pulumi.Input[str]] = None,
                 leasetime: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 ra: Optional[pulumi.Input[str]] = None,
                 ra_flags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 start: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering DhcpDhcp resources.
        :param pulumi.Input[str] dhcpv4: The mode of the DHCPv4 server. Must be one of: "disabled", "server".
        :param pulumi.Input[str] dhcpv6: The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
        :param pulumi.Input[bool] force: Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
        :param pulumi.Input[bool] ignore: Specifies whether dnsmasq should ignore this pool.
        :param pulumi.Input[str] interface: The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
               field in Terraform. Required if `ignore` is not `true`.
        :param pulumi.Input[str] leasetime: The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
        :param pulumi.Input[int] limit: Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
        :param pulumi.Input[str] ra: The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ra_flags: Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
        :param pulumi.Input[int] start: Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
        """
        if dhcpv4 is not None:
            pulumi.set(__self__, "dhcpv4", dhcpv4)
        if dhcpv6 is not None:
            pulumi.set(__self__, "dhcpv6", dhcpv6)
        if force is not None:
            pulumi.set(__self__, "force", force)
        if ignore is not None:
            pulumi.set(__self__, "ignore", ignore)
        if interface is not None:
            pulumi.set(__self__, "interface", interface)
        if leasetime is not None:
            pulumi.set(__self__, "leasetime", leasetime)
        if limit is not None:
            pulumi.set(__self__, "limit", limit)
        if ra is not None:
            pulumi.set(__self__, "ra", ra)
        if ra_flags is not None:
            pulumi.set(__self__, "ra_flags", ra_flags)
        if start is not None:
            pulumi.set(__self__, "start", start)

    @property
    @pulumi.getter
    def dhcpv4(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of the DHCPv4 server. Must be one of: "disabled", "server".
        """
        return pulumi.get(self, "dhcpv4")

    @dhcpv4.setter
    def dhcpv4(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dhcpv4", value)

    @property
    @pulumi.getter
    def dhcpv6(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
        """
        return pulumi.get(self, "dhcpv6")

    @dhcpv6.setter
    def dhcpv6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dhcpv6", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter
    def ignore(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether dnsmasq should ignore this pool.
        """
        return pulumi.get(self, "ignore")

    @ignore.setter
    def ignore(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore", value)

    @property
    @pulumi.getter
    def interface(self) -> Optional[pulumi.Input[str]]:
        """
        The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
        field in Terraform. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "interface")

    @interface.setter
    def interface(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface", value)

    @property
    @pulumi.getter
    def leasetime(self) -> Optional[pulumi.Input[str]]:
        """
        The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "leasetime")

    @leasetime.setter
    def leasetime(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "leasetime", value)

    @property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "limit", value)

    @property
    @pulumi.getter
    def ra(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
        """
        return pulumi.get(self, "ra")

    @ra.setter
    def ra(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ra", value)

    @property
    @pulumi.getter(name="raFlags")
    def ra_flags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
        """
        return pulumi.get(self, "ra_flags")

    @ra_flags.setter
    def ra_flags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ra_flags", value)

    @property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "start")

    @start.setter
    def start(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "start", value)


class DhcpDhcp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dhcpv4: Optional[pulumi.Input[str]] = None,
                 dhcpv6: Optional[pulumi.Input[str]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 ignore: Optional[pulumi.Input[bool]] = None,
                 interface: Optional[pulumi.Input[str]] = None,
                 leasetime: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 ra: Optional[pulumi.Input[str]] = None,
                 ra_flags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 start: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Per interface lease pools and settings for serving DHCP requests.

        ## Import

        Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["dhcp", "dhcp"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map({name.[".name"]})' # This command will output something like# [

         {

         "name""lan",

         },

         {

         "name""guest",

         } ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/dhcpDhcp:DhcpDhcp lan lan
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dhcpv4: The mode of the DHCPv4 server. Must be one of: "disabled", "server".
        :param pulumi.Input[str] dhcpv6: The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
        :param pulumi.Input[bool] force: Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
        :param pulumi.Input[bool] ignore: Specifies whether dnsmasq should ignore this pool.
        :param pulumi.Input[str] interface: The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
               field in Terraform. Required if `ignore` is not `true`.
        :param pulumi.Input[str] leasetime: The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
        :param pulumi.Input[int] limit: Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
        :param pulumi.Input[str] ra: The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ra_flags: Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
        :param pulumi.Input[int] start: Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DhcpDhcpArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Per interface lease pools and settings for serving DHCP requests.

        ## Import

        Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["dhcp", "dhcp"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map({name.[".name"]})' # This command will output something like# [

         {

         "name""lan",

         },

         {

         "name""guest",

         } ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/dhcpDhcp:DhcpDhcp lan lan
        ```

        :param str resource_name: The name of the resource.
        :param DhcpDhcpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DhcpDhcpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dhcpv4: Optional[pulumi.Input[str]] = None,
                 dhcpv6: Optional[pulumi.Input[str]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 ignore: Optional[pulumi.Input[bool]] = None,
                 interface: Optional[pulumi.Input[str]] = None,
                 leasetime: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 ra: Optional[pulumi.Input[str]] = None,
                 ra_flags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 start: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DhcpDhcpArgs.__new__(DhcpDhcpArgs)

            __props__.__dict__["dhcpv4"] = dhcpv4
            __props__.__dict__["dhcpv6"] = dhcpv6
            __props__.__dict__["force"] = force
            __props__.__dict__["ignore"] = ignore
            __props__.__dict__["interface"] = interface
            __props__.__dict__["leasetime"] = leasetime
            __props__.__dict__["limit"] = limit
            __props__.__dict__["ra"] = ra
            __props__.__dict__["ra_flags"] = ra_flags
            __props__.__dict__["start"] = start
        super(DhcpDhcp, __self__).__init__(
            'openwrt:index/dhcpDhcp:DhcpDhcp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dhcpv4: Optional[pulumi.Input[str]] = None,
            dhcpv6: Optional[pulumi.Input[str]] = None,
            force: Optional[pulumi.Input[bool]] = None,
            ignore: Optional[pulumi.Input[bool]] = None,
            interface: Optional[pulumi.Input[str]] = None,
            leasetime: Optional[pulumi.Input[str]] = None,
            limit: Optional[pulumi.Input[int]] = None,
            ra: Optional[pulumi.Input[str]] = None,
            ra_flags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            start: Optional[pulumi.Input[int]] = None) -> 'DhcpDhcp':
        """
        Get an existing DhcpDhcp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dhcpv4: The mode of the DHCPv4 server. Must be one of: "disabled", "server".
        :param pulumi.Input[str] dhcpv6: The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
        :param pulumi.Input[bool] force: Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
        :param pulumi.Input[bool] ignore: Specifies whether dnsmasq should ignore this pool.
        :param pulumi.Input[str] interface: The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
               field in Terraform. Required if `ignore` is not `true`.
        :param pulumi.Input[str] leasetime: The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
        :param pulumi.Input[int] limit: Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
        :param pulumi.Input[str] ra: The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ra_flags: Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
        :param pulumi.Input[int] start: Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DhcpDhcpState.__new__(_DhcpDhcpState)

        __props__.__dict__["dhcpv4"] = dhcpv4
        __props__.__dict__["dhcpv6"] = dhcpv6
        __props__.__dict__["force"] = force
        __props__.__dict__["ignore"] = ignore
        __props__.__dict__["interface"] = interface
        __props__.__dict__["leasetime"] = leasetime
        __props__.__dict__["limit"] = limit
        __props__.__dict__["ra"] = ra
        __props__.__dict__["ra_flags"] = ra_flags
        __props__.__dict__["start"] = start
        return DhcpDhcp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def dhcpv4(self) -> pulumi.Output[str]:
        """
        The mode of the DHCPv4 server. Must be one of: "disabled", "server".
        """
        return pulumi.get(self, "dhcpv4")

    @property
    @pulumi.getter
    def dhcpv6(self) -> pulumi.Output[str]:
        """
        The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
        """
        return pulumi.get(self, "dhcpv6")

    @property
    @pulumi.getter
    def force(self) -> pulumi.Output[bool]:
        """
        Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
        """
        return pulumi.get(self, "force")

    @property
    @pulumi.getter
    def ignore(self) -> pulumi.Output[bool]:
        """
        Specifies whether dnsmasq should ignore this pool.
        """
        return pulumi.get(self, "ignore")

    @property
    @pulumi.getter
    def interface(self) -> pulumi.Output[str]:
        """
        The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
        field in Terraform. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "interface")

    @property
    @pulumi.getter
    def leasetime(self) -> pulumi.Output[str]:
        """
        The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "leasetime")

    @property
    @pulumi.getter
    def limit(self) -> pulumi.Output[int]:
        """
        Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter
    def ra(self) -> pulumi.Output[str]:
        """
        The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
        """
        return pulumi.get(self, "ra")

    @property
    @pulumi.getter(name="raFlags")
    def ra_flags(self) -> pulumi.Output[Sequence[str]]:
        """
        Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
        """
        return pulumi.get(self, "ra_flags")

    @property
    @pulumi.getter
    def start(self) -> pulumi.Output[int]:
        """
        Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
        """
        return pulumi.get(self, "start")

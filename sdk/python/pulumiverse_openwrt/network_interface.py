# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['NetworkInterfaceArgs', 'NetworkInterface']

@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(__self__, *,
                 device: pulumi.Input[str],
                 proto: pulumi.Input[str],
                 auto: Optional[pulumi.Input[bool]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 dns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gateway: Optional[pulumi.Input[str]] = None,
                 ip6assign: Optional[pulumi.Input[int]] = None,
                 ipaddr: Optional[pulumi.Input[str]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 netmask: Optional[pulumi.Input[str]] = None,
                 peerdns: Optional[pulumi.Input[bool]] = None,
                 reqaddress: Optional[pulumi.Input[str]] = None,
                 reqprefix: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NetworkInterface resource.
        :param pulumi.Input[str] device: Name of the (physical or virtual) device. This name is what the device is known as in LuCI or the `name` field in
               Terraform. This is not the UCI config name.
        :param pulumi.Input[str] proto: The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
        :param pulumi.Input[bool] auto: Specifies whether to bring up this interface on boot.
        :param pulumi.Input[bool] disabled: Disables this interface.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns: DNS servers
        :param pulumi.Input[str] gateway: Gateway of the interface
        :param pulumi.Input[int] ip6assign: Delegate a prefix of given length to this interface
        :param pulumi.Input[str] ipaddr: IP address of the interface
        :param pulumi.Input[str] macaddr: Override the MAC Address of this interface.
        :param pulumi.Input[int] mtu: Override the default MTU on this interface.
        :param pulumi.Input[str] netmask: Netmask of the interface
        :param pulumi.Input[bool] peerdns: Use DHCP-provided DNS servers.
        :param pulumi.Input[str] reqaddress: Behavior for requesting address. Can only be one of "force", "try", or "none".
        :param pulumi.Input[str] reqprefix: Behavior for requesting prefixes. Currently, only "auto" is supported.
        """
        pulumi.set(__self__, "device", device)
        pulumi.set(__self__, "proto", proto)
        if auto is not None:
            pulumi.set(__self__, "auto", auto)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if dns is not None:
            pulumi.set(__self__, "dns", dns)
        if gateway is not None:
            pulumi.set(__self__, "gateway", gateway)
        if ip6assign is not None:
            pulumi.set(__self__, "ip6assign", ip6assign)
        if ipaddr is not None:
            pulumi.set(__self__, "ipaddr", ipaddr)
        if macaddr is not None:
            pulumi.set(__self__, "macaddr", macaddr)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if netmask is not None:
            pulumi.set(__self__, "netmask", netmask)
        if peerdns is not None:
            pulumi.set(__self__, "peerdns", peerdns)
        if reqaddress is not None:
            pulumi.set(__self__, "reqaddress", reqaddress)
        if reqprefix is not None:
            pulumi.set(__self__, "reqprefix", reqprefix)

    @property
    @pulumi.getter
    def device(self) -> pulumi.Input[str]:
        """
        Name of the (physical or virtual) device. This name is what the device is known as in LuCI or the `name` field in
        Terraform. This is not the UCI config name.
        """
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: pulumi.Input[str]):
        pulumi.set(self, "device", value)

    @property
    @pulumi.getter
    def proto(self) -> pulumi.Input[str]:
        """
        The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
        """
        return pulumi.get(self, "proto")

    @proto.setter
    def proto(self, value: pulumi.Input[str]):
        pulumi.set(self, "proto", value)

    @property
    @pulumi.getter
    def auto(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to bring up this interface on boot.
        """
        return pulumi.get(self, "auto")

    @auto.setter
    def auto(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Disables this interface.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def dns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        DNS servers
        """
        return pulumi.get(self, "dns")

    @dns.setter
    def dns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns", value)

    @property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[str]]:
        """
        Gateway of the interface
        """
        return pulumi.get(self, "gateway")

    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway", value)

    @property
    @pulumi.getter
    def ip6assign(self) -> Optional[pulumi.Input[int]]:
        """
        Delegate a prefix of given length to this interface
        """
        return pulumi.get(self, "ip6assign")

    @ip6assign.setter
    def ip6assign(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ip6assign", value)

    @property
    @pulumi.getter
    def ipaddr(self) -> Optional[pulumi.Input[str]]:
        """
        IP address of the interface
        """
        return pulumi.get(self, "ipaddr")

    @ipaddr.setter
    def ipaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipaddr", value)

    @property
    @pulumi.getter
    def macaddr(self) -> Optional[pulumi.Input[str]]:
        """
        Override the MAC Address of this interface.
        """
        return pulumi.get(self, "macaddr")

    @macaddr.setter
    def macaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "macaddr", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        Override the default MTU on this interface.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def netmask(self) -> Optional[pulumi.Input[str]]:
        """
        Netmask of the interface
        """
        return pulumi.get(self, "netmask")

    @netmask.setter
    def netmask(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "netmask", value)

    @property
    @pulumi.getter
    def peerdns(self) -> Optional[pulumi.Input[bool]]:
        """
        Use DHCP-provided DNS servers.
        """
        return pulumi.get(self, "peerdns")

    @peerdns.setter
    def peerdns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "peerdns", value)

    @property
    @pulumi.getter
    def reqaddress(self) -> Optional[pulumi.Input[str]]:
        """
        Behavior for requesting address. Can only be one of "force", "try", or "none".
        """
        return pulumi.get(self, "reqaddress")

    @reqaddress.setter
    def reqaddress(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reqaddress", value)

    @property
    @pulumi.getter
    def reqprefix(self) -> Optional[pulumi.Input[str]]:
        """
        Behavior for requesting prefixes. Currently, only "auto" is supported.
        """
        return pulumi.get(self, "reqprefix")

    @reqprefix.setter
    def reqprefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reqprefix", value)


@pulumi.input_type
class _NetworkInterfaceState:
    def __init__(__self__, *,
                 auto: Optional[pulumi.Input[bool]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 dns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gateway: Optional[pulumi.Input[str]] = None,
                 ip6assign: Optional[pulumi.Input[int]] = None,
                 ipaddr: Optional[pulumi.Input[str]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 netmask: Optional[pulumi.Input[str]] = None,
                 peerdns: Optional[pulumi.Input[bool]] = None,
                 proto: Optional[pulumi.Input[str]] = None,
                 reqaddress: Optional[pulumi.Input[str]] = None,
                 reqprefix: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NetworkInterface resources.
        :param pulumi.Input[bool] auto: Specifies whether to bring up this interface on boot.
        :param pulumi.Input[str] device: Name of the (physical or virtual) device. This name is what the device is known as in LuCI or the `name` field in
               Terraform. This is not the UCI config name.
        :param pulumi.Input[bool] disabled: Disables this interface.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns: DNS servers
        :param pulumi.Input[str] gateway: Gateway of the interface
        :param pulumi.Input[int] ip6assign: Delegate a prefix of given length to this interface
        :param pulumi.Input[str] ipaddr: IP address of the interface
        :param pulumi.Input[str] macaddr: Override the MAC Address of this interface.
        :param pulumi.Input[int] mtu: Override the default MTU on this interface.
        :param pulumi.Input[str] netmask: Netmask of the interface
        :param pulumi.Input[bool] peerdns: Use DHCP-provided DNS servers.
        :param pulumi.Input[str] proto: The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
        :param pulumi.Input[str] reqaddress: Behavior for requesting address. Can only be one of "force", "try", or "none".
        :param pulumi.Input[str] reqprefix: Behavior for requesting prefixes. Currently, only "auto" is supported.
        """
        if auto is not None:
            pulumi.set(__self__, "auto", auto)
        if device is not None:
            pulumi.set(__self__, "device", device)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if dns is not None:
            pulumi.set(__self__, "dns", dns)
        if gateway is not None:
            pulumi.set(__self__, "gateway", gateway)
        if ip6assign is not None:
            pulumi.set(__self__, "ip6assign", ip6assign)
        if ipaddr is not None:
            pulumi.set(__self__, "ipaddr", ipaddr)
        if macaddr is not None:
            pulumi.set(__self__, "macaddr", macaddr)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if netmask is not None:
            pulumi.set(__self__, "netmask", netmask)
        if peerdns is not None:
            pulumi.set(__self__, "peerdns", peerdns)
        if proto is not None:
            pulumi.set(__self__, "proto", proto)
        if reqaddress is not None:
            pulumi.set(__self__, "reqaddress", reqaddress)
        if reqprefix is not None:
            pulumi.set(__self__, "reqprefix", reqprefix)

    @property
    @pulumi.getter
    def auto(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to bring up this interface on boot.
        """
        return pulumi.get(self, "auto")

    @auto.setter
    def auto(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto", value)

    @property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the (physical or virtual) device. This name is what the device is known as in LuCI or the `name` field in
        Terraform. This is not the UCI config name.
        """
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Disables this interface.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def dns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        DNS servers
        """
        return pulumi.get(self, "dns")

    @dns.setter
    def dns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns", value)

    @property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[str]]:
        """
        Gateway of the interface
        """
        return pulumi.get(self, "gateway")

    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway", value)

    @property
    @pulumi.getter
    def ip6assign(self) -> Optional[pulumi.Input[int]]:
        """
        Delegate a prefix of given length to this interface
        """
        return pulumi.get(self, "ip6assign")

    @ip6assign.setter
    def ip6assign(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ip6assign", value)

    @property
    @pulumi.getter
    def ipaddr(self) -> Optional[pulumi.Input[str]]:
        """
        IP address of the interface
        """
        return pulumi.get(self, "ipaddr")

    @ipaddr.setter
    def ipaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipaddr", value)

    @property
    @pulumi.getter
    def macaddr(self) -> Optional[pulumi.Input[str]]:
        """
        Override the MAC Address of this interface.
        """
        return pulumi.get(self, "macaddr")

    @macaddr.setter
    def macaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "macaddr", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        Override the default MTU on this interface.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def netmask(self) -> Optional[pulumi.Input[str]]:
        """
        Netmask of the interface
        """
        return pulumi.get(self, "netmask")

    @netmask.setter
    def netmask(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "netmask", value)

    @property
    @pulumi.getter
    def peerdns(self) -> Optional[pulumi.Input[bool]]:
        """
        Use DHCP-provided DNS servers.
        """
        return pulumi.get(self, "peerdns")

    @peerdns.setter
    def peerdns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "peerdns", value)

    @property
    @pulumi.getter
    def proto(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
        """
        return pulumi.get(self, "proto")

    @proto.setter
    def proto(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proto", value)

    @property
    @pulumi.getter
    def reqaddress(self) -> Optional[pulumi.Input[str]]:
        """
        Behavior for requesting address. Can only be one of "force", "try", or "none".
        """
        return pulumi.get(self, "reqaddress")

    @reqaddress.setter
    def reqaddress(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reqaddress", value)

    @property
    @pulumi.getter
    def reqprefix(self) -> Optional[pulumi.Input[str]]:
        """
        Behavior for requesting prefixes. Currently, only "auto" is supported.
        """
        return pulumi.get(self, "reqprefix")

    @reqprefix.setter
    def reqprefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reqprefix", value)


class NetworkInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto: Optional[pulumi.Input[bool]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 dns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gateway: Optional[pulumi.Input[str]] = None,
                 ip6assign: Optional[pulumi.Input[int]] = None,
                 ipaddr: Optional[pulumi.Input[str]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 netmask: Optional[pulumi.Input[str]] = None,
                 peerdns: Optional[pulumi.Input[bool]] = None,
                 proto: Optional[pulumi.Input[str]] = None,
                 reqaddress: Optional[pulumi.Input[str]] = None,
                 reqprefix: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A logic network.

        ## Import

        Find the Terraform id is the same as the UCI name from LuCI's JSON-RPC API. It is also generally the lower-cased version of the interface name in LuCI's web UI. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["network", "interface"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map(.[".name"])' # This command will output something like# [

         "loopback",

         "wan",

         "wan6" ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/networkInterface:NetworkInterface loopback loopback
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto: Specifies whether to bring up this interface on boot.
        :param pulumi.Input[str] device: Name of the (physical or virtual) device. This name is what the device is known as in LuCI or the `name` field in
               Terraform. This is not the UCI config name.
        :param pulumi.Input[bool] disabled: Disables this interface.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns: DNS servers
        :param pulumi.Input[str] gateway: Gateway of the interface
        :param pulumi.Input[int] ip6assign: Delegate a prefix of given length to this interface
        :param pulumi.Input[str] ipaddr: IP address of the interface
        :param pulumi.Input[str] macaddr: Override the MAC Address of this interface.
        :param pulumi.Input[int] mtu: Override the default MTU on this interface.
        :param pulumi.Input[str] netmask: Netmask of the interface
        :param pulumi.Input[bool] peerdns: Use DHCP-provided DNS servers.
        :param pulumi.Input[str] proto: The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
        :param pulumi.Input[str] reqaddress: Behavior for requesting address. Can only be one of "force", "try", or "none".
        :param pulumi.Input[str] reqprefix: Behavior for requesting prefixes. Currently, only "auto" is supported.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInterfaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A logic network.

        ## Import

        Find the Terraform id is the same as the UCI name from LuCI's JSON-RPC API. It is also generally the lower-cased version of the interface name in LuCI's web UI. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["network", "interface"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map(.[".name"])' # This command will output something like# [

         "loopback",

         "wan",

         "wan6" ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/networkInterface:NetworkInterface loopback loopback
        ```

        :param str resource_name: The name of the resource.
        :param NetworkInterfaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInterfaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto: Optional[pulumi.Input[bool]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 dns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gateway: Optional[pulumi.Input[str]] = None,
                 ip6assign: Optional[pulumi.Input[int]] = None,
                 ipaddr: Optional[pulumi.Input[str]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 netmask: Optional[pulumi.Input[str]] = None,
                 peerdns: Optional[pulumi.Input[bool]] = None,
                 proto: Optional[pulumi.Input[str]] = None,
                 reqaddress: Optional[pulumi.Input[str]] = None,
                 reqprefix: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInterfaceArgs.__new__(NetworkInterfaceArgs)

            __props__.__dict__["auto"] = auto
            if device is None and not opts.urn:
                raise TypeError("Missing required property 'device'")
            __props__.__dict__["device"] = device
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["dns"] = dns
            __props__.__dict__["gateway"] = gateway
            __props__.__dict__["ip6assign"] = ip6assign
            __props__.__dict__["ipaddr"] = ipaddr
            __props__.__dict__["macaddr"] = macaddr
            __props__.__dict__["mtu"] = mtu
            __props__.__dict__["netmask"] = netmask
            __props__.__dict__["peerdns"] = peerdns
            if proto is None and not opts.urn:
                raise TypeError("Missing required property 'proto'")
            __props__.__dict__["proto"] = proto
            __props__.__dict__["reqaddress"] = reqaddress
            __props__.__dict__["reqprefix"] = reqprefix
        super(NetworkInterface, __self__).__init__(
            'openwrt:index/networkInterface:NetworkInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto: Optional[pulumi.Input[bool]] = None,
            device: Optional[pulumi.Input[str]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            dns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            gateway: Optional[pulumi.Input[str]] = None,
            ip6assign: Optional[pulumi.Input[int]] = None,
            ipaddr: Optional[pulumi.Input[str]] = None,
            macaddr: Optional[pulumi.Input[str]] = None,
            mtu: Optional[pulumi.Input[int]] = None,
            netmask: Optional[pulumi.Input[str]] = None,
            peerdns: Optional[pulumi.Input[bool]] = None,
            proto: Optional[pulumi.Input[str]] = None,
            reqaddress: Optional[pulumi.Input[str]] = None,
            reqprefix: Optional[pulumi.Input[str]] = None) -> 'NetworkInterface':
        """
        Get an existing NetworkInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto: Specifies whether to bring up this interface on boot.
        :param pulumi.Input[str] device: Name of the (physical or virtual) device. This name is what the device is known as in LuCI or the `name` field in
               Terraform. This is not the UCI config name.
        :param pulumi.Input[bool] disabled: Disables this interface.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns: DNS servers
        :param pulumi.Input[str] gateway: Gateway of the interface
        :param pulumi.Input[int] ip6assign: Delegate a prefix of given length to this interface
        :param pulumi.Input[str] ipaddr: IP address of the interface
        :param pulumi.Input[str] macaddr: Override the MAC Address of this interface.
        :param pulumi.Input[int] mtu: Override the default MTU on this interface.
        :param pulumi.Input[str] netmask: Netmask of the interface
        :param pulumi.Input[bool] peerdns: Use DHCP-provided DNS servers.
        :param pulumi.Input[str] proto: The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
        :param pulumi.Input[str] reqaddress: Behavior for requesting address. Can only be one of "force", "try", or "none".
        :param pulumi.Input[str] reqprefix: Behavior for requesting prefixes. Currently, only "auto" is supported.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkInterfaceState.__new__(_NetworkInterfaceState)

        __props__.__dict__["auto"] = auto
        __props__.__dict__["device"] = device
        __props__.__dict__["disabled"] = disabled
        __props__.__dict__["dns"] = dns
        __props__.__dict__["gateway"] = gateway
        __props__.__dict__["ip6assign"] = ip6assign
        __props__.__dict__["ipaddr"] = ipaddr
        __props__.__dict__["macaddr"] = macaddr
        __props__.__dict__["mtu"] = mtu
        __props__.__dict__["netmask"] = netmask
        __props__.__dict__["peerdns"] = peerdns
        __props__.__dict__["proto"] = proto
        __props__.__dict__["reqaddress"] = reqaddress
        __props__.__dict__["reqprefix"] = reqprefix
        return NetworkInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def auto(self) -> pulumi.Output[bool]:
        """
        Specifies whether to bring up this interface on boot.
        """
        return pulumi.get(self, "auto")

    @property
    @pulumi.getter
    def device(self) -> pulumi.Output[str]:
        """
        Name of the (physical or virtual) device. This name is what the device is known as in LuCI or the `name` field in
        Terraform. This is not the UCI config name.
        """
        return pulumi.get(self, "device")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[bool]:
        """
        Disables this interface.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def dns(self) -> pulumi.Output[Sequence[str]]:
        """
        DNS servers
        """
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output[str]:
        """
        Gateway of the interface
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter
    def ip6assign(self) -> pulumi.Output[int]:
        """
        Delegate a prefix of given length to this interface
        """
        return pulumi.get(self, "ip6assign")

    @property
    @pulumi.getter
    def ipaddr(self) -> pulumi.Output[str]:
        """
        IP address of the interface
        """
        return pulumi.get(self, "ipaddr")

    @property
    @pulumi.getter
    def macaddr(self) -> pulumi.Output[str]:
        """
        Override the MAC Address of this interface.
        """
        return pulumi.get(self, "macaddr")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[int]:
        """
        Override the default MTU on this interface.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def netmask(self) -> pulumi.Output[str]:
        """
        Netmask of the interface
        """
        return pulumi.get(self, "netmask")

    @property
    @pulumi.getter
    def peerdns(self) -> pulumi.Output[bool]:
        """
        Use DHCP-provided DNS servers.
        """
        return pulumi.get(self, "peerdns")

    @property
    @pulumi.getter
    def proto(self) -> pulumi.Output[str]:
        """
        The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
        """
        return pulumi.get(self, "proto")

    @property
    @pulumi.getter
    def reqaddress(self) -> pulumi.Output[str]:
        """
        Behavior for requesting address. Can only be one of "force", "try", or "none".
        """
        return pulumi.get(self, "reqaddress")

    @property
    @pulumi.getter
    def reqprefix(self) -> pulumi.Output[str]:
        """
        Behavior for requesting prefixes. Currently, only "auto" is supported.
        """
        return pulumi.get(self, "reqprefix")


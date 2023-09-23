# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['NetworkDeviceArgs', 'NetworkDevice']

@pulumi.input_type
class NetworkDeviceArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 bridge_empty: Optional[pulumi.Input[bool]] = None,
                 dadtransmits: Optional[pulumi.Input[int]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 mtu6: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 txqueuelen: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a NetworkDevice resource.
        :param pulumi.Input[str] type: The type of device. Currently, only "bridge" is supported.
        :param pulumi.Input[bool] bridge_empty: Bring up the bridge device even if no ports are attached
        :param pulumi.Input[int] dadtransmits: Amount of Duplicate Address Detection probes to send
        :param pulumi.Input[bool] ipv6: Enable IPv6 for the device.
        :param pulumi.Input[str] macaddr: MAC Address of the device.
        :param pulumi.Input[int] mtu: Maximum Transmissible Unit.
        :param pulumi.Input[int] mtu6: Maximum Transmissible Unit for IPv6.
        :param pulumi.Input[str] name: Name of the device. This name is referenced in other network configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ports: Specifies the wired ports to attach to this bridge.
        :param pulumi.Input[int] txqueuelen: Transmission queue length.
        """
        pulumi.set(__self__, "type", type)
        if bridge_empty is not None:
            pulumi.set(__self__, "bridge_empty", bridge_empty)
        if dadtransmits is not None:
            pulumi.set(__self__, "dadtransmits", dadtransmits)
        if ipv6 is not None:
            pulumi.set(__self__, "ipv6", ipv6)
        if macaddr is not None:
            pulumi.set(__self__, "macaddr", macaddr)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if mtu6 is not None:
            pulumi.set(__self__, "mtu6", mtu6)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)
        if txqueuelen is not None:
            pulumi.set(__self__, "txqueuelen", txqueuelen)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of device. Currently, only "bridge" is supported.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="bridgeEmpty")
    def bridge_empty(self) -> Optional[pulumi.Input[bool]]:
        """
        Bring up the bridge device even if no ports are attached
        """
        return pulumi.get(self, "bridge_empty")

    @bridge_empty.setter
    def bridge_empty(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bridge_empty", value)

    @property
    @pulumi.getter
    def dadtransmits(self) -> Optional[pulumi.Input[int]]:
        """
        Amount of Duplicate Address Detection probes to send
        """
        return pulumi.get(self, "dadtransmits")

    @dadtransmits.setter
    def dadtransmits(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dadtransmits", value)

    @property
    @pulumi.getter
    def ipv6(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable IPv6 for the device.
        """
        return pulumi.get(self, "ipv6")

    @ipv6.setter
    def ipv6(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ipv6", value)

    @property
    @pulumi.getter
    def macaddr(self) -> Optional[pulumi.Input[str]]:
        """
        MAC Address of the device.
        """
        return pulumi.get(self, "macaddr")

    @macaddr.setter
    def macaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "macaddr", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum Transmissible Unit.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def mtu6(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum Transmissible Unit for IPv6.
        """
        return pulumi.get(self, "mtu6")

    @mtu6.setter
    def mtu6(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu6", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the device. This name is referenced in other network configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the wired ports to attach to this bridge.
        """
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ports", value)

    @property
    @pulumi.getter
    def txqueuelen(self) -> Optional[pulumi.Input[int]]:
        """
        Transmission queue length.
        """
        return pulumi.get(self, "txqueuelen")

    @txqueuelen.setter
    def txqueuelen(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "txqueuelen", value)


@pulumi.input_type
class _NetworkDeviceState:
    def __init__(__self__, *,
                 bridge_empty: Optional[pulumi.Input[bool]] = None,
                 dadtransmits: Optional[pulumi.Input[int]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 mtu6: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 txqueuelen: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NetworkDevice resources.
        :param pulumi.Input[bool] bridge_empty: Bring up the bridge device even if no ports are attached
        :param pulumi.Input[int] dadtransmits: Amount of Duplicate Address Detection probes to send
        :param pulumi.Input[bool] ipv6: Enable IPv6 for the device.
        :param pulumi.Input[str] macaddr: MAC Address of the device.
        :param pulumi.Input[int] mtu: Maximum Transmissible Unit.
        :param pulumi.Input[int] mtu6: Maximum Transmissible Unit for IPv6.
        :param pulumi.Input[str] name: Name of the device. This name is referenced in other network configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ports: Specifies the wired ports to attach to this bridge.
        :param pulumi.Input[int] txqueuelen: Transmission queue length.
        :param pulumi.Input[str] type: The type of device. Currently, only "bridge" is supported.
        """
        if bridge_empty is not None:
            pulumi.set(__self__, "bridge_empty", bridge_empty)
        if dadtransmits is not None:
            pulumi.set(__self__, "dadtransmits", dadtransmits)
        if ipv6 is not None:
            pulumi.set(__self__, "ipv6", ipv6)
        if macaddr is not None:
            pulumi.set(__self__, "macaddr", macaddr)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if mtu6 is not None:
            pulumi.set(__self__, "mtu6", mtu6)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)
        if txqueuelen is not None:
            pulumi.set(__self__, "txqueuelen", txqueuelen)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="bridgeEmpty")
    def bridge_empty(self) -> Optional[pulumi.Input[bool]]:
        """
        Bring up the bridge device even if no ports are attached
        """
        return pulumi.get(self, "bridge_empty")

    @bridge_empty.setter
    def bridge_empty(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bridge_empty", value)

    @property
    @pulumi.getter
    def dadtransmits(self) -> Optional[pulumi.Input[int]]:
        """
        Amount of Duplicate Address Detection probes to send
        """
        return pulumi.get(self, "dadtransmits")

    @dadtransmits.setter
    def dadtransmits(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dadtransmits", value)

    @property
    @pulumi.getter
    def ipv6(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable IPv6 for the device.
        """
        return pulumi.get(self, "ipv6")

    @ipv6.setter
    def ipv6(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ipv6", value)

    @property
    @pulumi.getter
    def macaddr(self) -> Optional[pulumi.Input[str]]:
        """
        MAC Address of the device.
        """
        return pulumi.get(self, "macaddr")

    @macaddr.setter
    def macaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "macaddr", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum Transmissible Unit.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def mtu6(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum Transmissible Unit for IPv6.
        """
        return pulumi.get(self, "mtu6")

    @mtu6.setter
    def mtu6(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu6", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the device. This name is referenced in other network configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the wired ports to attach to this bridge.
        """
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ports", value)

    @property
    @pulumi.getter
    def txqueuelen(self) -> Optional[pulumi.Input[int]]:
        """
        Transmission queue length.
        """
        return pulumi.get(self, "txqueuelen")

    @txqueuelen.setter
    def txqueuelen(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "txqueuelen", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of device. Currently, only "bridge" is supported.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class NetworkDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bridge_empty: Optional[pulumi.Input[bool]] = None,
                 dadtransmits: Optional[pulumi.Input[int]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 mtu6: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 txqueuelen: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A physical or virtual "device" in OpenWrt jargon. Commonly referred to as an "interface" in other networking jargon.

        ## Import

        Find the Terraform id and UCI name from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["network", "device"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map({terraformId.[".name"], uciName.name})' # This command will output something like# [

         {

         "terraformId""cfg030f15",

         "uciName""foo"

         },

         {

         "terraformId""cfg040f15",

         "uciName""bar"

         } ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/networkDevice:NetworkDevice foo cfg030f15
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] bridge_empty: Bring up the bridge device even if no ports are attached
        :param pulumi.Input[int] dadtransmits: Amount of Duplicate Address Detection probes to send
        :param pulumi.Input[bool] ipv6: Enable IPv6 for the device.
        :param pulumi.Input[str] macaddr: MAC Address of the device.
        :param pulumi.Input[int] mtu: Maximum Transmissible Unit.
        :param pulumi.Input[int] mtu6: Maximum Transmissible Unit for IPv6.
        :param pulumi.Input[str] name: Name of the device. This name is referenced in other network configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ports: Specifies the wired ports to attach to this bridge.
        :param pulumi.Input[int] txqueuelen: Transmission queue length.
        :param pulumi.Input[str] type: The type of device. Currently, only "bridge" is supported.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkDeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A physical or virtual "device" in OpenWrt jargon. Commonly referred to as an "interface" in other networking jargon.

        ## Import

        Find the Terraform id and UCI name from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["network", "device"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map({terraformId.[".name"], uciName.name})' # This command will output something like# [

         {

         "terraformId""cfg030f15",

         "uciName""foo"

         },

         {

         "terraformId""cfg040f15",

         "uciName""bar"

         } ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/networkDevice:NetworkDevice foo cfg030f15
        ```

        :param str resource_name: The name of the resource.
        :param NetworkDeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkDeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bridge_empty: Optional[pulumi.Input[bool]] = None,
                 dadtransmits: Optional[pulumi.Input[int]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 mtu6: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 txqueuelen: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkDeviceArgs.__new__(NetworkDeviceArgs)

            __props__.__dict__["bridge_empty"] = bridge_empty
            __props__.__dict__["dadtransmits"] = dadtransmits
            __props__.__dict__["ipv6"] = ipv6
            __props__.__dict__["macaddr"] = macaddr
            __props__.__dict__["mtu"] = mtu
            __props__.__dict__["mtu6"] = mtu6
            __props__.__dict__["name"] = name
            __props__.__dict__["ports"] = ports
            __props__.__dict__["txqueuelen"] = txqueuelen
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(NetworkDevice, __self__).__init__(
            'openwrt:index/networkDevice:NetworkDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bridge_empty: Optional[pulumi.Input[bool]] = None,
            dadtransmits: Optional[pulumi.Input[int]] = None,
            ipv6: Optional[pulumi.Input[bool]] = None,
            macaddr: Optional[pulumi.Input[str]] = None,
            mtu: Optional[pulumi.Input[int]] = None,
            mtu6: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            txqueuelen: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'NetworkDevice':
        """
        Get an existing NetworkDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] bridge_empty: Bring up the bridge device even if no ports are attached
        :param pulumi.Input[int] dadtransmits: Amount of Duplicate Address Detection probes to send
        :param pulumi.Input[bool] ipv6: Enable IPv6 for the device.
        :param pulumi.Input[str] macaddr: MAC Address of the device.
        :param pulumi.Input[int] mtu: Maximum Transmissible Unit.
        :param pulumi.Input[int] mtu6: Maximum Transmissible Unit for IPv6.
        :param pulumi.Input[str] name: Name of the device. This name is referenced in other network configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ports: Specifies the wired ports to attach to this bridge.
        :param pulumi.Input[int] txqueuelen: Transmission queue length.
        :param pulumi.Input[str] type: The type of device. Currently, only "bridge" is supported.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkDeviceState.__new__(_NetworkDeviceState)

        __props__.__dict__["bridge_empty"] = bridge_empty
        __props__.__dict__["dadtransmits"] = dadtransmits
        __props__.__dict__["ipv6"] = ipv6
        __props__.__dict__["macaddr"] = macaddr
        __props__.__dict__["mtu"] = mtu
        __props__.__dict__["mtu6"] = mtu6
        __props__.__dict__["name"] = name
        __props__.__dict__["ports"] = ports
        __props__.__dict__["txqueuelen"] = txqueuelen
        __props__.__dict__["type"] = type
        return NetworkDevice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bridgeEmpty")
    def bridge_empty(self) -> pulumi.Output[bool]:
        """
        Bring up the bridge device even if no ports are attached
        """
        return pulumi.get(self, "bridge_empty")

    @property
    @pulumi.getter
    def dadtransmits(self) -> pulumi.Output[int]:
        """
        Amount of Duplicate Address Detection probes to send
        """
        return pulumi.get(self, "dadtransmits")

    @property
    @pulumi.getter
    def ipv6(self) -> pulumi.Output[bool]:
        """
        Enable IPv6 for the device.
        """
        return pulumi.get(self, "ipv6")

    @property
    @pulumi.getter
    def macaddr(self) -> pulumi.Output[str]:
        """
        MAC Address of the device.
        """
        return pulumi.get(self, "macaddr")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[int]:
        """
        Maximum Transmissible Unit.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def mtu6(self) -> pulumi.Output[int]:
        """
        Maximum Transmissible Unit for IPv6.
        """
        return pulumi.get(self, "mtu6")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the device. This name is referenced in other network configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ports(self) -> pulumi.Output[Sequence[str]]:
        """
        Specifies the wired ports to attach to this bridge.
        """
        return pulumi.get(self, "ports")

    @property
    @pulumi.getter
    def txqueuelen(self) -> pulumi.Output[int]:
        """
        Transmission queue length.
        """
        return pulumi.get(self, "txqueuelen")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of device. Currently, only "bridge" is supported.
        """
        return pulumi.get(self, "type")


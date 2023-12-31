# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DhcpHostArgs', 'DhcpHost']

@pulumi.input_type
class DhcpHostArgs:
    def __init__(__self__, *,
                 dns: Optional[pulumi.Input[bool]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DhcpHost resource.
        :param pulumi.Input[bool] dns: Add static forward and reverse DNS entries for this host.
        :param pulumi.Input[str] ip: The IP address to be used for this host, or `ignore` to ignore any DHCP request from this host.
        :param pulumi.Input[str] mac: The hardware address(es) of this host, separated by spaces.
        :param pulumi.Input[str] name: Hostname to assign.
        """
        if dns is not None:
            pulumi.set(__self__, "dns", dns)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def dns(self) -> Optional[pulumi.Input[bool]]:
        """
        Add static forward and reverse DNS entries for this host.
        """
        return pulumi.get(self, "dns")

    @dns.setter
    def dns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dns", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address to be used for this host, or `ignore` to ignore any DHCP request from this host.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[str]]:
        """
        The hardware address(es) of this host, separated by spaces.
        """
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Hostname to assign.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DhcpHostState:
    def __init__(__self__, *,
                 dns: Optional[pulumi.Input[bool]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DhcpHost resources.
        :param pulumi.Input[bool] dns: Add static forward and reverse DNS entries for this host.
        :param pulumi.Input[str] ip: The IP address to be used for this host, or `ignore` to ignore any DHCP request from this host.
        :param pulumi.Input[str] mac: The hardware address(es) of this host, separated by spaces.
        :param pulumi.Input[str] name: Hostname to assign.
        """
        if dns is not None:
            pulumi.set(__self__, "dns", dns)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def dns(self) -> Optional[pulumi.Input[bool]]:
        """
        Add static forward and reverse DNS entries for this host.
        """
        return pulumi.get(self, "dns")

    @dns.setter
    def dns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dns", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address to be used for this host, or `ignore` to ignore any DHCP request from this host.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[str]]:
        """
        The hardware address(es) of this host, separated by spaces.
        """
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Hostname to assign.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class DhcpHost(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns: Optional[pulumi.Input[bool]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Assign a fixed IP address to hosts.

        ## Import

        Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["dhcp", "host"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map({terraformId.[".name"]})' # This command will output something like# [

         {

         "terraformId""cfg123456",

         } ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/dhcpHost:DhcpHost this cfg123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] dns: Add static forward and reverse DNS entries for this host.
        :param pulumi.Input[str] ip: The IP address to be used for this host, or `ignore` to ignore any DHCP request from this host.
        :param pulumi.Input[str] mac: The hardware address(es) of this host, separated by spaces.
        :param pulumi.Input[str] name: Hostname to assign.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DhcpHostArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Assign a fixed IP address to hosts.

        ## Import

        Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["dhcp", "host"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map({terraformId.[".name"]})' # This command will output something like# [

         {

         "terraformId""cfg123456",

         } ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/dhcpHost:DhcpHost this cfg123456
        ```

        :param str resource_name: The name of the resource.
        :param DhcpHostArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DhcpHostArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns: Optional[pulumi.Input[bool]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DhcpHostArgs.__new__(DhcpHostArgs)

            __props__.__dict__["dns"] = dns
            __props__.__dict__["ip"] = ip
            __props__.__dict__["mac"] = mac
            __props__.__dict__["name"] = name
        super(DhcpHost, __self__).__init__(
            'openwrt:index/dhcpHost:DhcpHost',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dns: Optional[pulumi.Input[bool]] = None,
            ip: Optional[pulumi.Input[str]] = None,
            mac: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'DhcpHost':
        """
        Get an existing DhcpHost resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] dns: Add static forward and reverse DNS entries for this host.
        :param pulumi.Input[str] ip: The IP address to be used for this host, or `ignore` to ignore any DHCP request from this host.
        :param pulumi.Input[str] mac: The hardware address(es) of this host, separated by spaces.
        :param pulumi.Input[str] name: Hostname to assign.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DhcpHostState.__new__(_DhcpHostState)

        __props__.__dict__["dns"] = dns
        __props__.__dict__["ip"] = ip
        __props__.__dict__["mac"] = mac
        __props__.__dict__["name"] = name
        return DhcpHost(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def dns(self) -> pulumi.Output[bool]:
        """
        Add static forward and reverse DNS entries for this host.
        """
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Output[str]:
        """
        The IP address to be used for this host, or `ignore` to ignore any DHCP request from this host.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def mac(self) -> pulumi.Output[str]:
        """
        The hardware address(es) of this host, separated by spaces.
        """
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Hostname to assign.
        """
        return pulumi.get(self, "name")


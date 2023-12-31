# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WirelessWifiDeviceArgs', 'WirelessWifiDevice']

@pulumi.input_type
class WirelessWifiDeviceArgs:
    def __init__(__self__, *,
                 channel: pulumi.Input[str],
                 type: pulumi.Input[str],
                 band: Optional[pulumi.Input[str]] = None,
                 cell_density: Optional[pulumi.Input[int]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 htmode: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WirelessWifiDevice resource.
        :param pulumi.Input[str] channel: The wireless channel. Currently, only "auto" is supported.
        :param pulumi.Input[str] type: The type of device. Currently only "mac80211" is supported.
        :param pulumi.Input[str] band: Channel width. Must be one of: "2g", "5g", "6g".
        :param pulumi.Input[int] cell_density: Configures data rates based on the coverage cell density. Must be one of 0, 1, 2, 3.
        :param pulumi.Input[str] country: Two-digit country code. E.g. "US".
        :param pulumi.Input[str] htmode: Channel width. Must be one of: "HE20", "HE40", "HE80", "HE160", "HT20", "HT40", "HT40-", "HT40+", "NONE", "VHT20", "VHT40", "VHT80", "VHT160".
        :param pulumi.Input[str] path: Path of the device in `/sys/devices`.
        """
        pulumi.set(__self__, "channel", channel)
        pulumi.set(__self__, "type", type)
        if band is not None:
            pulumi.set(__self__, "band", band)
        if cell_density is not None:
            pulumi.set(__self__, "cell_density", cell_density)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if htmode is not None:
            pulumi.set(__self__, "htmode", htmode)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def channel(self) -> pulumi.Input[str]:
        """
        The wireless channel. Currently, only "auto" is supported.
        """
        return pulumi.get(self, "channel")

    @channel.setter
    def channel(self, value: pulumi.Input[str]):
        pulumi.set(self, "channel", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of device. Currently only "mac80211" is supported.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def band(self) -> Optional[pulumi.Input[str]]:
        """
        Channel width. Must be one of: "2g", "5g", "6g".
        """
        return pulumi.get(self, "band")

    @band.setter
    def band(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "band", value)

    @property
    @pulumi.getter(name="cellDensity")
    def cell_density(self) -> Optional[pulumi.Input[int]]:
        """
        Configures data rates based on the coverage cell density. Must be one of 0, 1, 2, 3.
        """
        return pulumi.get(self, "cell_density")

    @cell_density.setter
    def cell_density(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cell_density", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        Two-digit country code. E.g. "US".
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter
    def htmode(self) -> Optional[pulumi.Input[str]]:
        """
        Channel width. Must be one of: "HE20", "HE40", "HE80", "HE160", "HT20", "HT40", "HT40-", "HT40+", "NONE", "VHT20", "VHT40", "VHT80", "VHT160".
        """
        return pulumi.get(self, "htmode")

    @htmode.setter
    def htmode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "htmode", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Path of the device in `/sys/devices`.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)


@pulumi.input_type
class _WirelessWifiDeviceState:
    def __init__(__self__, *,
                 band: Optional[pulumi.Input[str]] = None,
                 cell_density: Optional[pulumi.Input[int]] = None,
                 channel: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 htmode: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WirelessWifiDevice resources.
        :param pulumi.Input[str] band: Channel width. Must be one of: "2g", "5g", "6g".
        :param pulumi.Input[int] cell_density: Configures data rates based on the coverage cell density. Must be one of 0, 1, 2, 3.
        :param pulumi.Input[str] channel: The wireless channel. Currently, only "auto" is supported.
        :param pulumi.Input[str] country: Two-digit country code. E.g. "US".
        :param pulumi.Input[str] htmode: Channel width. Must be one of: "HE20", "HE40", "HE80", "HE160", "HT20", "HT40", "HT40-", "HT40+", "NONE", "VHT20", "VHT40", "VHT80", "VHT160".
        :param pulumi.Input[str] path: Path of the device in `/sys/devices`.
        :param pulumi.Input[str] type: The type of device. Currently only "mac80211" is supported.
        """
        if band is not None:
            pulumi.set(__self__, "band", band)
        if cell_density is not None:
            pulumi.set(__self__, "cell_density", cell_density)
        if channel is not None:
            pulumi.set(__self__, "channel", channel)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if htmode is not None:
            pulumi.set(__self__, "htmode", htmode)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def band(self) -> Optional[pulumi.Input[str]]:
        """
        Channel width. Must be one of: "2g", "5g", "6g".
        """
        return pulumi.get(self, "band")

    @band.setter
    def band(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "band", value)

    @property
    @pulumi.getter(name="cellDensity")
    def cell_density(self) -> Optional[pulumi.Input[int]]:
        """
        Configures data rates based on the coverage cell density. Must be one of 0, 1, 2, 3.
        """
        return pulumi.get(self, "cell_density")

    @cell_density.setter
    def cell_density(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cell_density", value)

    @property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[str]]:
        """
        The wireless channel. Currently, only "auto" is supported.
        """
        return pulumi.get(self, "channel")

    @channel.setter
    def channel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        Two-digit country code. E.g. "US".
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter
    def htmode(self) -> Optional[pulumi.Input[str]]:
        """
        Channel width. Must be one of: "HE20", "HE40", "HE80", "HE160", "HT20", "HT40", "HT40-", "HT40+", "NONE", "VHT20", "VHT40", "VHT80", "VHT160".
        """
        return pulumi.get(self, "htmode")

    @htmode.setter
    def htmode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "htmode", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Path of the device in `/sys/devices`.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of device. Currently only "mac80211" is supported.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class WirelessWifiDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 band: Optional[pulumi.Input[str]] = None,
                 cell_density: Optional[pulumi.Input[int]] = None,
                 channel: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 htmode: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The physical radio device.

        ## Import

        Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["wireless", "wifi-device"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map({terraformId.[".name"]})' # This command will output something like# [

         {

         "terraformId""cfg123456",

         },

         {

         "terraformId""cfg123457",

         } ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/wirelessWifiDevice:WirelessWifiDevice five_ghz cfg123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] band: Channel width. Must be one of: "2g", "5g", "6g".
        :param pulumi.Input[int] cell_density: Configures data rates based on the coverage cell density. Must be one of 0, 1, 2, 3.
        :param pulumi.Input[str] channel: The wireless channel. Currently, only "auto" is supported.
        :param pulumi.Input[str] country: Two-digit country code. E.g. "US".
        :param pulumi.Input[str] htmode: Channel width. Must be one of: "HE20", "HE40", "HE80", "HE160", "HT20", "HT40", "HT40-", "HT40+", "NONE", "VHT20", "VHT40", "VHT80", "VHT160".
        :param pulumi.Input[str] path: Path of the device in `/sys/devices`.
        :param pulumi.Input[str] type: The type of device. Currently only "mac80211" is supported.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WirelessWifiDeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The physical radio device.

        ## Import

        Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \\

         --data '{"id"0, "method""foreach", "params"["wireless", "wifi-device"]}' \\

         http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \\

         | jq '.result | map({terraformId.[".name"]})' # This command will output something like# [

         {

         "terraformId""cfg123456",

         },

         {

         "terraformId""cfg123457",

         } ] # We'd then use the information to import the appropriate resource

        ```sh
         $ pulumi import openwrt:index/wirelessWifiDevice:WirelessWifiDevice five_ghz cfg123456
        ```

        :param str resource_name: The name of the resource.
        :param WirelessWifiDeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WirelessWifiDeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 band: Optional[pulumi.Input[str]] = None,
                 cell_density: Optional[pulumi.Input[int]] = None,
                 channel: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 htmode: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WirelessWifiDeviceArgs.__new__(WirelessWifiDeviceArgs)

            __props__.__dict__["band"] = band
            __props__.__dict__["cell_density"] = cell_density
            if channel is None and not opts.urn:
                raise TypeError("Missing required property 'channel'")
            __props__.__dict__["channel"] = channel
            __props__.__dict__["country"] = country
            __props__.__dict__["htmode"] = htmode
            __props__.__dict__["path"] = path
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(WirelessWifiDevice, __self__).__init__(
            'openwrt:index/wirelessWifiDevice:WirelessWifiDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            band: Optional[pulumi.Input[str]] = None,
            cell_density: Optional[pulumi.Input[int]] = None,
            channel: Optional[pulumi.Input[str]] = None,
            country: Optional[pulumi.Input[str]] = None,
            htmode: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'WirelessWifiDevice':
        """
        Get an existing WirelessWifiDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] band: Channel width. Must be one of: "2g", "5g", "6g".
        :param pulumi.Input[int] cell_density: Configures data rates based on the coverage cell density. Must be one of 0, 1, 2, 3.
        :param pulumi.Input[str] channel: The wireless channel. Currently, only "auto" is supported.
        :param pulumi.Input[str] country: Two-digit country code. E.g. "US".
        :param pulumi.Input[str] htmode: Channel width. Must be one of: "HE20", "HE40", "HE80", "HE160", "HT20", "HT40", "HT40-", "HT40+", "NONE", "VHT20", "VHT40", "VHT80", "VHT160".
        :param pulumi.Input[str] path: Path of the device in `/sys/devices`.
        :param pulumi.Input[str] type: The type of device. Currently only "mac80211" is supported.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WirelessWifiDeviceState.__new__(_WirelessWifiDeviceState)

        __props__.__dict__["band"] = band
        __props__.__dict__["cell_density"] = cell_density
        __props__.__dict__["channel"] = channel
        __props__.__dict__["country"] = country
        __props__.__dict__["htmode"] = htmode
        __props__.__dict__["path"] = path
        __props__.__dict__["type"] = type
        return WirelessWifiDevice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def band(self) -> pulumi.Output[str]:
        """
        Channel width. Must be one of: "2g", "5g", "6g".
        """
        return pulumi.get(self, "band")

    @property
    @pulumi.getter(name="cellDensity")
    def cell_density(self) -> pulumi.Output[int]:
        """
        Configures data rates based on the coverage cell density. Must be one of 0, 1, 2, 3.
        """
        return pulumi.get(self, "cell_density")

    @property
    @pulumi.getter
    def channel(self) -> pulumi.Output[str]:
        """
        The wireless channel. Currently, only "auto" is supported.
        """
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter
    def country(self) -> pulumi.Output[str]:
        """
        Two-digit country code. E.g. "US".
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def htmode(self) -> pulumi.Output[str]:
        """
        Channel width. Must be one of: "HE20", "HE40", "HE80", "HE160", "HT20", "HT40", "HT40-", "HT40+", "NONE", "VHT20", "VHT40", "VHT80", "VHT160".
        """
        return pulumi.get(self, "htmode")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        Path of the device in `/sys/devices`.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of device. Currently only "mac80211" is supported.
        """
        return pulumi.get(self, "type")


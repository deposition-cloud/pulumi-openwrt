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
    'GetWirelessWifiIfaceResult',
    'AwaitableGetWirelessWifiIfaceResult',
    'get_wireless_wifi_iface',
    'get_wireless_wifi_iface_output',
]

@pulumi.output_type
class GetWirelessWifiIfaceResult:
    """
    A collection of values returned by getWirelessWifiIface.
    """
    def __init__(__self__, device=None, encryption=None, id=None, isolate=None, key=None, mode=None, network=None, ssid=None, wpa_disable_eapol_key_retries=None):
        if device and not isinstance(device, str):
            raise TypeError("Expected argument 'device' to be a str")
        pulumi.set(__self__, "device", device)
        if encryption and not isinstance(encryption, str):
            raise TypeError("Expected argument 'encryption' to be a str")
        pulumi.set(__self__, "encryption", encryption)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if isolate and not isinstance(isolate, bool):
            raise TypeError("Expected argument 'isolate' to be a bool")
        pulumi.set(__self__, "isolate", isolate)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if ssid and not isinstance(ssid, str):
            raise TypeError("Expected argument 'ssid' to be a str")
        pulumi.set(__self__, "ssid", ssid)
        if wpa_disable_eapol_key_retries and not isinstance(wpa_disable_eapol_key_retries, bool):
            raise TypeError("Expected argument 'wpa_disable_eapol_key_retries' to be a bool")
        pulumi.set(__self__, "wpa_disable_eapol_key_retries", wpa_disable_eapol_key_retries)

    @property
    @pulumi.getter
    def device(self) -> str:
        return pulumi.get(self, "device")

    @property
    @pulumi.getter
    def encryption(self) -> str:
        """
        Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Name of the section. This name is only used when interacting with UCI directly.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def isolate(self) -> bool:
        """
        Isolate wireless clients from each other.
        """
        return pulumi.get(self, "isolate")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def network(self) -> str:
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def ssid(self) -> str:
        """
        The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
        """
        return pulumi.get(self, "ssid")

    @property
    @pulumi.getter(name="wpaDisableEapolKeyRetries")
    def wpa_disable_eapol_key_retries(self) -> bool:
        """
        Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
        """
        return pulumi.get(self, "wpa_disable_eapol_key_retries")


class AwaitableGetWirelessWifiIfaceResult(GetWirelessWifiIfaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWirelessWifiIfaceResult(
            device=self.device,
            encryption=self.encryption,
            id=self.id,
            isolate=self.isolate,
            key=self.key,
            mode=self.mode,
            network=self.network,
            ssid=self.ssid,
            wpa_disable_eapol_key_retries=self.wpa_disable_eapol_key_retries)


def get_wireless_wifi_iface(id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWirelessWifiIfaceResult:
    """
    A wireless network.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    testing = openwrt.get_wireless_wifi_iface(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('openwrt:index/getWirelessWifiIface:getWirelessWifiIface', __args__, opts=opts, typ=GetWirelessWifiIfaceResult).value

    return AwaitableGetWirelessWifiIfaceResult(
        device=pulumi.get(__ret__, 'device'),
        encryption=pulumi.get(__ret__, 'encryption'),
        id=pulumi.get(__ret__, 'id'),
        isolate=pulumi.get(__ret__, 'isolate'),
        key=pulumi.get(__ret__, 'key'),
        mode=pulumi.get(__ret__, 'mode'),
        network=pulumi.get(__ret__, 'network'),
        ssid=pulumi.get(__ret__, 'ssid'),
        wpa_disable_eapol_key_retries=pulumi.get(__ret__, 'wpa_disable_eapol_key_retries'))


@_utilities.lift_output_func(get_wireless_wifi_iface)
def get_wireless_wifi_iface_output(id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWirelessWifiIfaceResult]:
    """
    A wireless network.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openwrt as openwrt

    testing = openwrt.get_wireless_wifi_iface(id="testing")
    ```


    :param str id: Name of the section. This name is only used when interacting with UCI directly.
    """
    ...

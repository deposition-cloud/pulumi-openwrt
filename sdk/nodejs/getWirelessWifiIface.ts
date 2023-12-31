// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * A wireless network.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getWirelessWifiIface({
 *     id: "testing",
 * });
 * ```
 */
export function getWirelessWifiIface(args: GetWirelessWifiIfaceArgs, opts?: pulumi.InvokeOptions): Promise<GetWirelessWifiIfaceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("openwrt:index/getWirelessWifiIface:getWirelessWifiIface", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getWirelessWifiIface.
 */
export interface GetWirelessWifiIfaceArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: string;
}

/**
 * A collection of values returned by getWirelessWifiIface.
 */
export interface GetWirelessWifiIfaceResult {
    readonly device: string;
    /**
     * Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
     */
    readonly encryption: string;
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    readonly id: string;
    /**
     * Isolate wireless clients from each other.
     */
    readonly isolate: boolean;
    /**
     * The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
     */
    readonly key: string;
    /**
     * The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
     */
    readonly mode: string;
    readonly network: string;
    /**
     * The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
     */
    readonly ssid: string;
    /**
     * Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
     */
    readonly wpaDisableEapolKeyRetries: boolean;
}
/**
 * A wireless network.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getWirelessWifiIface({
 *     id: "testing",
 * });
 * ```
 */
export function getWirelessWifiIfaceOutput(args: GetWirelessWifiIfaceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetWirelessWifiIfaceResult> {
    return pulumi.output(args).apply((a: any) => getWirelessWifiIface(a, opts))
}

/**
 * A collection of arguments for invoking getWirelessWifiIface.
 */
export interface GetWirelessWifiIfaceOutputArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: pulumi.Input<string>;
}

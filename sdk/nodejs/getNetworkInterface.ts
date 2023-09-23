// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * A logic network.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const brTesting = openwrt.getNetworkInterface({
 *     id: "testing",
 * });
 * ```
 */
export function getNetworkInterface(args: GetNetworkInterfaceArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkInterfaceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("openwrt:index/getNetworkInterface:getNetworkInterface", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getNetworkInterface.
 */
export interface GetNetworkInterfaceArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: string;
}

/**
 * A collection of values returned by getNetworkInterface.
 */
export interface GetNetworkInterfaceResult {
    /**
     * Specifies whether to bring up this interface on boot.
     */
    readonly auto: boolean;
    readonly device: string;
    /**
     * Disables this interface.
     */
    readonly disabled: boolean;
    /**
     * DNS servers
     */
    readonly dns: string[];
    /**
     * Gateway of the interface
     */
    readonly gateway: string;
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    readonly id: string;
    /**
     * Delegate a prefix of given length to this interface
     */
    readonly ip6assign: number;
    /**
     * IP address of the interface
     */
    readonly ipaddr: string;
    /**
     * Override the MAC Address of this interface.
     */
    readonly macaddr: string;
    /**
     * Override the default MTU on this interface.
     */
    readonly mtu: number;
    /**
     * Netmask of the interface
     */
    readonly netmask: string;
    /**
     * Use DHCP-provided DNS servers.
     */
    readonly peerdns: boolean;
    /**
     * The protocol type of the interface. Currently, only "dhcp, and "static" are supported.
     */
    readonly proto: string;
    /**
     * Behavior for requesting address. Can only be one of "force", "try", or "none".
     */
    readonly reqaddress: string;
    /**
     * Behavior for requesting prefixes. Currently, only "auto" is supported.
     */
    readonly reqprefix: string;
}
/**
 * A logic network.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const brTesting = openwrt.getNetworkInterface({
 *     id: "testing",
 * });
 * ```
 */
export function getNetworkInterfaceOutput(args: GetNetworkInterfaceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetNetworkInterfaceResult> {
    return pulumi.output(args).apply((a: any) => getNetworkInterface(a, opts))
}

/**
 * A collection of arguments for invoking getNetworkInterface.
 */
export interface GetNetworkInterfaceOutputArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: pulumi.Input<string>;
}

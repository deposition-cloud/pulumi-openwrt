// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Legacy VLAN configuration
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getNetworkSwitchVlan({
 *     id: "testing",
 * });
 * ```
 */
export function getNetworkSwitchVlan(args: GetNetworkSwitchVlanArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkSwitchVlanResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("openwrt:index/getNetworkSwitchVlan:getNetworkSwitchVlan", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getNetworkSwitchVlan.
 */
export interface GetNetworkSwitchVlanArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: string;
}

/**
 * A collection of values returned by getNetworkSwitchVlan.
 */
export interface GetNetworkSwitchVlanResult {
    /**
     * A human-readable description of the VLAN configuration.
     */
    readonly description: string;
    /**
     * The switch to configure.
     */
    readonly device: string;
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    readonly id: string;
    /**
     * A string of space-separated port indicies that should be associated with the VLAN. Adding the suffix `"t"` to a port indicates that egress packets should be tagged, for example `"0 1 3t 5t"`.
     */
    readonly ports: string;
    /**
     * The VLAN tag number to use.
     */
    readonly vid: number;
    /**
     * The VLAN "table index" to configure. This index corresponds to the order on LuCI's UI
     */
    readonly vlan: number;
}
/**
 * Legacy VLAN configuration
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getNetworkSwitchVlan({
 *     id: "testing",
 * });
 * ```
 */
export function getNetworkSwitchVlanOutput(args: GetNetworkSwitchVlanOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetNetworkSwitchVlanResult> {
    return pulumi.output(args).apply((a: any) => getNetworkSwitchVlan(a, opts))
}

/**
 * A collection of arguments for invoking getNetworkSwitchVlan.
 */
export interface GetNetworkSwitchVlanOutputArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: pulumi.Input<string>;
}
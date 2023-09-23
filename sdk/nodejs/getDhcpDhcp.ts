// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Per interface lease pools and settings for serving DHCP requests.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getDhcpDhcp({
 *     id: "testing",
 * });
 * ```
 */
export function getDhcpDhcp(args: GetDhcpDhcpArgs, opts?: pulumi.InvokeOptions): Promise<GetDhcpDhcpResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("openwrt:index/getDhcpDhcp:getDhcpDhcp", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getDhcpDhcp.
 */
export interface GetDhcpDhcpArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: string;
}

/**
 * A collection of values returned by getDhcpDhcp.
 */
export interface GetDhcpDhcpResult {
    /**
     * The mode of the DHCPv4 server. Must be one of: "disabled", "server".
     */
    readonly dhcpv4: string;
    /**
     * The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
     */
    readonly dhcpv6: string;
    /**
     * Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
     */
    readonly force: boolean;
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    readonly id: string;
    /**
     * Specifies whether dnsmasq should ignore this pool.
     */
    readonly ignore: boolean;
    readonly interface: string;
    /**
     * The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
     */
    readonly leasetime: string;
    /**
     * Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
     */
    readonly limit: number;
    /**
     * The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
     */
    readonly ra: string;
    /**
     * Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
     */
    readonly raFlags: string[];
    /**
     * Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
     */
    readonly start: number;
}
/**
 * Per interface lease pools and settings for serving DHCP requests.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getDhcpDhcp({
 *     id: "testing",
 * });
 * ```
 */
export function getDhcpDhcpOutput(args: GetDhcpDhcpOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDhcpDhcpResult> {
    return pulumi.output(args).apply((a: any) => getDhcpDhcp(a, opts))
}

/**
 * A collection of arguments for invoking getDhcpDhcp.
 */
export interface GetDhcpDhcpOutputArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: pulumi.Input<string>;
}

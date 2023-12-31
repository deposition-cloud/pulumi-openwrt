// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * An embedded DHCP/DHCPv6/RA server & NDP relay.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getDhcpOdhcpd({
 *     id: "testing",
 * });
 * ```
 */
export function getDhcpOdhcpd(args: GetDhcpOdhcpdArgs, opts?: pulumi.InvokeOptions): Promise<GetDhcpOdhcpdResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("openwrt:index/getDhcpOdhcpd:getDhcpOdhcpd", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getDhcpOdhcpd.
 */
export interface GetDhcpOdhcpdArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: string;
}

/**
 * A collection of values returned by getDhcpOdhcpd.
 */
export interface GetDhcpOdhcpdResult {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    readonly id: string;
    /**
     * Location of the lease/hostfile for DHCPv4 and DHCPv6.
     */
    readonly leasefile: string;
    /**
     * Location of the lease trigger script.
     */
    readonly leasetrigger: string;
    /**
     * Enable DHCPv4 if the 'dhcp' section constains a `start` option, but no `dhcpv4` option set.
     */
    readonly legacy: boolean;
    /**
     * Syslog level priority (0-7).
     */
    readonly loglevel: number;
    /**
     * Use odhcpd as the main DHCPv4 service.
     */
    readonly maindhcp: boolean;
}
/**
 * An embedded DHCP/DHCPv6/RA server & NDP relay.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getDhcpOdhcpd({
 *     id: "testing",
 * });
 * ```
 */
export function getDhcpOdhcpdOutput(args: GetDhcpOdhcpdOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDhcpOdhcpdResult> {
    return pulumi.output(args).apply((a: any) => getDhcpOdhcpd(a, opts))
}

/**
 * A collection of arguments for invoking getDhcpOdhcpd.
 */
export interface GetDhcpOdhcpdOutputArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: pulumi.Input<string>;
}

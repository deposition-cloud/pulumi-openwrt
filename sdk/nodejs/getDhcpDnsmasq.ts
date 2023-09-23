// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * A lightweight DHCP and caching DNS server.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getDhcpDnsmasq({
 *     id: "testing",
 * });
 * ```
 */
export function getDhcpDnsmasq(args: GetDhcpDnsmasqArgs, opts?: pulumi.InvokeOptions): Promise<GetDhcpDnsmasqResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("openwrt:index/getDhcpDnsmasq:getDhcpDnsmasq", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getDhcpDnsmasq.
 */
export interface GetDhcpDnsmasqArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: string;
}

/**
 * A collection of values returned by getDhcpDnsmasq.
 */
export interface GetDhcpDnsmasqResult {
    /**
     * Force dnsmasq into authoritative mode. This speeds up DHCP leasing. Used if this is the only server on the network.
     */
    readonly authoritative: boolean;
    /**
     * DNS domain handed out to DHCP clients.
     */
    readonly domain: string;
    /**
     * Never forward queries for plain names, without dots or domain parts, to upstream nameservers.
     */
    readonly domainneeded: boolean;
    /**
     * Specify the largest EDNS.0 UDP packet which is supported by the DNS forwarder.
     */
    readonly ednspacketMax: number;
    /**
     * Never forward queries for plain names, without dots or domain parts, to upstream nameservers.
     */
    readonly expandhosts: boolean;
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    readonly id: string;
    /**
     * Store DHCP leases in this file.
     */
    readonly leasefile: string;
    /**
     * Look up DNS entries for this domain from `/etc/hosts`.
     */
    readonly local: string;
    /**
     * Choose IP address to match the incoming interface if multiple addresses are assigned to a host name in `/etc/hosts`.
     */
    readonly localiseQueries: boolean;
    /**
     * Accept DNS queries only from hosts whose address is on a local subnet.
     */
    readonly localservice: boolean;
    /**
     * Read static lease entries from `/etc/ethers`, re-read on SIGHUP.
     */
    readonly readethers: boolean;
    /**
     * Allows upstream 127.0.0.0/8 responses, required for DNS based blocklist services. Only takes effect if rebind protection is enabled.
     */
    readonly rebindLocalhost: boolean;
    /**
     * Enables DNS rebind attack protection by discarding upstream RFC1918 responses.
     */
    readonly rebindProtection: boolean;
    /**
     * Specifies an alternative resolv file.
     */
    readonly resolvfile: string;
}
/**
 * A lightweight DHCP and caching DNS server.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openwrt from "@pulumi/openwrt";
 *
 * const testing = openwrt.getDhcpDnsmasq({
 *     id: "testing",
 * });
 * ```
 */
export function getDhcpDnsmasqOutput(args: GetDhcpDnsmasqOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDhcpDnsmasqResult> {
    return pulumi.output(args).apply((a: any) => getDhcpDnsmasq(a, opts))
}

/**
 * A collection of arguments for invoking getDhcpDnsmasq.
 */
export interface GetDhcpDnsmasqOutputArgs {
    /**
     * Name of the section. This name is only used when interacting with UCI directly.
     */
    id: pulumi.Input<string>;
}

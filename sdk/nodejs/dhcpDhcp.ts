// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Per interface lease pools and settings for serving DHCP requests.
 *
 * ## Import
 *
 * Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \
 *
 *  --data '{"id"0, "method""foreach", "params"["dhcp", "dhcp"]}' \
 *
 *  http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \
 *
 *  | jq '.result | map({name.[".name"]})' # This command will output something like# [
 *
 *  {
 *
 *  "name""lan",
 *
 *  },
 *
 *  {
 *
 *  "name""guest",
 *
 *  } ] # We'd then use the information to import the appropriate resource
 *
 * ```sh
 *  $ pulumi import openwrt:index/dhcpDhcp:DhcpDhcp lan lan
 * ```
 */
export class DhcpDhcp extends pulumi.CustomResource {
    /**
     * Get an existing DhcpDhcp resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DhcpDhcpState, opts?: pulumi.CustomResourceOptions): DhcpDhcp {
        return new DhcpDhcp(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openwrt:index/dhcpDhcp:DhcpDhcp';

    /**
     * Returns true if the given object is an instance of DhcpDhcp.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DhcpDhcp {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DhcpDhcp.__pulumiType;
    }

    /**
     * The mode of the DHCPv4 server. Must be one of: "disabled", "server".
     */
    public readonly dhcpv4!: pulumi.Output<string>;
    /**
     * The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
     */
    public readonly dhcpv6!: pulumi.Output<string>;
    /**
     * Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
     */
    public readonly force!: pulumi.Output<boolean>;
    /**
     * Specifies whether dnsmasq should ignore this pool.
     */
    public readonly ignore!: pulumi.Output<boolean>;
    /**
     * The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
     * field in Terraform. Required if `ignore` is not `true`.
     */
    public readonly interface!: pulumi.Output<string>;
    /**
     * The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
     */
    public readonly leasetime!: pulumi.Output<string>;
    /**
     * Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
     */
    public readonly limit!: pulumi.Output<number>;
    /**
     * The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
     */
    public readonly ra!: pulumi.Output<string>;
    /**
     * Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
     */
    public readonly raFlags!: pulumi.Output<string[]>;
    /**
     * Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
     */
    public readonly start!: pulumi.Output<number>;

    /**
     * Create a DhcpDhcp resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DhcpDhcpArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DhcpDhcpArgs | DhcpDhcpState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DhcpDhcpState | undefined;
            resourceInputs["dhcpv4"] = state ? state.dhcpv4 : undefined;
            resourceInputs["dhcpv6"] = state ? state.dhcpv6 : undefined;
            resourceInputs["force"] = state ? state.force : undefined;
            resourceInputs["ignore"] = state ? state.ignore : undefined;
            resourceInputs["interface"] = state ? state.interface : undefined;
            resourceInputs["leasetime"] = state ? state.leasetime : undefined;
            resourceInputs["limit"] = state ? state.limit : undefined;
            resourceInputs["ra"] = state ? state.ra : undefined;
            resourceInputs["raFlags"] = state ? state.raFlags : undefined;
            resourceInputs["start"] = state ? state.start : undefined;
        } else {
            const args = argsOrState as DhcpDhcpArgs | undefined;
            resourceInputs["dhcpv4"] = args ? args.dhcpv4 : undefined;
            resourceInputs["dhcpv6"] = args ? args.dhcpv6 : undefined;
            resourceInputs["force"] = args ? args.force : undefined;
            resourceInputs["ignore"] = args ? args.ignore : undefined;
            resourceInputs["interface"] = args ? args.interface : undefined;
            resourceInputs["leasetime"] = args ? args.leasetime : undefined;
            resourceInputs["limit"] = args ? args.limit : undefined;
            resourceInputs["ra"] = args ? args.ra : undefined;
            resourceInputs["raFlags"] = args ? args.raFlags : undefined;
            resourceInputs["start"] = args ? args.start : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DhcpDhcp.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DhcpDhcp resources.
 */
export interface DhcpDhcpState {
    /**
     * The mode of the DHCPv4 server. Must be one of: "disabled", "server".
     */
    dhcpv4?: pulumi.Input<string>;
    /**
     * The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
     */
    dhcpv6?: pulumi.Input<string>;
    /**
     * Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
     */
    force?: pulumi.Input<boolean>;
    /**
     * Specifies whether dnsmasq should ignore this pool.
     */
    ignore?: pulumi.Input<boolean>;
    /**
     * The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
     * field in Terraform. Required if `ignore` is not `true`.
     */
    interface?: pulumi.Input<string>;
    /**
     * The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
     */
    leasetime?: pulumi.Input<string>;
    /**
     * Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
     */
    limit?: pulumi.Input<number>;
    /**
     * The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
     */
    ra?: pulumi.Input<string>;
    /**
     * Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
     */
    raFlags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
     */
    start?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a DhcpDhcp resource.
 */
export interface DhcpDhcpArgs {
    /**
     * The mode of the DHCPv4 server. Must be one of: "disabled", "server".
     */
    dhcpv4?: pulumi.Input<string>;
    /**
     * The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
     */
    dhcpv6?: pulumi.Input<string>;
    /**
     * Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
     */
    force?: pulumi.Input<boolean>;
    /**
     * Specifies whether dnsmasq should ignore this pool.
     */
    ignore?: pulumi.Input<boolean>;
    /**
     * The interface associated with this DHCP address pool. This name is what the interface is known as in UCI, or the `id`
     * field in Terraform. Required if `ignore` is not `true`.
     */
    interface?: pulumi.Input<string>;
    /**
     * The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
     */
    leasetime?: pulumi.Input<string>;
    /**
     * Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
     */
    limit?: pulumi.Input<number>;
    /**
     * The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
     */
    ra?: pulumi.Input<string>;
    /**
     * Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
     */
    raFlags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
     */
    start?: pulumi.Input<number>;
}
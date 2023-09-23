// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Binds a domain name to an IP address.
 *
 * ## Import
 *
 * Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \
 *
 *  --data '{"id"0, "method""foreach", "params"["dhcp", "domain"]}' \
 *
 *  http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \
 *
 *  | jq '.result | map({terraformId.[".name"]})' # This command will output something like# [
 *
 *  {
 *
 *  "terraformId""cfg123456",
 *
 *  } ] # We'd then use the information to import the appropriate resource
 *
 * ```sh
 *  $ pulumi import openwrt:index/dhcpDomain:DhcpDomain this cfg123456
 * ```
 */
export class DhcpDomain extends pulumi.CustomResource {
    /**
     * Get an existing DhcpDomain resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DhcpDomainState, opts?: pulumi.CustomResourceOptions): DhcpDomain {
        return new DhcpDomain(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openwrt:index/dhcpDomain:DhcpDomain';

    /**
     * Returns true if the given object is an instance of DhcpDomain.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DhcpDomain {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DhcpDomain.__pulumiType;
    }

    /**
     * The IP address to be used for this domain.
     */
    public readonly ip!: pulumi.Output<string>;
    /**
     * Hostname to assign.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a DhcpDomain resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DhcpDomainArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DhcpDomainArgs | DhcpDomainState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DhcpDomainState | undefined;
            resourceInputs["ip"] = state ? state.ip : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as DhcpDomainArgs | undefined;
            if ((!args || args.ip === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ip'");
            }
            resourceInputs["ip"] = args ? args.ip : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DhcpDomain.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DhcpDomain resources.
 */
export interface DhcpDomainState {
    /**
     * The IP address to be used for this domain.
     */
    ip?: pulumi.Input<string>;
    /**
     * Hostname to assign.
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DhcpDomain resource.
 */
export interface DhcpDomainArgs {
    /**
     * The IP address to be used for this domain.
     */
    ip: pulumi.Input<string>;
    /**
     * Hostname to assign.
     */
    name?: pulumi.Input<string>;
}

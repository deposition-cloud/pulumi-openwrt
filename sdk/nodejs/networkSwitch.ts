// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Legacy `swconfig` configuration
 *
 * ## Import
 *
 * The name can be found through LuCI's web UI. It will be in quotes on `/cgi-bin/luci/admin/network/switch`. The page might say:
 *
 *  Switch "switch0" # The "switch0" is the name. The name can also be found from LuCI's JSON-RPC API. # Find the Terraform id and UCI name from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \
 *
 *  --data '{"id"0, "method""foreach", "params"["network", "switch"]}' \
 *
 *  http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \
 *
 *  | jq '.result | map({terraformId.[".name"], uciName.name})' # This command will output something like# [
 *
 *  {
 *
 *  "terraformId""cfg123456",
 *
 *  "uciName""switch0"
 *
 *  } ] # We'd then use the information to import the appropriate resource
 *
 * ```sh
 *  $ pulumi import openwrt:index/networkSwitch:NetworkSwitch switch0 cfg123456
 * ```
 */
export class NetworkSwitch extends pulumi.CustomResource {
    /**
     * Get an existing NetworkSwitch resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkSwitchState, opts?: pulumi.CustomResourceOptions): NetworkSwitch {
        return new NetworkSwitch(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openwrt:index/networkSwitch:NetworkSwitch';

    /**
     * Returns true if the given object is an instance of NetworkSwitch.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NetworkSwitch {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NetworkSwitch.__pulumiType;
    }

    /**
     * Mirror received packets from the `mirrorSourcePort` to the `mirrorMonitorPort`.
     */
    public readonly enableMirrorRx!: pulumi.Output<boolean>;
    /**
     * Mirror transmitted packets from the `mirrorSourcePort` to the `mirrorMonitorPort`.
     */
    public readonly enableMirrorTx!: pulumi.Output<boolean>;
    /**
     * Enables VLAN functionality.
     */
    public readonly enableVlan!: pulumi.Output<boolean>;
    /**
     * Switch port to which packets are mirrored.
     */
    public readonly mirrorMonitorPort!: pulumi.Output<number>;
    /**
     * Switch port from which packets are mirrored.
     */
    public readonly mirrorSourcePort!: pulumi.Output<number>;
    /**
     * Name of the switch. This name is what is shown in LuCI or the `name` field in Terraform. This is not the UCI config
     * name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Reset the switch.
     */
    public readonly reset!: pulumi.Output<boolean>;

    /**
     * Create a NetworkSwitch resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: NetworkSwitchArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkSwitchArgs | NetworkSwitchState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NetworkSwitchState | undefined;
            resourceInputs["enableMirrorRx"] = state ? state.enableMirrorRx : undefined;
            resourceInputs["enableMirrorTx"] = state ? state.enableMirrorTx : undefined;
            resourceInputs["enableVlan"] = state ? state.enableVlan : undefined;
            resourceInputs["mirrorMonitorPort"] = state ? state.mirrorMonitorPort : undefined;
            resourceInputs["mirrorSourcePort"] = state ? state.mirrorSourcePort : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["reset"] = state ? state.reset : undefined;
        } else {
            const args = argsOrState as NetworkSwitchArgs | undefined;
            resourceInputs["enableMirrorRx"] = args ? args.enableMirrorRx : undefined;
            resourceInputs["enableMirrorTx"] = args ? args.enableMirrorTx : undefined;
            resourceInputs["enableVlan"] = args ? args.enableVlan : undefined;
            resourceInputs["mirrorMonitorPort"] = args ? args.mirrorMonitorPort : undefined;
            resourceInputs["mirrorSourcePort"] = args ? args.mirrorSourcePort : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["reset"] = args ? args.reset : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(NetworkSwitch.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NetworkSwitch resources.
 */
export interface NetworkSwitchState {
    /**
     * Mirror received packets from the `mirrorSourcePort` to the `mirrorMonitorPort`.
     */
    enableMirrorRx?: pulumi.Input<boolean>;
    /**
     * Mirror transmitted packets from the `mirrorSourcePort` to the `mirrorMonitorPort`.
     */
    enableMirrorTx?: pulumi.Input<boolean>;
    /**
     * Enables VLAN functionality.
     */
    enableVlan?: pulumi.Input<boolean>;
    /**
     * Switch port to which packets are mirrored.
     */
    mirrorMonitorPort?: pulumi.Input<number>;
    /**
     * Switch port from which packets are mirrored.
     */
    mirrorSourcePort?: pulumi.Input<number>;
    /**
     * Name of the switch. This name is what is shown in LuCI or the `name` field in Terraform. This is not the UCI config
     * name.
     */
    name?: pulumi.Input<string>;
    /**
     * Reset the switch.
     */
    reset?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a NetworkSwitch resource.
 */
export interface NetworkSwitchArgs {
    /**
     * Mirror received packets from the `mirrorSourcePort` to the `mirrorMonitorPort`.
     */
    enableMirrorRx?: pulumi.Input<boolean>;
    /**
     * Mirror transmitted packets from the `mirrorSourcePort` to the `mirrorMonitorPort`.
     */
    enableMirrorTx?: pulumi.Input<boolean>;
    /**
     * Enables VLAN functionality.
     */
    enableVlan?: pulumi.Input<boolean>;
    /**
     * Switch port to which packets are mirrored.
     */
    mirrorMonitorPort?: pulumi.Input<number>;
    /**
     * Switch port from which packets are mirrored.
     */
    mirrorSourcePort?: pulumi.Input<number>;
    /**
     * Name of the switch. This name is what is shown in LuCI or the `name` field in Terraform. This is not the UCI config
     * name.
     */
    name?: pulumi.Input<string>;
    /**
     * Reset the switch.
     */
    reset?: pulumi.Input<boolean>;
}

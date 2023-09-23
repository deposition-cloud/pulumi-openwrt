// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * A wireless network.
 *
 * ## Import
 *
 * Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \
 *
 *  --data '{"id"0, "method""foreach", "params"["wireless", "wifi-iface"]}' \
 *
 *  http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \
 *
 *  | jq '.result | map({terraformId.[".name"]})' # This command will output something like# [
 *
 *  {
 *
 *  "terraformId""cfg123456",
 *
 *  },
 *
 *  {
 *
 *  "terraformId""cfg123457",
 *
 *  } ] # We'd then use the information to import the appropriate resource
 *
 * ```sh
 *  $ pulumi import openwrt:index/wirelessWifiIface:WirelessWifiIface home_network cfg123456
 * ```
 */
export class WirelessWifiIface extends pulumi.CustomResource {
    /**
     * Get an existing WirelessWifiIface resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WirelessWifiIfaceState, opts?: pulumi.CustomResourceOptions): WirelessWifiIface {
        return new WirelessWifiIface(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openwrt:index/wirelessWifiIface:WirelessWifiIface';

    /**
     * Returns true if the given object is an instance of WirelessWifiIface.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WirelessWifiIface {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WirelessWifiIface.__pulumiType;
    }

    /**
     * Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
     */
    public readonly device!: pulumi.Output<string>;
    /**
     * Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
     */
    public readonly encryption!: pulumi.Output<string>;
    /**
     * Isolate wireless clients from each other.
     */
    public readonly isolate!: pulumi.Output<boolean>;
    /**
     * The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
     */
    public readonly key!: pulumi.Output<string>;
    /**
     * The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
     */
    public readonly mode!: pulumi.Output<string>;
    /**
     * Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
     * in Terraform.
     */
    public readonly network!: pulumi.Output<string>;
    /**
     * The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
     */
    public readonly ssid!: pulumi.Output<string>;
    /**
     * Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
     */
    public readonly wpaDisableEapolKeyRetries!: pulumi.Output<boolean>;

    /**
     * Create a WirelessWifiIface resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WirelessWifiIfaceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WirelessWifiIfaceArgs | WirelessWifiIfaceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as WirelessWifiIfaceState | undefined;
            resourceInputs["device"] = state ? state.device : undefined;
            resourceInputs["encryption"] = state ? state.encryption : undefined;
            resourceInputs["isolate"] = state ? state.isolate : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["mode"] = state ? state.mode : undefined;
            resourceInputs["network"] = state ? state.network : undefined;
            resourceInputs["ssid"] = state ? state.ssid : undefined;
            resourceInputs["wpaDisableEapolKeyRetries"] = state ? state.wpaDisableEapolKeyRetries : undefined;
        } else {
            const args = argsOrState as WirelessWifiIfaceArgs | undefined;
            if ((!args || args.device === undefined) && !opts.urn) {
                throw new Error("Missing required property 'device'");
            }
            if ((!args || args.mode === undefined) && !opts.urn) {
                throw new Error("Missing required property 'mode'");
            }
            if ((!args || args.network === undefined) && !opts.urn) {
                throw new Error("Missing required property 'network'");
            }
            if ((!args || args.ssid === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ssid'");
            }
            resourceInputs["device"] = args ? args.device : undefined;
            resourceInputs["encryption"] = args ? args.encryption : undefined;
            resourceInputs["isolate"] = args ? args.isolate : undefined;
            resourceInputs["key"] = args?.key ? pulumi.secret(args.key) : undefined;
            resourceInputs["mode"] = args ? args.mode : undefined;
            resourceInputs["network"] = args ? args.network : undefined;
            resourceInputs["ssid"] = args ? args.ssid : undefined;
            resourceInputs["wpaDisableEapolKeyRetries"] = args ? args.wpaDisableEapolKeyRetries : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["key"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(WirelessWifiIface.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WirelessWifiIface resources.
 */
export interface WirelessWifiIfaceState {
    /**
     * Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
     */
    device?: pulumi.Input<string>;
    /**
     * Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
     */
    encryption?: pulumi.Input<string>;
    /**
     * Isolate wireless clients from each other.
     */
    isolate?: pulumi.Input<boolean>;
    /**
     * The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
     */
    key?: pulumi.Input<string>;
    /**
     * The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
     */
    mode?: pulumi.Input<string>;
    /**
     * Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
     * in Terraform.
     */
    network?: pulumi.Input<string>;
    /**
     * The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
     */
    ssid?: pulumi.Input<string>;
    /**
     * Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
     */
    wpaDisableEapolKeyRetries?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a WirelessWifiIface resource.
 */
export interface WirelessWifiIfaceArgs {
    /**
     * Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
     */
    device: pulumi.Input<string>;
    /**
     * Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
     */
    encryption?: pulumi.Input<string>;
    /**
     * Isolate wireless clients from each other.
     */
    isolate?: pulumi.Input<boolean>;
    /**
     * The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
     */
    key?: pulumi.Input<string>;
    /**
     * The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
     */
    mode: pulumi.Input<string>;
    /**
     * Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
     * in Terraform.
     */
    network: pulumi.Input<string>;
    /**
     * The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
     */
    ssid: pulumi.Input<string>;
    /**
     * Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
     */
    wpaDisableEapolKeyRetries?: pulumi.Input<boolean>;
}

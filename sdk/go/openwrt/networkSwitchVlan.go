// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package openwrt

import (
	"context"
	"reflect"

	"errors"
	"github.com/deposition-cloud/pulumi-openwrt/sdk/go/openwrt/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Legacy VLAN configuration
//
// ## Import
//
// Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \
//
//	--data '{"id"0, "method""foreach", "params"["network", "switch_vlan"]}' \
//
//	http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \
//
//	| jq '.result | map({terraformId.[".name"]})' # This command will output something like# [
//
//	{
//
//	"terraformId""cfg123456",
//
//	},
//
//	{
//
//	"terraformId""cfg123457",
//
//	} ] # We'd then use the information to import the appropriate resource
//
// ```sh
//
//	$ pulumi import openwrt:index/networkSwitchVlan:NetworkSwitchVlan administration cfg123456
//
// ```
type NetworkSwitchVlan struct {
	pulumi.CustomResourceState

	// A human-readable description of the VLAN configuration.
	Description pulumi.StringOutput `pulumi:"description"`
	// The switch to configure.
	Device pulumi.StringOutput `pulumi:"device"`
	// A string of space-separated port indicies that should be associated with the VLAN. Adding the suffix `"t"` to a port indicates that egress packets should be tagged, for example `"0 1 3t 5t"`.
	Ports pulumi.StringOutput `pulumi:"ports"`
	// The VLAN tag number to use.
	Vid pulumi.IntOutput `pulumi:"vid"`
	// The VLAN "table index" to configure. This index corresponds to the order on LuCI's UI
	Vlan pulumi.IntOutput `pulumi:"vlan"`
}

// NewNetworkSwitchVlan registers a new resource with the given unique name, arguments, and options.
func NewNetworkSwitchVlan(ctx *pulumi.Context,
	name string, args *NetworkSwitchVlanArgs, opts ...pulumi.ResourceOption) (*NetworkSwitchVlan, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Device == nil {
		return nil, errors.New("invalid value for required argument 'Device'")
	}
	if args.Ports == nil {
		return nil, errors.New("invalid value for required argument 'Ports'")
	}
	if args.Vlan == nil {
		return nil, errors.New("invalid value for required argument 'Vlan'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource NetworkSwitchVlan
	err := ctx.RegisterResource("openwrt:index/networkSwitchVlan:NetworkSwitchVlan", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkSwitchVlan gets an existing NetworkSwitchVlan resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkSwitchVlan(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkSwitchVlanState, opts ...pulumi.ResourceOption) (*NetworkSwitchVlan, error) {
	var resource NetworkSwitchVlan
	err := ctx.ReadResource("openwrt:index/networkSwitchVlan:NetworkSwitchVlan", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkSwitchVlan resources.
type networkSwitchVlanState struct {
	// A human-readable description of the VLAN configuration.
	Description *string `pulumi:"description"`
	// The switch to configure.
	Device *string `pulumi:"device"`
	// A string of space-separated port indicies that should be associated with the VLAN. Adding the suffix `"t"` to a port indicates that egress packets should be tagged, for example `"0 1 3t 5t"`.
	Ports *string `pulumi:"ports"`
	// The VLAN tag number to use.
	Vid *int `pulumi:"vid"`
	// The VLAN "table index" to configure. This index corresponds to the order on LuCI's UI
	Vlan *int `pulumi:"vlan"`
}

type NetworkSwitchVlanState struct {
	// A human-readable description of the VLAN configuration.
	Description pulumi.StringPtrInput
	// The switch to configure.
	Device pulumi.StringPtrInput
	// A string of space-separated port indicies that should be associated with the VLAN. Adding the suffix `"t"` to a port indicates that egress packets should be tagged, for example `"0 1 3t 5t"`.
	Ports pulumi.StringPtrInput
	// The VLAN tag number to use.
	Vid pulumi.IntPtrInput
	// The VLAN "table index" to configure. This index corresponds to the order on LuCI's UI
	Vlan pulumi.IntPtrInput
}

func (NetworkSwitchVlanState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkSwitchVlanState)(nil)).Elem()
}

type networkSwitchVlanArgs struct {
	// A human-readable description of the VLAN configuration.
	Description *string `pulumi:"description"`
	// The switch to configure.
	Device string `pulumi:"device"`
	// A string of space-separated port indicies that should be associated with the VLAN. Adding the suffix `"t"` to a port indicates that egress packets should be tagged, for example `"0 1 3t 5t"`.
	Ports string `pulumi:"ports"`
	// The VLAN tag number to use.
	Vid *int `pulumi:"vid"`
	// The VLAN "table index" to configure. This index corresponds to the order on LuCI's UI
	Vlan int `pulumi:"vlan"`
}

// The set of arguments for constructing a NetworkSwitchVlan resource.
type NetworkSwitchVlanArgs struct {
	// A human-readable description of the VLAN configuration.
	Description pulumi.StringPtrInput
	// The switch to configure.
	Device pulumi.StringInput
	// A string of space-separated port indicies that should be associated with the VLAN. Adding the suffix `"t"` to a port indicates that egress packets should be tagged, for example `"0 1 3t 5t"`.
	Ports pulumi.StringInput
	// The VLAN tag number to use.
	Vid pulumi.IntPtrInput
	// The VLAN "table index" to configure. This index corresponds to the order on LuCI's UI
	Vlan pulumi.IntInput
}

func (NetworkSwitchVlanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkSwitchVlanArgs)(nil)).Elem()
}

type NetworkSwitchVlanInput interface {
	pulumi.Input

	ToNetworkSwitchVlanOutput() NetworkSwitchVlanOutput
	ToNetworkSwitchVlanOutputWithContext(ctx context.Context) NetworkSwitchVlanOutput
}

func (*NetworkSwitchVlan) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkSwitchVlan)(nil)).Elem()
}

func (i *NetworkSwitchVlan) ToNetworkSwitchVlanOutput() NetworkSwitchVlanOutput {
	return i.ToNetworkSwitchVlanOutputWithContext(context.Background())
}

func (i *NetworkSwitchVlan) ToNetworkSwitchVlanOutputWithContext(ctx context.Context) NetworkSwitchVlanOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkSwitchVlanOutput)
}

func (i *NetworkSwitchVlan) ToOutput(ctx context.Context) pulumix.Output[*NetworkSwitchVlan] {
	return pulumix.Output[*NetworkSwitchVlan]{
		OutputState: i.ToNetworkSwitchVlanOutputWithContext(ctx).OutputState,
	}
}

// NetworkSwitchVlanArrayInput is an input type that accepts NetworkSwitchVlanArray and NetworkSwitchVlanArrayOutput values.
// You can construct a concrete instance of `NetworkSwitchVlanArrayInput` via:
//
//	NetworkSwitchVlanArray{ NetworkSwitchVlanArgs{...} }
type NetworkSwitchVlanArrayInput interface {
	pulumi.Input

	ToNetworkSwitchVlanArrayOutput() NetworkSwitchVlanArrayOutput
	ToNetworkSwitchVlanArrayOutputWithContext(context.Context) NetworkSwitchVlanArrayOutput
}

type NetworkSwitchVlanArray []NetworkSwitchVlanInput

func (NetworkSwitchVlanArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkSwitchVlan)(nil)).Elem()
}

func (i NetworkSwitchVlanArray) ToNetworkSwitchVlanArrayOutput() NetworkSwitchVlanArrayOutput {
	return i.ToNetworkSwitchVlanArrayOutputWithContext(context.Background())
}

func (i NetworkSwitchVlanArray) ToNetworkSwitchVlanArrayOutputWithContext(ctx context.Context) NetworkSwitchVlanArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkSwitchVlanArrayOutput)
}

func (i NetworkSwitchVlanArray) ToOutput(ctx context.Context) pulumix.Output[[]*NetworkSwitchVlan] {
	return pulumix.Output[[]*NetworkSwitchVlan]{
		OutputState: i.ToNetworkSwitchVlanArrayOutputWithContext(ctx).OutputState,
	}
}

// NetworkSwitchVlanMapInput is an input type that accepts NetworkSwitchVlanMap and NetworkSwitchVlanMapOutput values.
// You can construct a concrete instance of `NetworkSwitchVlanMapInput` via:
//
//	NetworkSwitchVlanMap{ "key": NetworkSwitchVlanArgs{...} }
type NetworkSwitchVlanMapInput interface {
	pulumi.Input

	ToNetworkSwitchVlanMapOutput() NetworkSwitchVlanMapOutput
	ToNetworkSwitchVlanMapOutputWithContext(context.Context) NetworkSwitchVlanMapOutput
}

type NetworkSwitchVlanMap map[string]NetworkSwitchVlanInput

func (NetworkSwitchVlanMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkSwitchVlan)(nil)).Elem()
}

func (i NetworkSwitchVlanMap) ToNetworkSwitchVlanMapOutput() NetworkSwitchVlanMapOutput {
	return i.ToNetworkSwitchVlanMapOutputWithContext(context.Background())
}

func (i NetworkSwitchVlanMap) ToNetworkSwitchVlanMapOutputWithContext(ctx context.Context) NetworkSwitchVlanMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkSwitchVlanMapOutput)
}

func (i NetworkSwitchVlanMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*NetworkSwitchVlan] {
	return pulumix.Output[map[string]*NetworkSwitchVlan]{
		OutputState: i.ToNetworkSwitchVlanMapOutputWithContext(ctx).OutputState,
	}
}

type NetworkSwitchVlanOutput struct{ *pulumi.OutputState }

func (NetworkSwitchVlanOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkSwitchVlan)(nil)).Elem()
}

func (o NetworkSwitchVlanOutput) ToNetworkSwitchVlanOutput() NetworkSwitchVlanOutput {
	return o
}

func (o NetworkSwitchVlanOutput) ToNetworkSwitchVlanOutputWithContext(ctx context.Context) NetworkSwitchVlanOutput {
	return o
}

func (o NetworkSwitchVlanOutput) ToOutput(ctx context.Context) pulumix.Output[*NetworkSwitchVlan] {
	return pulumix.Output[*NetworkSwitchVlan]{
		OutputState: o.OutputState,
	}
}

// A human-readable description of the VLAN configuration.
func (o NetworkSwitchVlanOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkSwitchVlan) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// The switch to configure.
func (o NetworkSwitchVlanOutput) Device() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkSwitchVlan) pulumi.StringOutput { return v.Device }).(pulumi.StringOutput)
}

// A string of space-separated port indicies that should be associated with the VLAN. Adding the suffix `"t"` to a port indicates that egress packets should be tagged, for example `"0 1 3t 5t"`.
func (o NetworkSwitchVlanOutput) Ports() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkSwitchVlan) pulumi.StringOutput { return v.Ports }).(pulumi.StringOutput)
}

// The VLAN tag number to use.
func (o NetworkSwitchVlanOutput) Vid() pulumi.IntOutput {
	return o.ApplyT(func(v *NetworkSwitchVlan) pulumi.IntOutput { return v.Vid }).(pulumi.IntOutput)
}

// The VLAN "table index" to configure. This index corresponds to the order on LuCI's UI
func (o NetworkSwitchVlanOutput) Vlan() pulumi.IntOutput {
	return o.ApplyT(func(v *NetworkSwitchVlan) pulumi.IntOutput { return v.Vlan }).(pulumi.IntOutput)
}

type NetworkSwitchVlanArrayOutput struct{ *pulumi.OutputState }

func (NetworkSwitchVlanArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkSwitchVlan)(nil)).Elem()
}

func (o NetworkSwitchVlanArrayOutput) ToNetworkSwitchVlanArrayOutput() NetworkSwitchVlanArrayOutput {
	return o
}

func (o NetworkSwitchVlanArrayOutput) ToNetworkSwitchVlanArrayOutputWithContext(ctx context.Context) NetworkSwitchVlanArrayOutput {
	return o
}

func (o NetworkSwitchVlanArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*NetworkSwitchVlan] {
	return pulumix.Output[[]*NetworkSwitchVlan]{
		OutputState: o.OutputState,
	}
}

func (o NetworkSwitchVlanArrayOutput) Index(i pulumi.IntInput) NetworkSwitchVlanOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *NetworkSwitchVlan {
		return vs[0].([]*NetworkSwitchVlan)[vs[1].(int)]
	}).(NetworkSwitchVlanOutput)
}

type NetworkSwitchVlanMapOutput struct{ *pulumi.OutputState }

func (NetworkSwitchVlanMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkSwitchVlan)(nil)).Elem()
}

func (o NetworkSwitchVlanMapOutput) ToNetworkSwitchVlanMapOutput() NetworkSwitchVlanMapOutput {
	return o
}

func (o NetworkSwitchVlanMapOutput) ToNetworkSwitchVlanMapOutputWithContext(ctx context.Context) NetworkSwitchVlanMapOutput {
	return o
}

func (o NetworkSwitchVlanMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*NetworkSwitchVlan] {
	return pulumix.Output[map[string]*NetworkSwitchVlan]{
		OutputState: o.OutputState,
	}
}

func (o NetworkSwitchVlanMapOutput) MapIndex(k pulumi.StringInput) NetworkSwitchVlanOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *NetworkSwitchVlan {
		return vs[0].(map[string]*NetworkSwitchVlan)[vs[1].(string)]
	}).(NetworkSwitchVlanOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkSwitchVlanInput)(nil)).Elem(), &NetworkSwitchVlan{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkSwitchVlanArrayInput)(nil)).Elem(), NetworkSwitchVlanArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkSwitchVlanMapInput)(nil)).Elem(), NetworkSwitchVlanMap{})
	pulumi.RegisterOutputType(NetworkSwitchVlanOutput{})
	pulumi.RegisterOutputType(NetworkSwitchVlanArrayOutput{})
	pulumi.RegisterOutputType(NetworkSwitchVlanMapOutput{})
}
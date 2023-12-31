// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package openwrt

import (
	"context"
	"reflect"

	"github.com/deposition-cloud/pulumi-openwrt/sdk/go/openwrt/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Contains interface-independent options affecting the network configuration in general.
//
// ## Import
//
// There should only be one `network.globals` config. It seems to default to the UCI name of `globals`.
//
// ```sh
//
//	$ pulumi import openwrt:index/networkGlobals:NetworkGlobals this globals
//
// ```
type NetworkGlobals struct {
	pulumi.CustomResourceState

	// Use every CPU to handle packet traffic.
	PacketSteering pulumi.BoolOutput `pulumi:"packetSteering"`
	// IPv6 ULA prefix for this device.
	UlaPrefix pulumi.StringOutput `pulumi:"ulaPrefix"`
}

// NewNetworkGlobals registers a new resource with the given unique name, arguments, and options.
func NewNetworkGlobals(ctx *pulumi.Context,
	name string, args *NetworkGlobalsArgs, opts ...pulumi.ResourceOption) (*NetworkGlobals, error) {
	if args == nil {
		args = &NetworkGlobalsArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource NetworkGlobals
	err := ctx.RegisterResource("openwrt:index/networkGlobals:NetworkGlobals", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkGlobals gets an existing NetworkGlobals resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkGlobals(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkGlobalsState, opts ...pulumi.ResourceOption) (*NetworkGlobals, error) {
	var resource NetworkGlobals
	err := ctx.ReadResource("openwrt:index/networkGlobals:NetworkGlobals", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkGlobals resources.
type networkGlobalsState struct {
	// Use every CPU to handle packet traffic.
	PacketSteering *bool `pulumi:"packetSteering"`
	// IPv6 ULA prefix for this device.
	UlaPrefix *string `pulumi:"ulaPrefix"`
}

type NetworkGlobalsState struct {
	// Use every CPU to handle packet traffic.
	PacketSteering pulumi.BoolPtrInput
	// IPv6 ULA prefix for this device.
	UlaPrefix pulumi.StringPtrInput
}

func (NetworkGlobalsState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkGlobalsState)(nil)).Elem()
}

type networkGlobalsArgs struct {
	// Use every CPU to handle packet traffic.
	PacketSteering *bool `pulumi:"packetSteering"`
	// IPv6 ULA prefix for this device.
	UlaPrefix *string `pulumi:"ulaPrefix"`
}

// The set of arguments for constructing a NetworkGlobals resource.
type NetworkGlobalsArgs struct {
	// Use every CPU to handle packet traffic.
	PacketSteering pulumi.BoolPtrInput
	// IPv6 ULA prefix for this device.
	UlaPrefix pulumi.StringPtrInput
}

func (NetworkGlobalsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkGlobalsArgs)(nil)).Elem()
}

type NetworkGlobalsInput interface {
	pulumi.Input

	ToNetworkGlobalsOutput() NetworkGlobalsOutput
	ToNetworkGlobalsOutputWithContext(ctx context.Context) NetworkGlobalsOutput
}

func (*NetworkGlobals) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkGlobals)(nil)).Elem()
}

func (i *NetworkGlobals) ToNetworkGlobalsOutput() NetworkGlobalsOutput {
	return i.ToNetworkGlobalsOutputWithContext(context.Background())
}

func (i *NetworkGlobals) ToNetworkGlobalsOutputWithContext(ctx context.Context) NetworkGlobalsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkGlobalsOutput)
}

func (i *NetworkGlobals) ToOutput(ctx context.Context) pulumix.Output[*NetworkGlobals] {
	return pulumix.Output[*NetworkGlobals]{
		OutputState: i.ToNetworkGlobalsOutputWithContext(ctx).OutputState,
	}
}

// NetworkGlobalsArrayInput is an input type that accepts NetworkGlobalsArray and NetworkGlobalsArrayOutput values.
// You can construct a concrete instance of `NetworkGlobalsArrayInput` via:
//
//	NetworkGlobalsArray{ NetworkGlobalsArgs{...} }
type NetworkGlobalsArrayInput interface {
	pulumi.Input

	ToNetworkGlobalsArrayOutput() NetworkGlobalsArrayOutput
	ToNetworkGlobalsArrayOutputWithContext(context.Context) NetworkGlobalsArrayOutput
}

type NetworkGlobalsArray []NetworkGlobalsInput

func (NetworkGlobalsArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkGlobals)(nil)).Elem()
}

func (i NetworkGlobalsArray) ToNetworkGlobalsArrayOutput() NetworkGlobalsArrayOutput {
	return i.ToNetworkGlobalsArrayOutputWithContext(context.Background())
}

func (i NetworkGlobalsArray) ToNetworkGlobalsArrayOutputWithContext(ctx context.Context) NetworkGlobalsArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkGlobalsArrayOutput)
}

func (i NetworkGlobalsArray) ToOutput(ctx context.Context) pulumix.Output[[]*NetworkGlobals] {
	return pulumix.Output[[]*NetworkGlobals]{
		OutputState: i.ToNetworkGlobalsArrayOutputWithContext(ctx).OutputState,
	}
}

// NetworkGlobalsMapInput is an input type that accepts NetworkGlobalsMap and NetworkGlobalsMapOutput values.
// You can construct a concrete instance of `NetworkGlobalsMapInput` via:
//
//	NetworkGlobalsMap{ "key": NetworkGlobalsArgs{...} }
type NetworkGlobalsMapInput interface {
	pulumi.Input

	ToNetworkGlobalsMapOutput() NetworkGlobalsMapOutput
	ToNetworkGlobalsMapOutputWithContext(context.Context) NetworkGlobalsMapOutput
}

type NetworkGlobalsMap map[string]NetworkGlobalsInput

func (NetworkGlobalsMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkGlobals)(nil)).Elem()
}

func (i NetworkGlobalsMap) ToNetworkGlobalsMapOutput() NetworkGlobalsMapOutput {
	return i.ToNetworkGlobalsMapOutputWithContext(context.Background())
}

func (i NetworkGlobalsMap) ToNetworkGlobalsMapOutputWithContext(ctx context.Context) NetworkGlobalsMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkGlobalsMapOutput)
}

func (i NetworkGlobalsMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*NetworkGlobals] {
	return pulumix.Output[map[string]*NetworkGlobals]{
		OutputState: i.ToNetworkGlobalsMapOutputWithContext(ctx).OutputState,
	}
}

type NetworkGlobalsOutput struct{ *pulumi.OutputState }

func (NetworkGlobalsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkGlobals)(nil)).Elem()
}

func (o NetworkGlobalsOutput) ToNetworkGlobalsOutput() NetworkGlobalsOutput {
	return o
}

func (o NetworkGlobalsOutput) ToNetworkGlobalsOutputWithContext(ctx context.Context) NetworkGlobalsOutput {
	return o
}

func (o NetworkGlobalsOutput) ToOutput(ctx context.Context) pulumix.Output[*NetworkGlobals] {
	return pulumix.Output[*NetworkGlobals]{
		OutputState: o.OutputState,
	}
}

// Use every CPU to handle packet traffic.
func (o NetworkGlobalsOutput) PacketSteering() pulumi.BoolOutput {
	return o.ApplyT(func(v *NetworkGlobals) pulumi.BoolOutput { return v.PacketSteering }).(pulumi.BoolOutput)
}

// IPv6 ULA prefix for this device.
func (o NetworkGlobalsOutput) UlaPrefix() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkGlobals) pulumi.StringOutput { return v.UlaPrefix }).(pulumi.StringOutput)
}

type NetworkGlobalsArrayOutput struct{ *pulumi.OutputState }

func (NetworkGlobalsArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkGlobals)(nil)).Elem()
}

func (o NetworkGlobalsArrayOutput) ToNetworkGlobalsArrayOutput() NetworkGlobalsArrayOutput {
	return o
}

func (o NetworkGlobalsArrayOutput) ToNetworkGlobalsArrayOutputWithContext(ctx context.Context) NetworkGlobalsArrayOutput {
	return o
}

func (o NetworkGlobalsArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*NetworkGlobals] {
	return pulumix.Output[[]*NetworkGlobals]{
		OutputState: o.OutputState,
	}
}

func (o NetworkGlobalsArrayOutput) Index(i pulumi.IntInput) NetworkGlobalsOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *NetworkGlobals {
		return vs[0].([]*NetworkGlobals)[vs[1].(int)]
	}).(NetworkGlobalsOutput)
}

type NetworkGlobalsMapOutput struct{ *pulumi.OutputState }

func (NetworkGlobalsMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkGlobals)(nil)).Elem()
}

func (o NetworkGlobalsMapOutput) ToNetworkGlobalsMapOutput() NetworkGlobalsMapOutput {
	return o
}

func (o NetworkGlobalsMapOutput) ToNetworkGlobalsMapOutputWithContext(ctx context.Context) NetworkGlobalsMapOutput {
	return o
}

func (o NetworkGlobalsMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*NetworkGlobals] {
	return pulumix.Output[map[string]*NetworkGlobals]{
		OutputState: o.OutputState,
	}
}

func (o NetworkGlobalsMapOutput) MapIndex(k pulumi.StringInput) NetworkGlobalsOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *NetworkGlobals {
		return vs[0].(map[string]*NetworkGlobals)[vs[1].(string)]
	}).(NetworkGlobalsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkGlobalsInput)(nil)).Elem(), &NetworkGlobals{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkGlobalsArrayInput)(nil)).Elem(), NetworkGlobalsArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkGlobalsMapInput)(nil)).Elem(), NetworkGlobalsMap{})
	pulumi.RegisterOutputType(NetworkGlobalsOutput{})
	pulumi.RegisterOutputType(NetworkGlobalsArrayOutput{})
	pulumi.RegisterOutputType(NetworkGlobalsMapOutput{})
}

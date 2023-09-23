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

// A physical or virtual "device" in OpenWrt jargon. Commonly referred to as an "interface" in other networking jargon.
//
// ## Import
//
// Find the Terraform id and UCI name from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \
//
//	--data '{"id"0, "method""foreach", "params"["network", "device"]}' \
//
//	http://192.168.1.1/cgi-bin/luci/rpc/uci?auth=$AUTH_TOKEN \
//
//	| jq '.result | map({terraformId.[".name"], uciName.name})' # This command will output something like# [
//
//	{
//
//	"terraformId""cfg030f15",
//
//	"uciName""foo"
//
//	},
//
//	{
//
//	"terraformId""cfg040f15",
//
//	"uciName""bar"
//
//	} ] # We'd then use the information to import the appropriate resource
//
// ```sh
//
//	$ pulumi import openwrt:index/networkDevice:NetworkDevice foo cfg030f15
//
// ```
type NetworkDevice struct {
	pulumi.CustomResourceState

	// Bring up the bridge device even if no ports are attached
	BridgeEmpty pulumi.BoolOutput `pulumi:"bridgeEmpty"`
	// Amount of Duplicate Address Detection probes to send
	Dadtransmits pulumi.IntOutput `pulumi:"dadtransmits"`
	// Enable IPv6 for the device.
	Ipv6 pulumi.BoolOutput `pulumi:"ipv6"`
	// MAC Address of the device.
	Macaddr pulumi.StringOutput `pulumi:"macaddr"`
	// Maximum Transmissible Unit.
	Mtu pulumi.IntOutput `pulumi:"mtu"`
	// Maximum Transmissible Unit for IPv6.
	Mtu6 pulumi.IntOutput `pulumi:"mtu6"`
	// Name of the device. This name is referenced in other network configuration.
	Name pulumi.StringOutput `pulumi:"name"`
	// Specifies the wired ports to attach to this bridge.
	Ports pulumi.StringArrayOutput `pulumi:"ports"`
	// Transmission queue length.
	Txqueuelen pulumi.IntOutput `pulumi:"txqueuelen"`
	// The type of device. Currently, only "bridge" is supported.
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewNetworkDevice registers a new resource with the given unique name, arguments, and options.
func NewNetworkDevice(ctx *pulumi.Context,
	name string, args *NetworkDeviceArgs, opts ...pulumi.ResourceOption) (*NetworkDevice, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource NetworkDevice
	err := ctx.RegisterResource("openwrt:index/networkDevice:NetworkDevice", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkDevice gets an existing NetworkDevice resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkDevice(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkDeviceState, opts ...pulumi.ResourceOption) (*NetworkDevice, error) {
	var resource NetworkDevice
	err := ctx.ReadResource("openwrt:index/networkDevice:NetworkDevice", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkDevice resources.
type networkDeviceState struct {
	// Bring up the bridge device even if no ports are attached
	BridgeEmpty *bool `pulumi:"bridgeEmpty"`
	// Amount of Duplicate Address Detection probes to send
	Dadtransmits *int `pulumi:"dadtransmits"`
	// Enable IPv6 for the device.
	Ipv6 *bool `pulumi:"ipv6"`
	// MAC Address of the device.
	Macaddr *string `pulumi:"macaddr"`
	// Maximum Transmissible Unit.
	Mtu *int `pulumi:"mtu"`
	// Maximum Transmissible Unit for IPv6.
	Mtu6 *int `pulumi:"mtu6"`
	// Name of the device. This name is referenced in other network configuration.
	Name *string `pulumi:"name"`
	// Specifies the wired ports to attach to this bridge.
	Ports []string `pulumi:"ports"`
	// Transmission queue length.
	Txqueuelen *int `pulumi:"txqueuelen"`
	// The type of device. Currently, only "bridge" is supported.
	Type *string `pulumi:"type"`
}

type NetworkDeviceState struct {
	// Bring up the bridge device even if no ports are attached
	BridgeEmpty pulumi.BoolPtrInput
	// Amount of Duplicate Address Detection probes to send
	Dadtransmits pulumi.IntPtrInput
	// Enable IPv6 for the device.
	Ipv6 pulumi.BoolPtrInput
	// MAC Address of the device.
	Macaddr pulumi.StringPtrInput
	// Maximum Transmissible Unit.
	Mtu pulumi.IntPtrInput
	// Maximum Transmissible Unit for IPv6.
	Mtu6 pulumi.IntPtrInput
	// Name of the device. This name is referenced in other network configuration.
	Name pulumi.StringPtrInput
	// Specifies the wired ports to attach to this bridge.
	Ports pulumi.StringArrayInput
	// Transmission queue length.
	Txqueuelen pulumi.IntPtrInput
	// The type of device. Currently, only "bridge" is supported.
	Type pulumi.StringPtrInput
}

func (NetworkDeviceState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkDeviceState)(nil)).Elem()
}

type networkDeviceArgs struct {
	// Bring up the bridge device even if no ports are attached
	BridgeEmpty *bool `pulumi:"bridgeEmpty"`
	// Amount of Duplicate Address Detection probes to send
	Dadtransmits *int `pulumi:"dadtransmits"`
	// Enable IPv6 for the device.
	Ipv6 *bool `pulumi:"ipv6"`
	// MAC Address of the device.
	Macaddr *string `pulumi:"macaddr"`
	// Maximum Transmissible Unit.
	Mtu *int `pulumi:"mtu"`
	// Maximum Transmissible Unit for IPv6.
	Mtu6 *int `pulumi:"mtu6"`
	// Name of the device. This name is referenced in other network configuration.
	Name *string `pulumi:"name"`
	// Specifies the wired ports to attach to this bridge.
	Ports []string `pulumi:"ports"`
	// Transmission queue length.
	Txqueuelen *int `pulumi:"txqueuelen"`
	// The type of device. Currently, only "bridge" is supported.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a NetworkDevice resource.
type NetworkDeviceArgs struct {
	// Bring up the bridge device even if no ports are attached
	BridgeEmpty pulumi.BoolPtrInput
	// Amount of Duplicate Address Detection probes to send
	Dadtransmits pulumi.IntPtrInput
	// Enable IPv6 for the device.
	Ipv6 pulumi.BoolPtrInput
	// MAC Address of the device.
	Macaddr pulumi.StringPtrInput
	// Maximum Transmissible Unit.
	Mtu pulumi.IntPtrInput
	// Maximum Transmissible Unit for IPv6.
	Mtu6 pulumi.IntPtrInput
	// Name of the device. This name is referenced in other network configuration.
	Name pulumi.StringPtrInput
	// Specifies the wired ports to attach to this bridge.
	Ports pulumi.StringArrayInput
	// Transmission queue length.
	Txqueuelen pulumi.IntPtrInput
	// The type of device. Currently, only "bridge" is supported.
	Type pulumi.StringInput
}

func (NetworkDeviceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkDeviceArgs)(nil)).Elem()
}

type NetworkDeviceInput interface {
	pulumi.Input

	ToNetworkDeviceOutput() NetworkDeviceOutput
	ToNetworkDeviceOutputWithContext(ctx context.Context) NetworkDeviceOutput
}

func (*NetworkDevice) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkDevice)(nil)).Elem()
}

func (i *NetworkDevice) ToNetworkDeviceOutput() NetworkDeviceOutput {
	return i.ToNetworkDeviceOutputWithContext(context.Background())
}

func (i *NetworkDevice) ToNetworkDeviceOutputWithContext(ctx context.Context) NetworkDeviceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkDeviceOutput)
}

func (i *NetworkDevice) ToOutput(ctx context.Context) pulumix.Output[*NetworkDevice] {
	return pulumix.Output[*NetworkDevice]{
		OutputState: i.ToNetworkDeviceOutputWithContext(ctx).OutputState,
	}
}

// NetworkDeviceArrayInput is an input type that accepts NetworkDeviceArray and NetworkDeviceArrayOutput values.
// You can construct a concrete instance of `NetworkDeviceArrayInput` via:
//
//	NetworkDeviceArray{ NetworkDeviceArgs{...} }
type NetworkDeviceArrayInput interface {
	pulumi.Input

	ToNetworkDeviceArrayOutput() NetworkDeviceArrayOutput
	ToNetworkDeviceArrayOutputWithContext(context.Context) NetworkDeviceArrayOutput
}

type NetworkDeviceArray []NetworkDeviceInput

func (NetworkDeviceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkDevice)(nil)).Elem()
}

func (i NetworkDeviceArray) ToNetworkDeviceArrayOutput() NetworkDeviceArrayOutput {
	return i.ToNetworkDeviceArrayOutputWithContext(context.Background())
}

func (i NetworkDeviceArray) ToNetworkDeviceArrayOutputWithContext(ctx context.Context) NetworkDeviceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkDeviceArrayOutput)
}

func (i NetworkDeviceArray) ToOutput(ctx context.Context) pulumix.Output[[]*NetworkDevice] {
	return pulumix.Output[[]*NetworkDevice]{
		OutputState: i.ToNetworkDeviceArrayOutputWithContext(ctx).OutputState,
	}
}

// NetworkDeviceMapInput is an input type that accepts NetworkDeviceMap and NetworkDeviceMapOutput values.
// You can construct a concrete instance of `NetworkDeviceMapInput` via:
//
//	NetworkDeviceMap{ "key": NetworkDeviceArgs{...} }
type NetworkDeviceMapInput interface {
	pulumi.Input

	ToNetworkDeviceMapOutput() NetworkDeviceMapOutput
	ToNetworkDeviceMapOutputWithContext(context.Context) NetworkDeviceMapOutput
}

type NetworkDeviceMap map[string]NetworkDeviceInput

func (NetworkDeviceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkDevice)(nil)).Elem()
}

func (i NetworkDeviceMap) ToNetworkDeviceMapOutput() NetworkDeviceMapOutput {
	return i.ToNetworkDeviceMapOutputWithContext(context.Background())
}

func (i NetworkDeviceMap) ToNetworkDeviceMapOutputWithContext(ctx context.Context) NetworkDeviceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkDeviceMapOutput)
}

func (i NetworkDeviceMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*NetworkDevice] {
	return pulumix.Output[map[string]*NetworkDevice]{
		OutputState: i.ToNetworkDeviceMapOutputWithContext(ctx).OutputState,
	}
}

type NetworkDeviceOutput struct{ *pulumi.OutputState }

func (NetworkDeviceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkDevice)(nil)).Elem()
}

func (o NetworkDeviceOutput) ToNetworkDeviceOutput() NetworkDeviceOutput {
	return o
}

func (o NetworkDeviceOutput) ToNetworkDeviceOutputWithContext(ctx context.Context) NetworkDeviceOutput {
	return o
}

func (o NetworkDeviceOutput) ToOutput(ctx context.Context) pulumix.Output[*NetworkDevice] {
	return pulumix.Output[*NetworkDevice]{
		OutputState: o.OutputState,
	}
}

// Bring up the bridge device even if no ports are attached
func (o NetworkDeviceOutput) BridgeEmpty() pulumi.BoolOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.BoolOutput { return v.BridgeEmpty }).(pulumi.BoolOutput)
}

// Amount of Duplicate Address Detection probes to send
func (o NetworkDeviceOutput) Dadtransmits() pulumi.IntOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.IntOutput { return v.Dadtransmits }).(pulumi.IntOutput)
}

// Enable IPv6 for the device.
func (o NetworkDeviceOutput) Ipv6() pulumi.BoolOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.BoolOutput { return v.Ipv6 }).(pulumi.BoolOutput)
}

// MAC Address of the device.
func (o NetworkDeviceOutput) Macaddr() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.StringOutput { return v.Macaddr }).(pulumi.StringOutput)
}

// Maximum Transmissible Unit.
func (o NetworkDeviceOutput) Mtu() pulumi.IntOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.IntOutput { return v.Mtu }).(pulumi.IntOutput)
}

// Maximum Transmissible Unit for IPv6.
func (o NetworkDeviceOutput) Mtu6() pulumi.IntOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.IntOutput { return v.Mtu6 }).(pulumi.IntOutput)
}

// Name of the device. This name is referenced in other network configuration.
func (o NetworkDeviceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Specifies the wired ports to attach to this bridge.
func (o NetworkDeviceOutput) Ports() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.StringArrayOutput { return v.Ports }).(pulumi.StringArrayOutput)
}

// Transmission queue length.
func (o NetworkDeviceOutput) Txqueuelen() pulumi.IntOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.IntOutput { return v.Txqueuelen }).(pulumi.IntOutput)
}

// The type of device. Currently, only "bridge" is supported.
func (o NetworkDeviceOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkDevice) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

type NetworkDeviceArrayOutput struct{ *pulumi.OutputState }

func (NetworkDeviceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkDevice)(nil)).Elem()
}

func (o NetworkDeviceArrayOutput) ToNetworkDeviceArrayOutput() NetworkDeviceArrayOutput {
	return o
}

func (o NetworkDeviceArrayOutput) ToNetworkDeviceArrayOutputWithContext(ctx context.Context) NetworkDeviceArrayOutput {
	return o
}

func (o NetworkDeviceArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*NetworkDevice] {
	return pulumix.Output[[]*NetworkDevice]{
		OutputState: o.OutputState,
	}
}

func (o NetworkDeviceArrayOutput) Index(i pulumi.IntInput) NetworkDeviceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *NetworkDevice {
		return vs[0].([]*NetworkDevice)[vs[1].(int)]
	}).(NetworkDeviceOutput)
}

type NetworkDeviceMapOutput struct{ *pulumi.OutputState }

func (NetworkDeviceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkDevice)(nil)).Elem()
}

func (o NetworkDeviceMapOutput) ToNetworkDeviceMapOutput() NetworkDeviceMapOutput {
	return o
}

func (o NetworkDeviceMapOutput) ToNetworkDeviceMapOutputWithContext(ctx context.Context) NetworkDeviceMapOutput {
	return o
}

func (o NetworkDeviceMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*NetworkDevice] {
	return pulumix.Output[map[string]*NetworkDevice]{
		OutputState: o.OutputState,
	}
}

func (o NetworkDeviceMapOutput) MapIndex(k pulumi.StringInput) NetworkDeviceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *NetworkDevice {
		return vs[0].(map[string]*NetworkDevice)[vs[1].(string)]
	}).(NetworkDeviceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkDeviceInput)(nil)).Elem(), &NetworkDevice{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkDeviceArrayInput)(nil)).Elem(), NetworkDeviceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkDeviceMapInput)(nil)).Elem(), NetworkDeviceMap{})
	pulumi.RegisterOutputType(NetworkDeviceOutput{})
	pulumi.RegisterOutputType(NetworkDeviceArrayOutput{})
	pulumi.RegisterOutputType(NetworkDeviceMapOutput{})
}
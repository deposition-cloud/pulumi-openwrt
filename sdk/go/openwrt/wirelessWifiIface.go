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

// A wireless network.
//
// ## Import
//
// Find the Terraform id from LuCI's JSON-RPC API. One way to find this information is with `curl` and `jq`# curl \
//
//	--data '{"id"0, "method""foreach", "params"["wireless", "wifi-iface"]}' \
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
//	$ pulumi import openwrt:index/wirelessWifiIface:WirelessWifiIface home_network cfg123456
//
// ```
type WirelessWifiIface struct {
	pulumi.CustomResourceState

	// Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
	Device pulumi.StringOutput `pulumi:"device"`
	// Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
	Encryption pulumi.StringOutput `pulumi:"encryption"`
	// Isolate wireless clients from each other.
	Isolate pulumi.BoolOutput `pulumi:"isolate"`
	// The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
	Key pulumi.StringOutput `pulumi:"key"`
	// The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
	Mode pulumi.StringOutput `pulumi:"mode"`
	// Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
	// in Terraform.
	Network pulumi.StringOutput `pulumi:"network"`
	// The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
	Ssid pulumi.StringOutput `pulumi:"ssid"`
	// Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
	WpaDisableEapolKeyRetries pulumi.BoolOutput `pulumi:"wpaDisableEapolKeyRetries"`
}

// NewWirelessWifiIface registers a new resource with the given unique name, arguments, and options.
func NewWirelessWifiIface(ctx *pulumi.Context,
	name string, args *WirelessWifiIfaceArgs, opts ...pulumi.ResourceOption) (*WirelessWifiIface, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Device == nil {
		return nil, errors.New("invalid value for required argument 'Device'")
	}
	if args.Mode == nil {
		return nil, errors.New("invalid value for required argument 'Mode'")
	}
	if args.Network == nil {
		return nil, errors.New("invalid value for required argument 'Network'")
	}
	if args.Ssid == nil {
		return nil, errors.New("invalid value for required argument 'Ssid'")
	}
	if args.Key != nil {
		args.Key = pulumi.ToSecret(args.Key).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"key",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource WirelessWifiIface
	err := ctx.RegisterResource("openwrt:index/wirelessWifiIface:WirelessWifiIface", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWirelessWifiIface gets an existing WirelessWifiIface resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWirelessWifiIface(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WirelessWifiIfaceState, opts ...pulumi.ResourceOption) (*WirelessWifiIface, error) {
	var resource WirelessWifiIface
	err := ctx.ReadResource("openwrt:index/wirelessWifiIface:WirelessWifiIface", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WirelessWifiIface resources.
type wirelessWifiIfaceState struct {
	// Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
	Device *string `pulumi:"device"`
	// Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
	Encryption *string `pulumi:"encryption"`
	// Isolate wireless clients from each other.
	Isolate *bool `pulumi:"isolate"`
	// The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
	Key *string `pulumi:"key"`
	// The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
	Mode *string `pulumi:"mode"`
	// Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
	// in Terraform.
	Network *string `pulumi:"network"`
	// The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
	Ssid *string `pulumi:"ssid"`
	// Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
	WpaDisableEapolKeyRetries *bool `pulumi:"wpaDisableEapolKeyRetries"`
}

type WirelessWifiIfaceState struct {
	// Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
	Device pulumi.StringPtrInput
	// Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
	Encryption pulumi.StringPtrInput
	// Isolate wireless clients from each other.
	Isolate pulumi.BoolPtrInput
	// The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
	Key pulumi.StringPtrInput
	// The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
	Mode pulumi.StringPtrInput
	// Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
	// in Terraform.
	Network pulumi.StringPtrInput
	// The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
	Ssid pulumi.StringPtrInput
	// Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
	WpaDisableEapolKeyRetries pulumi.BoolPtrInput
}

func (WirelessWifiIfaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*wirelessWifiIfaceState)(nil)).Elem()
}

type wirelessWifiIfaceArgs struct {
	// Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
	Device string `pulumi:"device"`
	// Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
	Encryption *string `pulumi:"encryption"`
	// Isolate wireless clients from each other.
	Isolate *bool `pulumi:"isolate"`
	// The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
	Key *string `pulumi:"key"`
	// The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
	Mode string `pulumi:"mode"`
	// Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
	// in Terraform.
	Network string `pulumi:"network"`
	// The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
	Ssid string `pulumi:"ssid"`
	// Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
	WpaDisableEapolKeyRetries *bool `pulumi:"wpaDisableEapolKeyRetries"`
}

// The set of arguments for constructing a WirelessWifiIface resource.
type WirelessWifiIfaceArgs struct {
	// Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
	Device pulumi.StringInput
	// Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
	Encryption pulumi.StringPtrInput
	// Isolate wireless clients from each other.
	Isolate pulumi.BoolPtrInput
	// The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
	Key pulumi.StringPtrInput
	// The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
	Mode pulumi.StringInput
	// Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
	// in Terraform.
	Network pulumi.StringInput
	// The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
	Ssid pulumi.StringInput
	// Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
	WpaDisableEapolKeyRetries pulumi.BoolPtrInput
}

func (WirelessWifiIfaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*wirelessWifiIfaceArgs)(nil)).Elem()
}

type WirelessWifiIfaceInput interface {
	pulumi.Input

	ToWirelessWifiIfaceOutput() WirelessWifiIfaceOutput
	ToWirelessWifiIfaceOutputWithContext(ctx context.Context) WirelessWifiIfaceOutput
}

func (*WirelessWifiIface) ElementType() reflect.Type {
	return reflect.TypeOf((**WirelessWifiIface)(nil)).Elem()
}

func (i *WirelessWifiIface) ToWirelessWifiIfaceOutput() WirelessWifiIfaceOutput {
	return i.ToWirelessWifiIfaceOutputWithContext(context.Background())
}

func (i *WirelessWifiIface) ToWirelessWifiIfaceOutputWithContext(ctx context.Context) WirelessWifiIfaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WirelessWifiIfaceOutput)
}

func (i *WirelessWifiIface) ToOutput(ctx context.Context) pulumix.Output[*WirelessWifiIface] {
	return pulumix.Output[*WirelessWifiIface]{
		OutputState: i.ToWirelessWifiIfaceOutputWithContext(ctx).OutputState,
	}
}

// WirelessWifiIfaceArrayInput is an input type that accepts WirelessWifiIfaceArray and WirelessWifiIfaceArrayOutput values.
// You can construct a concrete instance of `WirelessWifiIfaceArrayInput` via:
//
//	WirelessWifiIfaceArray{ WirelessWifiIfaceArgs{...} }
type WirelessWifiIfaceArrayInput interface {
	pulumi.Input

	ToWirelessWifiIfaceArrayOutput() WirelessWifiIfaceArrayOutput
	ToWirelessWifiIfaceArrayOutputWithContext(context.Context) WirelessWifiIfaceArrayOutput
}

type WirelessWifiIfaceArray []WirelessWifiIfaceInput

func (WirelessWifiIfaceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WirelessWifiIface)(nil)).Elem()
}

func (i WirelessWifiIfaceArray) ToWirelessWifiIfaceArrayOutput() WirelessWifiIfaceArrayOutput {
	return i.ToWirelessWifiIfaceArrayOutputWithContext(context.Background())
}

func (i WirelessWifiIfaceArray) ToWirelessWifiIfaceArrayOutputWithContext(ctx context.Context) WirelessWifiIfaceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WirelessWifiIfaceArrayOutput)
}

func (i WirelessWifiIfaceArray) ToOutput(ctx context.Context) pulumix.Output[[]*WirelessWifiIface] {
	return pulumix.Output[[]*WirelessWifiIface]{
		OutputState: i.ToWirelessWifiIfaceArrayOutputWithContext(ctx).OutputState,
	}
}

// WirelessWifiIfaceMapInput is an input type that accepts WirelessWifiIfaceMap and WirelessWifiIfaceMapOutput values.
// You can construct a concrete instance of `WirelessWifiIfaceMapInput` via:
//
//	WirelessWifiIfaceMap{ "key": WirelessWifiIfaceArgs{...} }
type WirelessWifiIfaceMapInput interface {
	pulumi.Input

	ToWirelessWifiIfaceMapOutput() WirelessWifiIfaceMapOutput
	ToWirelessWifiIfaceMapOutputWithContext(context.Context) WirelessWifiIfaceMapOutput
}

type WirelessWifiIfaceMap map[string]WirelessWifiIfaceInput

func (WirelessWifiIfaceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WirelessWifiIface)(nil)).Elem()
}

func (i WirelessWifiIfaceMap) ToWirelessWifiIfaceMapOutput() WirelessWifiIfaceMapOutput {
	return i.ToWirelessWifiIfaceMapOutputWithContext(context.Background())
}

func (i WirelessWifiIfaceMap) ToWirelessWifiIfaceMapOutputWithContext(ctx context.Context) WirelessWifiIfaceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WirelessWifiIfaceMapOutput)
}

func (i WirelessWifiIfaceMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*WirelessWifiIface] {
	return pulumix.Output[map[string]*WirelessWifiIface]{
		OutputState: i.ToWirelessWifiIfaceMapOutputWithContext(ctx).OutputState,
	}
}

type WirelessWifiIfaceOutput struct{ *pulumi.OutputState }

func (WirelessWifiIfaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WirelessWifiIface)(nil)).Elem()
}

func (o WirelessWifiIfaceOutput) ToWirelessWifiIfaceOutput() WirelessWifiIfaceOutput {
	return o
}

func (o WirelessWifiIfaceOutput) ToWirelessWifiIfaceOutputWithContext(ctx context.Context) WirelessWifiIfaceOutput {
	return o
}

func (o WirelessWifiIfaceOutput) ToOutput(ctx context.Context) pulumix.Output[*WirelessWifiIface] {
	return pulumix.Output[*WirelessWifiIface]{
		OutputState: o.OutputState,
	}
}

// Name of the physical device. This name is what the device is known as in LuCI/UCI, or the `id` field in Terraform.
func (o WirelessWifiIfaceOutput) Device() pulumi.StringOutput {
	return o.ApplyT(func(v *WirelessWifiIface) pulumi.StringOutput { return v.Device }).(pulumi.StringOutput)
}

// Encryption method. Currently, only PSK encryption methods are supported. Must be one of: "none", "psk", "psk2", "psk2+aes", "psk2+ccmp", "psk2+tkip", "psk2+tkip+aes", "psk2+tkip+ccmp", "psk+aes", "psk+ccmp", "psk-mixed", "psk-mixed+aes", "psk-mixed+ccmp", "psk-mixed+tkip", "psk-mixed+tkip+aes", "psk-mixed+tkip+ccmp", "psk+tkip", "psk+tkip+aes", "psk+tkip+ccmp", "sae", "sae-mixed".
func (o WirelessWifiIfaceOutput) Encryption() pulumi.StringOutput {
	return o.ApplyT(func(v *WirelessWifiIface) pulumi.StringOutput { return v.Encryption }).(pulumi.StringOutput)
}

// Isolate wireless clients from each other.
func (o WirelessWifiIfaceOutput) Isolate() pulumi.BoolOutput {
	return o.ApplyT(func(v *WirelessWifiIface) pulumi.BoolOutput { return v.Isolate }).(pulumi.BoolOutput)
}

// The pre-shared passphrase from which the pre-shared key will be derived. The clear text key has to be 8-63 characters long.
func (o WirelessWifiIfaceOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *WirelessWifiIface) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

// The operation mode of the wireless network interface controller.. Currently only "ap" is supported.
func (o WirelessWifiIfaceOutput) Mode() pulumi.StringOutput {
	return o.ApplyT(func(v *WirelessWifiIface) pulumi.StringOutput { return v.Mode }).(pulumi.StringOutput)
}

// Network interface to attach the wireless network. This name is what the interface is known as in UCI, or the `id` field
// in Terraform.
func (o WirelessWifiIfaceOutput) Network() pulumi.StringOutput {
	return o.ApplyT(func(v *WirelessWifiIface) pulumi.StringOutput { return v.Network }).(pulumi.StringOutput)
}

// The broadcasted SSID of the wireless network. This is what actual clients will see the network as.
func (o WirelessWifiIfaceOutput) Ssid() pulumi.StringOutput {
	return o.ApplyT(func(v *WirelessWifiIface) pulumi.StringOutput { return v.Ssid }).(pulumi.StringOutput)
}

// Enable WPA key reinstallation attack (KRACK) workaround. This should be `true` to enable KRACK workaround (you almost surely want this enabled).
func (o WirelessWifiIfaceOutput) WpaDisableEapolKeyRetries() pulumi.BoolOutput {
	return o.ApplyT(func(v *WirelessWifiIface) pulumi.BoolOutput { return v.WpaDisableEapolKeyRetries }).(pulumi.BoolOutput)
}

type WirelessWifiIfaceArrayOutput struct{ *pulumi.OutputState }

func (WirelessWifiIfaceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WirelessWifiIface)(nil)).Elem()
}

func (o WirelessWifiIfaceArrayOutput) ToWirelessWifiIfaceArrayOutput() WirelessWifiIfaceArrayOutput {
	return o
}

func (o WirelessWifiIfaceArrayOutput) ToWirelessWifiIfaceArrayOutputWithContext(ctx context.Context) WirelessWifiIfaceArrayOutput {
	return o
}

func (o WirelessWifiIfaceArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*WirelessWifiIface] {
	return pulumix.Output[[]*WirelessWifiIface]{
		OutputState: o.OutputState,
	}
}

func (o WirelessWifiIfaceArrayOutput) Index(i pulumi.IntInput) WirelessWifiIfaceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *WirelessWifiIface {
		return vs[0].([]*WirelessWifiIface)[vs[1].(int)]
	}).(WirelessWifiIfaceOutput)
}

type WirelessWifiIfaceMapOutput struct{ *pulumi.OutputState }

func (WirelessWifiIfaceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WirelessWifiIface)(nil)).Elem()
}

func (o WirelessWifiIfaceMapOutput) ToWirelessWifiIfaceMapOutput() WirelessWifiIfaceMapOutput {
	return o
}

func (o WirelessWifiIfaceMapOutput) ToWirelessWifiIfaceMapOutputWithContext(ctx context.Context) WirelessWifiIfaceMapOutput {
	return o
}

func (o WirelessWifiIfaceMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*WirelessWifiIface] {
	return pulumix.Output[map[string]*WirelessWifiIface]{
		OutputState: o.OutputState,
	}
}

func (o WirelessWifiIfaceMapOutput) MapIndex(k pulumi.StringInput) WirelessWifiIfaceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *WirelessWifiIface {
		return vs[0].(map[string]*WirelessWifiIface)[vs[1].(string)]
	}).(WirelessWifiIfaceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WirelessWifiIfaceInput)(nil)).Elem(), &WirelessWifiIface{})
	pulumi.RegisterInputType(reflect.TypeOf((*WirelessWifiIfaceArrayInput)(nil)).Elem(), WirelessWifiIfaceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WirelessWifiIfaceMapInput)(nil)).Elem(), WirelessWifiIfaceMap{})
	pulumi.RegisterOutputType(WirelessWifiIfaceOutput{})
	pulumi.RegisterOutputType(WirelessWifiIfaceArrayOutput{})
	pulumi.RegisterOutputType(WirelessWifiIfaceMapOutput{})
}

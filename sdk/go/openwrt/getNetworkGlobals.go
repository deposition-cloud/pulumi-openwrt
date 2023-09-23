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
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/deposition-cloud/pulumi-openwrt/sdk/go/openwrt"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := openwrt.LookupNetworkGlobals(ctx, &openwrt.LookupNetworkGlobalsArgs{
//				Id: "globals",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupNetworkGlobals(ctx *pulumi.Context, args *LookupNetworkGlobalsArgs, opts ...pulumi.InvokeOption) (*LookupNetworkGlobalsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNetworkGlobalsResult
	err := ctx.Invoke("openwrt:index/getNetworkGlobals:getNetworkGlobals", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNetworkGlobals.
type LookupNetworkGlobalsArgs struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id string `pulumi:"id"`
}

// A collection of values returned by getNetworkGlobals.
type LookupNetworkGlobalsResult struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id string `pulumi:"id"`
	// Use every CPU to handle packet traffic.
	PacketSteering bool `pulumi:"packetSteering"`
	// IPv6 ULA prefix for this device.
	UlaPrefix string `pulumi:"ulaPrefix"`
}

func LookupNetworkGlobalsOutput(ctx *pulumi.Context, args LookupNetworkGlobalsOutputArgs, opts ...pulumi.InvokeOption) LookupNetworkGlobalsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNetworkGlobalsResult, error) {
			args := v.(LookupNetworkGlobalsArgs)
			r, err := LookupNetworkGlobals(ctx, &args, opts...)
			var s LookupNetworkGlobalsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupNetworkGlobalsResultOutput)
}

// A collection of arguments for invoking getNetworkGlobals.
type LookupNetworkGlobalsOutputArgs struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupNetworkGlobalsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkGlobalsArgs)(nil)).Elem()
}

// A collection of values returned by getNetworkGlobals.
type LookupNetworkGlobalsResultOutput struct{ *pulumi.OutputState }

func (LookupNetworkGlobalsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkGlobalsResult)(nil)).Elem()
}

func (o LookupNetworkGlobalsResultOutput) ToLookupNetworkGlobalsResultOutput() LookupNetworkGlobalsResultOutput {
	return o
}

func (o LookupNetworkGlobalsResultOutput) ToLookupNetworkGlobalsResultOutputWithContext(ctx context.Context) LookupNetworkGlobalsResultOutput {
	return o
}

func (o LookupNetworkGlobalsResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupNetworkGlobalsResult] {
	return pulumix.Output[LookupNetworkGlobalsResult]{
		OutputState: o.OutputState,
	}
}

// Name of the section. This name is only used when interacting with UCI directly.
func (o LookupNetworkGlobalsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkGlobalsResult) string { return v.Id }).(pulumi.StringOutput)
}

// Use every CPU to handle packet traffic.
func (o LookupNetworkGlobalsResultOutput) PacketSteering() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupNetworkGlobalsResult) bool { return v.PacketSteering }).(pulumi.BoolOutput)
}

// IPv6 ULA prefix for this device.
func (o LookupNetworkGlobalsResultOutput) UlaPrefix() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkGlobalsResult) string { return v.UlaPrefix }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNetworkGlobalsResultOutput{})
}

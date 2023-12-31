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

// Per interface lease pools and settings for serving DHCP requests.
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
//			_, err := openwrt.LookupDhcpDhcp(ctx, &openwrt.LookupDhcpDhcpArgs{
//				Id: "testing",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupDhcpDhcp(ctx *pulumi.Context, args *LookupDhcpDhcpArgs, opts ...pulumi.InvokeOption) (*LookupDhcpDhcpResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDhcpDhcpResult
	err := ctx.Invoke("openwrt:index/getDhcpDhcp:getDhcpDhcp", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDhcpDhcp.
type LookupDhcpDhcpArgs struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id string `pulumi:"id"`
}

// A collection of values returned by getDhcpDhcp.
type LookupDhcpDhcpResult struct {
	// The mode of the DHCPv4 server. Must be one of: "disabled", "server".
	Dhcpv4 string `pulumi:"dhcpv4"`
	// The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
	Dhcpv6 string `pulumi:"dhcpv6"`
	// Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
	Force bool `pulumi:"force"`
	// Name of the section. This name is only used when interacting with UCI directly.
	Id string `pulumi:"id"`
	// Specifies whether dnsmasq should ignore this pool.
	Ignore    bool   `pulumi:"ignore"`
	Interface string `pulumi:"interface"`
	// The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
	Leasetime string `pulumi:"leasetime"`
	// Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
	Limit int `pulumi:"limit"`
	// The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
	Ra string `pulumi:"ra"`
	// Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
	RaFlags []string `pulumi:"raFlags"`
	// Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
	Start int `pulumi:"start"`
}

func LookupDhcpDhcpOutput(ctx *pulumi.Context, args LookupDhcpDhcpOutputArgs, opts ...pulumi.InvokeOption) LookupDhcpDhcpResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDhcpDhcpResult, error) {
			args := v.(LookupDhcpDhcpArgs)
			r, err := LookupDhcpDhcp(ctx, &args, opts...)
			var s LookupDhcpDhcpResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDhcpDhcpResultOutput)
}

// A collection of arguments for invoking getDhcpDhcp.
type LookupDhcpDhcpOutputArgs struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDhcpDhcpOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDhcpDhcpArgs)(nil)).Elem()
}

// A collection of values returned by getDhcpDhcp.
type LookupDhcpDhcpResultOutput struct{ *pulumi.OutputState }

func (LookupDhcpDhcpResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDhcpDhcpResult)(nil)).Elem()
}

func (o LookupDhcpDhcpResultOutput) ToLookupDhcpDhcpResultOutput() LookupDhcpDhcpResultOutput {
	return o
}

func (o LookupDhcpDhcpResultOutput) ToLookupDhcpDhcpResultOutputWithContext(ctx context.Context) LookupDhcpDhcpResultOutput {
	return o
}

func (o LookupDhcpDhcpResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupDhcpDhcpResult] {
	return pulumix.Output[LookupDhcpDhcpResult]{
		OutputState: o.OutputState,
	}
}

// The mode of the DHCPv4 server. Must be one of: "disabled", "server".
func (o LookupDhcpDhcpResultOutput) Dhcpv4() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) string { return v.Dhcpv4 }).(pulumi.StringOutput)
}

// The mode of the DHCPv6 server. Must be one of: "disabled", "relay", "server".
func (o LookupDhcpDhcpResultOutput) Dhcpv6() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) string { return v.Dhcpv6 }).(pulumi.StringOutput)
}

// Forces DHCP serving on the specified interface even if another DHCP server is detected on the same network segment.
func (o LookupDhcpDhcpResultOutput) Force() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) bool { return v.Force }).(pulumi.BoolOutput)
}

// Name of the section. This name is only used when interacting with UCI directly.
func (o LookupDhcpDhcpResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) string { return v.Id }).(pulumi.StringOutput)
}

// Specifies whether dnsmasq should ignore this pool.
func (o LookupDhcpDhcpResultOutput) Ignore() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) bool { return v.Ignore }).(pulumi.BoolOutput)
}

func (o LookupDhcpDhcpResultOutput) Interface() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) string { return v.Interface }).(pulumi.StringOutput)
}

// The lease time of addresses handed out to clients. E.g. `12h`, or `30m`. Required if `ignore` is not `true`.
func (o LookupDhcpDhcpResultOutput) Leasetime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) string { return v.Leasetime }).(pulumi.StringOutput)
}

// Specifies the size of the address pool. E.g. With start = 100, and limit = 150, the maximum address will be 249. Required if `ignore` is not `true`.
func (o LookupDhcpDhcpResultOutput) Limit() pulumi.IntOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) int { return v.Limit }).(pulumi.IntOutput)
}

// The mode of Router Advertisements. Must be one of: "disabled", "relay", "server".
func (o LookupDhcpDhcpResultOutput) Ra() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) string { return v.Ra }).(pulumi.StringOutput)
}

// Router Advertisement flags to include in messages. Must be one of: "home-agent", "managed-config", "none", "other-config".
func (o LookupDhcpDhcpResultOutput) RaFlags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) []string { return v.RaFlags }).(pulumi.StringArrayOutput)
}

// Specifies the offset from the network address of the underlying interface to calculate the minimum address that may be leased to clients. It may be greater than 255 to span subnets. Required if `ignore` is not `true`.
func (o LookupDhcpDhcpResultOutput) Start() pulumi.IntOutput {
	return o.ApplyT(func(v LookupDhcpDhcpResult) int { return v.Start }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDhcpDhcpResultOutput{})
}

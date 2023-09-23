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

// Binds a domain name to an IP address.
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
//			_, err := openwrt.LookupDhcpDomain(ctx, &openwrt.LookupDhcpDomainArgs{
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
func LookupDhcpDomain(ctx *pulumi.Context, args *LookupDhcpDomainArgs, opts ...pulumi.InvokeOption) (*LookupDhcpDomainResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDhcpDomainResult
	err := ctx.Invoke("openwrt:index/getDhcpDomain:getDhcpDomain", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDhcpDomain.
type LookupDhcpDomainArgs struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id string `pulumi:"id"`
}

// A collection of values returned by getDhcpDomain.
type LookupDhcpDomainResult struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id string `pulumi:"id"`
	// The IP address to be used for this domain.
	Ip string `pulumi:"ip"`
	// Hostname to assign.
	Name string `pulumi:"name"`
}

func LookupDhcpDomainOutput(ctx *pulumi.Context, args LookupDhcpDomainOutputArgs, opts ...pulumi.InvokeOption) LookupDhcpDomainResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDhcpDomainResult, error) {
			args := v.(LookupDhcpDomainArgs)
			r, err := LookupDhcpDomain(ctx, &args, opts...)
			var s LookupDhcpDomainResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDhcpDomainResultOutput)
}

// A collection of arguments for invoking getDhcpDomain.
type LookupDhcpDomainOutputArgs struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDhcpDomainOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDhcpDomainArgs)(nil)).Elem()
}

// A collection of values returned by getDhcpDomain.
type LookupDhcpDomainResultOutput struct{ *pulumi.OutputState }

func (LookupDhcpDomainResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDhcpDomainResult)(nil)).Elem()
}

func (o LookupDhcpDomainResultOutput) ToLookupDhcpDomainResultOutput() LookupDhcpDomainResultOutput {
	return o
}

func (o LookupDhcpDomainResultOutput) ToLookupDhcpDomainResultOutputWithContext(ctx context.Context) LookupDhcpDomainResultOutput {
	return o
}

func (o LookupDhcpDomainResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupDhcpDomainResult] {
	return pulumix.Output[LookupDhcpDomainResult]{
		OutputState: o.OutputState,
	}
}

// Name of the section. This name is only used when interacting with UCI directly.
func (o LookupDhcpDomainResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDomainResult) string { return v.Id }).(pulumi.StringOutput)
}

// The IP address to be used for this domain.
func (o LookupDhcpDomainResultOutput) Ip() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDomainResult) string { return v.Ip }).(pulumi.StringOutput)
}

// Hostname to assign.
func (o LookupDhcpDomainResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDhcpDomainResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDhcpDomainResultOutput{})
}

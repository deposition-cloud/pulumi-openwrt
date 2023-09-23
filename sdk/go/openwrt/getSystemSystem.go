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

// Provides system data about an OpenWrt device
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
//			_, err := openwrt.LookupSystemSystem(ctx, &openwrt.LookupSystemSystemArgs{
//				Id: "cfg01e48a",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupSystemSystem(ctx *pulumi.Context, args *LookupSystemSystemArgs, opts ...pulumi.InvokeOption) (*LookupSystemSystemResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSystemSystemResult
	err := ctx.Invoke("openwrt:index/getSystemSystem:getSystemSystem", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSystemSystem.
type LookupSystemSystemArgs struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id string `pulumi:"id"`
}

// A collection of values returned by getSystemSystem.
type LookupSystemSystemResult struct {
	// The maximum log level for kernel messages to be logged to the console.
	Conloglevel int `pulumi:"conloglevel"`
	// The minimum level for cron messages to be logged to syslog.
	Cronloglevel int `pulumi:"cronloglevel"`
	// The hostname for the system.
	Description string `pulumi:"description"`
	// A short single-line description for the system.
	Hostname string `pulumi:"hostname"`
	// Name of the section. This name is only used when interacting with UCI directly.
	Id string `pulumi:"id"`
	// Size of the file based log buffer in KiB.
	LogSize int `pulumi:"logSize"`
	// Multi-line free-form text about the system.
	Notes string `pulumi:"notes"`
	// The POSIX.1 time zone string. This has no corresponding value in LuCI. See: https://github.com/openwrt/luci/blob/cd82ccacef78d3bb8b8af6b87dabb9e892e2b2aa/modules/luci-base/luasrc/sys/zoneinfo/tzdata.lua.
	Timezone string `pulumi:"timezone"`
	// Require authentication for local users to log in the system.
	Ttylogin bool `pulumi:"ttylogin"`
	// The IANA/Olson time zone string. This corresponds to "Timezone" in LuCI. See: https://github.com/openwrt/luci/blob/cd82ccacef78d3bb8b8af6b87dabb9e892e2b2aa/modules/luci-base/luasrc/sys/zoneinfo/tzdata.lua.
	Zonename string `pulumi:"zonename"`
}

func LookupSystemSystemOutput(ctx *pulumi.Context, args LookupSystemSystemOutputArgs, opts ...pulumi.InvokeOption) LookupSystemSystemResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSystemSystemResult, error) {
			args := v.(LookupSystemSystemArgs)
			r, err := LookupSystemSystem(ctx, &args, opts...)
			var s LookupSystemSystemResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSystemSystemResultOutput)
}

// A collection of arguments for invoking getSystemSystem.
type LookupSystemSystemOutputArgs struct {
	// Name of the section. This name is only used when interacting with UCI directly.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupSystemSystemOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSystemSystemArgs)(nil)).Elem()
}

// A collection of values returned by getSystemSystem.
type LookupSystemSystemResultOutput struct{ *pulumi.OutputState }

func (LookupSystemSystemResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSystemSystemResult)(nil)).Elem()
}

func (o LookupSystemSystemResultOutput) ToLookupSystemSystemResultOutput() LookupSystemSystemResultOutput {
	return o
}

func (o LookupSystemSystemResultOutput) ToLookupSystemSystemResultOutputWithContext(ctx context.Context) LookupSystemSystemResultOutput {
	return o
}

func (o LookupSystemSystemResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupSystemSystemResult] {
	return pulumix.Output[LookupSystemSystemResult]{
		OutputState: o.OutputState,
	}
}

// The maximum log level for kernel messages to be logged to the console.
func (o LookupSystemSystemResultOutput) Conloglevel() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) int { return v.Conloglevel }).(pulumi.IntOutput)
}

// The minimum level for cron messages to be logged to syslog.
func (o LookupSystemSystemResultOutput) Cronloglevel() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) int { return v.Cronloglevel }).(pulumi.IntOutput)
}

// The hostname for the system.
func (o LookupSystemSystemResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) string { return v.Description }).(pulumi.StringOutput)
}

// A short single-line description for the system.
func (o LookupSystemSystemResultOutput) Hostname() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) string { return v.Hostname }).(pulumi.StringOutput)
}

// Name of the section. This name is only used when interacting with UCI directly.
func (o LookupSystemSystemResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) string { return v.Id }).(pulumi.StringOutput)
}

// Size of the file based log buffer in KiB.
func (o LookupSystemSystemResultOutput) LogSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) int { return v.LogSize }).(pulumi.IntOutput)
}

// Multi-line free-form text about the system.
func (o LookupSystemSystemResultOutput) Notes() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) string { return v.Notes }).(pulumi.StringOutput)
}

// The POSIX.1 time zone string. This has no corresponding value in LuCI. See: https://github.com/openwrt/luci/blob/cd82ccacef78d3bb8b8af6b87dabb9e892e2b2aa/modules/luci-base/luasrc/sys/zoneinfo/tzdata.lua.
func (o LookupSystemSystemResultOutput) Timezone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) string { return v.Timezone }).(pulumi.StringOutput)
}

// Require authentication for local users to log in the system.
func (o LookupSystemSystemResultOutput) Ttylogin() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) bool { return v.Ttylogin }).(pulumi.BoolOutput)
}

// The IANA/Olson time zone string. This corresponds to "Timezone" in LuCI. See: https://github.com/openwrt/luci/blob/cd82ccacef78d3bb8b8af6b87dabb9e892e2b2aa/modules/luci-base/luasrc/sys/zoneinfo/tzdata.lua.
func (o LookupSystemSystemResultOutput) Zonename() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSystemSystemResult) string { return v.Zonename }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSystemSystemResultOutput{})
}

---
title: Openwrt Installation & Configuration
meta_desc: Information on how to install the Openwrt provider.
layout: installation
---

## Installation

The Pulumi Openwrt provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@deposition-cloud/openwrt`](https://www.npmjs.com/package/@deposition-cloud/openwrt)
* Python: [`pulumiverse_openwrt`](https://pypi.org/project/pulumiverse_openwrt/)
* Go: [`github.com/deposition-cloud/pulumi-openwrt/sdk/go/openwrt`](https://pkg.go.dev/github.com/deposition-cloud/pulumi-openwrt/sdk/go/openwrt)
* .NET: [`Pulumiverse.Openwrt`](https://www.nuget.org/packages/Pulumiverse.Openwrt)


## Configuration

> Note:  
> Replace the following **sample content**, with the configuration options
> of the wrapped Terraform provider and remove this note.

The following configuration points are available for the `openwrt` provider:

- `openwrt:apiKey` (environment: `openwrt_API_KEY`) - the API key for `openwrt`
- `openwrt:region` (environment: `openwrt_REGION`) - the region in which to deploy resources

### Provider Binary

The Openwrt provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource openwrt <version>
```

Replace the version string `<version>` with your desired version.

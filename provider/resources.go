// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package openwrt

import (
	_ "embed"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/deposition-cloud/pulumi-openwrt/provider/pkg/version"
	"github.com/ettle/strcase"
	"github.com/joneshf/terraform-provider-openwrt/openwrt"
	pf "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
)

//go:embed cmd/pulumi-resource-openwrt/bridge-metadata.json
var bridgeMetadata []byte

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	mainMod = "index" // the openwrt module
)

func convertName(name string) string {
	idx := strings.Index(name, "_")
	contract.Assertf(idx > 0 && idx < len(name)-1, "Invalid snake case name %s", name)
	name = name[idx+1:]
	contract.Assertf(len(name) > 0, "Invalid snake case name %s", name)
	return strcase.ToPascal(name)
}

func makeDataSource(mod string, name string) tokens.ModuleMember {
	name = convertName(name)
	return tfbridge.MakeDataSource("openwrt", mod, "get"+name)
}

func makeResource(mod string, res string) tokens.Type {
	return tfbridge.MakeResource("openwrt", mod, convertName(res))
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := pf.ShimProvider(openwrt.New(version.Version, os.LookupEnv))
	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "openwrt",
		// DisplayName is a way to be able to change the casing of the provider
		// name when being displayed on the Pulumi registry
		DisplayName: "OpenWRT",
		// The default publisher for all packages is Pulumi.
		// Change this to your personal name (or a company name) that you
		// would like to be shown in the Pulumi Registry if this package is published
		// there.
		Publisher: "deposition-cloud",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "https://raw.githubusercontent.com/deposition-cloud/pulumi-openwrt/main/docs/openwrt.png",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "github://api.github.com/deposition-cloud/pulumi-openwrt",
		Description:       "A Pulumi package for creating and managing OpenWRT resources",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords: []string{
			"pulumi",
			"openwrt",
			"category/network",
		},
		License:    "Apache-2.0",
		Homepage:   "https://github.com/deposition-cloud/pulumi-openwrt",
		Repository: "https://github.com/deposition-cloud/pulumi-openwrt",
		// The GitHub Org for the provider - defaults to `terraform-providers`. Note that this
		// should match the TF provider module's require directive, not any replace directives.
		Version:      version.Version,
		GitHubOrg:    "joneshf",
		MetadataInfo: tfbridge.NewProviderMetadata(bridgeMetadata),
		Config:       map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: tfbridge.MakeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			// Map each resource in the Terraform provider to a Pulumi type. Two examples
			// are below - the single line form is the common case. The multi-line form is
			// needed only if you wish to override types or other default options.
			//
			// "aws_iam_role": {Tok: makeResource(mainMod(mainMod, "aws_iam_role")}
			//
			// "aws_acm_certificate": {
			// 	Tok: Tok: makeResource(mainMod(mainMod, "aws_acm_certificate"),
			// 	Fields: map[string]*tfbridge.SchemaInfo{
			// 		"tags": {Type: tfbridge.MakeType("openwrt", "Tags")},
			// 	},
			// },
			"openwrt_dhcp_dhcp":            {Tok: makeResource(mainMod, "openwrt_dhcp_dhcp")},
			"openwrt_dhcp_dnsmasq":         {Tok: makeResource(mainMod, "openwrt_dhcp_dnsmasq")},
			"openwrt_dhcp_domain":          {Tok: makeResource(mainMod, "openwrt_dhcp_domain")},
			"openwrt_dhcp_host":            {Tok: makeResource(mainMod, "openwrt_dhcp_host")},
			"openwrt_dhcp_odhcpd":          {Tok: makeResource(mainMod, "openwrt_dhcp_odhcpd")},
			"openwrt_network_device":       {Tok: makeResource(mainMod, "openwrt_network_device")},
			"openwrt_network_globals":      {Tok: makeResource(mainMod, "openwrt_network_globals")},
			"openwrt_network_interface":    {Tok: makeResource(mainMod, "openwrt_network_interface")},
			"openwrt_network_switch":       {Tok: makeResource(mainMod, "openwrt_network_switch")},
			"openwrt_network_switch_vlan":  {Tok: makeResource(mainMod, "openwrt_network_switch_vlan")},
			"openwrt_system_system":        {Tok: makeResource(mainMod, "openwrt_system_system")},
			"openwrt_wireless_wifi_device": {Tok: makeResource(mainMod, "openwrt_wireless_wifi_device")},
			"openwrt_wireless_wifi_iface":  {Tok: makeResource(mainMod, "openwrt_wireless_wifi_iface")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: makeDataSource(mainMod, "aws_ami")},
			"openwrt_dhcp_dhcp":            {Tok: makeDataSource(mainMod, "openwrt_dhcp_dhcp")},
			"openwrt_dhcp_dnsmasq":         {Tok: makeDataSource(mainMod, "openwrt_dhcp_dnsmasq")},
			"openwrt_dhcp_domain":          {Tok: makeDataSource(mainMod, "openwrt_dhcp_domain")},
			"openwrt_dhcp_host":            {Tok: makeDataSource(mainMod, "openwrt_dhcp_host")},
			"openwrt_dhcp_odhcpd":          {Tok: makeDataSource(mainMod, "openwrt_dhcp_odhcpd")},
			"openwrt_network_device":       {Tok: makeDataSource(mainMod, "openwrt_network_device")},
			"openwrt_network_globals":      {Tok: makeDataSource(mainMod, "openwrt_network_globals")},
			"openwrt_network_interface":    {Tok: makeDataSource(mainMod, "openwrt_network_interface")},
			"openwrt_network_switch":       {Tok: makeDataSource(mainMod, "openwrt_network_switch")},
			"openwrt_network_switch_vlan":  {Tok: makeDataSource(mainMod, "openwrt_network_switch_vlan")},
			"openwrt_system_system":        {Tok: makeDataSource(mainMod, "openwrt_system_system")},
			"openwrt_wireless_wifi_device": {Tok: makeDataSource(mainMod, "openwrt_wireless_wifi_device")},
			"openwrt_wireless_wifi_iface":  {Tok: makeDataSource(mainMod, "openwrt_wireless_wifi_iface")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@deposition-cloud/pulumi-openwrt",

			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "pulumiverse_openwrt",

			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/deposition-cloud/pulumi-%[1]s/sdk/", "openwrt"),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				"openwrt",
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "Pulumiverse",

			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
		Java: &tfbridge.JavaInfo{
			BasePackage: "com.deposition-cloud",
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}

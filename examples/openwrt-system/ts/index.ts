import * as pulumi from "@pulumi/pulumi";
import * as openwrt from "@deposition-cloud/pulumi-openwrt"
import { password } from "@deposition-cloud/pulumi-openwrt/config";

const openWrtProvider = new openwrt.Provider('openwrt', {
  hostname: '192.168.1.1',
  username: 'root',
  scheme: 'http',
  password: process.env.ROUTER_PASSWORD
})

const system = openwrt.getSystemSystem({
  id: "cfg01e48a"
}, {
  provider: openWrtProvider
} )

const ip = new openwrt.DhcpHost('testing', {
  ip: '192.168.1.201',
  mac: '12:23:34:45:56:67',
  name: 'pulumi-openwrt-host'
}, {
  id: "blah2",
  provider: openWrtProvider
})

export const out = {
  system
}
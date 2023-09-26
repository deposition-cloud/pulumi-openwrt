terraform {
  required_providers {
    openwrt = {
      source  = "joneshf/openwrt"
    }
  }
}

provider "openwrt" {
  hostname = "192.168.1.1"
  username = "root"
  password = var.openwrt_password
}

data "openwrt_system_system" "this" {
  id = "cfg01e48a"
}

resource "openwrt_dhcp_host" "testing" {
  id = "blah"
  ip   = "192.168.1.202"
  mac  = "12:34:56:78:90:ab"
  name = "testing"
}
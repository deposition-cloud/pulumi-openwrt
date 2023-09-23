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
  //scheme   = "https"
  //port     = 443
  password = var.openwrt_password
}

data "openwrt_system_system" "this" {
  id = "cfg01e48a"
}
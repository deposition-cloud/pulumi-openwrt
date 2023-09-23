// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("openwrt");

/**
 * The hostname to use. Defaults to "192.168.1.1".
 */
export declare const hostname: string | undefined;
Object.defineProperty(exports, "hostname", {
    get() {
        return __config.get("hostname");
    },
    enumerable: true,
});

/**
 * The password to use. Defaults to "".
 */
export declare const password: string | undefined;
Object.defineProperty(exports, "password", {
    get() {
        return __config.get("password");
    },
    enumerable: true,
});

/**
 * The port to use. Defaults to 80.
 */
export declare const port: number | undefined;
Object.defineProperty(exports, "port", {
    get() {
        return __config.getObject<number>("port");
    },
    enumerable: true,
});

/**
 * The URI scheme to use. Defaults to "http".
 */
export declare const scheme: string | undefined;
Object.defineProperty(exports, "scheme", {
    get() {
        return __config.get("scheme");
    },
    enumerable: true,
});

/**
 * The username to use. Defaults to "root".
 */
export declare const username: string | undefined;
Object.defineProperty(exports, "username", {
    get() {
        return __config.get("username");
    },
    enumerable: true,
});


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

hostname: Optional[str]
"""
The hostname to use. Defaults to "192.168.1.1".
"""

password: Optional[str]
"""
The password to use. Defaults to "".
"""

port: Optional[int]
"""
The port to use. Defaults to 80.
"""

scheme: Optional[str]
"""
The URI scheme to use. Defaults to "http".
"""

username: Optional[str]
"""
The username to use. Defaults to "root".
"""


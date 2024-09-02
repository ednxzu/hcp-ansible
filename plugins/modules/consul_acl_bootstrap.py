#!/usr/bin/python

from __future__ import absolute_import, division, print_function
from typing import Tuple

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ednz_cloud.hashistack.consul_acl_bootstrap

short_description: Bootstraps ACL for a Consul cluster.

version_added: "0.1.0"

description:
    - This module bootstraps ACL (Access Control List) for a Consul cluster. It performs the ACL bootstrap operation,
        creating the initial tokens needed for secure communication within the cluster.

options:
    api_addr:
        description: The address of the Consul API.
        required: true
        type: str
    scheme:
        description: The URL scheme to use (http or https).
        required: false
        type: str
        default: http
    port:
        description: The port on which the Consul API is running.
        required: false
        type: int
        default: 8500

author:
    - Bertrand Lanson (@ednz_cloud)
"""

EXAMPLES = r"""
# Example: Bootstrap ACL for a Consul cluster
- name: Bootstrap ACL for Consul cluster
    ednz_cloud.hashistack.consul_acl_bootstrap:
        api_addr: 127.0.0.1
        scheme: http
        port: 8500
"""

RETURN = r"""
state:
    description: Information about the state of ACL bootstrap for the Consul cluster.
    type: dict
    returned: always
    sample:
        accessor_id: "uuuuuuuu-uuuu-iiii-dddd-111111111111",
        secret_id: "uuuuuuuu-uuuu-iiii-dddd-222222222222"
"""

from ansible.module_utils.basic import AnsibleModule
import traceback

try:
    import requests
except ImportError:
    HAS_REQUESTS = False
    REQUESTS_IMPORT_ERROR = traceback.format_exc()
else:
    REQUESTS_IMPORT_ERROR = None
    HAS_REQUESTS = True


def bootstrap_acl(scheme: str, api_addr: str, port: int) -> Tuple[bool, dict]:
    url = f"{scheme}://" + f"{api_addr}:{port}" + "/v1/acl/bootstrap"

    # Make a PUT request to bootstrap the cluster
    response = requests.put(url)

    # Check the HTTP status code and handle the response
    if response.status_code == 200:
        return True, {
            "accessor_id": response.json()["AccessorID"],
            "secret_id": response.json()["SecretID"],
        }
    elif response.status_code == 403:
        return False, {"message": "Cluster has already been bootstrapped"}
    else:
        response.raise_for_status()  # Raise an exception for other status codes


def run_module():
    module_args = dict(
        api_addr=dict(type="str", required=True),
        scheme=dict(type="str", required=False, default="http"),
        port=dict(type="int", required=False, default=8500),
    )

    result = dict(changed=False, state="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    try:
        if not HAS_REQUESTS:
            module.fail_json(
                msg="Requests library is required but not installed. {}".format(
                    REQUESTS_IMPORT_ERROR
                )
            )

        acl_bootstrap_result, response_data = bootstrap_acl(
            scheme=module.params["scheme"],
            api_addr=module.params["api_addr"],
            port=module.params["port"],
        )

        result["changed"] = acl_bootstrap_result
        result["state"] = response_data

        module.exit_json(**result)

    except requests.exceptions.RequestException as e:
        module.fail_json(msg="Error during ACL Bootstrap: {}".format(str(e)))


def main():
    run_module()


if __name__ == "__main__":
    main()

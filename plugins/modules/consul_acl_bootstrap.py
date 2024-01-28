#!/usr/bin/python

from __future__ import absolute_import, division, print_function
from typing import Tuple

__metaclass__ = type

DOCUMENTATION = r"""
"""

EXAMPLES = r"""
"""

RETURN = r"""
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
        return False, "Cluster has already been bootstrapped"
    else:
        response.raise_for_status()  # Raise an exception for other status codes


def run_module():
    module_args = dict(
        api_addr=dict(type="str", required=True),
        scheme=dict(type="str", required=False, default="http"),
        port=dict(type="int", required=False, default=8500),
    )

    result = dict(changed=False, state="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    api_addr = module.params["api_addr"]
    scheme = module.params["scheme"]
    port = module.params["port"]

    try:
        if not HAS_REQUESTS:
            module.fail_json(
                msg="Requests library is required but not installed. {}".format(
                    REQUESTS_IMPORT_ERROR
                )
            )

        # Perform ACL Bootstrap
        acl_bootstrap_result, response_data = bootstrap_acl(
            api_addr=api_addr, port=port
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

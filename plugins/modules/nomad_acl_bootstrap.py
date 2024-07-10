#!/usr/bin/python

from __future__ import absolute_import, division, print_function
from typing import Tuple

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ednz_cloud.hashistack.nomad_acl_bootstrap

short_description: Manages the ACL bootstrap of HashiCorp Nomad.

description:
    - This module bootstraps HashiCorp Nomad ACL, ensuring that it is securely set up for use.

requirements:
  - C(requests) (L(Python library,https://requests.readthedocs.io/en/latest/))

options:
    api_url:
        description: The URL of the HashiCorp Nomad API.
        required: true
        type: str
    bootstrap_secret:
        description:
            - The secret to use for the bootstrap operation.
        required: false
        type: str
    tls_verify:
        description:
            - Whether to verify the TLS certificate of the Nomad API URL.
            - Default is true.
        required: false
        type: bool
        default: true

author:
    - Bertrand Lanson (@ednz_cloud)
"""

EXAMPLES = r"""
# Example: Bootstrap HashiCorp Nomad ACL with default settings
- name: Bootstrap HashiCorp Nomad ACL
  ednz_cloud.hashistack.nomad_acl_bootstrap:
    api_url: https://nomad.example.com

# Example: Bootstrap HashiCorp Nomad ACL with a custom bootstrap secret
- name: Bootstrap HashiCorp Nomad ACL with custom settings
  ednz_cloud.hashistack.nomad_acl_bootstrap:
    api_url: https://nomad.example.com
    bootstrap_secret: 2b778dd9-f5f1-6f29-b4b4-9a5fa948757a
"""

RETURN = r"""
state:
    description:
        - Information about the state of HashiCorp Nomad after ACL bootstrap.
        - This is a complex dictionary with details of the bootstrap.
    type: dict
    returned: always
    sample:
      - AccessorID: "b780e702-98ce-521f-2e5f-c6b87de05b24",
      - SecretID: "3f4a0fcd-7c42-773c-25db-2d31ba0c05fe",
      - Name: "Bootstrap Token",
      - Type: "management",
      - Policies: null,
      - Global: true,
      - CreateTime: "2017-08-23T22:47:14.695408057Z",
      - CreateIndex: 7,
      - ModifyIndex: 7
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


def bootstrap_nomad_acl(
    api_url: str, tls_verify: bool, bootstrap_secret: str
) -> Tuple[bool, dict]:
    payload = {}
    if bootstrap_secret:
        payload["BootstrapSecret"] = bootstrap_secret

    response = None

    try:
        response = requests.post(
            f"{api_url}/v1/acl/bootstrap", json=payload, verify=tls_verify
        )
        response.raise_for_status()
        return True, response.json()
    except requests.exceptions.HTTPError as e:
        if response is not None and response.status_code == 400:
            try:
                error_message = response.json().get(
                    "Errors", ["Nomad ACL bootstrap already done"]
                )[0]
            except ValueError:
                error_message = response.text
            return False, {"message": error_message}
        raise ValueError(f"Nomad ACL bootstrap failed: {str(e)}")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Nomad ACL bootstrap failed: {str(e)}")


def run_module():
    module_args = dict(
        api_url=dict(type="str", required=True),
        bootstrap_secret=dict(type="str", required=False, no_log=True),
        tls_verify=dict(type="bool", required=False, default=True),
    )

    result = dict(changed=False, state="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_REQUESTS:
        module.fail_json(
            msg="Missing required library: requests", exception=REQUESTS_IMPORT_ERROR
        )

    try:
        changed, response_data = bootstrap_nomad_acl(
            api_url=module.params["api_url"],
            tls_verify=module.params["tls_verify"],
            bootstrap_secret=module.params.get("bootstrap_secret"),
        )

        result["changed"] = changed
        result["state"] = response_data

        module.exit_json(**result)

    except ValueError as e:
        module.fail_json(msg=str(e))


def main():
    run_module()


if __name__ == "__main__":
    main()

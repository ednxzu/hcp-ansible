#!/usr/bin/python

from __future__ import absolute_import, division, print_function
from typing import Tuple

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ednz_cloud.hashistack.vault_init

short_description: Manages the initialization of HashiCorp Vault.

description:
    - This module initializes HashiCorp Vault, ensuring that it is securely set up for use.

requirements:
  - C(hvac) (L(Python library,https://hvac.readthedocs.io/en/stable/overview.html))

options:
    api_url:
        description: The URL of the HashiCorp Vault API.
        required: true
        type: str
    key_shares:
        description:
            - The number of key shares to split the master key into.
            - Default is 5.
        required: false
        type: int
        default: 5
    key_threshold:
        description:
            - The number of key shares required to reconstruct the master key.
            - Default is 3.
        required: false
        type: int
        default: 3

author:
    - Bertrand Lanson (@ednz_cloud)
"""

EXAMPLES = r"""
# Example: Initialize HashiCorp Vault with default settings
- name: Initialize HashiCorp Vault
  my_namespace.my_collection.my_test:
    api_url: https://vault.example.com

# Example: Initialize HashiCorp Vault with custom key shares and threshold
- name: Initialize HashiCorp Vault with custom settings
  my_namespace.my_collection.my_test:
    api_url: https://vault.example.com
    key_shares: 7
    key_threshold: 4
"""

RETURN = r"""
state:
    description:
        - Information about the state of HashiCorp Vault after initialization.
        - This is a complex dictionary with the following keys:
            - keys
            - keys_base64
            - root_token
        - If the vault is already initialized, it will return a simple dict with a message stating it.
    type: dict
    returned: always
    sample:
        keys:
            - wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
            - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            - yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
        keys_base64:
            - wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
            - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            - yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
        root_token: hvs.zzzzzzzzzzzzzzzzzzzzzzzz
"""

from ansible.module_utils.basic import AnsibleModule
import traceback

try:
    import hvac
except ImportError:
    HAS_HVAC = False
    HVAC_IMPORT_ERROR = traceback.format_exc()
else:
    HVAC_IMPORT_ERROR = None
    HAS_HVAC = True


def initialize_vault(
    api_url: str, key_shares: int, key_threshold: int
) -> Tuple[bool, dict]:
    client = hvac.Client(url=api_url)

    try:
        if not client.sys.is_initialized():
            return True, client.sys.initialize(key_shares, key_threshold)
        else:
            return False, {"message": "Vault is already initialized"}
    except hvac.exceptions.VaultError as e:
        raise hvac.exceptions.VaultError(f"Vault initialization failed: {str(e)}")


def run_module():
    module_args = dict(
        api_url=dict(type="str", required=True),
        key_shares=dict(type="int", required=False, default=5),
        key_threshold=dict(type="int", required=False, default=3),
    )

    result = dict(changed=False, state="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_HVAC:
        module.fail_json(
            msg="Missing required library: hvac", exception=HVAC_IMPORT_ERROR
        )

    try:
        vault_init_result, response_data = initialize_vault(
            module.params["api_url"],
            module.params["key_shares"],
            module.params["key_threshold"],
        )

        result["changed"] = vault_init_result
        result["state"] = response_data

        module.exit_json(**result)

    except ValueError as e:
        module.fail_json(msg=str(e))


def main():
    run_module()


if __name__ == "__main__":
    main()

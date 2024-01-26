#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ednxzu.hashistack.vault_init

short_description: Manages the initialization of HashiCorp Vault.

version_added: "1.0.0"

description:
    - This module initializes HashiCorp Vault, ensuring that it is securely set up for use.

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
    - Bertrand Lanson (@ednxzu)
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
    description: Information about the state of HashiCorp Vault after initialization.
    type: complex
    returned: always
    sample: {
        "keys": [
            "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        ],
        "keys_base64": [
            "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
        ],
        "root_token": "hvs.xxxxxxxxxxxxxxxxxxxxxxxx"
    }
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


def run_module():
    module_args = dict(
        api_url=dict(type="str", required=True),
        key_shares=dict(type="int", required=False, default=5),
        key_threshold=dict(type="int", required=False, default=3),
    )

    result = dict(changed=False, state="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_HVAC:
        module.fail_json(
            msg="Missing required library: hvac", exception=HVAC_IMPORT_ERROR
        )

    if module.check_mode:
        module.exit_json(**result)

    vault_init_result = None
    client = hvac.Client(url=module.params["api_url"])

    try:
        if not client.sys.is_initialized():
            vault_init_result = client.sys.initialize(
                module.params["key_shares"], module.params["key_threshold"]
            )
            result["state"] = vault_init_result
    except Exception as e:
        module.fail_json(msg=f"Vault initialization failed: {str(e)}")

    if vault_init_result:
        result["changed"] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()

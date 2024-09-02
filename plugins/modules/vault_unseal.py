#!/usr/bin/python

from __future__ import absolute_import, division, print_function
from typing import Tuple

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ednz_cloud.hashistack.vault_unseal

short_description: Unseals a Vault cluster.

version_added: "0.1.0"

description:
    - This module unseals a Vault cluster by submitting the necessary unseal keys. It checks whether the Vault is sealed and performs the unseal operation if needed. The response will reflect the state after the last unseal key is submitted.

requirements:
- C(hvac) (L(Python library,https://hvac.readthedocs.io/en/stable/overview.html))

options:
    api_url:
        description: The URL of the Vault API.
        required: true
        type: str
    tls_verify:
        description: Whether to verify TLS certificates.
        required: false
        type: bool
        default: true
    key_shares:
        description: List of unseal keys required to unseal the Vault.
        required: false
        type: list
        default: []

author:
    - Bertrand Lanson (@ednz_cloud)
"""

EXAMPLES = r"""
# Example: Unseal a Vault cluster
- name: Unseal Vault cluster
  ednz_cloud.hashistack.vault_unseal:
    api_url: "https://127.0.0.1:8200"
    tls_verify: true
    key_shares:
        - "key1"
        - "key2"
        - "key3"

# Example: Unseal Vault cluster with no TLS verification
- name: Unseal Vault cluster without TLS verification
  ednz_cloud.hashistack.vault_unseal:
    api_url: "https://127.0.0.1:8200"
    tls_verify: false
    key_shares:
        - "key1"
        - "key2"
"""

RETURN = r"""
state:
    description: Information about the state of the Vault unseal operation.
    type: dict
    returned: always
    sample:
        sealed: true,
        t: 3,
        n: 5,
        progress: 2,
        version: "0.6.2"
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


def unseal_vault(api_url: str, tls_verify: bool, key_shares: list) -> Tuple[bool, dict]:
    client = hvac.Client(url=api_url, verify=tls_verify)

    try:
        if client.sys.is_sealed():
            return True, client.sys.submit_unseal_keys(key_shares)
        else:
            return False, {"message": "Vault is already unsealed"}
    except hvac.exceptions.VaultError as e:
        raise hvac.exceptions.VaultError(f"Vault unsealing failed: {str(e)}")


def run_module():
    module_args = dict(
        api_url=dict(type="str", required=True),
        tls_verify=dict(type="bool", required=False, default=True),
        key_shares=dict(type="list", required=False, default=[]),
    )
    result = dict(changed=False, state="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    client = hvac.Client(
        url=module.params["api_url"], verify=module.params["tls_verify"]
    )

    if not client.sys.is_sealed():
        module.exit_json(**result)

    try:
        if not HAS_HVAC:
            module.fail_json(
                msg="Missing required library: hvac", exception=HVAC_IMPORT_ERROR
            )
        vault_unseal_result, response_data = unseal_vault(
            api_url=module.params["api_url"],
            tls_verify=module.params["tls_verify"],
            key_shares=module.params["key_shares"],
        )

        if hvac.Client(
            url=module.params["api_url"], verify=module.params["tls_verify"]
        ).sys.is_sealed():
            module.fail_json(
                msg="Vault unsealing failed. The unseal operation worked, but the vault is still sealed, maybe you didn't pass enough keys ?"
            )

        result["changed"] = vault_unseal_result
        result["state"] = response_data
    except hvac.exceptions.VaultError as ve:
        module.fail_json(msg=f"Vault unsealing failed: {ve}")

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()

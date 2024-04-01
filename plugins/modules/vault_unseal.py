#!/usr/bin/python

from __future__ import absolute_import, division, print_function
from typing import Tuple

__metaclass__ = type

DOCUMENTATION = r"""
---
module: my_test

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
"""

EXAMPLES = r"""
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
"""

RETURN = r"""
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
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


def unseal_vault(api_url: str, key_shares: list) -> Tuple[bool, dict]:
    client = hvac.Client(url=api_url)

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
        key_shares=dict(type="list", required=False, default=[]),
    )
    result = dict(changed=False, state="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    client = hvac.Client(url=module.params["api_url"])

    if not client.sys.is_sealed():
        module.exit_json(**result)

    try:
        if not HAS_HVAC:
            module.fail_json(
                msg="Missing required library: hvac", exception=HVAC_IMPORT_ERROR
            )
        vault_unseal_result, response_data = unseal_vault(
            api_url=module.params["api_url"], key_shares=module.params["key_shares"]
        )

        if hvac.Client(url=module.params["api_url"]).sys.is_sealed():
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

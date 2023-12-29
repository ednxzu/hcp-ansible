#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
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
'''

EXAMPLES = r'''
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
'''

RETURN = r'''
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
'''

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
        api_url=dict(type='str', required=True),
        key_shares=dict(type='list', required=False, default=[]),
        max_retries=dict(type='int', required=False, default=3)
    )

    result = dict(
        changed=False,
        original_message='',
        state=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Check if hvac module is available
    try:
        import hvac
    except ImportError:
        module.fail_json(
            msg="Missing required library: hvac",
            exception=HVAC_IMPORT_ERROR
        )

    if module.check_mode:
        module.exit_json(**result)

    # Initialize HashiCorp Vault client
    client = hvac.Client(
        url=module.params['api_url']
    )

    # Unseal Vault
    try:
        retries = 0
        while client.sys.is_sealed() and retries < module.params['max_retries']:
            key_share = module.params['key_shares'][min(retries, len(module.params['key_shares']) - 1)]
            vault_unseal_result = client.sys.submit_unseal_key(key_share)
            retries += 1
    except hvac.exceptions.VaultError as ve:
        module.fail_json(msg=f"Vault unsealing failed: {ve}")

    # Check if the Vault is successfully unsealed
    if client.sys.is_sealed():
        module.fail_json(msg="Vault unsealing failed: Maximum retries reached.")

    result['state'] = vault_unseal_result
    result['changed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

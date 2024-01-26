#!/usr/bin/python

from __future__ import absolute_import, division, print_function

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


def run_module():
    module_args = dict(
        api_url=dict(type="str", required=True),
    )

    result = dict(changed=False, state="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)


def main():
    run_module()


if __name__ == "__main__":
    main()

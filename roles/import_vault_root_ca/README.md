import_vault_root_ca
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role imports root CA certificates from Vault to the trust store on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/import_vault_root_ca.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
import_vault_root_ca_certificate_force_download: false # by default, set to false
```
This variable defines whether the role should always download the provided certificate even if it already exists. This can be useful if you want to replace an existing CA, but note that **it breaks idempotence**.

```yaml
import_vault_root_ca_certificate_list: [] # by default, set to an empty dict
  - url: <someurl>
    cert_name: <name_of_ca>
```
This variable defines which CA certificate to install on the machine, it is only tested with CA from Hashicorp Vault pki engine, but should work with any CA that can be downloaded from a webserver.

Dependencies
------------

`ednxzu.manage_apt_packages` to install consul-template.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.import_vault_root_ca
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.

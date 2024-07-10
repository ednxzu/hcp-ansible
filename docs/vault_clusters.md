# Deploying a Vault cluster

This documentation explains each steps necessary to successfully deploy a Vault cluster using the ednz_cloud.hashistack ansible collection.

## Prerequisites

You should, before attempting any deployment, have read through the [Quick Start Guide](./quick_start.md). These steps are necessary in order to ensure smooth operations going forward.

## Variables

### Basics

First, in order to deploy a Vault cluster, you need to enable it.

```yaml
enable_vault: "yes"
```

Selecting the vault version to install is done with the `vault_version` variable.

```yaml
vault_version: latest
```

The vault version can either be `latest` or `X.Y.Z`.

For production deployment, it is recommended to use the `X.Y.Z` syntax.

### General settings

First, you can change some general settings for vault.

```yaml
vault_cluster_name: vault
vault_enable_ui: true
vault_seal_configuration:
  key_shares: 3
  key_threshold: 2
```

### Storage settings

The storage configuration for vault can be edited as well. By default, vault will be configured to setup `raft` storage between all declared vault servers (in the `vault_servers` group).

```yaml
vault_storage_configuration:
  raft:
    path: "{{ hashicorp_vault_data_dir }}/data"
    node_id: "{{ ansible_hostname }}"
    retry_join: |
      [
      {% for host in groups['vault_servers'] %}
        {
          'leader_api_addr': 'http://{{ hostvars[host].api_interface_address }}:8200'
        }{% if not loop.last %},{% endif %}
      {% endfor %}
      ]
```

While this is the [recommended](https://developer.hashicorp.com/vault/docs/configuration/storage#integrated-storage-vs-external-storage) way to configure storage for vault, you can edit this variable to enable any storage you want. Refer to the [vault documentation](https://developer.hashicorp.com/vault/docs/configuration/storage) for compatibility and syntax details about this variable.

Example:

```yaml
# MySQL storage configuration
vault_storage_configuration:
  mysql:
    address: "10.1.10.10:3006"
    username: "vault"
    password: "vault"
    database: "vault"
```

### Listener settings

#### TCP listeners

By default, TLS is **disabled** for vault. This goes against the Hashicorp recommendations on the matter, but there is no simple way to force the use of TLS (yet), without adding a lot of complexity to the deployment.

The listener configuration settings can be modified in `vault_listener_configuration` variable.

```yaml
vault_listener_configuration:
  tcp:
    address: "0.0.0.0:8200"
    tls_disable: true
```
By default, vault will listen on all interfaces, on port 8200. you can change it by modifying the `tcp.address` property, and adding you own listener preferences.

#### Enabling TLS for Vault

In order to enable TLS for Vault, you simply need to set the `vault_enable_tls` variable to `true`.

At the moment, hashistack-Ansible does nothing to help you generate the certificates and renew them. All it does is look inside the `etc/hashistack/vault_servers/tls` directory on the deployment node, and copy the files to the destination hosts in `/etc/vault.d/config/tls`. The listener expect **2 files** by default, a `cert.pem`, and a `key.pem` file.

Please refer to the [vault documentation](https://developer.hashicorp.com/vault/docs/configuration/listener/tcp) for details bout enabling TLS on vault listeners.

In case you want to add more configuration to the vault listeners, you can add it to the `vault_extra_listener_configuration` variable, which by default is empty. This variable will be merge with the rest ofthe listener configuration variables, and takes precedence over all the others.

> **Waring**
> At the moment, hashistack-ansible does not support setting up multiple TCP listeners. Only one can be set.

### Plugins for Vault

To enable plugin support for Vault, you can set the `vault_enable_plugins` variable to true. This variable will add the necessary configuration options in the vault.json file to enable support. Once enabled, you can simply place your compiled plugin files into the `etc/hashistack/vault_servers/plugin` directory. They will be copied over to the `/etc/vault.d/config/plugin` directory on the target nodes.

Refer to the [vault documentation](https://developer.hashicorp.com/vault/docs/plugins/plugin-management) for details about enabling and using plugins.

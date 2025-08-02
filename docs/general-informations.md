# General Information

## Inventory

Hashistack-Ansible relies on an Ansible inventory file to understand which host handles which role. You can find a sample inventory file under `playbooks/inventory/multinode` within the collection directory.

The groups required by the playbooks are as follow:

- `vault_servers` running vault in server mode
- `consul_servers` running consul in server mode
- `nomad_servers` running nomad in server mode
- `nomad_clients` running nomad in client mode
- `consul_agents` running consul in client mode
- `deployment` which is the group of the deployment machine

Some additional meta groups are used by the different playbooks:

- `nomad` englobes all nomad nodes (client and servers)
- `vault` englobes all vault nodes
- `consul` englobes all consul nodes (agents and servers)
- `common` englobes all the groups (equivalent to the native `all` group, except it does not include the deployment machine)

By default, the `consul_agents` group englobes all the hosts that are not in the `consul_servers` group (useful when enabling service registration for vault or nomad. It will automatically start a consul agent on the nodes to register the service in consul service catalog)

## Main Configuration Directory

HCP-Ansible uses a configuration directory to store all necessary files and artifacts. The directory is defined by the `hashistack_configuration_directory` variable. By default, it’s set to `$(pwd)/etc/hashistack`.

In this directory, place your `globals.yml` file with your configurations. You can find a template for this file at `playbooks/inventory/group_vars/all/globals.yml` in the collection's directory. This file starts simple, but it’s highly extensible. Additional service configurations can be found in `consul.yml`, `vault.yml`, `nomad.yml`, `cni.yml`, and `all.yml` within the same directory.

!!! note
    Instead of editing these service configuration files directly, extend them by adding your own values to your `globals.yml` file.

## Sub-Configuration Directories

You can fine-tune configurations by using sub-directories for group-specific or host-specific settings.

By loading the `globals.yml` at the start of the playbooks, we introduce a problem which is that this globals file will override any values set in the `host_vars` or `group_vars` for the inventory. This prevents using those methods to customize the deployment per groups or per host.

The good news is, we introduced another method to allow you to customize those values without relying on the `group_vars` and `host_vars` variable sets!

### Group Configuration Directories

Each group in the inventory can have its own sub-directory within the main configuration directory:

- The `nomad_servers` group will look in `{{ hashistack_configuration_directory }}/nomad_servers`
- The `vault_servers` group will look in `{{ hashistack_configuration_directory }}/vault_servers`
- The `consul_servers` group will look in `{{ hashistack_configuration_directory }}/consul_servers`

Inside each of these directories, you can place a `globals.yml` file that will override settings in the main `globals.yml`.

**Example:**

If `etc/hashistack/globals.yml` looks like this:
```yaml
---
enable_vault: "no"
enable_consul: "no"
enable_nomad: "no"
```

And `etc/hashistack/nomad_servers/globals.yml` looks like this:
```yaml
---
enable_nomad: "yes"
```

Then the `nomad_servers` group will have this configuration:
```yaml
---
enable_vault: "no"
enable_consul: "no"
enable_nomad: "yes"
```

This has its limitations, has the group variables are loaded in a sequential order, if a host is a member of multiple groups, only the last loaded group for this host will apply the desired variables.

For this scenario, it is recommended to use the host configuration directories mentioned below, and load variables on a per-host basis.

### Host Configuration Directories

For even more granularity, each group configuration directory can contain sub-directories for individual hosts, named after the hosts in your inventory. These host directories can include a `globals.yml` file to override both group and global settings.

**Example:**

If `etc/hashistack/globals.yml` looks like this:
```yaml
---
enable_vault: "no"
enable_consul: "no"
enable_nomad: "no"
api_interface: "eth0"
```

And `etc/hashistack/nomad_servers/globals.yml` looks like this:
```yaml
---
enable_nomad: "yes"
api_interface: "eth1"
```

And `etc/hashistack/nomad_servers/nomad-master-01/globals.yml` looks like this:
```yaml
api_interface: "eth0.vlan40"
```

Then all servers in the `nomad_servers` group will have this configuration:
```yaml
---
enable_vault: "no"
enable_consul: "no"
enable_nomad: "yes"
api_interface: "eth1"
```
Except for `nomad-master-01`, which will have this configuration:
```yaml
---
enable_vault: "no"
enable_consul: "no"
enable_nomad: "yes"
api_interface: "eth0.vlan40"
```

This flexible approach lets you tailor the deployment to your exact needs, ensuring everything works just the way you want! 🎯

## Configuring Roles

Every deployment is done through a role named after itself, and located in the `roles/` directory for the collection. Under the `defaults/` within each role, you can find a `main.yml` file containing all of the variables  that can be used to configure said role.

When using the collection, some defaults are changed in order to limit the amount of variables you have to customize in order to deploy the clusters. These overrides are located in the `playbooks/group_vars/all/` directory, under `<service_name>_default.yml`

The collection uses a combination of multiple variables to allow you to override any value:

- `hashistack_default_<variable_name>` is the variable set by default by the developers, and its value should not be altered. It acts as a last resort, in case no value is passed by the user.
- `hashistack_<variable_name>` is the variable the user should use to override the default values for a specific variable. This value is either merged with its `hashistack_default_` counterpart, or replaces it completely. This allows you to override part of the default values, but not all, for variables where this is interesting. For values that cannot be partially overridden, the `hashistack_<variable_name>` replaces the default one completely.
- Finally, `hashistack_<variable_name>` is set its correct value.

**Example:**

```yaml
hashistack_default_consul_config_dir: "{% raw %}{{ hashistack_remote_config_dir }}/consul.d{% endraw %}"
consul_config_dir: "{% raw %}{{ hashistack_consul_config_dir | default(hashistack_default_consul_config_dir) }}{% endraw %}"
```
In this case, if the user supplies a `hashistack_consul_config_dir` value in `globals.yml`, the entire value will be overridden, and `consul_config_dir` will take the value of `hashistack_consul_config_dir`

```yaml
hashistack_default_consul_acl_configuration:
  enabled: true
  default_policy: "deny"
  enable_token_persistence: true
  tokens:
    agent: "{% raw %}{{ _credentials.consul.tokens.agent.secret_id }}{% endraw %}"
consul_acl_configuration: >-
  {% raw %}{{
    hashistack_default_consul_acl_configuration |
    combine((hashistack_consul_acl_configuration | default({})), recursive=true)
  }}{% endraw %}
```
In this scenario, the values of `hashistack_default_consul_acl_configuration` and `hashistack_consul_acl_configuration` will be merged, with precedence being given to the non-default value, so that you can only override part of the defualt without having to re-specify all of it.

```yaml
hashistack_consul_acl_configuration:
  default_policy: "allow"
```
This would result in the final `consul_acl_configuration` looking like:

```yaml
consul_acl_configuration:
  enabled: true
  default_policy: "allow"
  enable_token_persistence: true
  tokens:
    agent: "{% raw %}{{ _credentials.consul.tokens.agent.secret_id }}{% endraw %}"
```

# General documentation

## Configuration directory

### Main configuration directory

Hashistack Ansible uses a configuration directory to store all the configuration files and other artifacts.

This directory is defined with the variable `configuration_directory`. By default, it will look at `{{ lookup('env', 'PWD') }}/etc/hashistack`, which equals `$(pwd)/etc/hashistack`.

Under this directory, you are expected to place the `globals.yml` file, with your configuration.

### Sub configuration directories

#### Group configuration directories

Additionally, subdirectories can be used to tailor the configuration further.

Each group within the `inventory` will look at a directory named after itself:

- nomad_servers group will look for `{{ configuration_directory }}/nomad_servers`
- vault_servers group will look for `{{ configuration_directory }}/vault_servers`
- consul_servers group will look for `{{ configuration_directory }}/consul_servers`

Within each of these directories, you can place an additional `globals.yml file`, that will superseed the file at the root of the configuration directory.

- **Example**:

  If `etc/hashistack/globals.yml` looks like:

  ```yaml
  ---
  enable_vault: "no"
  enable_consul: "no"
  enable_nomad: "no"
  ```

  And `etc/hashistack/nomad_servers/globals.yml` looks like:

  ```yaml
  ---
  enable_nomad: "yes"
  ```

  Servers in the `nomad_servers` group will end up with the following configuration:

  ```yaml
  ---
  enable_vault: "no"
  enable_consul: "no"
  enable_nomad: "yes"
  ```

This approach lets you customize your deployment for your exact needs.

#### Host configuration directories

Additionally, within each `group configuration directory`, you can add `host configuration directory`, that will be named after the hosts defined in your `inventory`. These host directories can also be populated with a `globals.yml` file, that will superseed the `group` and `deployment` configuration files.

- **Example**

  If `etc/hashistack/globals.yml` looks like:

  ```yaml
  ---
  enable_vault: "no"
  enable_consul: "no"
  enable_nomad: "no"
  api_interface: "eth0"
  ```

  And `etc/hashistack/nomad_servers/globals.yml` looks like:

  ```yaml
  ---
  enable_nomad: "yes"
  api_interface: "eth1"
  ```

  And `etc/hashistack/nomad_servers/nomad-master-01/globals.yml` looks like:

  ```yaml
    api_interface: "eth0.vlan40"
  ```

  Servers in the `nomad_servers` group will end up with the following configuration:

  ```yaml
  ---
  enable_vault: "no"
  enable_consul: "no"
  enable_nomad: "yes"
  api_interface: "eth1"
  ```
  Except for host `nomad-master-01`, who will have the following:

  ```yaml
  ---
  enable_vault: "no"
  enable_consul: "no"
  enable_nomad: "yes"
  api_interface: "eth0.vlan40"
  ```

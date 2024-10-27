**Vault**
=========

This role configures [HashiCorp Vault](https://www.hashicorp.com/products/vault) on **Debian-based** distributions.

**Requirements**
------------

This role requires that the `unzip` package is installed on the target host.
If using the auto-unseal feature from this role, it also requires the `hvac` Python library to be installed on the target host.

**Role Variables**
--------------

### Service Configuration

```yaml
vault_version: latest
```
Specifies the version of Vault to install. Default is `latest`, which installs the latest stable version. It is recommended to pin the vault version to install, as setting latest will cause the role to query the github API, andyou might run into rate limiting issues. A pinned version should look like `X.Y.Z`, in accordance with the vault's [release repository](https://releases.hashicorp.com/vault/) (just strip out the leading `vault_`)

```yaml
vault_start_service: true
```
Indicates whether the Vault service should start after installation. Defaults to `true`.

```yaml
vault_config_dir: "/etc/vault.d"
```
Path to the directory where Vault's configuration files are stored.

```yaml
vault_data_dir: "/opt/vault"
```
Specifies the directory where Vault will store its data.

```yaml
vault_certs_dir: "{{ vault_config_dir }}/tls"
```
Path to the directory where Vault's TLS certificates should be stored when using internal TLS.

```yaml
vault_logs_dir: "/var/log/vault"
```
Directory path where Vault's log files will be stored if logging to file is enabled.

```yaml
vault_extra_files: false
```
If `true`, allows additional files to be copied over to the target host by the role.

```yaml
vault_extra_files_list: []
```
A list of additional files to manage with the role if `vault_extra_files` is set to `true`. This is a list of objects like:

```yaml
- src: /path/on/deploy/machine
  dest: /path/to/copy/over
```

Sources can be any type of file, directory or jinja2 templates. Destination should match the type of the source. Jinja2 templates inside of a directory that would be copied over are also templated, and their `.j2` extensions will be stripped out.

Example:

```yaml
vault_extra_files_list:
  - src: /local/path/to/tls/files
    dest: "{{ vault_certs_dir }}"
  - src: /another/single/file.j2
    dest: /var/lib/file
```

```yaml
vault_env_variables: {}
```
Environment variables to be set for the Vault service, defined as key-value pairs.

### Extra Configuration

```yaml
vault_extra_configuration: {}
```
Dictionary for any additional Vault configuration options not covered by other variables. This should be used only for options not provided by existing variables.

### General

```yaml
vault_cluster_name: vault
```
Specifies the name of the Vault cluster. Default is `vault`.

```yaml
vault_bind_addr: "0.0.0.0"
```
Defines the IP address that Vault will bind to for communication. Default is `"0.0.0.0"`, allowing connections from any IP address.

```yaml
vault_cluster_addr: "{{ ansible_default_ipv4.address }}"
```
Sets the address for Vault cluster communication, typically the IP of the host running Vault.

```yaml
vault_enable_ui: true
```
Enables the Vault web UI if set to `true`. Default is `true`.

```yaml
vault_disable_mlock: false
```
If set to `true`, disables the use of `mlock` syscall, which can prevent Vault from being able to lock its memory. Useful in environments where `mlock` is restricted.

```yaml
vault_disable_cache: false
```
Disables Vault’s cache if set to `true`, forcing Vault to avoid caching data.

### Storage Configuration

```yaml
vault_storage_configuration:
  file:
    path: "{{ vault_data_dir }}"
```
Defines the storage backend configuration for Vault, provided as a dictionary. This configuration should resemble the `storage` stanza from the [Vault documentation](https://developer.hashicorp.com/vault/docs/configuration/storage), allowing users to specify their preferred storage backend and its associated options. Here, `file` storage is configured, with `path` set to `vault_data_dir` for file-based storage.

### Auto-Unseal Configuration

```yaml
vault_enable_auto_unseal: false
```
Enables or disables Vault's auto-unseal feature. If set to `true` and `vault_unseal_keys` is not empty, the role will attempt to unseal Vault automatically after it has started or restarted. Requires the `hvac` Python library.

```yaml
vault_unseal_url: "https://127.0.0.1:8200"
```
Specifies the URL of the Vault server used for the unseal operation.

```yaml
vault_unseal_tls_verify: true
```
Determines whether TLS verification is enabled for the unseal process. If `true`, Vault will verify the TLS certificate when connecting to `vault_unseal_url`.

```yaml
vault_unseal_keys: []
```
A list of unseal keys used to unseal the Vault server. This list should contain valid unseal keys if `vault_enable_auto_unseal` is `true`.

### Listener Configuration

```yaml
vault_enable_tls: false
```
Enables TLS for Vault listeners if set to `true`. When enabled, `vault_tls_listener_configuration` settings will take precedence over non-TLS settings.

```yaml
vault_listener_configuration:
  - tcp:
      address: "{{ vault_cluster_addr }}:8200"
      tls_disable: true
```
Defines the default listener configuration for Vault. Here, it uses TCP with TLS disabled, binding to the `vault_cluster_addr` on port `8200`.

```yaml
vault_tls_listener_configuration:
  - tcp:
      tls_disable: false
      tls_cert_file: "{{ vault_certs_dir }}/cert.pem"
      tls_key_file: "{{ vault_certs_dir }}/key.pem"
      tls_disable_client_certs: true
```
Specifies the TLS listener configuration for Vault. When `vault_enable_tls` is `true`, this configuration merges with `vault_listener_configuration`, with TLS settings overriding non-TLS values where applicable.

```yaml
vault_certificates_extra_files_dir: []
```
List of directories/files containing additional TLS certificates. These will be appended to `vault_extra_files_list` (with `vault_extra_files` set to `true`), ensuring Vault has access to required certificate files.

```yaml
vault_extra_listener_configuration: []
```
Allows adding custom listener configurations to extend the main listener settings. This configuration merges with the combined result of `vault_listener_configuration` and `vault_tls_listener_configuration`.

**Note on Merging Configuration:**

- If `vault_enable_tls` is set to `true`, `vault_listener_configuration` and `vault_tls_listener_configuration` are merged with priority given to TLS settings.
- The combined listener configurations are further extended by `vault_extra_listener_configuration`, enabling a flexible and layered configuration approach.
- `vault_certificates_extra_files_dir` directories will add entries to `vault_extra_files_list`, ensuring certificate files are available for Vault. To activate this, `vault_extra_files` should be set to `true`.

### Service Registration

```yaml
vault_enable_service_registration: false
```
Enables or disables service registration for Vault. When set to `true`, Vault will attempt to register itself with the specified service registration provider.

```yaml
vault_service_registration_configuration:
  consul:
    address: "127.0.0.1:8500"
    scheme: "http"
    token: ""
```
Defines the configuration for service registration, resembling a `service_registration` stanza from the [Vault documentation](https://developer.hashicorp.com/vault/docs/configuration/service-registration). Here, Consul is configured as the service registry with its `address`, `scheme`, and optional `token`. This allows Vault to register with Consul for service discovery if `vault_enable_service_registration` is `true`.

### Plugins Configuration

```yaml
vault_enable_plugins: false
```
Enables plugin configuration for Vault if set to `true`. This only adds the necessary entries to the Vault configuration file; actual plugin files must be copied to the plugins directory by the user or managed using the `vault_extra_files` variable.

```yaml
vault_plugins_directory: "{{ vault_config_dir }}/plugins"
```
Specifies the directory where Vault plugins are stored. Plugins should be manually placed in this directory, as enabling plugins within Vault itself is not yet managed by this role.

### Vault Logging

```yaml
vault_log_level: info
```
Sets the logging level for Vault. Accepted values are `trace`, `debug`, `info`, `warn`, and `error`. See [Vault documentation on log levels](https://developer.hashicorp.com/vault/docs/configuration#log_level) for more details.

```yaml
vault_enable_log_to_file: false
```
Enables logging to a file if set to `true`. When enabled, the settings in `vault_log_to_file_configuration` will define the log file path, rotation frequency, and retention of logs.

```yaml
vault_log_to_file_configuration:
  log_file: "{{ vault_logs_dir }}/vault.log"
  log_rotate_duration: 24h
  log_rotate_max_files: 30
```
Specifies configuration for file-based logging:
- **`log_file`**: Defines the path to the Vault log file (e.g., `vault_logs_dir/vault.log`). See [Vault log file configuration](https://developer.hashicorp.com/vault/docs/configuration#log_file) for details.
- **`log_rotate_duration`**: Sets the duration before log rotation occurs (e.g., `24h` for daily rotation).
- **`log_rotate_max_files`**: Maximum number of rotated log files to retain.

With `vault_enable_log_to_file` set to `true`, these settings provide a default configuration for logging to a file, allowing Vault to manage log files and rotation automatically.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednz_cloud.hashistack.vault
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.

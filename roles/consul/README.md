**Consul**
=========

This role configures [HashiCorp consul](https://www.hashicorp.com/products/consul) on **Debian-based** distributions.

**Requirements**
------------

This role requires that the `unzip` package is installed on the target host.

**Role Variables**
--------------

### Service Configuration

```yaml
consul_version: latest
```
Specifies the version of Consul to install. Default is `latest`, which installs the latest stable version. It is recommended to pin the consul version to install, as setting latest will cause the role to query the github API, andyou might run into rate limiting issues. A pinned version should look like `X.Y.Z`, in accordance with the consul's [release repository](https://releases.hashicorp.com/consul/) (just strip out the leading `consul_`)

```yaml
consul_start_service: true
```
Indicates whether the Consul service should start after installation. Defaults to `true`.

```yaml
consul_config_dir: "/etc/consul.d"
```
Path to the directory where Consul's configuration files are stored.

```yaml
consul_data_dir: "/opt/consul"
```
Specifies the directory where Consul will store its data.

```yaml
consul_certs_dir: "{{ consul_config_dir }}/tls"
```
Path to the directory where Consul's TLS certificates should be stored when using internal TLS.

```yaml
consul_logs_dir: "/var/log/consul"
```
Directory path where Consul's log files will be stored if logging to file is enabled.

```yaml
consul_extra_files: false
```
If `true`, allows additional files to be copied over to the target host by the role.

```yaml
consul_extra_files_list: []
```
A list of additional files to manage with the role if `consul_extra_files` is set to `true`. This is a list of objects like:

```yaml
- src: /path/on/deploy/machine
  dest: /path/to/copy/over
```

Sources can be any type of file, directory or jinja2 templates. Destination should match the type of the source. Jinja2 templates inside of a directory that would be copied over are also templated, and their `.j2` extensions will be stripped out.

Example:

```yaml
consul_extra_files_list:
  - src: /local/path/to/tls/files
    dest: "{{ consul_certs_dir }}"
  - src: /another/single/file.j2
    dest: /var/lib/file
```

```yaml
consul_env_variables: {}
```
Environment variables to be set for the Consul service, defined as key-value pairs.

### Extra Configuration

```yaml
consul_extra_configuration: {}
```
Dictionary for any additional Consul configuration options not covered by other variables. This should be used only for options not provided by existing variables.

### General Configuration

```yaml
consul_domain: consul
```
The domain for Consul, typically set to `consul`.

```yaml
consul_datacenter: dc1
```
Specifies the datacenter for the Consul instance.

```yaml
consul_primary_datacenter: "{{ consul_datacenter }}"
```
Sets the primary datacenter, defaulting to the value of `consul_datacenter`.

```yaml
consul_gossip_encryption_key: "{{ 'mysupersecretgossipencryptionkey' | b64encode }}"
```
Sets the gossip encryption key for secure communication between Consul agents. This key must be a 32-byte base64-encoded string.

```yaml
consul_enable_script_checks: false
```
Indicates whether script checks are enabled for Consul.

### Leave Configuration

```yaml
consul_leave_on_terminate: true
```
Specifies whether the consul agent should leave the cluster when it is terminated (e.g., SIGTERM). Defaults to `false`, indicating the agent will not leave the cluster upon termination.

```yaml
consul_rejoin_after_leave: true
```
Specifies whether the Consul agent should automatically rejoin the cluster after leaving.

### Join Configuration

```yaml
consul_join_configuration:
  retry_join:
    - "{{ ansible_default_ipv4.address }}"
  retry_interval: 30s
  retry_max: 0
```
Specifies the addresses that the Consul agent should attempt to join upon starting, the interval between attempts to join the cluster, and the maximum number of join attempts before giving up. A value of `0` for `retry_max` indicates unlimited retries.

### Server Configuration

```yaml
consul_enable_server: true
```
Enables the Consul server functionality.

```yaml
consul_bootstrap_expect: 1
```
Specifies the number of servers that are expected to bootstrap the cluster. In this example, `1` indicates that this server will be the only one in the cluster during the initial bootstrapping phase.

### UI Configuration

```yaml
consul_ui_configuration:
  enabled: "{{ consul_enable_server }}"
```
Enables the Consul UI based on whether the Consul server is enabled. If `consul_enable_server` is set to `true`, the UI will be accessible.

### Address Configuration

```yaml
consul_bind_addr: "0.0.0.0"
```
Specifies the address that Consul will bind to for incoming connections.

```yaml
consul_advertise_addr: "{{ ansible_default_ipv4.address }}"
```
Defines the address that Consul will advertise to other members of the cluster.

```yaml
consul_address_configuration:
  client_addr: "{{ consul_bind_addr }}"
  bind_addr: "{{ consul_advertise_addr }}"
  advertise_addr: "{{ consul_advertise_addr }}"
```
This block contains the address configuration for Consul. It will be merged into the global Consul configuration to facilitate setup and avoid repeating entries.

### ACL Configuration

```yaml
consul_acl_configuration:
  enabled: false
  default_policy: "deny"
  enable_token_persistence: true
  # tokens:
  #   agent: ""
```
This block matches the "acl" stanza from the [Consul documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files#acl).

### Service Mesh Configuration

```yaml
consul_mesh_configuration:
  enabled: false
```
This block matches the "connect" stanza from the [Consul documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files#connect).

### DNS Configuration

```yaml
consul_dns_configuration:
  allow_stale: true
  enable_truncate: true
  only_passing: true
```
This block matches the "dns_config" stanza from the [Consul documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files#dns_config).

### Internal TLS Configuration

```yaml
consul_enable_tls: false
```
Enables TLS for Consul listeners if set to `true`.

```yaml
consul_tls_configuration:
  defaults:
    ca_file: "/etc/ssl/certs/ca-certificates.crt"
    cert_file: "{{ consul_certs_dir }}/cert.pem"
    key_file: "{{ consul_certs_dir }}/key.pem"
    verify_incoming: false
    verify_outgoing: true
  internal_rpc:
    verify_server_hostname: true
```
The `consul_tls_configuration` value matches the "tls" block from the [Consul documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files#tls-configuration-reference).


```yaml
consul_certificates_extra_files_dir: []
```
The `consul_certificates_extra_files_dir` values allows users to copy certificates by appending to `consul_extra_files_list`. `consul_extra_files` must be set to `true` if using this feature.


### Telemetry Configuration

```yaml
consul_enable_prometheus_metrics: false
```
This variable enable prometheus metrics for the Consul server or agent.

```yaml
consul_prometheus_retention_time: 60s
```
This variable matches the `telemetry.prometheus_retention_time` from the [Consul documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files#telemetry-parameters). It defaults to `60s` and derives from the default `0s` because in case `consul_enable_prometheus_metrics` is `true`, this variable need to be greater than `0s` in order to enable prometheus metrics endpoint.

```yaml
consul_telemetry_configuration: {}
```
This block matches the "telemetry" stanza from the [Consul documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files#telemetry-parameters).

### Consul Logging

```yaml
consul_log_level: info
```
Sets the logging level for Consul. Accepted values are `trace`, `debug`, `info`, `warn`, and `error`. See [Consul documentation on log levels](https://developer.hashicorp.com/consul/docs/agent/config/cli-flags#_log_level) for more details.

```yaml
consul_enable_log_to_file: false
```
Enables logging to a file if set to `true`. When enabled, the settings in `consul_log_to_file_configuration` will define the log file path, rotation frequency, and retention of logs.

```yaml
consul_log_to_file_configuration:
  log_file: "{{ consul_logs_dir }}/consul.log"
  log_rotate_duration: 24h
  log_rotate_max_files: 30
```
Specifies configuration for file-based logging:
- **`log_file`**: Defines the path to the Consul log file (e.g., `consul_logs_dir/consul.log`). See [Consul log file configuration](https://developer.hashicorp.com/consul/docs/agent/config/config-files#log-parameters) for details.
- **`log_rotate_duration`**: Sets the duration before log rotation occurs (e.g., `24h` for daily rotation).
- **`log_rotate_max_files`**: Maximum number of rotated log files to retain.

With `consul_enable_log_to_file` set to `true`, these settings provide a default configuration for logging to a file, allowing Consul to manage log files and rotation automatically.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednz_cloud.hashistack.consul
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.

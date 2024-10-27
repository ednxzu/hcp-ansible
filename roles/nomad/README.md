**Nomad**
=========

This role configures [HashiCorp nomad](https://www.hashicorp.com/products/nomad) on **Debian-based** distributions.

**Requirements**
------------

This role requires that the `unzip` package is installed on the target host.

**Role Variables**
--------------

### Service Configuration

```yaml
nomad_version: latest
```
Specifies the version of Nomad to install. Default is `latest`, which installs the latest stable version. It is recommended to pin the nomad version to install, as setting latest will cause the role to query the github API, andyou might run into rate limiting issues. A pinned version should look like `X.Y.Z`, in accordance with the nomad's [release repository](https://releases.hashicorp.com/nomad/) (just strip out the leading `nomad_`)

```yaml
nomad_start_service: true
```
Indicates whether the Nomad service should start after installation. Defaults to `true`.

```yaml
nomad_config_dir: "/etc/nomad.d"
```
Path to the directory where Nomad's configuration files are stored.

```yaml
nomad_data_dir: "/opt/nomad"
```
Specifies the directory where Nomad will store its data.

```yaml
nomad_certs_dir: "{{ nomad_config_dir }}/tls"
```
Path to the directory where Nomad's TLS certificates should be stored when using internal TLS.

```yaml
nomad_logs_dir: "/var/log/nomad"
```
Directory path where Nomad's log files will be stored if logging to file is enabled.

```yaml
nomad_extra_files: false
```
If `true`, allows additional files to be copied over to the target host by the role.

```yaml
nomad_extra_files_list: []
```
A list of additional files to manage with the role if `nomad_extra_files` is set to `true`. This is a list of objects like:

```yaml
- src: /path/on/deploy/machine
  dest: /path/to/copy/over
```

Sources can be any type of file, directory or jinja2 templates. Destination should match the type of the source. Jinja2 templates inside of a directory that would be copied over are also templated, and their `.j2` extensions will be stripped out.

Example:

```yaml
nomad_extra_files_list:
  - src: /local/path/to/tls/files
    dest: "{{ nomad_certs_dir }}"
  - src: /another/single/file.j2
    dest: /var/lib/file
```

```yaml
nomad_env_variables: {}
```
Environment variables to be set for the Nomad service, defined as key-value pairs.

### Extra Configuration

```yaml
nomad_extra_configuration: {}
```
Dictionary for any additional Nomad configuration options not covered by other variables. This should be used only for options not provided by existing variables.

### General Configuration

```yaml
nomad_region: global
```
Sets the region of the Nomad cluster. This value is used to define the cluster's region and should match the desired regional configuration.

```yaml
nomad_datacenter: dc1
```
Defines the datacenter name for the Nomad agent. This is used for grouping nodes and services within a specific datacenter.

### Address Configuration

```yaml
nomad_bind_addr: "0.0.0.0"
```
Specifies the address that Nomad will bind to for incoming connections. The default value `0.0.0.0` allows Nomad to listen on all available interfaces.

```yaml
nomad_advertise_addr: "{{ ansible_default_ipv4.address }}"
```
Sets the address that Nomad will advertise to other nodes in the cluster. It typically uses the default IPv4 address of the host.

```yaml
nomad_address_configuration:
  bind_addr: "{{ nomad_bind_addr }}"
  addresses:
    http: "{{ nomad_advertise_addr }}"
    rpc: "{{ nomad_advertise_addr }}"
    serf: "{{ nomad_advertise_addr }}"
  advertise:
    http: "{{ nomad_advertise_addr }}"
    rpc: "{{ nomad_advertise_addr }}"
    serf: "{{ nomad_advertise_addr }}"
  ports:
    http: 4646
    rpc: 4647
    serf: 4648
```
Defines the address configuration for the Nomad agent. This block matches the structure specified in the [Nomad documentation](https://developer.hashicorp.com/nomad/docs/configuration#advertise), including:

- **bind_addr**: The address on which Nomad will listen for incoming connections.
- **addresses**: Specifies the addresses used for different communication channels (`http`, `rpc`, and `serf`).
- **advertise**: Lists the addresses that Nomad will advertise to other nodes for the respective channels (`http`, `rpc`, and `serf`).
- **ports**: Defines the ports for the various services, with `http`, `rpc`, and `serf` ports specified.

### Autopilot Configuration

```yaml
nomad_autopilot_configuration: {}
```
This variable defines the Autopilot configuration for the Nomad agent. It should match the structure of the Autopilot stanza as described in the [Nomad documentation](https://developer.hashicorp.com/nomad/docs/configuration/autopilot). The Autopilot configuration allows you to enable and configure features like automatic leader elections and health checks for the Nomad cluster.

Example configuration:

```yaml
nomad_autopilot_configuration:
  cleanup_dead_servers: true
  last_contact_threshold: "200ms"
  max_trailing_logs: 250
  server_stabilization_time: "10s"
```

### Leave Configuration

```yaml
nomad_leave_on_interrupt: false
```
Determines whether the Nomad agent should gracefully leave the cluster when it receives an interrupt signal (e.g., SIGINT). Defaults to `false`, meaning the agent will not leave the cluster on interrupt.

```yaml
nomad_leave_on_terminate: false
```
Specifies whether the Nomad agent should leave the cluster when it is terminated (e.g., SIGTERM). Defaults to `false`, indicating the agent will not leave the cluster upon termination.

### Server Configuration

```yaml
nomad_enable_server: true
```
Indicates whether the Nomad agent should operate as a server. Defaults to `true`, enabling the server stanza.

```yaml
nomad_server_bootstrap_expect: 1
```
Specifies the number of servers that should join the cluster before bootstrapping. This value is set outside the server configuration block due to Jinja2's inability to convert strings to integers during dict merging.

```yaml
nomad_server_configuration:
  enabled: "{{ nomad_enable_server }}"
  data_dir: "{{ nomad_data_dir }}/server"
  encrypt: "{{ 'mysupersecretgossipencryptionkey' | b64encode }}"
  server_join:
    retry_join:
      - "{{ ansible_default_ipv4.address }}"
```
Defines the server configuration stanza. Includes:
- `enabled`: References the `nomad_enable_server` variable to enable or disable the server.
- `data_dir`: Path to the directory where server data will be stored.
- `encrypt`: Base64-encoded key for gossip encryption.
- `server_join.retry_join`: A list of addresses to which the server will attempt to join the cluster.

Refer to the Nomad documentation for more details on the server configuration [here](https://developer.hashicorp.com/nomad/docs/configuration/server).

### Client Configuration

```yaml
nomad_enable_client: false
```
Indicates whether the Nomad agent should operate as a client. Defaults to `false`, disabling the client stanza.

```yaml
nomad_client_configuration:
  enabled: "{{ nomad_enable_client }}"
  state_dir: "{{ nomad_data_dir }}/client"
  cni_path: "/opt/cni/bin"
  bridge_network_name: nomad
  bridge_network_subnet: "172.26.64.0/20"
```
Defines the client configuration stanza. Includes:
- `enabled`: References the `nomad_enable_client` variable to enable or disable the client.
- `state_dir`: Path to the directory where client state data will be stored.
- `cni_path`: Specifies the path to the Container Network Interface (CNI) binaries.
- `bridge_network_name`: The name of the bridge network used by the client.
- `bridge_network_subnet`: The subnet for the bridge network.

Refer to the Nomad documentation for more details on the client configuration [here](https://developer.hashicorp.com/nomad/docs/configuration/client).

### UI Configuration

```yaml
nomad_ui_configuration:
  enabled: "{{ nomad_enable_server }}"
```
Configures the Nomad UI. By default, the `enabled` field determines whether the UI is active and is set based on the `nomad_enable_server` variable, meaning the UI will only be enabled if the Nomad server is enabled.

### Drivers Configuration

```yaml
nomad_driver_enable_docker: true
```
Indicates whether the Docker driver should be enabled. Currently, this setting is not functional but is included for future development.

```yaml
nomad_driver_enable_podman: false
```
Indicates whether the Podman driver should be enabled. Currently, this setting is not functional.

```yaml
nomad_driver_enable_raw_exec: false
```
Indicates whether the Raw Exec driver should be enabled. Currently, this setting is not functional.

```yaml
nomad_driver_enable_java: false
```
Indicates whether the Java driver should be enabled. Currently, this setting is not functional.

```yaml
nomad_driver_enable_qemu: false
```
Indicates whether the QEMU driver should be enabled. Currently, this setting is not functional.

```yaml
nomad_driver_configuration:
  raw_exec:
    enabled: false
```
This block defines the configuration for Nomad drivers. The example shows the configuration for the Raw Exec driver, which is currently disabled.

```yaml
nomad_driver_extra_configuration: {}
```
A dictionary for any additional driver configuration options not covered by other variables. This should be used only for options not provided by existing variables and will be merged with the `nomad_driver_configuration`, taking precedence over existing settings.

### Nomad Logging

```yaml
nomad_log_level: info
```
Sets the logging level for Nomad. Accepted values are `trace`, `debug`, `info`, `warn`, and `error`. See [Nomad documentation on log levels](https://developer.hashicorp.com/nomad/docs/configuration#log_level) for more details.

```yaml
nomad_enable_log_to_file: false
```
Enables logging to a file if set to `true`. When enabled, the settings in `nomad_log_to_file_configuration` will define the log file path, rotation frequency, and retention of logs.

```yaml
nomad_log_to_file_configuration:
  log_file: "{{ nomad_logs_dir }}/nomad.log"
  log_rotate_duration: 24h
  log_rotate_max_files: 30
```
Specifies configuration for file-based logging:
- **`log_file`**: Defines the path to the Nomad log file (e.g., `nomad_logs_dir/nomad.log`). See [Nomad log file configuration](https://developer.hashicorp.com/nomad/docs/configuration#log_file) for details.
- **`log_rotate_duration`**: Sets the duration before log rotation occurs (e.g., `24h` for daily rotation).
- **`log_rotate_max_files`**: Maximum number of rotated log files to retain.

With `nomad_enable_log_to_file` set to `true`, these settings provide a default configuration for logging to a file, allowing Nomad to manage log files and rotation automatically.

### ACL Configuration

```yaml
nomad_acl_configuration:
  enabled: false
  token_ttl: "30s"
  policy_ttl: "60s"
  role_ttl: "60s"
```
This variable corresponds to the ACL stanza in the Nomad configuration, defining the following settings:
This configuration mirrors the structure outlined in the [Nomad ACL documentation](https://developer.hashicorp.com/nomad/docs/configuration/acl).

### Internal TLS Configuration

```yaml
nomad_enable_tls: false
```
Indicates whether internal TLS should be enabled for the Nomad cluster.

```yaml
nomad_tls_configuration:
  http: true
  rpc: true
  ca_file: "/etc/ssl/certs/ca-certificates.crt"
  cert_file: "{{ nomad_certs_dir }}/cert.pem"
  key_file: "{{ nomad_certs_dir }}/key.pem"
  verify_server_hostname: true
```
This block defines the TLS configuration for the Nomad cluster. It includes options for enabling TLS for HTTP and RPC, paths to the CA file, certificate file, key file, and verification settings for the server hostname. For detailed information, refer to the [Nomad TLS documentation](https://developer.hashicorp.com/nomad/docs/configuration/tls).

```yaml
nomad_certificates_extra_files_dir: []
```
A list for additional certificate files that can be added to the `nomad_extra_files_list` variable. If used, `nomad_extra_files` should be set to true to ensure the certificates are copied to the target host.

### Telemetry Configuration

```yaml
nomad_telemetry_configuration:
  collection_interval: 10s
  disable_hostname: false
  use_node_name: false
  publish_allocation_metrics: false
  publish_node_metrics: false
  prefix_filter: []
  disable_dispatched_job_summary_metrics: false
  prometheus_metrics: false
```
This block configures telemetry settings for Nomad. Each option adjusts different aspects of telemetry data collection and publication. For more information, refer to the [Nomad Telemetry documentation](https://developer.hashicorp.com/nomad/docs/configuration/telemetry).

### Consul Integration Configuration

```yaml
nomad_enable_consul_integration: false
```
This variable enables the Consul integration for service registration in Nomad.

```yaml
nomad_consul_integration_configuration:
  address: "127.0.0.1:8500"
  auto_advertise: true
  ssl: false
  token: ""
  tags: []
```
This block represents the **Consul** stanza, which configures the integration with Consul for service registration. For more details, refer to the [Nomad Consul documentation](https://developer.hashicorp.com/nomad/docs/configuration/consul).

```yaml
nomad_consul_integration_tls_configuration:
  ca_file: "/etc/ssl/certs/ca-certificates.crt"
```
If `nomad_consul_integration_configuration.ssl` is defined and set to `true`, the **TLS configuration** will be merged with the `nomad_consul_integration_configuration` for defining TLS-specific settings.

```yaml
nomad_consul_integration_server_configuration:
  server_auto_join: true
```
If `nomad_enable_server` is set to `true`, this configuration block will be merged with `nomad_consul_integration_configuration` to provide additional settings for the server's integration with Consul.

```yaml
nomad_consul_integration_client_configuration:
  client_auto_join: true
  grpc_address: "127.0.0.1:8502"
```
If `nomad_enable_client` is set to `true`, this block will be merged with `nomad_consul_integration_configuration` to define the client configuration for the Consul integration.

```yaml
nomad_consul_integration_client_tls_configuration:
  grpc_ca_file: "/etc/ssl/certs/ca-certificates.crt"
```
If both the client is enabled and SSL is enabled, this configuration will be merged with `nomad_consul_integration_client_configuration` for the gRPC connection to Consul.

Here's the refined **Nomad Vault Integration Configuration** section with the correct formatting and linking to the documentation:

### Nomad Vault Integration Configuration

```yaml
nomad_enable_vault_integration: false
```
This variable enables the Vault integration in Nomad.

```yaml
nomad_vault_integration_configuration: {}
```
This block represents the **Vault** stanza, which configures the integration with HashiCorp Vault for managing secrets and sensitive data. For more details, refer to the [Nomad Vault documentation](https://developer.hashicorp.com/nomad/docs/configuration/vault).

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednz_cloud.hashistack.nomad
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.

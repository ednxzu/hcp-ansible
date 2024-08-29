<!-- DOCSIBLE START -->

# 📃 Role overview

## nomad



Description: Install and configure hashicorp nomad for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 26/08/2024 |






### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [nomad_version](defaults/main.yml#L4)   | str   | `latest`  |  n/a  |  n/a |
| [nomad_start_service](defaults/main.yml#L5)   | bool   | `True`  |  n/a  |  n/a |
| [nomad_config_dir](defaults/main.yml#L6)   | str   | `/etc/nomad.d`  |  n/a  |  n/a |
| [nomad_data_dir](defaults/main.yml#L7)   | str   | `/opt/nomad`  |  n/a  |  n/a |
| [nomad_certs_dir](defaults/main.yml#L8)   | str   | `{{ nomad_config_dir }}/tls`  |  n/a  |  n/a |
| [nomad_logs_dir](defaults/main.yml#L9)   | str   | `/var/log/nomad`  |  n/a  |  n/a |
| [nomad_extra_files](defaults/main.yml#L11)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_extra_files_list](defaults/main.yml#L12)   | list   | `[]`  |  n/a  |  n/a |
| [nomad_env_variables](defaults/main.yml#L14)   | dict   | `{}`  |  n/a  |  n/a |
| [nomad_extra_configuration](defaults/main.yml#L25)   | dict   | `{}`  |  n/a  |  n/a |
| [nomad_region](defaults/main.yml#L31)   | str   | `global`  |  n/a  |  n/a |
| [nomad_datacenter](defaults/main.yml#L32)   | str   | `dc1`  |  n/a  |  n/a |
| [nomad_bind_addr](defaults/main.yml#L38)   | str   | `0.0.0.0`  |  n/a  |  n/a |
| [nomad_advertise_addr](defaults/main.yml#L39)   | str   | `{{ ansible_default_ipv4.address }}`  |  n/a  |  n/a |
| [nomad_address_configuration](defaults/main.yml#L40)   | dict   | `{'bind_addr': '{{ nomad_bind_addr }}', 'addresses': {'http': '{{ nomad_advertise_addr }}', 'rpc': '{{ nomad_advertise_addr }}', 'serf': '{{ nomad_advertise_addr }}'}, 'advertise': {'http': '{{ nomad_advertise_addr }}', 'rpc': '{{ nomad_advertise_addr }}', 'serf': '{{ nomad_advertise_addr }}'}, 'ports': {'http': 4646, 'rpc': 4647, 'serf': 4648}}`  |  n/a  |  n/a |
| [nomad_autopilot_configuration](defaults/main.yml#L59)   | dict   | `{}`  |  n/a  |  n/a |
| [nomad_leave_on_interrupt](defaults/main.yml#L65)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_leave_on_terminate](defaults/main.yml#L66)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_enable_server](defaults/main.yml#L72)   | bool   | `True`  |  n/a  |  n/a |
| [nomad_server_bootstrap_expect](defaults/main.yml#L73)   | int   | `1`  |  n/a  |  n/a |
| [nomad_server_configuration](defaults/main.yml#L74)   | dict   | `{'enabled': '{{ nomad_enable_server }}', 'data_dir': '{{ nomad_data_dir }}/server', 'encrypt': "{{ 'mysupersecretgossipencryptionkey'\|b64encode }}", 'server_join': {'retry_join': ['{{ ansible_default_ipv4.address }}']}}`  |  n/a  |  n/a |
| [nomad_enable_client](defaults/main.yml#L86)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_client_configuration](defaults/main.yml#L87)   | dict   | `{'enabled': '{{ nomad_enable_client }}', 'state_dir': '{{ nomad_data_dir }}/client', 'cni_path': '/opt/cni/bin', 'bridge_network_name': 'nomad', 'bridge_network_subnet': '172.26.64.0/20'}`  |  n/a  |  n/a |
| [nomad_ui_configuration](defaults/main.yml#L98)   | dict   | `{'enabled': '{{ nomad_enable_server }}'}`  |  n/a  |  n/a |
| [nomad_driver_enable_docker](defaults/main.yml#L105)   | bool   | `True`  |  n/a  |  n/a |
| [nomad_driver_enable_podman](defaults/main.yml#L106)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_driver_enable_raw_exec](defaults/main.yml#L107)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_driver_enable_java](defaults/main.yml#L108)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_driver_enable_qemu](defaults/main.yml#L109)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_driver_configuration](defaults/main.yml#L111)   | dict   | `{'raw_exec': {'enabled': False}}`  |  n/a  |  n/a |
| [nomad_driver_extra_configuration](defaults/main.yml#L115)   | dict   | `{}`  |  n/a  |  n/a |
| [nomad_log_level](defaults/main.yml#L121)   | str   | `info`  |  n/a  |  n/a |
| [nomad_enable_log_to_file](defaults/main.yml#L122)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_log_to_file_configuration](defaults/main.yml#L123)   | dict   | `{'log_file': '{{ nomad_logs_dir }}/nomad.log', 'log_rotate_duration': '24h', 'log_rotate_max_files': 30}`  |  n/a  |  n/a |
| [nomad_acl_configuration](defaults/main.yml#L132)   | dict   | `{'enabled': False, 'token_ttl': '30s', 'policy_ttl': '60s', 'role_ttl': '60s'}`  |  n/a  |  n/a |
| [nomad_enable_tls](defaults/main.yml#L142)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_tls_configuration](defaults/main.yml#L143)   | dict   | `{'http': True, 'rpc': True, 'ca_file': '/etc/ssl/certs/ca-certificates.crt', 'cert_file': '{{ nomad_certs_dir }}/cert.pem', 'key_file': '{{ nomad_certs_dir }}/key.pem', 'verify_server_hostname': True}`  |  n/a  |  n/a |
| [nomad_certificates_extra_files_dir](defaults/main.yml#L151)   | list   | `[]`  |  n/a  |  n/a |
| [nomad_telemetry_configuration](defaults/main.yml#L160)   | dict   | `{'collection_interval': '10s', 'disable_hostname': False, 'use_node_name': False, 'publish_allocation_metrics': False, 'publish_node_metrics': False, 'prefix_filter': [], 'disable_dispatched_job_summary_metrics': False, 'prometheus_metrics': False}`  |  n/a  |  n/a |
| [nomad_enable_consul_integration](defaults/main.yml#L174)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_consul_integration_configuration](defaults/main.yml#L175)   | dict   | `{'address': '127.0.0.1:8500', 'auto_advertise': True, 'ssl': False, 'token': '', 'tags': []}`  |  n/a  |  n/a |
| [nomad_consul_integration_tls_configuration](defaults/main.yml#L182)   | dict   | `{'ca_file': '/etc/ssl/certs/ca-certificates.crt'}`  |  n/a  |  n/a |
| [nomad_consul_integration_server_configuration](defaults/main.yml#L185)   | dict   | `{'server_auto_join': True}`  |  n/a  |  n/a |
| [nomad_consul_integration_client_configuration](defaults/main.yml#L188)   | dict   | `{'client_auto_join': True, 'grpc_address': '127.0.0.1:8502'}`  |  n/a  |  n/a |
| [nomad_consul_integration_client_tls_configuration](defaults/main.yml#L192)   | dict   | `{'grpc_ca_file': '/etc/ssl/certs/ca-certificates.crt'}`  |  n/a  |  n/a |
| [nomad_enable_vault_integration](defaults/main.yml#L199)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_vault_integration_configuration](defaults/main.yml#L200)   | dict   | `{}`  |  n/a  |  n/a |


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [nomad_user](vars/main.yml#L3)    | str   | `nomad`  | n/a | n/a |
| [nomad_group](vars/main.yml#L4)    | str   | `nomad`  | n/a | n/a |
| [nomad_binary_path](vars/main.yml#L5)    | str   | `/usr/local/bin/nomad`  | n/a | n/a |
| [nomad_deb_architecture_map](vars/main.yml#L6)    | dict   | `{'x86_64': 'amd64', 'aarch64': 'arm64', 'armv7l': 'arm', 'armv6l': 'arm'}`  | n/a | n/a |
| [nomad_architecture](vars/main.yml#L11)    | str   | `{{ nomad_deb_architecture_map[ansible_architecture] \| default(ansible_architecture) }}`  | n/a | n/a |
| [nomad_service_name](vars/main.yml#L12)    | str   | `nomad`  | n/a | n/a |
| [nomad_github_api](vars/main.yml#L13)    | str   | `https://api.github.com/repos`  | n/a | n/a |
| [nomad_github_project](vars/main.yml#L14)    | str   | `hashicorp/nomad`  | n/a | n/a |
| [nomad_github_url](vars/main.yml#L15)    | str   | `https://github.com`  | n/a | n/a |
| [nomad_repository_url](vars/main.yml#L16)    | str   | `https://releases.hashicorp.com/nomad`  | n/a | n/a |
| [nomad_configuration](vars/main.yml#L18)    | dict   | `{'datacenter': '{{ nomad_datacenter }}', 'region': '{{ nomad_region }}', 'data_dir': '{{ nomad_data_dir }}', 'leave_on_interrupt': '{{ nomad_leave_on_interrupt }}', 'leave_on_terminate': '{{ nomad_leave_on_terminate }}', 'acl': '{{ nomad_acl_configuration }}', 'server': '{{ nomad_server_configuration }}', 'client': '{{ nomad_client_configuration }}', 'ui': '{{ nomad_ui_configuration }}', 'log_level': '{{ nomad_log_level }}'}`  | n/a | n/a |
| [nomad_configuration_string](vars/main.yml#L30)    | str   | `<multiline value>`  | n/a | n/a |


### Tasks


#### File: tasks/recursive_copy_extra_dirs.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Ensure destination directory exists | ansible.builtin.file | False |
| Nomad \| Create extra directory sources | ansible.builtin.file | True |
| Nomad \| Template extra directory sources | ansible.builtin.template | True |

#### File: tasks/merge_variables.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Merge stringified configuration | vars | False |
| Nomad \| Merge addresses configuration | vars | False |
| Nomad \| Merge consul integration configuration | block | True |
| Nomad \| Merge consul tls configuration | block | True |
| Nomad \| Merge consul default client configuration | vars | False |
| Nomad \| Merge consul configuration for nomad servers | block | True |
| Nomad \| Merge consul default server configuration | vars | False |
| Nomad \| Merge consul configuration for nomad clients | block | True |
| Nomad \| Merge consul default client configuration | vars | False |
| Nomad \| Merge consul tls client configuration | vars | True |
| Nomad \| Merge consul block into main configuration | vars | False |
| Nomad \| Merge TLS configuration | block | True |
| Nomad \| Merge TLS configuration | vars | False |
| Nomad \| Add certificates directory to extra_files_dir | ansible.builtin.set_fact | False |
| Nomad \| Merge plugin configuration | vars | True |
| Nomad \| Merge extra configuration settings | vars | False |
| Nomad \| Merge log to file configuration | vars | True |
| Nomad \| Merge telemetry configuration | vars | False |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Set reload-check & restart-check variable | ansible.builtin.set_fact | False |
| Nomad \| Import merge_variables.yml | ansible.builtin.include_tasks | False |
| Nomad \| Import prerequisites.yml | ansible.builtin.include_tasks | False |
| Nomad \| Import install.yml | ansible.builtin.include_tasks | False |
| Nomad \| Import configure.yml | ansible.builtin.include_tasks | False |
| Nomad \| Populate service facts | ansible.builtin.service_facts | False |
| Nomad \| Set restart-check variable | ansible.builtin.set_fact | True |
| Nomad \| Enable service: {{ nomad_service_name }} | ansible.builtin.service | False |
| Nomad \| Reload systemd daemon | ansible.builtin.systemd | True |
| Nomad \| Start service: {{ nomad_service_name }} | ansible.builtin.service | True |

#### File: tasks/install.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Get latest release of nomad | block | True |
| Nomad \| Get latest nomad release from github api | ansible.builtin.uri | False |
| Nomad \| Set wanted nomad version to latest tag | ansible.builtin.set_fact | False |
| Nomad \| Set wanted nomad version to {{ nomad_version }} | ansible.builtin.set_fact | True |
| Nomad \| Get current nomad version | block | False |
| Nomad \| Stat nomad version file | ansible.builtin.stat | False |
| Nomad \| Get current nomad version | ansible.builtin.slurp | True |
| Nomad \| Download and install nomad binary | block | True |
| Nomad \| Set nomad package name to download | ansible.builtin.set_fact | False |
| Nomad \| Download checksum file for nomad archive | ansible.builtin.get_url | False |
| Nomad \| Extract correct checksum from checksum file | ansible.builtin.command | False |
| Nomad \| Parse the expected checksum | ansible.builtin.set_fact | False |
| Nomad \| Download nomad binary archive | ansible.builtin.get_url | False |
| Nomad \| Create temporary directory for archive decompression | ansible.builtin.file | False |
| Nomad \| Unpack nomad archive | ansible.builtin.unarchive | False |
| Nomad \| Copy nomad binary to {{ nomad_binary_path }} | ansible.builtin.copy | False |
| Nomad \| Update nomad version file | ansible.builtin.copy | False |
| Nomad \| Set restart-check variable | ansible.builtin.set_fact | False |
| Nomad \| Cleanup temporary directory | ansible.builtin.file | False |
| Nomad \| Copy systemd service file for nomad | ansible.builtin.template | False |
| Nomad \| Set reload-check & restart-check variable | ansible.builtin.set_fact | True |

#### File: tasks/prerequisites.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Create group {{ nomad_group }} | ansible.builtin.group | False |
| Nomad \| Create user {{ nomad_user }} | ansible.builtin.user | False |
| Nomad \| Create directory {{ nomad_config_dir }} | ansible.builtin.file | False |
| Nomad \| Create directory {{ nomad_data_dir }} | ansible.builtin.file | False |
| Nomad \| Create directory {{ nomad_certs_dir }} | ansible.builtin.file | False |
| Nomad \| Create directory {{ nomad_logs_dir }} | ansible.builtin.file | True |

#### File: tasks/configure.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Create nomad.env | ansible.builtin.template | False |
| Nomad \| Copy nomad.json template | ansible.builtin.template | False |
| Nomad \| Set restart-check variable | ansible.builtin.set_fact | True |
| Nomad \| Copy extra configuration files | block | True |
| Nomad \| Get extra file types | ansible.builtin.stat | False |
| Nomad \| Set list for file sources | vars | True |
| Nomad \| Set list for directory sources | vars | True |
| Nomad \| Template extra file sources | ansible.builtin.template | True |
| Nomad \| Template extra directory sources | ansible.builtin.include_tasks | True |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['focal', 'jammy', 'noble']
- **Debian**: ['bullseye', 'bookworm']

<!-- DOCSIBLE END -->

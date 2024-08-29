<!-- DOCSIBLE START -->

# 📃 Role overview

## vault



Description: Install and configure hashicorp vault for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 26/08/2024 |






### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [vault_version](defaults/main.yml#L3)   | str   | `latest`  |  n/a  |  n/a |
| [vault_start_service](defaults/main.yml#L4)   | bool   | `True`  |  n/a  |  n/a |
| [vault_config_dir](defaults/main.yml#L5)   | str   | `/etc/vault.d`  |  n/a  |  n/a |
| [vault_data_dir](defaults/main.yml#L6)   | str   | `/opt/vault`  |  n/a  |  n/a |
| [vault_certs_dir](defaults/main.yml#L7)   | str   | `{{ vault_config_dir }}/tls`  |  n/a  |  n/a |
| [vault_logs_dir](defaults/main.yml#L8)   | str   | `/var/log/vault`  |  n/a  |  n/a |
| [vault_extra_files](defaults/main.yml#L10)   | bool   | `False`  |  n/a  |  n/a |
| [vault_extra_files_list](defaults/main.yml#L11)   | list   | `[]`  |  n/a  |  n/a |
| [vault_env_variables](defaults/main.yml#L13)   | dict   | `{}`  |  n/a  |  n/a |
| [vault_extra_configuration](defaults/main.yml#L24)   | dict   | `{}`  |  n/a  |  n/a |
| [vault_cluster_name](defaults/main.yml#L30)   | str   | `vault`  |  n/a  |  n/a |
| [vault_bind_addr](defaults/main.yml#L31)   | str   | `0.0.0.0`  |  n/a  |  n/a |
| [vault_cluster_addr](defaults/main.yml#L32)   | str   | `{{ ansible_default_ipv4.address }}`  |  n/a  |  n/a |
| [vault_enable_ui](defaults/main.yml#L33)   | bool   | `True`  |  n/a  |  n/a |
| [vault_disable_mlock](defaults/main.yml#L34)   | bool   | `False`  |  n/a  |  n/a |
| [vault_disable_cache](defaults/main.yml#L35)   | bool   | `False`  |  n/a  |  n/a |
| [vault_storage_configuration](defaults/main.yml#L41)   | dict   | `{'file': {'path': '{{ vault_data_dir }}'}}`  |  n/a  |  n/a |
| [vault_enable_tls](defaults/main.yml#L49)   | bool   | `False`  |  n/a  |  n/a |
| [vault_listener_configuration](defaults/main.yml#L50)   | list   | `[{'tcp': {'address': '{{ vault_cluster_addr }}:8200', 'tls_disable': True}}]`  |  n/a  |  n/a |
| [vault_tls_listener_configuration](defaults/main.yml#L55)   | list   | `[{'tcp': {'tls_disable': False, 'tls_cert_file': '{{ vault_certs_dir }}/cert.pem', 'tls_key_file': '{{ vault_certs_dir }}/key.pem', 'tls_disable_client_certs': True}}]`  |  n/a  |  n/a |
| [vault_certificates_extra_files_dir](defaults/main.yml#L62)   | list   | `[]`  |  n/a  |  n/a |
| [vault_extra_listener_configuration](defaults/main.yml#L67)   | list   | `[]`  |  n/a  |  n/a |
| [vault_enable_service_registration](defaults/main.yml#L73)   | bool   | `False`  |  n/a  |  n/a |
| [vault_service_registration_configuration](defaults/main.yml#L74)   | dict   | `{'consul': {'address': '127.0.0.1:8500', 'scheme': 'http', 'token': ''}}`  |  n/a  |  n/a |
| [vault_enable_plugins](defaults/main.yml#L84)   | bool   | `False`  |  n/a  |  n/a |
| [vault_plugins_directory](defaults/main.yml#L85)   | str   | `{{ vault_config_dir }}/plugins`  |  n/a  |  n/a |
| [vault_log_level](defaults/main.yml#L91)   | str   | `info`  |  n/a  |  n/a |
| [vault_enable_log_to_file](defaults/main.yml#L92)   | bool   | `False`  |  n/a  |  n/a |
| [vault_log_to_file_configuration](defaults/main.yml#L93)   | dict   | `{'log_file': '{{ vault_logs_dir }}/vault.log', 'log_rotate_duration': '24h', 'log_rotate_max_files': 30}`  |  n/a  |  n/a |


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [vault_user](vars/main.yml#L3)    | str   | `vault`  | n/a | n/a |
| [vault_group](vars/main.yml#L4)    | str   | `vault`  | n/a | n/a |
| [vault_binary_path](vars/main.yml#L5)    | str   | `/usr/local/bin/vault`  | n/a | n/a |
| [vault_deb_architecture_map](vars/main.yml#L6)    | dict   | `{'x86_64': 'amd64', 'aarch64': 'arm64', 'armv7l': 'arm', 'armv6l': 'arm'}`  | n/a | n/a |
| [vault_architecture](vars/main.yml#L11)    | str   | `{{ vault_deb_architecture_map[ansible_architecture] \| default(ansible_architecture) }}`  | n/a | n/a |
| [vault_service_name](vars/main.yml#L12)    | str   | `vault`  | n/a | n/a |
| [vault_github_api](vars/main.yml#L13)    | str   | `https://api.github.com/repos`  | n/a | n/a |
| [vault_github_project](vars/main.yml#L14)    | str   | `hashicorp/vault`  | n/a | n/a |
| [vault_github_url](vars/main.yml#L15)    | str   | `https://github.com`  | n/a | n/a |
| [vault_repository_url](vars/main.yml#L16)    | str   | `https://releases.hashicorp.com/vault`  | n/a | n/a |
| [vault_configuration](vars/main.yml#L18)    | dict   | `{'cluster_name': '{{ vault_cluster_name }}', 'cluster_addr': "{{ 'https' if vault_enable_tls else 'http'}}://{{ vault_cluster_addr }}:8201", 'api_addr': "{{ 'https' if vault_enable_tls else 'http'}}://{{ vault_cluster_addr }}:8200", 'ui': '{{ vault_enable_ui }}', 'disable_mlock': '{{ vault_disable_mlock }}', 'disable_cache': '{{ vault_disable_cache }}', 'listener': '{{ vault_listener_configuration }}', 'storage': '{{ vault_storage_configuration }}'}`  | n/a | n/a |


### Tasks


#### File: tasks/recursive_copy_extra_dirs.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Vault \| Ensure destination directory exists | ansible.builtin.file | False |
| Vault \| Create extra directory sources | ansible.builtin.file | True |
| Vault \| Template extra directory sources | ansible.builtin.template | True |

#### File: tasks/merge_variables.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Vault \| Merge listener configuration | block | False |
| Vault \| Merge tls listener configuration | vars | True |
| Vault \| Merge extra listener configuration | vars | False |
| Vault \| Add certificates directory to extra_files_dir | ansible.builtin.set_fact | False |
| Vault \| Merge service registration configuration | vars | True |
| Vault \| Merge plugins configuration | vars | True |
| Vault \| Merge logging configuration | vars | True |
| Vault \| Merge extra configuration settings | vars | True |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Vault \| Set reload-check & restart-check variable | ansible.builtin.set_fact | False |
| Vault \| Import merge_variables.yml | ansible.builtin.include_tasks | False |
| Vault \| Import prerequisites.yml | ansible.builtin.include_tasks | False |
| Vault \| Import install.yml | ansible.builtin.include_tasks | False |
| Vault \| Import configure.yml | ansible.builtin.include_tasks | False |
| Vault \| Populate service facts | ansible.builtin.service_facts | False |
| Vault \| Set restart-check variable | ansible.builtin.set_fact | True |
| Vault \| Enable service: {{ vault_service_name }} | ansible.builtin.service | False |
| Vault \| Reload systemd daemon | ansible.builtin.systemd | True |
| Vault \| Start service: {{ vault_service_name }} | ansible.builtin.service | True |

#### File: tasks/install.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Vault \| Get latest release of vault | block | True |
| Vault \| Get latest vault release from github api | ansible.builtin.uri | False |
| Vault \| Set wanted vault version to latest tag | ansible.builtin.set_fact | False |
| Vault \| Set wanted vault version to {{ vault_version }} | ansible.builtin.set_fact | True |
| Vault \| Get current vault version | block | False |
| Vault \| Stat vault version file | ansible.builtin.stat | False |
| Vault \| Get current vault version | ansible.builtin.slurp | True |
| Vault \| Download and install vault binary | block | True |
| Vault \| Set vault package name to download | ansible.builtin.set_fact | False |
| Vault \| Download checksum file for vault archive | ansible.builtin.get_url | False |
| Vault \| Extract correct checksum from checksum file | ansible.builtin.command | False |
| Vault \| Parse the expected checksum | ansible.builtin.set_fact | False |
| Vault \| Download vault binary archive | ansible.builtin.get_url | False |
| Vault \| Create temporary directory for archive decompression | ansible.builtin.file | False |
| Vault \| Unpack vault archive | ansible.builtin.unarchive | False |
| Vault \| Copy vault binary to {{ vault_binary_path }} | ansible.builtin.copy | False |
| Vault \| Update vault version file | ansible.builtin.copy | False |
| Vault \| Set restart-check variable | ansible.builtin.set_fact | False |
| Vault \| Cleanup temporary directory | ansible.builtin.file | False |
| Vault \| Copy systemd service file for vault | ansible.builtin.template | False |
| Vault \| Set reload-check & restart-check variable | ansible.builtin.set_fact | True |
| Vault \| Copy systemd service file for vault | ansible.builtin.template | False |

#### File: tasks/prerequisites.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Vault \| Create group {{ vault_group }} | ansible.builtin.group | False |
| Vault \| Create user {{ vault_user }} | ansible.builtin.user | False |
| Vault \| Create directory {{ vault_config_dir }} | ansible.builtin.file | False |
| Vault \| Create directory {{ vault_data_dir}} | ansible.builtin.file | False |
| Vault \| Create directory {{ vault_certs_dir }} | ansible.builtin.file | False |
| Vault \| Create directory {{ vault_logs_dir }} | ansible.builtin.file | True |

#### File: tasks/configure.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Vault \| Create vault.env | ansible.builtin.template | False |
| Vault \| Copy vault.json template | ansible.builtin.template | False |
| Vault \| Set restart-check variable | ansible.builtin.set_fact | True |
| Vault \| Copy extra configuration files | block | True |
| Vault \| Get extra file types | ansible.builtin.stat | False |
| Vault \| Set list for file sources | vars | True |
| Vault \| Set list for directory sources | vars | True |
| Vault \| Template extra file sources | ansible.builtin.template | True |
| Vault \| Template extra directory sources | ansible.builtin.include_tasks | True |







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

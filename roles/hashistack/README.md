<!-- DOCSIBLE START -->

# 📃 Role overview

## hashistack



Description: Merge variables for the playbooks contained in ednz_cloud.hashistack collection


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 26/08/2024 |






### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [hashistack_configuration_directory](defaults/main.yml#L3)   | str   | `{{ lookup('env', 'PWD') }}/etc/hashistack`  |  n/a  |  n/a |
| [hashistack_sub_configuration_directories](defaults/main.yml#L4)   | dict   | `{'secrets': '{{ hashistack_configuration_directory }}/secrets', 'certificates': '{{ hashistack_configuration_directory }}/certificates', 'nomad_servers': '{{ hashistack_configuration_directory }}/nomad_servers', 'vault_servers': '{{ hashistack_configuration_directory }}/vault_servers', 'consul_servers': '{{ hashistack_configuration_directory }}/consul_servers'}`  |  n/a  |  n/a |
| [hashistack_configuration_global_vars_file](defaults/main.yml#L11)   | str   | `globals.yml`  |  n/a  |  n/a |
| [hashistack_configuration_credentials_vars_file](defaults/main.yml#L12)   | str   | `credentials.yml`  |  n/a  |  n/a |
| [hashistack_remote_config_dir](defaults/main.yml#L14)   | str   | `/etc/hashistack`  |  n/a  |  n/a |
| [hashistack_remote_log_dir](defaults/main.yml#L15)   | str   | `/var/log/hashistack`  |  n/a  |  n/a |
| [hashistack_only_load_credentials](defaults/main.yml#L17)   | bool   | `False`  |  n/a  |  n/a |





### Tasks


#### File: tasks/load_group_vars.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Variables \| Stat group specific config file | ansible.builtin.stat | False |
| Variables \| Load group specific variables | ansible.builtin.include_vars | True |

#### File: tasks/load_credentials_vars.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Variables \| Stat credentials file | ansible.builtin.stat | False |
| Variables \| Stat vault credentials file | ansible.builtin.stat | False |
| Variables \| Make sure credentials file exists | ansible.builtin.assert | False |
| Variables \| Load credentials variables | ansible.builtin.include_vars | False |
| Variables \| Load vault credentials if vault.yml exists | ansible.builtin.include_vars | True |
| Variables \| Merge vault credentials into _credentials | vars | True |

#### File: tasks/load_host_vars.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Variables \| Stat host specific config file | ansible.builtin.stat | False |
| Variables \| Load host specific variables | ansible.builtin.include_vars | True |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Variables \| Load global variables | ansible.builtin.include_tasks | True |
| Variables \| Load credentials variables | ansible.builtin.include_tasks | False |
| Variables \| Load group specific variables | ansible.builtin.include_tasks | True |
| Variables \| Load host specific variables | ansible.builtin.include_tasks | True |
| Ensure remote directories exists | ansible.builtin.file | True |
| Variables \| Load custom CA certificates | ansible.builtin.include_tasks | True |

#### File: tasks/load_ca_certificates.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Check if CA directory exists | ansible.builtin.stat | False |
| Find custom ca certificates to copy | ansible.builtin.find | True |
| Ensure remote ca directory exists | ansible.builtin.file | False |
| Copy custom ca certificates | ansible.builtin.copy | True |
| Copy and update trust store | block | True |
| Copy ca certificates to /usr/local/share/ca-certificates | ansible.builtin.file | False |
| Update the trust store | ansible.builtin.command | True |

#### File: tasks/load_global_vars.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Variables \| Include all default variables | ansible.builtin.include_vars | False |
| Variables \| Stat global configuration file | ansible.builtin.stat | False |
| Variables \| Make sure global configuration file exists | ansible.builtin.assert | False |
| Variables \| Load global variables | ansible.builtin.include_vars | False |







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

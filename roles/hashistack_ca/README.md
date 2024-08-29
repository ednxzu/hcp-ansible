<!-- DOCSIBLE START -->

# 📃 Role overview

## hashistack_ca




Description: Not available.

| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 26/08/2024 |






### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [hashistack_ca_directory](defaults/main.yml#L3)   | str   | `/etc/hashistack/certificates`  |  n/a  |  n/a |
| [hashistack_ca_use_cryptography](defaults/main.yml#L4)   | bool   | `False`  |  n/a  |  n/a |
| [hashistack_ca_action](defaults/main.yml#L5)   | str   | `noop`  |  n/a  |  n/a |
| [hashistack_ca_domain](defaults/main.yml#L6)   | str   | `example.com`  |  n/a  |  n/a |
| [hashistack_ca_directory_owner](defaults/main.yml#L7)   | str   | `root`  |  n/a  |  n/a |
| [hashistack_ca_root_org_name](defaults/main.yml#L12)   | str   | `EDNZ Cloud`  |  n/a  |  n/a |
| [hashistack_ca_root_country](defaults/main.yml#L13)   | str   | `FR`  |  n/a  |  n/a |
| [hashistack_ca_root_locality](defaults/main.yml#L14)   | str   | `Paris`  |  n/a  |  n/a |
| [hashistack_ca_root_common_name](defaults/main.yml#L15)   | str   | `{{ hashistack_ca_domain }} Root CA`  |  n/a  |  n/a |
| [hashistack_ca_root_email](defaults/main.yml#L16)   | NoneType   | `None`  |  n/a  |  n/a |
| [hashistack_ca_root_key_usage](defaults/main.yml#L17)   | list   | `['keyCertSign', 'cRLSign']`  |  n/a  |  n/a |
| [hashistack_ca_root_key_usage_critical](defaults/main.yml#L20)   | bool   | `True`  |  n/a  |  n/a |
| [hashistack_ca_root_basic_constraints](defaults/main.yml#L21)   | list   | `['CA:TRUE']`  |  n/a  |  n/a |
| [hashistack_ca_root_basic_constraints_critical](defaults/main.yml#L23)   | bool   | `True`  |  n/a  |  n/a |
| [hashistack_ca_root_state_or_province_name](defaults/main.yml#L26)   | NoneType   | `None`  |  n/a  |  n/a |
| [hashistack_ca_root_email_address](defaults/main.yml#L27)   | NoneType   | `None`  |  n/a  |  n/a |
| [hashistack_ca_root_valid_for](defaults/main.yml#L30)   | str   | `1825d`  |  n/a  |  n/a |
| [hashistack_ca_root_renew_threshold](defaults/main.yml#L31)   | str   | `180d`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_org_name](defaults/main.yml#L36)   | str   | `EDNZ Cloud Intermediate`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_country](defaults/main.yml#L37)   | str   | `FR`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_locality](defaults/main.yml#L38)   | str   | `Paris`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_common_name](defaults/main.yml#L39)   | str   | `{{ hashistack_ca_domain }} Intermediate CA`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_email](defaults/main.yml#L40)   | NoneType   | `None`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_key_usage](defaults/main.yml#L41)   | list   | `['keyCertSign', 'cRLSign']`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_key_usage_critical](defaults/main.yml#L44)   | bool   | `True`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_basic_constraints](defaults/main.yml#L45)   | list   | `['CA:TRUE', 'pathlen:0']`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_basic_constraints_critical](defaults/main.yml#L48)   | bool   | `True`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_state_or_province_name](defaults/main.yml#L51)   | NoneType   | `None`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_email_address](defaults/main.yml#L52)   | NoneType   | `None`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_valid_for](defaults/main.yml#L55)   | str   | `365d`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_renew_threshold](defaults/main.yml#L56)   | str   | `90d`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_name_constraints_permitted](defaults/main.yml#L59)   | list   | `['DNS:.{{ hashistack_ca_domain }}', 'DNS:.nomad', 'DNS:.consul', 'DNS:localhost', 'IP:192.168.0.0/16', 'IP:172.16.0.0/16', 'IP:10.0.0.0/8', 'IP:127.0.0.0/8']`  |  n/a  |  n/a |
| [hashistack_ca_intermediate_name_constraints_critical](defaults/main.yml#L68)   | str   | `{{ (hashistack_ca_intermediate_name_constraints_permitted is defined and hashistack_ca_intermediate_name_constraints_permitted \| length > 0) }}`  |  n/a  |  n/a |
| [hashistack_ca_leaf_valid_for](defaults/main.yml#L74)   | str   | `90d`  |  n/a  |  n/a |
| [hashistack_ca_leaf_renew_threshold](defaults/main.yml#L75)   | str   | `30d`  |  n/a  |  n/a |
| [hashistack_ca_consul_org_name](defaults/main.yml#L80)   | str   | `{{ hashistack_ca_root_org_name }}`  |  n/a  |  n/a |
| [hashistack_ca_consul_common_name](defaults/main.yml#L81)   | str   | `{{ inventory_hostname }}`  |  n/a  |  n/a |
| [hashistack_ca_consul_csr_sans](defaults/main.yml#L82)   | list   | `['DNS:consul.service.consul', 'DNS:localhost', 'IP:127.0.0.1']`  |  n/a  |  n/a |
| [hashistack_ca_nomad_org_name](defaults/main.yml#L90)   | str   | `{{ hashistack_ca_root_org_name }}`  |  n/a  |  n/a |
| [hashistack_ca_nomad_common_name](defaults/main.yml#L91)   | str   | `{{ inventory_hostname }}`  |  n/a  |  n/a |
| [hashistack_ca_nomad_csr_sans](defaults/main.yml#L92)   | list   | `['DNS:server.global.nomad', 'DNS:client.global.nomad', 'DNS:nomad.service.consul', 'DNS:localhost', 'IP:127.0.0.1']`  |  n/a  |  n/a |
| [hashistack_ca_vault_org_name](defaults/main.yml#L102)   | str   | `{{ hashistack_ca_root_org_name }}`  |  n/a  |  n/a |
| [hashistack_ca_vault_common_name](defaults/main.yml#L103)   | str   | `{{ inventory_hostname }}`  |  n/a  |  n/a |
| [hashistack_ca_vault_csr_sans](defaults/main.yml#L104)   | list   | `['DNS:vault.service.consul', 'DNS:active.vault.service.consul', 'DNS:standby.vault.service.consul', 'DNS:localhost', 'IP:127.0.0.1']`  |  n/a  |  n/a |


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [hashistack_ca_action_list](vars/main.yml#L3)    | str   | `{{ hashistack_ca_action.split(',') }}`  | n/a | n/a |
| [hashistack_ca_generate_root](vars/main.yml#L6)    | str   | `{{ 'root_ca' in hashistack_ca_action_list }}`  | n/a | n/a |
| [hashistack_ca_generate_intermediate](vars/main.yml#L7)    | str   | `{{ 'int_ca' in hashistack_ca_action_list }}`  | n/a | n/a |
| [hashistack_ca_generate_leaf](vars/main.yml#L8)    | str   | `{{ 'leaf_cert' in hashistack_ca_action_list }}`  | n/a | n/a |
| [hashistack_ca_renew_root](vars/main.yml#L9)    | str   | `{{ 'renew_root' in hashistack_ca_action_list }}`  | n/a | n/a |
| [hashistack_ca_renew_intermediate](vars/main.yml#L10)    | str   | `{{ 'renew_int' in hashistack_ca_action_list }}`  | n/a | n/a |
| [hashistack_ca_renew_leaf](vars/main.yml#L11)    | str   | `{{ 'renew_leaf' in hashistack_ca_action_list }}`  | n/a | n/a |
| [hashistack_ca_public_dir](vars/main.yml#L13)    | str   | `{{ hashistack_ca_directory }}/ca`  | n/a | n/a |
| [hashistack_ca_root_dir](vars/main.yml#L15)    | str   | `{{ hashistack_ca_directory }}/root`  | n/a | n/a |
| [hashistack_ca_root_backup_dir](vars/main.yml#L16)    | str   | `{{ hashistack_ca_root_dir }}/backup`  | n/a | n/a |
| [hashistack_ca_root_key_path](vars/main.yml#L17)    | str   | `{{ hashistack_ca_root_dir }}/ca.key`  | n/a | n/a |
| [hashistack_ca_root_cert_path](vars/main.yml#L18)    | str   | `{{ hashistack_ca_root_dir }}/ca.crt`  | n/a | n/a |
| [hashistack_ca_intermediate_dir](vars/main.yml#L20)    | str   | `{{ hashistack_ca_directory }}/intermediate`  | n/a | n/a |
| [hashistack_ca_intermediate_backup_dir](vars/main.yml#L21)    | str   | `{{ hashistack_ca_intermediate_dir }}/backup`  | n/a | n/a |
| [hashistack_ca_intermediate_key_path](vars/main.yml#L22)    | str   | `{{ hashistack_ca_intermediate_dir }}/ca.key`  | n/a | n/a |
| [hashistack_ca_intermediate_csr_path](vars/main.yml#L23)    | str   | `{{ hashistack_ca_intermediate_dir }}/ca.csr`  | n/a | n/a |
| [hashistack_ca_intermediate_cert_path](vars/main.yml#L24)    | str   | `{{ hashistack_ca_intermediate_dir }}/ca.crt`  | n/a | n/a |
| [hashistack_ca_consul_dir](vars/main.yml#L26)    | str   | `{{ hashistack_ca_directory }}/consul/{{ inventory_hostname }}`  | n/a | n/a |
| [hashistack_ca_consul_key_path](vars/main.yml#L27)    | str   | `{{ hashistack_ca_consul_dir }}/cert.key`  | n/a | n/a |
| [hashistack_ca_consul_cert_path](vars/main.yml#L28)    | str   | `{{ hashistack_ca_consul_dir }}/cert.crt`  | n/a | n/a |
| [hashistack_ca_consul_fullchain_path](vars/main.yml#L29)    | str   | `{{ hashistack_ca_consul_dir }}/fullchain.crt`  | n/a | n/a |
| [hashistack_ca_nomad_dir](vars/main.yml#L31)    | str   | `{{ hashistack_ca_directory }}/nomad/{{ inventory_hostname }}`  | n/a | n/a |
| [hashistack_ca_nomad_key_path](vars/main.yml#L32)    | str   | `{{ hashistack_ca_nomad_dir }}/cert.key`  | n/a | n/a |
| [hashistack_ca_nomad_cert_path](vars/main.yml#L33)    | str   | `{{ hashistack_ca_nomad_dir }}/cert.crt`  | n/a | n/a |
| [hashistack_ca_nomad_fullchain_path](vars/main.yml#L34)    | str   | `{{ hashistack_ca_nomad_dir }}/fullchain.crt`  | n/a | n/a |
| [hashistack_ca_vault_dir](vars/main.yml#L36)    | str   | `{{ hashistack_ca_directory }}/vault/{{ inventory_hostname }}`  | n/a | n/a |
| [hashistack_ca_vault_key_path](vars/main.yml#L37)    | str   | `{{ hashistack_ca_vault_dir }}/cert.key`  | n/a | n/a |
| [hashistack_ca_vault_cert_path](vars/main.yml#L38)    | str   | `{{ hashistack_ca_vault_dir }}/cert.crt`  | n/a | n/a |
| [hashistack_ca_vault_fullchain_path](vars/main.yml#L39)    | str   | `{{ hashistack_ca_vault_dir }}/fullchain.crt`  | n/a | n/a |


### Tasks


#### File: tasks/prepare_ca_to_copy.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| CA \| Check if CA directory exists | ansible.builtin.stat | False |
| CA \| Find custom CA certificates to copy | ansible.builtin.find | True |
| CA \| Ensure public CA directory exists | ansible.builtin.file | False |
| CA \| Copy root CA certificates | ansible.builtin.copy | True |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| CA \| Import generate_root.yml | ansible.builtin.include_tasks | True |
| CA \| Import generate_intermediate.yml | ansible.builtin.include_tasks | True |
| CA \| Import renew_root.yml | ansible.builtin.include_tasks | True |
| CA \| Import renew_intermediate.yml | ansible.builtin.include_tasks | True |
| CA \| Import prepare_ca_to_copy.yml | ansible.builtin.include_tasks | False |
| CA \| Import cleanup_backups.yml | ansible.builtin.include_tasks | False |
| Consul leaf certificates \| Import generate/generate_consul.yml | ansible.builtin.include_tasks | True |
| Nomad leaf certificates \| Import generate/generate_nomad.yml | ansible.builtin.include_tasks | True |
| Vault leaf certificates \| Import generate/generate_vault.yml | ansible.builtin.include_tasks | True |
| Consul leaf certificates \| Import renew_consul.yml | ansible.builtin.include_tasks | True |

#### File: tasks/cleanup_backups.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Cleanup \| Check if root CA backup directory exists | ansible.builtin.stat | False |
| Cleanup \| Check if intermediate CA backup directory exists | ansible.builtin.stat | False |
| Cleanup \| Root CA backups | block | True |
| Root CA \| Find root CA backup certificates | ansible.builtin.find | False |
| Root CA \| Check expiration for root CA backup certificates | when | True |
| Root CA \| Remove expired root CA backup certificates | when | True |
| Cleanup \| Intermediate CA backups | block | True |
| Intermediate CA \| Find intermediate CA backup certificates | ansible.builtin.find | False |
| Intermediate CA \| Check expiration for intermediate CA backup certificates | when | True |
| Intermediate CA \| Remove expired intermediate CA backup certificates | when | True |

#### File: tasks/generate/generate_consul.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Consul leaf certificates \| Create certificate directory in for consul servers | ansible.builtin.file | False |
| Consul leaf certificates \| Create Consul certificates | block | False |
| Consul leaf certificates \| Create Consul certificate keys | community.crypto.openssl_privatekey | False |
| Consul leaf certificates \| Create CSRs for Consul servers | community.crypto.openssl_csr_pipe | False |
| Consul leaf certificates \| Sign certificates with internal CA | community.crypto.x509_certificate | False |
| Consul leaf certificates \| Generate fullchain certificate | block | False |
| Consul leaf certificates \| Read content of root ca certificate | ansible.builtin.slurp | False |
| Consul leaf certificates \| Read content of intermediate ca certificate | ansible.builtin.slurp | False |
| Consul leaf certificates \| Read content of leaf certificate | ansible.builtin.slurp | False |
| Consul leaf certificates \| Concatenate certificates | ansible.builtin.copy | False |

#### File: tasks/generate/generate_intermediate.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Intermediate CA \| Create temporary cert directory in {{ hashistack_ca_directory }}/intermediate | ansible.builtin.file | False |
| Intermediate CA \| Generate internal certificates | block | False |
| Intermediate CA \| Create intermediate CA private key | community.crypto.openssl_privatekey | False |
| Intermediate CA \| Create intermediate CA signing request | community.crypto.openssl_csr_pipe | False |
| Intermediate CA \| Create signed intermediate CA certificate from CSR | community.crypto.x509_certificate | False |

#### File: tasks/generate/generate_nomad.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad leaf certificates \| Create certificate directory in for nomad servers | ansible.builtin.file | False |
| Nomad leaf certificates \| Create Nomad certificates | block | False |
| Nomad leaf certificates \| Create Nomad certificate keys | community.crypto.openssl_privatekey | False |
| Nomad leaf certificates \| Create CSRs for Nomad servers | community.crypto.openssl_csr_pipe | False |
| Nomad leaf certificates \| Sign certificates with internal CA | community.crypto.x509_certificate | False |
| Nomad leaf certificates \| Generate fullchain certificate | block | False |
| Nomad leaf certificates \| Read content of root ca certificate | ansible.builtin.slurp | False |
| Nomad leaf certificates \| Read content of intermediate ca certificate | ansible.builtin.slurp | False |
| Nomad leaf certificates \| Read content of leaf certificate | ansible.builtin.slurp | False |
| Nomad leaf certificates \| Concatenate certificates | ansible.builtin.copy | False |

#### File: tasks/generate/generate_vault.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Vault leaf certificates \| Create certificate directory in for vault servers | ansible.builtin.file | False |
| Vault leaf certificates \| Create Vault certificates | block | False |
| Vault leaf certificates \| Create Vault certificate keys | community.crypto.openssl_privatekey | False |
| Vault leaf certificates \| Create CSRs for Vault servers | community.crypto.openssl_csr_pipe | False |
| Vault leaf certificates \| Sign certificates with internal CA | community.crypto.x509_certificate | False |
| Vault leaf certificates \| Generate fullchain certificate | block | False |
| Vault leaf certificates \| Read content of root ca certificate | ansible.builtin.slurp | False |
| Vault leaf certificates \| Read content of intermediate ca certificate | ansible.builtin.slurp | False |
| Vault leaf certificates \| Read content of leaf certificate | ansible.builtin.slurp | False |
| Vault leaf certificates \| Concatenate certificates | ansible.builtin.copy | False |

#### File: tasks/generate/generate_root.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Root CA \| Create temporary cert directory in {{ hashistack_ca_directory }} | ansible.builtin.file | False |
| Root CA \| Generate root Authority | block | False |
| Root CA \| Create CA private key | community.crypto.openssl_privatekey | False |
| Root CA \| Create CA signing request | community.crypto.openssl_csr_pipe | False |
| Root CA \| Create self-signed CA certificate from CSR | community.crypto.x509_certificate | False |
| Root CA \| Create self-signed CA certificate from CSR | community.crypto.x509_certificate | False |

#### File: tasks/renew/renew_root.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Root CA \| Check if root CA certificate exists | ansible.builtin.stat | False |
| Root CA \| Check CA for renewal | block | True |
| Root CA \| Get root CA certificate expiration date | community.crypto.x509_certificate_info | False |
| Root CA \| Check if root CA certificate is expiring within the threshold | ansible.builtin.set_fact | False |
| Root CA \| Renew CA if expiring soon | block | True |
| Root CA \| Create backup directory for root CA | ansible.builtin.file | False |
| Root CA \| Format expiration date for backup | ansible.builtin.set_fact | False |
| Root CA \| Rename existing root CA certificate | ansible.builtin.command | False |
| Root CA \| Remove existing root CA key | ansible.builtin.file | False |
| Root CA \| Generate new root CA if renaming was successful | ansible.builtin.include_tasks | False |
| Root CA \| Generate new intermediate CA | ansible.builtin.include_tasks | False |

#### File: tasks/renew/renew_consul.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Consul leaf certificates \| Check if certificate exists | ansible.builtin.stat | False |
| Consul leaf certificates \| Check if intermediate CA certificate exists | ansible.builtin.stat | False |
| Consul leaf certificates \| Check certificate for renewal | block | True |
| Consul leaf certificates \| Get certificate expiration date | community.crypto.x509_certificate_info | False |
| Intermediate CA \| Get intermediate CA certificate info | community.crypto.x509_certificate_info | False |
| Consul leaf certificates \| Check if certificate is expiring within the threshold | ansible.builtin.set_fact | False |
| Consul leaf certificates \| Check if intermediate CA has been renewed | ansible.builtin.set_fact | False |
| Consul leaf certificates \| Renew certificate if expiring soon or intermediate CA has been renewed | block | True |
| Consul leaf certificates \| Remove old certificate before renewal | ansible.builtin.file | False |
| Consul leaf certificates \| Remove old certificate key before renewal | ansible.builtin.file | False |
| Consul leaf certificates \| Generate new consul leaf certificate | ansible.builtin.include_tasks | False |

#### File: tasks/renew/renew_nomad.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad leaf certificates \| Check if certificate exists | ansible.builtin.stat | False |
| Nomad leaf certificates \| Check if intermediate CA certificate exists | ansible.builtin.stat | False |
| Nomad leaf certificates \| Check certificate for renewal | block | True |
| Nomad leaf certificates \| Get certificate expiration date | community.crypto.x509_certificate_info | False |
| Intermediate CA \| Get intermediate CA certificate info | community.crypto.x509_certificate_info | False |
| Nomad leaf certificates \| Check if certificate is expiring within the threshold | ansible.builtin.set_fact | False |
| Nomad leaf certificates \| Check if intermediate CA has been renewed | ansible.builtin.set_fact | False |
| Nomad leaf certificates \| Renew certificate if expiring soon or intermediate CA has been renewed | block | True |
| Nomad leaf certificates \| Remove old certificate before renewal | ansible.builtin.file | False |
| Nomad leaf certificates \| Remove old certificate key before renewal | ansible.builtin.file | False |
| Nomad leaf certificates \| Generate new nomad leaf certificate | ansible.builtin.include_tasks | False |

#### File: tasks/renew/renew_intermediate.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Intermediate CA \| Check if intermediate CA certificate exists | ansible.builtin.stat | False |
| Intermediate CA \| Check if root CA certificate exists | ansible.builtin.stat | False |
| Intermediate CA \| Check CA for renewal | block | True |
| Intermediate CA \| Get intermediate CA certificate expiration date | community.crypto.x509_certificate_info | False |
| Root CA \| Get root CA certificate info | community.crypto.x509_certificate_info | False |
| Intermediate CA \| Check if intermediate CA certificate is expiring within the threshold | ansible.builtin.set_fact | False |
| Intermediate CA \| Check if root CA has been renewed | ansible.builtin.set_fact | False |
| Intermediate CA \| Renew CA if expiring soon or root CA has been renewed | block | True |
| Intermediate CA \| Create backup directory for intermediate CA | ansible.builtin.file | False |
| Intermediate CA \| Format expiration date for backup | ansible.builtin.set_fact | False |
| Intermediate CA \| Backup existing intermediate CA certificate | ansible.builtin.command | False |
| Intermediate CA \| Backup existing intermediate CA key | ansible.builtin.command | False |
| Intermediate CA \| Generate new intermediate CA if backups were successful | ansible.builtin.include_tasks | False |
| Intermediate CA \| Generate new consul leaf certificates | ansible.builtin.include_tasks | False |
| Intermediate CA \| Generate new nomad leaf certificates | ansible.builtin.include_tasks | False |
| Intermediate CA \| Generate new vault leaf certificates | ansible.builtin.include_tasks | False |

#### File: tasks/renew/renew_vault.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Vault leaf certificates \| Check if certificate exists | ansible.builtin.stat | False |
| Vault leaf certificates \| Check if intermediate CA certificate exists | ansible.builtin.stat | False |
| Vault leaf certificates \| Check certificate for renewal | block | True |
| Vault leaf certificates \| Get certificate expiration date | community.crypto.x509_certificate_info | False |
| Intermediate CA \| Get intermediate CA certificate info | community.crypto.x509_certificate_info | False |
| Vault leaf certificates \| Check if certificate is expiring within the threshold | ansible.builtin.set_fact | False |
| Vault leaf certificates \| Check if intermediate CA has been renewed | ansible.builtin.set_fact | False |
| Vault leaf certificates \| Renew certificate if expiring soon or intermediate CA has been renewed | block | True |
| Vault leaf certificates \| Remove old certificate before renewal | ansible.builtin.file | False |
| Vault leaf certificates \| Remove old certificate key before renewal | ansible.builtin.file | False |
| Vault leaf certificates \| Generate new vault leaf certificate | ansible.builtin.include_tasks | False |








<!-- DOCSIBLE END -->

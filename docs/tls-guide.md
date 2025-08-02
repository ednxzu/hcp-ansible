# TLS Guide

## Quick Start Guide

This section covers the essential variables to get started quickly with managing a CA in Nomad, Consul, and Vault clusters using playbooks available in the collection.

### Required Variables (Quick Start)

Below are the core variables you need to configure to set up a basic CA:

```yaml
# Directory for storing generated certificates
hashistack_ca_directory: "{% raw %}{{ hashistack_sub_configuration_directories['certificates'] }}{% endraw %}"

# Whether to use the cryptography library (set to true if required; needs installation)
hashistack_ca_use_cryptography: false

# CA action(s) to perform, separated by commas
hashistack_ca_action: "noop"

# Domain name for the certificates
hashistack_ca_domain: example.com

# Owner of the certificate directory
hashistack_ca_directory_owner: "{% raw %}{{ lookup('env', 'USER') }}{% endraw %}"
```

- **`hashistack_ca_use_cryptography`**: When set to `true`, this uses the cryptography library for enhanced security operations. Ensure the library is installed before enabling.

- **`hashistack_ca_action`**: Defines the CA actions to perform, as a comma-separated list. Possible actions include:
    - `root_ca`: Creates the root Certificate Authority.
    - `int_ca`: Generates an intermediate CA.
    - `leaf_cert`: Issues client certificates (leaf certificates).
    - `renew_root`, `renew_int`, `renew_leaf`: Renews respective certificates (root, intermediate, and leaf).

### Running the Certificates Playbook

To use the role, create a playbook in the same collection or use the example provided below. Run the playbook with the following command, specifying the action(s) you need:

```bash
ansible-playbook -i inventory/inventory.ini ednz_cloud.hashistack.certificates.yml -e hashistack_ca_action="<your_action>"
```

!!! note
    For the initial setup of the PKI, set `hashistack_ca_action` to include all necessary generation flags (e.g., `root_ca,int_ca,leaf_cert`) to establish the full certificate chain.

## Customizing the Root Certificate Authority (CA)

The Root CA serves as the cornerstone of your PKI, issuing and validating subordinate certificates. Below are the configuration variables for customizing the Root CA’s properties, allowing you to specify organizational, location, and cryptographic settings for secure and trusted certificate generation.

### Root CA Configuration Variables

```yaml
# Organization name for the Root CA
hashistack_ca_root_org_name: EDNZ Cloud

# Country code for the Root CA (ISO 3166-1 alpha-2 format)
hashistack_ca_root_country: FR

# Locality (city) for the Root CA
hashistack_ca_root_locality: Paris

# Common Name for the Root CA
hashistack_ca_root_common_name: "{% raw %}{{ hashistack_ca_domain }} Root CA{% endraw %}"

# Email address for the Root CA (optional)
hashistack_ca_root_email:

# Key usage purposes for the Root CA (usually includes keyCertSign and cRLSign)
hashistack_ca_root_key_usage:
  - keyCertSign
  - cRLSign

# Mark the key usage extension as critical
hashistack_ca_root_key_usage_critical: true

# Basic constraints for the Root CA, marking it as a CA
hashistack_ca_root_basic_constraints:
  - CA:TRUE

# Mark the basic constraints extension as critical
hashistack_ca_root_basic_constraints_critical: true

# Optional fields
hashistack_ca_root_state_or_province_name: # State or province (if applicable)
hashistack_ca_root_email_address: # Contact email for Root CA

# Validity duration for the Root CA certificate
hashistack_ca_root_valid_for: 1825d

# Renewal threshold, after which the certificate can be renewed
hashistack_ca_root_renew_threshold: 180d
```

- **`hashistack_ca_root_org_name`**: Specifies the name of the organization issuing the Root CA. This appears in the certificate's Subject field.

- **`hashistack_ca_root_country`** and **`hashistack_ca_root_locality`**: Define the Root CA's location, essential for unique identification in the certificate. Use the two-letter country code (ISO 3166-1) for `country`.

- **`hashistack_ca_root_common_name`**: Common Name (CN) of the Root CA. Typically, this follows the format `<domain> Root CA`, as specified by `hashistack_ca_domain`.

- **`hashistack_ca_root_key_usage`**: Lists permissible uses for the Root CA’s private key. By default, it includes `keyCertSign` for signing subordinate certificates and `cRLSign` for Certificate Revocation Lists (CRLs).

- **`hashistack_ca_root_key_usage_critical`**: Marks the key usage extension as critical, indicating its importance to the Root CA’s purpose.

- **`hashistack_ca_root_basic_constraints`**: Defines constraints for the Root CA, specifically marking it as a CA with `CA:TRUE`.

- **`hashistack_ca_root_valid_for`**: Sets the validity period of the Root CA certificate (in days), here defined as `1825d` (5 years). After this period, the certificate will need to be renewed.

- **`hashistack_ca_root_renew_threshold`**: Specifies when renewal becomes allowable; set here to `180d` (180 days before expiration).

!!! tip
    It’s good practice to review the `valid_for` and `renew_threshold` values to align with your organization’s certificate lifecycle management policies.

## Customizing the Intermediate Certificate Authority (CA)

The Intermediate CA (or subordinate CA) issues certificates to clients and services, creating an additional layer of security between the root and end entities. Below are the variables for configuring the Intermediate CA to suit your environment and security needs.

### Intermediate CA Configuration Variables

```yaml
# Organizational details for the Intermediate CA
hashistack_ca_intermediate_org_name: EDNZ Cloud Intermediate
hashistack_ca_intermediate_country: FR
hashistack_ca_intermediate_locality: Paris
hashistack_ca_intermediate_common_name: "{% raw %}{{ hashistack_ca_domain }} Intermediate CA{% endraw %}"
hashistack_ca_intermediate_email:

# Key usage policies
hashistack_ca_intermediate_key_usage:
  - keyCertSign
  - cRLSign
hashistack_ca_intermediate_key_usage_critical: true

# Basic constraints
hashistack_ca_intermediate_basic_constraints:
  - CA:TRUE
  - pathlen:0
hashistack_ca_intermediate_basic_constraints_critical: true

# Optional fields
hashistack_ca_intermediate_state_or_province_name: # State or province (optional)
hashistack_ca_intermediate_email_address: # Contact email for the Intermediate CA (optional)

# Certificate validity and renewal
hashistack_ca_intermediate_valid_for: 365d
hashistack_ca_intermediate_renew_threshold: 90d

# Name constraints
hashistack_ca_intermediate_name_constraints_permitted:
  - "{% raw %}DNS:.{{ hashistack_ca_domain }}{% endraw %}"
  - DNS:.nomad
  - DNS:.consul
  - DNS:localhost
  - IP:192.168.0.0/16
  - IP:172.16.0.0/16
  - IP:10.0.0.0/8
  - IP:127.0.0.0/8
hashistack_ca_intermediate_name_constraints_critical: "{% raw %}{{ (hashistack_ca_intermediate_name_constraints_permitted is defined and hashistack_ca_intermediate_name_constraints_permitted | length > 0) }}{% endraw %}"
```

- **`hashistack_ca_intermediate_org_name`**: Specifies the organization responsible for the Intermediate CA, aligning it with your organization’s name.

- **`hashistack_ca_intermediate_country`** and **`hashistack_ca_intermediate_locality`**: Location details that help identify the Intermediate CA in the certificate’s Subject field.

- **`hashistack_ca_intermediate_common_name`**: Common Name (CN) for the Intermediate CA, typically including the root domain and identifying it as the Intermediate CA.

- **`hashistack_ca_intermediate_key_usage`**: Defines permitted uses of the Intermediate CA’s private key. Typically includes `keyCertSign` for signing certificates and `cRLSign` for CRLs.

- **`hashistack_ca_intermediate_basic_constraints`**: Specifies that this CA can issue certificates with the `CA:TRUE` setting. The `pathlen:0` restricts any further sub-CA issuance, ensuring it remains an end-issuing CA.

- **`hashistack_ca_intermediate_valid_for`**: Sets the validity period for the Intermediate CA certificate (in days). In this case, it's set for 1 year (`365d`), so periodic renewals will be necessary.

- **`hashistack_ca_intermediate_renew_threshold`**: Specifies when renewal can occur, here set to `90d` (90 days before expiration).

- **`hashistack_ca_intermediate_name_constraints_permitted`**: Restricts the Intermediate CA’s issuance to specified domains and IP ranges, preventing certificate creation for unlisted domains. Commonly used entries include:
    - `DNS:.{{ hashistack_ca_domain }}`, `DNS:.nomad`, `DNS:.consul`: These restrict issuance to specified DNS zones.
    - `IP` entries like `192.168.0.0/16`, `127.0.0.0/8`: These limit issuance to certain IP ranges.

- **`hashistack_ca_intermediate_name_constraints_critical`**: Marks name constraints as critical if they are defined, ensuring that only permitted domains and IP ranges are authorized for certificates.

## Customizing Leaf Certificates

Leaf certificates are end-entity certificates issued to clients or services (like Consul, Nomad, and Vault) by the Intermediate CA. These certificates secure service communication, ensuring that each entity can be authenticated. Below are the configuration variables for setting up leaf certificates.

### General Leaf Certificate Variables

```yaml
hashistack_ca_leaf_valid_for: 90d
hashistack_ca_leaf_renew_threshold: 30d
```

- **`hashistack_ca_leaf_valid_for`**: The lifespan of each leaf certificate. For high-security environments, a shorter validity period, such as `90d`, is recommended.

- **`hashistack_ca_leaf_renew_threshold`**: The renewal threshold for each certificate, here set to `30d`, allowing certificates to renew a month before expiration.

---

### Consul Leaf Certificate Configuration

The following variables define Consul-specific certificate attributes, including SANs to identify the Consul nodes by DNS and IP addresses.

```yaml
hashistack_ca_consul_org_name: "{% raw %}{{ hashistack_ca_root_org_name }}{% endraw %}"
hashistack_ca_consul_common_name: "{% raw %}{{ inventory_hostname }}{% endraw %}"
hashistack_ca_consul_csr_sans:
  - "{% raw %}DNS:{{ inventory_hostname }}{% endraw %}"
  - "DNS:consul.service.consul"
  - "DNS:localhost"
  - "{% raw %}IP:{{ api_interface_address }}{% endraw %}"
  - "IP:127.0.0.1"
  - "{% raw %}{{ 'DNS:server.' ~ consul_datacenter ~ '.' ~ consul_domain if consul_enable_server else omit }}{% endraw %}"

```

- **`hashistack_ca_consul_org_name`**: Organization name for the Consul certificate, often aligning with the Root CA organization.

- **`hashistack_ca_consul_common_name`**: Sets the Common Name for the Consul certificate, typically the node’s hostname.

- **`hashistack_ca_consul_csr_sans`**: Generates SANs based on the inventory, enabling access to Consul by both DNS and IP. Common SANs include:
    - The hostname (`inventory_hostname`)
    - Consul service discovery (`consul.service.consul`)
    - Localhost (`127.0.0.1`)
    - `consul_enable_server`: Adds `server.<datacenter>.<domain>` to SANs if the server mode is enabled.

---

### Nomad Leaf Certificate Configuration

These variables configure Nomad-specific certificate attributes, including SANs that cover both server and client modes.

```yaml
hashistack_ca_nomad_org_name: "{% raw %}{{ hashistack_ca_root_org_name }}{% endraw %}"
hashistack_ca_nomad_common_name: "{% raw %}{{ inventory_hostname }}{% endraw %}"
hashistack_ca_nomad_csr_sans:
  - "{% raw %}DNS:{{ inventory_hostname }}{% endraw %}"
  - "DNS:localhost"
  - "{% raw %}IP:{{ api_interface_address }}{% endraw %}"
  - "IP:127.0.0.1"
  - "{% raw %}{{ 'DNS:server.' ~ nomad_region ~ '.nomad' if nomad_enable_server else omit }}{% endraw %}"
  - "{% raw %}{{ 'DNS:nomad.service.consul' if (nomad_enable_server and enable_consul) else omit }}{% endraw %}"

```

- **`hashistack_ca_nomad_org_name`**: Organization name for Nomad, usually the same as the Root CA.

- **`hashistack_ca_nomad_common_name`**: Sets the Common Name for the Nomad certificate, typically the node’s hostname.

- **`hashistack_ca_nomad_csr_sans`**: Generates SANs, enabling Nomad nodes to be identified via DNS and IP. Includes:
  - Hostname and localhost SANs
  - `nomad_enable_server`: Adds `server.<region>.nomad` SAN for server mode.
  - `enable_consul`: Adds `nomad.service.consul` if Consul is enabled with Nomad.
  - `nomad_enable_client`: Adds `client.<region>.nomad` SAN for client mode.

---

### Vault Leaf Certificate Configuration

These variables configure Vault-specific certificate attributes, including SANs needed for Vault service communication within Consul.

```yaml
hashistack_ca_vault_org_name: "{% raw %}{{ hashistack_ca_root_org_name }}{% endraw %}"
hashistack_ca_vault_common_name: "{% raw %}{{ inventory_hostname }}{% endraw %}"
hashistack_ca_vault_csr_sans:
  - "{% raw %}DNS:{{ inventory_hostname }}{% endraw %}"
  - "{% raw %}{{ 'DNS:active.vault.service.consul' if enable_consul else omit }}{% endraw %}"
  - "{% raw %}{{ 'DNS:standby.vault.service.consul' if enable_consul else omit }}{% endraw %}"
  - "{% raw %}{{ 'DNS:vault.service.consul' if enable_consul else omit }}{% endraw %}"
  - "DNS:localhost"
  - "{% raw %}IP:{{ api_interface_address }}{% endraw %}"
  - "IP:127.0.0.1"
```

- **`hashistack_ca_vault_org_name`**: Organization name for Vault, typically the same as the Root CA.

- **`hashistack_ca_vault_common_name`**: Common Name for Vault certificates, generally the hostname of the Vault node.

- **`hashistack_ca_vault_csr_sans`**: Lists SANs for Vault, allowing connections by DNS and IP, including:
    - The hostname
    - Vault service discovery SANs (`vault.service.consul`, `active.vault.service.consul`, and `standby.vault.service.consul`)
    - Localhost (`127.0.0.1`)

!!! note
    Carefully consider SANs to ensure each service certificate allows appropriate access points for secure, service-specific communication.

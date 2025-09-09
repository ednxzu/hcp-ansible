## v0.13.1 (2025-09-09)

### Fix

- **ca**: include the correct root CA certificate file in leaf certificate

## v0.13.0 (2025-09-09)

### Feat

- add ensure_domain filter plugin

### Fix

- **globals/ca**: ensure certificates are generated for proper names

## v0.12.1 (2025-09-08)

### Fix

- **globals/nomad**: add server_join block when consul is disabled

## v0.12.0 (2025-08-22)

### Feat

- **playbook/bootstrap**: make setting timezone optional
- **playbooks/nomad**: adjust templating to comply with ansible 2.19
- **roles/nomad**: adjust templating to comply with ansible 2.19
- **playbooks/vault**: adjust deploy playbook for vault to conform with ansible 2.19 requirements
- **roles/vault**: adjust templating to conform to ansible 2.19
- **consul**: simplify templating and type conversions
- **roles/consul**: improve templating to be compatible with ansible 2.19
- **roles/consul**: avoid overriding permissions on recursive copy task

### Fix

- **playbook/preflight**: skip /etc/timezone check as it is getting phased out
- **playbook/bootstrap**: fix missconfiguration in setting up /etc/localtime
- **roles/consul**: crrect template syntax for merge join list to avoid deprecation warning
- **roles/vault**: some templating tweaks for generating certificate watchlist

## v0.11.1 (2025-07-13)

### Fix

- **roles/hashistack**: do not manually load playbook group_vars to prevent user variables override

## v0.11.0 (2025-07-12)

### Feat

- add molecule tests for full cluster deployment
- **roles/vault**: add openstack e2e tests instead of docker based tests
- **roles/nomad**: add openstack e2e tests instead of docker based tests
- **roles/consul**: add openstack e2e tests instead of docker based tests
- **roles/cni**: add molecule testing scenarios
- adjust dependencies to new ednz_cloud.utils collection

### Fix

- **roles/cni**: set correct permissions on cni version file and only consul-cni and necessary

## v0.10.1 (2025-03-12)

### Fix

- **roles/vault**: set vault log_level correctly according to variable
- change variable for pip install role to break system packages following upstream change

## v0.10.0 (2024-11-13)

### Feat

- add automatic reload of vault service for certificate reloading
- enable certificate renewal for nomad and vault in hashistack_ca
- add automatic reload of nomad service for certificate reloading
- add automatic reload of consul service for certificate reloading

### Fix

- allow override of the hashistack_ca_action via extra-vars flag
- only reload consul if the service is set to be started

## v0.9.0 (2024-10-30)

### Feat

- **group_vars/cni**: allow overrides of the cni values like any other role
- simplify hashistack_ca default SANs for nomad and consul

### Fix

- **group_vars/hashistack_ca**: update default owner for pkito avoid permission issues
- rename default inventory file, delete old assets
- **playbooks**: update execution scope of playbooks
- **roles/vault**: do not merge TLS certificateextra files if tls is not enabled

## v0.8.2 (2024-10-06)

### Fix

- remove mentions of haproxy_servers, as the feature is deprecated

## v0.8.1 (2024-09-16)

### Fix

- set default vault_enable_tls variable to follow global internal tls value

## v0.8.0 (2024-09-16)

### Feat

- add default variables files for nomad and vault
- add override options for all consul variables
- use override variables in globals.yml
- add ovveride options for vault variables
- add ovveride options for nomad variables
- add version documentation to nomad_acl_bootstrap module

## v0.7.0 (2024-09-02)

### Feat

- **vault**: enable rolling restart with no full seal

## v0.6.2 (2024-09-01)

### Fix

- allow break system package for pip install on ubuntu 24+, and do not try to install python-consul on bootstrap

## v0.6.1 (2024-08-29)

### Fix

- do not package actions and assets into build

## v0.6.0 (2024-08-29)

### Feat

- redirect to wiki and add assets
- rename playbooks for certificates and credentials
- initial cool readme
- add some templating for nomad haproxy job
- new tls_multi_node test for molecule with some adjustment to tags

### Fix

- remove duplicate tags for nomad tasks

## v0.5.0 (2024-08-17)

### Feat

- add global internal TLS option, make externally_managed_certs work
- playbooks revamp
- organise group_vars
- add renewal process for leaf CA
- add leaf certificate genearation
- **tests**: add molecule scenario for testing CA
- **roles**: add hashistack_ca role to manage clusters certificates
- **playbooks**: use newly created hashistack role to load and merge variables
- **hashistack**: move variable loading to specific role
- **nomad**: remove cni installation option from nomad role, as it has been moved to its own role
- **cni**: add specialized role ton install cni plugins
- **vault**: adjust variable merging behaviour for allowing multiple tcp and unix socket listeners
- **vault**: adjust default values for allowing multiple tcp and unix socket listeners
- **roles**: integrate nomad role to hashistack collection
- **roles**: integrate consul role to hashistack collection
- **roles**: integrate vault role to hashistack collection
- **deployment**: Implement new structure for deploying components

### Fix

- remove failure message as variable is undefined if directory does not exist
- empty tests for cni role for now
- renew should cascade
- use new hashistack role on preflight playbook
- add meta file for cni role
- **nomad**: adjust variable merging for nomad
- **consul**: merge join configuration variable
- add standalone consul_agents gorup, and add nomad_clients to the common group
- force load all variables in group_vars uring the variable loading process to make them top priority over every role variables
- update various variables and bring some of them back out of globals.yml
- update preflight checks
- do not try to install docker during bootstrap, as it will depend on which hosts are docker-enabled
- add conventional tags to galaxy.yml file
- consul_primary_datacenter defaults to consul_datacenter for ease of configuration in single cluster mode, remove some useless comments
- generate proper 32 bytes base 64 random strings for gossip encryption for both nomad and consul
- more deployment host exclusion
- exclude deployment host from all playbooks where it does not need to be included (and can cause issues)
- do not use run_once instructions as it is wildly unreliable
- typo in credentials template preventing from generating the initial credential file

## v0.4.0 (2024-07-10)

### Feat

- add barebone driver options for nomad (not fully working)
- add docs on generating credentials
- **nomad**: move variables to globals.yml, adjust bootstrap module for nomad ACLs
- add nomad deployment options, variables, and playbooks
- use new vault and consul roles, and only allow for host deployment after docker support drop
- add global variables for nomad deployment

### Fix

- implement longer wait to stabilize consul cluster before bootstrapping to avoid timeout errors

## v0.3.0 (2024-05-13)

### Feat

- **generate_credentials**: generate new accesor ids and vault token credentials
- **vault**: enable consul service registration automatically if consul is also enabled

## v0.2.0 (2024-05-05)

### Feat

- **consul**: allow enabling consul internal TLS

### Fix

- **globals**: restore default globals.yml file, move changes to test directory
- **vault/consul**: ensure idempotence of extra_volumes list to avoid restarting on each run due to slightly different service files

## v0.1.0 (2024-05-03)

### Feat

- add new way of loading vars following move to misc task group
- **consul**: utilize the new pre-generated credentials on consul deployment
- update vault deployment to utilize the new variable loading solution
- split load_vars play into multiple specific plays
- generate credentials.yml from template
- add playbook to generate credentials before deploying
- **TLS**: add tls features to vault and trust hosts store on containers
- **certs**: generate_certs playbook now generate internal CA for vault
- **haproxy**: add a lot to haproxy, and generate_certs playbook + docs
- **proxy**: add consul agents to proxies and register haproxy service to consul is consul is enabled
- **consul**: start configuring and deploying agents
- **deploy**: add haproxy deployment, integrate with consul
- **consul**: polish initial deployment of consul, and agent token generation
- **consul**: start creation of agents token, merge it with primary config if already present
- **inventory**: add haproxy nodes to test and inventory
- **core**: change namespace of collection
- **docs**: start writing the architecture guide
- **vault**: wrote some more documentation on using the tool
- **consul**: first working version of acl_bootstrap module
- **consul**: start on consul_acl_bootstrap module
- **consul**: make ACL default to enabled with default policy to deny
- **vault**: added version variables for vault
- **consul**: add initial simple consul cluster
- **vault**: break things trying to fix vault unseal not returning anything on mulitple retries
- **docs**: add docstrings to vault_init module and typos in documentation pages
- **license**: add license to galaxy.yml
- **vars**: add logging configuration for vault
- **vault/docs/license**: added plugin ability to vault, update documentation and license
- **vault**: start working on configuration merging to allow customization
- **vault**: variabilize seal_configuration
- **docs**: add collection install documentation to quick-start
- **docs**: started working on documentation for the collection
- **preflight**: fix config directory checks
- **preflight**: add checks to ensure config directories are present before running
- **vars**: variable loading now mostly works for groups and hosts
- **vars**: add host specific vars inclusion
- **vars**: load group vars dynamically if files exist
- **vars**: add check to load global vars file before running deployment
- **variables**: fix listener not passing correct syntax
- **vars**: add more customization for vault deployment
- **readme**: add WIP warning
- **variables**: start polishing variables for customization
- **playbook**: vault deployment is smooth-ish, unseals and initialize cluster as needed
- **modules**: added unseal module
- **tests**: move molecule tests to extensions directory for it to work properly
- **module**: vault operator init module somewhat working
- **module**: some more on vault init
- **modules**: try catch on import
- **module**: try catch on importing hvac
- **test**: add single node molecule scenario for testing modules
- **vault**: fix , in unseal module
- **vault**: start of unseal module, and start of default variables
- **preflight**: consolidate preflight playbook
- **roles**: add hashicorp roles as submodules
- **roles**: remove roles before adding submodules
- **variables**: add some formatting to globals.yml, remove unused roles
- **tests**: test playbboks are played correctly on molecule scenarios
- **tests**: draft for molecule collection testing
- commit collection skeleton

### Fix

- adjust galaxy version for commitizen
- vault extra files list not being idempotent between runs
- various fixes to accomodate the new pre-generated credentials
- **tests**: update converge and prepare playbook for test suite
- various small issues on generate playbooks
- various inconsistencies and idempotence issues related to variable computing
- **syntax**: typo in docs

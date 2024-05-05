## 0.2.0 (2024-05-05)

### Feat

- **consul**: allow enabling consul internal TLS

### Fix

- **globals**: restore default globals.yml file, move changes to test directory
- **vault/consul**: ensure idempotence of extra_volumes list to avoid restarting on each run due to slightly different service files

## 0.1.0 (2024-05-03)

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

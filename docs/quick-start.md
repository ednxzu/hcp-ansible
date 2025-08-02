# Quick Start Guide

Welcome to the **Hashistack-Ansible** Quick Start Guide! This guide will help you get your environment ready to deploy HashiCorp product clusters (Nomad, Consul, Vault) with ease.

## Prerequisites

### Recommended Readings
Before diving in, it’s helpful to familiarize yourself with the basics of:

- [Ansible](https://docs.ansible.com/)
- [Nomad](https://developer.hashicorp.com/nomad/docs)
- [Consul](https://developer.hashicorp.com/consul/docs)
- [Vault](https://developer.hashicorp.com/vault/docs)

### Supported Operating Systems
We officially support the following operating systems:

- **Debian**
    - 11 (Bullseye)
    - 12 (Bookworm)
- **Ubuntu**
    - 20.04 (Focal)
    - 22.04 (Jammy)
    - 24.04 (Noble)

!!! note
    Other Debian-based distributions might work, but they are **not tested** and may break with updates.

### Target Hosts

Target hosts are the machines where you’ll be deploying your clusters. They should meet the following minimum requirements:

**Must-Haves**:

- **SSH Access:** Ensure target hosts are reachable via SSH by the deployment node (the machine running the Ansible playbooks). The user must have privilege escalation (e.g., sudo).
- **Network Communication:** Hosts must communicate with each other based on your cluster topology (e.g., Vault hosts must all reach each other).
- **Time Sync:** Hosts should be synced to a common time source.
- **Low Latency:** Ensure less than 10ms of latency between hosts (crucial for the Raft consensus algorithm).
- **Systemd:** Hosts must use systemd as their init system.

**Recommendations**:

- **Two Network Interfaces:**
  - One public-facing for client-to-server traffic.
  - One private for server-to-server and deployment-to-server communications.
- **Memory:** At least 8GB of RAM (more for larger scale setups).
- **Disk Space:** Minimum of 40GB of free disk space.

## Preparing the Deployment Host

Follow these steps to prepare your deployment host:

### 1. Install Dependencies
Start by installing the necessary packages:

```shell
sudo apt update
sudo apt install git python3-dev libffi-dev gcc libssl-dev python3-venv
```

### 2. Set Up a Python Virtual Environment
Create and activate a Python virtual environment to isolate your setup:

```shell
python3 -m venv /path/to/venv
source /path/to/venv/bin/activate
```

### 3. Ensure Latest Version of pip
Update pip to the latest version:

```shell
pip install -U pip
```

### 4. Install Ansible
HCP-Ansible requires at least Ansible **7** (or ansible-core **2.15**):

```shell
pip install 'ansible>=7'
```

### 5. Create Directory Structure
Organize your project with the following structure (optional but recommended):

```shell
mkdir -p etc/hashistack collections inventory roles
touch ansible.cfg
```

Your directory should look like this:

```shell
.
├── ansible.cfg
├── collections
├── etc
│   └── hashistack
├── inventory
└── roles
```

### 6. Configure Ansible
Edit your `ansible.cfg` file to include the minimum required settings:

```ini
[defaults]
roles_path = ./roles/
collections_path = ./collections/
inventory  = ./inventory/
```

### 7. Install the HCP-Ansible Collection
Install the `ednz_cloud.hashistack` collection:

```shell
ansible-galaxy collection install git+https://github.com/ednxzu/hcp-ansible.git,tags/<version>
```

This will create a directory under `./collections/ansible_collections/ednz_cloud/hashistack`.

Alternatively, you can create a `requirements.yml` file, following the [Ansible documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file). This would look something like:

```yaml
---
collections:
  - name: https://github.com/ednxzu/hcp-ansible.git
    type: git
    version: v0.9.0
```

### 8. Install Additional Dependencies
Some roles aren’t packaged with the collection, so you’ll need to install them:

```shell
ansible-galaxy install -r ./collections/ansible_collections/ednz_cloud/hashistack/roles/requirements.yml
```

These roles will be installed inside `./roles/`.

### 9. Set Up Inventory and Configuration Files
Copy the sample inventory and global configuration files to your local environment:

```shell
cp ./collections/ansible_collections/ednz_cloud/hashistack/playbooks/inventory/inventory.ini inventory/
cp ./collections/ansible_collections/ednz_cloud/hashistack/playbooks/group_vars/all/globals.yml etc/hashistack/globals.yml
```

## Generate Credentials

Before deploying your infrastructure, you need to generate credentials for cluster bootstrapping:

```shell
ansible-playbook -i inventory/inventory.ini ednz_cloud.hashistack.credentials.yml
```

This will create and populate `etc/hashistack/secrets/credentials.yml`.

!!! warning
    This file contains root tokens and other sensitive credentials for Consul and Nomad clusters. **Handle it with care**!

Vault credentials will be generated during the Vault cluster bootstrap process and stored in `etc/hashistack/secrets/vault.yml`.

!!! note
    Encrypt these sensitive files before committing them to source control using [ansible-vault](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html) or [sops](https://github.com/getsops/sops).

## Running Preflight Checks and Bootstrap Playbooks

To ensure everything is correctly set up, run the `bootstrap` and `preflight` playbooks:

```shell
ansible-playbook -i inventory/inventory.ini ednz_cloud.hashistack.bootstrap.yml
ansible-playbook -i inventory/inventory.ini ednz_cloud.hashistack.preflight.yml
```

These playbooks will perform checks and installations to prepare your target hosts and deployment environment.

## Deploying and Updating Clusters

### Initial Deployment

This collection uses a single playbook to deploy, manage and update the different clusters.

To run:

```shell
ansible-playbook -i inventory/inventory.ini ednz_cloud.hashistack.deploy.yml
```

This will perform a full deployment, and is what should be run on the initial deployment.

### Day Two Operations and Management

The deployment playbook includes all the necessary logic in order to allow you to manage separate parts of your deployment independently. You can target the different components using tags.

There are **global** tags, that let you manage all nodes for a specific component:

- `nomad`
- `consul`
- `vault`

But you can choose to be even more granular than this, and use group-specific tags, to only update part of a component.

The available group tags are:

- `nomad_servers`
- `nomad_clients`
- `consul_servers`
- `consul_agents`
- `vault_servers`

For example, you can update only the servers in your nomad deployment, by running:

```shell
ansible-playbook -i inventory/inventory.ini ednz_cloud.hashistack.deploy.yml --tags nomad_servers
```

Or you can choose to update all the nomad nodes with:

```shell
ansible-playbook -i inventory/inventory.ini ednz_cloud.hashistack.deploy.yml --tags nomad
```

You can also run deployment on multiple groups, by using multiple tags:

```shell
ansible-playbook -i inventory/inventory.ini ednz_cloud.hashistack.deploy.yml --tags nomad,consul_agents,vault_servers
```

---

You're now all set to deploy your HashiStack clusters! 🎉

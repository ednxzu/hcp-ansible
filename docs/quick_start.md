# Quick Start Guide

This documentation will show you the preparation steps necessary to ensure that you environment is ready to deploy cluster(s).

## Prerequisites

### Recommended readings

It’s beneficial to learn basics of both [Ansible](https://docs.ansible.com/) and [Docker](https://docs.docker.com/)(for docker deployments) before running Hashistack Ansible.

### Operating

The only supported operating systems currently are:
- Debian
  - 11, Bullseye
  - 12, Bookworm
- Ubuntu
  - 20.04, Focal
  - 22.04, Jammy

Other Debian-based distributions might work, but **are not tested**, and may break at any given update.

### Target Hosts

Target hosts are the hosts you are planning on deploying cluster(s) to.

These hosts must satisfy the following minimum requirements:
- Be reachable via ssh by the deployment node (the machine running the ansible playbooks), with a user that has the ability to escalate privileges.
- Be able to comunicate with each other, according to your cluster topology (vault hosts must all be able to reach each other, etc...)
- Be synced to a common time
- Have less than 10ms of latency to reach each other (raft consensus algorithm requirement)
- Be using systemd as their init system.

Ideally, hosts are recommended to satisfy the following recommendations:
- Have 2 network interfaces:
  - One that is public facing for client-to-server traffic
  - One that is not public facing for server-to-server and deployment-to-server communications
- Have a minimum of 8GB of memory (less will work, but the larger the scale, the higher the RAM requirements will be)
- Have a minimum of 40GB of free disk space

## Prepare the deployment host

1. Install the virtual environment dependencies.

```bash
sudo apt update
sudo apt install git python3-dev libffi-dev gcc libssl-dev python3-venv
```

2. Create a python virtual environment and activate it.

```bash
python3 -m venv /path/to/venv
source /path/to/venv/bin/activate
```

3. Ensure the latest version of pip is installed

```bash
pip install -U pip
```

4. Install [Ansible](http://www.ansible.com/). Hashistack Ansible requires at least Ansible **7**(or ansible-core **2.15**)

```bash
pip install 'ansible-core>=2.15'
```

5. Create the directory structure. This is not required but **heavily** recommended.

```bash
mkdir -p etc/hashistack collections inventory roles
touch ansible.cfg
```

Your directory structure should look like this

```bash
.
├── ansible.cfg
├── collections
├── etc
│   └── hashistack
├── inventory
└── roles
```

6. Edit the `ansible.cfg` file with the minimum requirements.

```bash
[defaults]
roles_path = ./roles/
collections_path = ./collections/
inventory  = ./inventory/
```

7. Install the `ednxzu.hashistack` ansible collection

```bash
ansible-galaxy collection install ednxzu.hashistack:==<version>
```

You should now have a directory under `./collections/ansible_collections/ednxzu/hashistack`

8. Install the other dependencies required by `ednxzu.hashistack`

```bash
ansible-galaxy install -r ./collections/ansible_collections/ednxzu/hashistack/roles/requirements.yml
```

This will install roles that are not packaged with the collection, but are still required in order to run the playbooks.

You should now have some roles inside `./roles/`.

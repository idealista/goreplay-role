![Logo](logo.gif)

# GOR Ansible role

This ansible role installs and configure go replay.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install the [go replay](https://goreplay.org/) utility as a service in your Debian system.

### Prerequisities

Ansible 2.2.0.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: http://github.com/idealista-tech/gor-role.git
  scm: git
  version: 0.0.3
  name: gor
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - { role: gor,
        gor_input: '--input-raw :80',
        gor_output: ''--output-http=http://test01:80',
        gor_service_enabled: yes
      }
```

## Usage

To enable gor and replicate traffic on another host

```
gor_input: --input-raw :80
gor_output: --output-http=http://test01:80
gor_service_enabled: yes
```

To save it to a file

```
gor_input: --input-raw :80
gor_output: "--output-file={{ gor_output_dir }}/requests.gor"
gor_service_enabled: yes
```

!Stop gor to retrieve the file, otherwise you could lost last requests https://github.com/buger/gor/wiki/Saving-and-Replaying-from-file#buffered-file-output

```
gor_service_state: stopped
```

Or stop the service manually

```
ssh user@host
sudo service gor stop
```

Or start the service with a low flush interval

```
gor_input: --input-raw :80
gor_output: "--output-file={{ gor_output_dir }}/requests.gor"
gor_service_enabled: yes
gor_options:
  - output-file-flush-interval 0m1s
```

## Testing

```
molecule test
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.0.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista-tech/gor-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista-tech](https://github.com/idealista-tech)

See also the list of [contributors](https://github.com/idealista-tech/gor-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](http://img.shields.io/badge/license-Apache-2.0-blue.svg?style=flat-square)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Acknowledgments

* Leonid Bugaev, @buger, https://leonsbox.com - For such an excellent tool ;)

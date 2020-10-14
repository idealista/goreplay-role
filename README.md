![Logo](logo.gif)

[![CircleCI](https://circleci.com/gh/idealista/gor-role.svg?style=svg)](https://circleci.com/gh/idealista/gor-role)

# GoReplay Ansible role

This ansible role installs and configure GoReplay.

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

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install the [GoReplay](https://goreplay.org/) utility as a service in your Debian system.

### Prerequisities

Ansible 2.9.x version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.goreplay_role
  version: 1.0.0
  name: goreplay
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
    - { role: goreplay,
        goreplay_input: '--input-raw :80',
        goreplay_output: '--output-http=http://test01:80',
        goreplay_service_enabled: yes
      }
```

## Usage

To enable GoReplay and replicate traffic on another host

```
goreplay_input: --input-raw :80
goreplay_output: --output-http=http://test01:80
goreplay_service_enabled: yes
```

To save it to a file

```
goreplay_input: --input-raw :80
goreplay_output: "--output-file={{ goreplay_output_dir }}/requests.gor"
goreplay_service_enabled: yes
```

!Stop GoReplay to retrieve the file, otherwise you could lost last requests https://github.com/buger/gor/wiki/Saving-and-Replaying-from-file#buffered-file-output

```
goreplay_service_state: stopped
```

Or stop the service manually

```
ssh user@host
sudo service goreplay stop
```

Or start the service with a low flush interval

```
goreplay_input: --input-raw :80
goreplay_output: "--output-file={{ goreplay_output_dir }}/requests.gor"
goreplay_service_enabled: yes
goreplay_options:
  - output-file-flush-interval 0m1s
```

## Testing

```
molecule test
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.4.0.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/gor-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/gor-role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Acknowledgments

* Leonid Bugaev, @buger, https://leonsbox.com - for such an excellent tool ;)

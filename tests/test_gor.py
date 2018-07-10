import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def Hostname(TestinfraBackend):
    return TestinfraBackend.get_hostname()


def test_gor_template_user(User, Group, AnsibleDefaults):
    assert Group(AnsibleDefaults["goreplay_group"]).exists
    assert User(AnsibleDefaults["goreplay_user"]).exists
    assert User(AnsibleDefaults["goreplay_user"]).group == AnsibleDefaults["goreplay_group"]


def test_gor_binary(File, AnsibleDefaults):
    gor = File(AnsibleDefaults["goreplay_bin_dir"] + "/goreplay")
    assert gor.user == AnsibleDefaults["goreplay_user"]
    assert gor.group == AnsibleDefaults["goreplay_group"]
    assert File("/usr/bin/goreplay").exists
    assert File("/usr/bin/goreplay").is_symlink
    assert File("/usr/bin/goreplay").linked_to == AnsibleDefaults["goreplay_root_dir"] + "/bin/goreplay"


def test_gor_service(File, Service, Socket, Interface, Hostname):
    assert File("/etc/systemd/system/goreplay.service").exists
    assert not Service("goreplay").is_enabled
    assert Service("goreplay").is_running

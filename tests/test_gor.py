import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def Hostname(TestinfraBackend):
    return TestinfraBackend.get_hostname()


def test_gor_template_user(User, Group, AnsibleDefaults):
    assert Group(AnsibleDefaults["gor_group"]).exists
    assert User(AnsibleDefaults["gor_user"]).exists
    assert User(AnsibleDefaults["gor_user"]).group == AnsibleDefaults["gor_group"]


def test_gor_binary(File, AnsibleDefaults):
    gor = File(AnsibleDefaults["gor_bin_dir"] + "/goreplay")
    assert gor.user == AnsibleDefaults["gor_user"]
    assert gor.group == AnsibleDefaults["gor_group"]
    assert File("/usr/bin/gor").exists
    assert File("/usr/bin/gor").is_symlink
    assert File("/usr/bin/gor").linked_to == AnsibleDefaults["gor_root_dir"] + "/bin/goreplay"


def test_gor_service(File, Service, Socket, Interface, Hostname):
    assert File("/etc/systemd/system/gor.service").exists
    assert not Service("gor").is_enabled
    assert Service("gor").is_running


def test_gor_functionality(File, Sudo, Hostname):
    requests = File("/opt/gor/out/requests_0.gor")
    if Hostname in ("prod02.vm"):
        assert requests.exists
        with Sudo("gor"):
            assert requests.contains("ansible-httpget")
    else:
        assert not requests.exists

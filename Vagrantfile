# Ansible example
Vagrant.configure("2") do |config|
  config.vm.define "host1"
  config.vm.box = "ubuntu/bionic64"

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "playbook.yml"
  end
end

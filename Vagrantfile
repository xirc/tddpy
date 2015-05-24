# -*- mode: ruby -*-
# vi: set ft=ruby :

# load .env
Dotenv.load

# change default provider to digital_ocean
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'digital_ocean'

VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider :digital_ocean do |provider, override|
    override.vm.hostname          = 'tddpy'
    override.vm.box               = 'digital_ocean'
    override.vm.box_url           = 'https://github.com/smdahlen/vagrant-digitalocean/raw/master/box/digital_ocean.box'

    override.ssh.pty              = true
    override.ssh.username         = ENV['DO_SSH_USERNAME']
    override.ssh.private_key_path = ENV['DO_SSH_KEY']

    provider.ssh_key_name         = ENV['DO_SSH_KEY_NAME']
    provider.token                = ENV['DO_TOKEN']
    provider.image                = 'fedora-20-x64'
    provider.region               = 'sgp1'
    provider.size                 = '512mb'
    provider.ipv6                 = false
    provider.private_networking   = false
    provider.backups_enabled      = false   # WARN: This option charges you extra cost.
    provider.setup                = true

    # disable synced_folder
    override.vm.synced_folder "./", "/vagrant", disabled: true
  end

  config.vm.provision :fabric do |fabric|
    fabric.fabfile_path = "./deploy/provision.py"
    fabric.tasks = ["provision"]
  end

  config.vm.provision :fabric do |fabric|
    fabric.fabfile_path  = "./deploy/deploy.py"
    fabric.tasks = ["deploy"]
  end

end

# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "bento/ubuntu-18.04"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "webcam_test", "/home/vagrant/webcam_test"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    vb.name = "webcam_test"
  #   # Display the VirtualBox GUI when booting the machine
    #vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
    vb.memory = "8192"
    vb.cpus = 4

    vb.customize [
      "modifyvm", :id,
      "--cpuexecutioncap", "80",
      "--vram", "256",
      "--accelerate3d", "on",
      "--clipboard", "bidirectional",
      "--hwvirtex", "on",
      "--nestedpaging", "on",
      "--largepages", "on",
      "--ioapic", "on",
      "--pae", "on",
      "--paravirtprovider", "kvm",
      "--natdnshostresolver1", "on",
      "--usb", "on",
      "--usbehci", "on",
    ]
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  config.vm.provision "docker"
  config.vm.provision "docker_compose"

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    sudo timedatectl set-timezone Asia/Tokyo
    sudo sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list
    sudo apt update
    sudo apt -y upgrade
    #sudo apt -y install xserver-xorg-video-dummy xvfb
    sudo usermod -aG video vagrant
    curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    echo "export DISPLAY=192.168.33.1:0.0" >> /home/vagrant/.bashrc
  SHELL

  config.ssh.forward_x11 = true

  config.trigger.after [:up, :reload]  do |trigger|
    if File.file?(File.expand_path(".vagrant/machines/default/virtualbox/id"))
      id = File.read(".vagrant\\machines\\default\\virtualbox\\id")
      trigger.info = "Mount webcam to #{id}"
      trigger.run = {
        inline: "VBoxManage controlvm #{id} webcam attach .1",
      }
    end
  end

end

Vagrant.configure("2") do |config|

  config.vm.box = "airduino"
  config.vm.box_url = "dev/airduino.box"

  config.ssh.forward_x11 = true

  config.vm.hostname = "airduino"
  config.vm.provider :virtualbox do |virtualbox|
    virtualbox.name = "airduino"
    # virtualbox.gui = true
  end

  config.vm.network :forwarded_port, guest: 3000, host: 3000
end

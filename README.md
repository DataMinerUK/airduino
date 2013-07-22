Airduino
========

An Arduino based rotating model airplane which runs according to a given flight
path. The user sends an SMS with the flight number to a web service. This then
watches for flight take off and sends an SMS to the Airduino to drive the motor.
When the plane lands the motor is switched off. Thus the owner of the Airduino
can monitor when his/her relative are in the air.


Developing: Google AppEngine
----------------------------
Airduino is a Google AppEngine Python application so you will need the SDK from
[here](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python).

When you have made your changes, update the version number in `app.yaml` so
that you can roll back in the AppEngine console if necessary and then run the
following command from the root of your cloned repository:

    <path-to-google_appengine-sdk>/appcfg.py --oauth2 update .

The URL to set up Twilio to notify on inbound SMS messages is:

    http://<application-name>.appspot.com/sms/inbound


Developing: Arduino
-------------------
Airduino was developed with the
[Arduino GSM shield](http://arduino.cc/en/Main/ArduinoGSMShield).

A tutorial of receiving SMS messages with the GSM library is
[here](http://arduino.cc/en/Tutorial/GSMExamplesReceiveSMS).

If you are using an Arduino Leonardo or Mega, there are extra considerations
about connecting the GSM shield that you need to pay close attention to. Make
sure to follow the instructions
[here](http://arduino.cc/en/Guide/GSMShieldLeonardoMega).


Developing: Nodecopter
----------------------
For information on Nodecopter see [here](http://nodecopter.com).

Get started with a Drone REPL using:

    npm install && node repl.js


Developing: Vagrant/Virtualbox VMs
----------------------------------
VirtualBox and Vagrant are tools to "create and configure lightweight,
reproducible, and portable development environments." Vagrant itself is a
virtual instance creation and startup tool on top of Oracle VirtualBox which
takes care of the virtualisation.

Download and install the Open Source Edition of [VirtualBox].

Then download and install [Vagrant]. The Linux packages install the `vagrant`
executable at `/opt/vagrant/bin` and you will want to add this to your path.

There is a `Vagrantfile` at the toplevel which includes software to help
develop the Airduino applications. To build the VM, change to the `dev`
directory and run the provide `Rakefile` target:

    rake

Building the VM may take some time, particularly on the first occasion when
Ubuntu base images are downloaded. The completed VM will be output in `dev` with
a `.box` suffix.

To use this VM, change back to the repository root and use the `Vagrantfile`
provided there to create an instance of the VM:

    vagrant up

When this is complete, you can ssh onto the instance using:

    vagrant ssh

The directory where the `Vagrantfile` was sourced is mounted at `/vagrant` on
the VM so change there for development.

    cd /vagrant

When finished developing, you can destroy the VM using:

    vagrant destroy -f

To see more verbose output on any vagrant command, add a VAGRANT_LOG environment
variable setting, e.g.:

    VAGRANT_LOG=INFO /opt/vagrant/bin/vagrant up

Further help troubleshooting can be obtained by editing your `Vagrantfile` and
enabling the `virtualbox.gui = true` setting. This will pop up a VirtualBox
GUI window on boot.

Note that VT-x/AMD-V hardware acceleration may need to be enabled in your BIOS
to use VirtualBox virtualisation

[VirtualBox]: https://www.virtualbox.org/wiki/Downloads
[Vagrant]: http://vagrantup.com

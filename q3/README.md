# Documentation stuff
Just some brief notes for configuration

## systemd config
Before starting, move the q3_server.service file into /lib/systemd/system directory.
Then do the following,
* set the actual username after User=
* set the proper path to the binary after ExecStart=

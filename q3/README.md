# Documentation stuff
Just some brief notes for configuration
(__G++ version 7.3.0__)

## Compiling
```
g++ server.cpp -o server
g++ client.cpp -o client
```

## Execution
```
./server
./client
```

## systemd config
Before starting, move the q3_server.service file into /lib/systemd/system directory.
Then do the following,
* set the actual username after User=
* set the proper path to the binary after ExecStart=

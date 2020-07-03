# Power Manager

## A RESTful server for waking up and putting to sleep machines

The power manager will attempt to wake up remote machines in the same
LAN by sending a magic packet, and will suspend the machine on which
it is in execution by using the `systemctl suspend` command.
If the machine to be suspended is another machine, pm will relay the
suspend command to that machine, if another pm is in execution on that
machine, the machine will be suspended.

## Installation

To install all the packages with pip:

```
pip3 install --user -r requirements.txt
```

## Configuration

The configuration file will be in the form of a TOML file, which will
describe for each known client, its MAC address, and its hostname.

Copy the configuration file template and modify it:

```
cp config.toml.example config.toml
```

## Usage

Launch the server:

```
./pm.py
```

The following is a description of the RESTful API:

### Waking up machines

Machines can be awoken using the `/wake` endpoint,
if the machine to be awaked is present in the config file,
the server will send a magic packet to turn it on.
A manual MAC address can also be specified.

| Parameter | Value | Semantics                                                    |
|:----------|-------|--------------------------------------------------------------|
| `name`    | str   | The name of the client to be awoken                          |
| `address` | str   | The MAC address of the client to be awoken, overrides config |

### Putting machines to sleep

Machines can be suspended using the `/sleep` endpoint,
if the machine to be suspended is present in the config file,
the server will forward the request to the target machine, which will
execute the `systemctl suspend` command and enter S3 state.

| Parameter  | Value | Semantics                                                 |
|:-----------|-------|-----------------------------------------------------------|
| `name`     | str   | The name of the client to be suspended                    |
| `hostname` | str   | The hostname of the client to be awoken, overrides config |

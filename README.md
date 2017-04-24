# Wercker Kubernetes Demo: Hello!

A simple Python application that uses the Bottle framework to serve a custom
message over HTTP.

This application is used to showcase how easy it is to deploy to Kubernetes
using Wercker.

```
usage: hello.py [-h] hostname port messagefile

Serve a hello message over HTTP.

positional arguments:
  hostname     The host IP to listen on.
  port         The port to listen on.
  messagefile  A file that contains the message to display

optional arguments:
  -h, --help   show this help message and exit
```

Requires `Python 2` `pip` & `virtualenv` to run.


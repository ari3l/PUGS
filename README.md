# PUGS

## Usage
1. Generate parameters using `python prepare.py` and specify `--n-value` in command line
2. Run the example `python clientExample.py` and specify `--username`, `--password`, `--site`, `--category`, and `--update` in command line

## Generating Certificates
1. Generate server cert:
    * ``openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt
``
      > Make sure to enter 'example.com' for the Common Name.

2. Generate client cert:
    * ``openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout client.key -out client.crt
``

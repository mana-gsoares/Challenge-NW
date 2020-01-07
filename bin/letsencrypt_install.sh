#!/bin/bash
# File  : letsencrypt_install.sh

git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt
/opt/letsencrypt/letsencrypt-auto certonly --standalone --email $1 --agree-tos --no-eff-email -d $2

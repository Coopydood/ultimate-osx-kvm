#!/bin/sh

# Fixes for Fedora's SELinux integration within this repository.*
# Needs to be run with sudo.
# * = Testing, script is not ready until conformation.

sudo semanage fcontext -a -t virt_image_t 'OVMF_CODE.fd'
sudo restorecon -v 'OVMF_CODE.fd'
sudo ausearch -c 'rpc-virtqemud' --raw | audit2allow -M my-rpcvirtqemud
sudo semodule -i my-rpcvirtqemud.pp
sudo ausearch -c 'qemu-system-x86' --raw | audit2allow -M my-qemusystemx86.pp
sudo semodule -X 300 my-qemusystemx86.pp

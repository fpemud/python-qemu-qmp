/usr/bin/qemu-system-x86_64 -name "testvm" \
                            -machine type=q35 \
                            -display gtk \
                            -monitor none \
                            -qmp tcp:127.0.0.1:4444,server

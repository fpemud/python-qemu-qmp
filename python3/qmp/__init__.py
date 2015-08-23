#!/usr/bin/env python3

# Copyright (c) 2005-2014 Fpemud <fpemud@sina.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
qmp

@author: Fpemud
@license: LGPLv2 License
@contact: fpemud@sina.com

Reference:
  qmp-commands.txt: commands and queries
  qmp-events.txt:   events
"""

__author__ = "fpemud@sina.com (Fpemud)"
__version__ = "0.0.1"

import json
import socket


class QmpClient:
    """This library provides an interface to QEMU's QMP server, allowing you to
       manage and query running virtual machines."""

    def __init__(self):
        self.sock = None

    def connect_tcp(self, host, port, local_host=None, local_port=None):
        assert local_host is None and local_port is None

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            self._negotiateCapabilities()
        except:
            if self.sock is not None:
                self.sock.close()
                self.sock = None

    def connect_unix(self, filename):
        try:
            self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.sock.connect(filename)
            self._negotiateCapabilities()
        except:
            if self.sock is not None:
                self.sock.close()
                self.sock = None

    def close(self):
        if self.sock is not None:
            self.sock.close()
            self.sock = None

    def cmd_quit(self):
        assert self.sock is not None
        json.dump(self.sock, {"execute": "quit"})
        self._returnProc()

    def cmd_stop(self):
        assert self.sock is not None
        json.dump(self.sock, {"execute": "stop"})
        self._returnProc()

    def cmd_conti(self):
        assert self.sock is not None
        json.dump(self.sock, {"execute": "conti"})
        self._returnProc()

    def cmd_system_powerdown(self):
        assert self.sock is not None
        json.dump(self.sock, {"execute": "system_powerdown"})
        self._returnProc()

    def cmd_system_reset(self):
        assert self.sock is not None
        json.dump(self.sock, {"execute": "system_reset"})
        self._returnProc()

    def cmd_system_wakeup(self):
        assert self.sock is not None
        json.dump(self.sock, {"execute": "system_wakeup"})
        self._returnProc()

    def cmd_device_add(self):
        assert self.sock is not None

    def cmd_device_del(self):
        assert self.sock is not None

    def cmd_chardev_add(self, chardev_id, backend):
        assert self.sock is not None

    def cmd_chardev_remove(self, chardev_id):
        assert self.sock is not None

    def cmd_netdev_add(self):
        assert self.sock is not None

    def cmd_netdev_del(self):
        assert self.sock is not None

    def cmd_set_link(self, name, up):
        assert self.sock is not None
        assert isinstance(name, str) and isinstance(up, bool)
        json.dump(self.sock, {"execute": "set_link", "arguments": {"name": name, "up": up}})
        self._returnProc()

    def cmd_balloon(self, value):
        assert self.sock is not None
        assert isinstance(value, int)
        json.dump(self.sock, {"execute": "set_link", "arguments": {"value": value}})
        self._returnProc()

    def cmd_eject(self, devname, force=False):
        assert False		# not implemented yet

    def cmd_change(self):
        assert False		# not implemented yet

    def cmd_screen_dump(self, filename):
        assert False		# not implemented yet

    def cmd_object_add(self):
        assert False		# not implemented yet

    def cmd_object_del(self):
        assert False		# not implemented yet

    def cmd_send_key(self, keys):
        assert False		# not implemented yet

    def cmd_cpu(self, cpu_id):
        assert False		# not implemented yet

    def cmd_cpu_add(self, cpu_id):
        assert False		# not implemented yet

    def cmd_memsave(self, cpu_id):
        assert False		# not implemented yet

    def cmd_pmemsave(self, cpu_id):
        assert False		# not implemented yet

    def cmd_inject_nmi(self):
        assert False		# not implemented yet

    def cmd_ringbuf_write(self):
        assert False		# not implemented yet

    def cmd_ringbuf_read(self):
        assert False		# not implemented yet

    def query_version(self):
        assert False		# not implemented yet

    def query_name(self):
        assert False		# not implemented yet

    def query_uuid(self):
        assert False		# not implemented yet

    def query_balloon(self):
        # return int, async?

        assert False		# not implemented yet

    def query_commands(self):
        assert False		# not implemented yet

    def query_command_line_options(self):
        assert False		# not implemented yet

    def query_events(self):
        assert False		# not implemented yet

    def query_chardev(self):
        assert False		# not implemented yet

    def query_chardev_backends(self):
        assert False		# not implemented yet

    def query_block(self):
        assert False		# not implemented yet

    def query_blockstats(self):
        assert False		# not implemented yet

    def query_cpus(self):
        assert False		# not implemented yet

    def query_iothreads(self):
        assert False		# not implemented yet

    def query_pci(self):
        assert False		# not implemented yet

    def query_kvm(self):
        assert False		# not implemented yet

    def query_mice(self):
        assert False		# not implemented yet

    def query_vnc(self):
        assert False		# not implemented yet

    def query_spice(self):
        assert False		# not implemented yet

    def _negotiateCapabilities(self):
        assert self.sock is not None

        json.load(self.sock)
        json.dump(self.sock, {"execute": "qmp_capabilities"})
        self._returnProc()

    def _returnProc(self):
        val = json.load(self.sock).get("return", "illegal json string format")
        if val != "":
            raise QmpCmdError(val)


class QmpClientEventHandler:

    def on_powerdown(self):
        pass

    def on_shutdown(self):
        pass

    def on_reset(self):
        pass

    def on_suspend(self):
        pass

    def on_suspend_disk(self):
        pass

    def on_wakeup(self):
        pass

    def on_stop(self):
        pass

    def on_resume(self):
        pass

    def on_balloon_change(self, actual):
        pass

    def on_device_deleted(self, device, path):
        pass

    def on_device_tray_moved(self, device, tray_open):
        pass


class QmpCmdError(Exception):

    def __init__(self, message):
        super(QmpCmdError, self).__init__(message)

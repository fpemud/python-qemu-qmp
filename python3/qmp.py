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
    """This library is used to access the QEMU's QMP interface, allowing you to
       manage and query running virtual machines."""

    def __init__(self):
        self.handler = None
        self.sock = None
        self.sockf = None

    def set_event_handler(self, handler):
        self.handler = handler

    def connect_tcp(self, host, port, local_host=None, local_port=None):
        """Connects to QEMU's QMP server via TCP socket."""
        assert self.sock is None and self.sockf is None

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            self.sockf = self.sock.makefile(mode="rw", buffering=2)
            self._connectBottomHalf()
        except:
            self.close()
            raise

    def connect_unix(self, filename):
        """Connects to QEMU's QMP server via UNIX socket."""
        assert self.sock is None and self.sockf is None

        try:
            self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.sock.connect(filename)
            self.sockf = self.sock.makefile(mode="rw", buffering=2)
            self._connectBottomHalf()
        except:
            self.close()
            raise

    def is_connected(self):
        return self.sockf is not None

    def close(self):
        if self.sockf is not None:
            self.sockf.close()
            self.sockf = None
        if self.sock is not None:
            self.sock.close()
            self.sock = None

    def cmd_quit(self):
        assert self.sockf is not None
        json.dump({"execute": "quit"}, self.sockf)
        self._returnProc()

    def cmd_stop(self):
        assert self.sockf is not None
        json.dump({"execute": "stop"}, self.sockf)
        self._returnProc()

    def cmd_conti(self):
        assert self.sockf is not None
        json.dump({"execute": "conti"}, self.sockf)
        self._returnProc()

    def cmd_system_powerdown(self):
        assert self.sockf is not None
        json.dump({"execute": "system_powerdown"}, self.sockf)
        self._returnProc()

    def cmd_system_reset(self):
        assert self.sockf is not None
        json.dump({"execute": "system_reset"}, self.sockf)
        self._returnProc()

    def cmd_system_wakeup(self):
        assert self.sockf is not None
        json.dump({"execute": "system_wakeup"}, self.sockf)
        self._returnProc()

    def cmd_object_add(self, qom_type, qom_id, **kwargs):
        assert self.sockf is not None
        json.dump({"execute": "object-add", "arguments": {"qom-type": qom_type, "id": qom_id, "props": kwargs}}, self.sockf)
        self._returnProc()

    def cmd_object_del(self, qom_id):
        assert self.sockf is not None
        json.dump({"execute": "object-del", "arguments": {"id": qom_id}}, self.sockf)
        self._returnProc()

    def cmd_device_add(self):
        assert self.sockf is not None

    def cmd_device_del(self):
        assert self.sockf is not None

    def cmd_chardev_add(self, chardev_id, backend):
        assert self.sockf is not None

    def cmd_chardev_remove(self, chardev_id):
        assert self.sockf is not None

    def cmd_netdev_add(self):
        assert self.sockf is not None

    def cmd_netdev_del(self):
        assert self.sockf is not None

    def cmd_set_link(self, name, up):
        assert self.sockf is not None
        assert isinstance(name, str) and isinstance(up, bool)
        json.dump({"execute": "set_link", "arguments": {"name": name, "up": up}}, self.sockf)
        self._returnProc()

    def cmd_balloon(self, value):
        assert self.sockf is not None
        assert isinstance(value, int)
        json.dump({"execute": "set_link", "arguments": {"value": value}}, self.sockf)
        self._returnProc()

    def cmd_eject(self, devname, force=False):
        assert False		# not implemented yet

    def cmd_change(self):
        assert False		# not implemented yet

    def cmd_screen_dump(self, filename):
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

    def _connectBottomHalf(self):
        self._wtfJsonLoad(self.sockf)
        json.dump({"execute": "qmp_capabilities"}, self.sockf)
        self._returnProc()

    def _returnProc(self):
        while True:
            obj = self._wtfJsonLoad(self.sockf)
            if "return" not in obj:
                continue
            if not isinstance(obj["return"], dict) or len(obj["return"]) != 0:
                raise QmpCmdError(obj["return"])
            break

    def _wtfJsonLoad(self, f):
        """I suppose json.load() should parse object one by one, but it only starts parsing after all the bytes are read.
           This behavior is broken on sockets: http://stackoverflow.com/questions/7337523/how-to-read-json-from-socket-in-python-incremental-parsing-of-json
           I tried ijson but it seems wierd either. Fortunately QEMU returns one json object in one line, so I can do this trick."""
        return json.loads(f.readline())


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

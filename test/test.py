#!/usr/bin/python3

import time
import qmp

o = qmp.QmpClient()
o.connect_tcp("127.0.0.1", 4444)
#time.sleep(1)
#o.cmd_conti()
o.close()

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

import ijson


class UnexpectedDataError(Exception):
    pass


def jsonLoadObject(f):
    ret = None
    mkey = None
    bfirst = True

    def initial_set(value):
        ret = value
    containers = [initial_set]

    for prefix, event, value in ijson.parse(f):
        if bfirst:
            if prefix != "":
                raise UnexpectedDataError("invalid prefix %s" % (prefix))
            if event in ["map_key", "end_array", "end_map"]:
                raise UnexpectedDataError("invalid event %s" % (event))
            bfirst = False

        if event == "start_map":
            m = {}
            containers[-1](m)
            def setter(value):
                m[mkey] = value
            containers.append(setter)
        elif event == 'start_array':
            a = []
            containers[-1](a)
            containers.append(a.append)
        elif event == 'map_key':
            mkey = value
        elif event == 'end_array' or event == 'end_map':
            containers.pop()
        elif event in ["boolean", "number", "string"]:
            containers[-1](value)
        else:
            print("debug1", prefix, event, value)
            assert False

        if prefix == "" and event in ["end_array", "end_map", "boolean", "number", "string"]:
            return ret

#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from hatvenom.core.cli import HatVenomCLI
from hatvenom.core.payload import PayloadGenerator


class HatVenom(PayloadGenerator):
    def ip_bytes(self, ip):
        return self.ip_to_bytes(ip)

    def port_bytes(self, port):
        return self.port_to_bytes(port)

    def string_bytes(self, string):
        return self.string_to_bytes(string)

    def generate(self, file_format, arch, shellcode, offsets={}):
        return self.generate_payload(file_format, arch, shellcode, offsets)

    def generate_to(self, file_format, arch, shellcode, offsets={}, filename='a.out'):
        with open(filename, 'wb') as f:
            f.write(self.generate_payload(file_format, arch, shellcode, offsets))

if __name__ == '__main__':
    hatvenom = HatVenomCLI()
    hatvenom.start()
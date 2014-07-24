# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    'get_tox_ini',
]

import ConfigParser
import os

_tox_ini = None


def get_tox_ini():
    global _tox_ini
    if _tox_ini is None:
        _tox_ini = ToxIni()
    return _tox_ini


class ToxIni(object):

    _ini = None

    def _open_tox_ini(self):
        if self._ini is None:
            self._ini = ConfigParser.ConfigParser()
            self._ini.read('tox.ini')
        return self._ini

    def exists(self):
        return os.path.exists('tox.ini')

    def get_image(self, image):
        ini = self._open_tox_ini()
        if ini.has_option('docker', 'image'):
            image = ini.get('docker', 'image')
        return image

    def get_payload(self, payload):
        ini = self._open_tox_ini()
        if ini.has_option('testenv', 'commands'):
            payload = ini.get('testenv', 'commands')
        return payload

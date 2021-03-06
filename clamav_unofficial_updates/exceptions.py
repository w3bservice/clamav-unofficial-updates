# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# clamav-unofficial-updates: ClamAV third party signature updates library
# Copyright (C) 2015  Andrew Colin Kissa <andrew@topdog.za.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
clamav-unofficial-updates: ClamAV third party signature updates library

Exceptions
"""


class ClamAVUUError(Exception):
    """ClamAVUUError Exceptions"""
    def __init__(self, message):
        """Init"""
        super(ClamAVUUError, self).__init__(message)


class ClamAVUUCfgError(ClamAVUUError):
    """Configuration Exceptions"""
    pass


class ClamAVUUDownloadError(ClamAVUUError):
    """Download Exceptions"""
    pass


class ClamAVUUNameError(ClamAVUUError):
    """Download Exceptions"""
    pass

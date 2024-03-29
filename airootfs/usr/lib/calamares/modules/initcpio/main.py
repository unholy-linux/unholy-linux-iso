#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2014, Philip Müller <philm@manjaro.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import libcalamares
import subprocess
from libcalamares.utils import check_target_env_call, target_env_call
from libcalamares.utils import *


def run_mkinitcpio():
    """ Runs mkinitcpio with given kernel profile """
    kernel = libcalamares.job.configuration['kernel']
    check_target_env_call(['mkinitcpio', '-p', kernel])


def run():
    """ Calls routine to create kernel initramfs image.

    :return:
    """
    root_mount_point = libcalamares.globalstorage.value("rootMountPoint")
    subprocess.check_call(["cp", "/run/archiso/bootmnt/arch/boot/x86_64/vmlinuz", root_mount_point + "/boot/vmlinuz-linux"])
    target_env_call(["/usr/bin/cleanup.sh"])
    target_env_call(["sed -i 's/base udev/base udev plymouth/g' /etc/mkinitcpio.conf"])
    target_env_call(["plymouth-set-default-theme -R dark-arch"])
    run_mkinitcpio()

    return None

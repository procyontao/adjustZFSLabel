#!/usr/bin/env python3

# Copyright (c) 2017 Hristo Iliev <github@hiliev.eu>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from zfs.label import Label


import argparse
import datetime

from os import path, makedirs

parser = argparse.ArgumentParser()
parser.add_argument('--label', '-l', dest='label', type=str, default='label1')

args = parser.parse_args()
BLK_INITIAL_DISK = args.label      # device to read the label from

id_l = Label(BLK_INITIAL_DISK)
id_l.write('path','/dev/multipath/mpathad')
id_l = Label(BLK_INITIAL_DISK)
id_l.write('guid',8324053655394529542)
id_l = Label(BLK_INITIAL_DISK)
id_l.write('top_guid',8324053655394529542)
id_l = Label(BLK_INITIAL_DISK)
id_l.write('id',4)
id_l = Label(BLK_INITIAL_DISK)
id_l.write('metaslab_array',134)
#id_l._print_nvlist(id_l.get_nvlist())



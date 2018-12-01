#!/usr/bin/env python3

from zfs.label import Label
import argparse

parser = argparse.ArgumentParser(description='zfs_rescue')
parser.add_argument('--label', '-l', dest='label', type=str, default='/dev/sde2',
                    help='Device where to read the initial label from')

args = parser.parse_args()

id_l = Label(args.label)
id_l.read(2)
id_l._print_nvlist(id_l.get_nvlist())
#id_l._print_ubarray()



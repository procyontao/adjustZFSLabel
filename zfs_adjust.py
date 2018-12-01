#!/usr/bin/env python3


from zfs.label import Label
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--label', '-l', dest='label', type=str, default='label1')

args = parser.parse_args()
label = args.label

id_l = Label(label)
id_l.write('path','/dev/multipath/mpathad')
id_l = Label(label)
id_l.write('guid',8324053655394529542)
id_l = Label(label)
id_l.write('top_guid',8324053655394529542)
id_l = Label(label)
id_l.write('id',4)
id_l = Label(label)
id_l.write('metaslab_array',134)
#id_l._print_nvlist(id_l.get_nvlist())



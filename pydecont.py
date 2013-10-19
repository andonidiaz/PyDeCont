#!/usr/bin/python
#   Andoni Diaz <andoni94@gmail.com>

from sys import argv, exit, stderr
from optparse import OptionParser

from twisted.internet import reactor
from deluge.log import setupLogger
from deluge.ui.client import client
import logging
import os

# set up command-line options
parser = OptionParser()
parser.add_option("--max_active_limit", help="sets the absolute maximum number of active torrents on the deluge backend", dest="max_active_limit")
parser.add_option("--max_active_downloading", help="sets the maximum number of active downloading torrents on the deluge backend", dest="max_active_downloading")
parser.add_option("--max_active_seeding", help="sets the maximum number of active seeding torrents on the deluge backend", dest="max_active_seeding")
parser.add_option("--max_download_speed", help="sets the maximum global download speed on the deluge backend", dest="max_download_speed")
parser.add_option("--max_upload_speed", help="sets the maximum global upload speed on the deluge backend", dest="max_upload_speed")
parser.add_option("--debug", help="outputs debug information to the console", default=False, action="store_true", dest="debug")
parser.add_option("--get_torrent_status", default=False, action="store_true", dest="get_torrent_status")
# grab command-line options
(options, args) = parser.parse_args()

if not options.debug:
    logging.disable(logging.ERROR)

# Get the torrent status
if options.get_torrent_status:
    data = os.popen("deluge-console 'info'")
    print data.read()


if options.max_active_limit:
    data = os.popen("deluge-console 'config -s max_active_limit %i'" % int(options.max_active_limit))
    print data.read()

if options.max_active_downloading:
    data = os.popen("deluge-console 'config -s max_active_seeding %i'" % int(options.max_active_downloading))
    print data.read()

if options.max_active_seeding:
    data = os.popen("deluge-console 'config -s max_active_seeding %i'" % int(options.max_active_seeding))
    print data.read()

if options.max_download_speed:
    data = os.popen("deluge-console 'config -s max_download_speed %i'" % int(options.max_download_speed))
    print data.read()

if options.max_upload_speed:
    data = os.popen("deluge-console 'config -s max_upload_speed %i'" % int(options.max_upload_speed))
    print data.read()
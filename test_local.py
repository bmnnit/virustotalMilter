from __future__ import print_function
# A simple milter.

# Author: Stuart D. Gathman <stuart@bmsi.com>
# Copyright 2001 Business Management Systems, Inc.
# This code is under GPL.  See COPYING for details.

import sys
import os
try:
  from io import BytesIO
except:
  from StringIO import StringIO as BytesIO
import mime
import Milter
import tempfile
from time import strftime

fp = BytesIO()
out = "/home/yohighnest/PycharmProjects/virustotalMilter/mail.data.virus"
fp = open(out, "rb")

msg = mime.message_from_file(fp)

mime.defang (msg, "asd")
#!/usr/bin/env python
# coding: utf-8
#
# Copyright (C) 2017 hidenorly
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2
from optparse import OptionParser, OptionValueError

from pkg_resources import parse_version
OPCV3 = parse_version(cv2.__version__) >= parse_version('3')

def getCapAttrId(prop):
  return getattr(cv2 if OPCV3 else cv2.cv,
    ("" if OPCV3 else "CV_") + "CAP_PROP_" + prop)

def captureImage(captureIndex, width, height, filename, skipFrame):
	cap = cv2.VideoCapture(captureIndex)

	if cap:
		if width and height:
			cap.set(getCapAttrId("FRAME_WIDTH"), width)
			cap.set(getCapAttrId("FRAME_HEIGHT"), height)
			#print "Request:{}x{} Current:{}x{}".format(width,height, cap.get(getCapAttrId("FRAME_WIDTH")), cap.get(getCapAttrId("FRAME_HEIGHT")))

		for i in range(skipFrame):
			cap.read()

		ret, frame = cap.read()
		cv2.imwrite(filename,frame)

		# When everything done, release the capture
		cap.release()

def getResolution(resolution):
	resolutions=[]
	if resolution:
		resolutions = resolution.split("x")
	if len(resolutions):
		return int(resolutions[0]), int(resolutions[1])
	else:
		return None, None

if __name__ == '__main__':
	parser = OptionParser()

	parser.add_option("-c", "--captureIndex", action="store", type="int", dest="captureIndex", help="Specify capture Index (set 0 if /dev/video0)", default="0")
	parser.add_option("-r", "--resolution", action="store", type="string", dest="resolution", help="Specify resolution")
	parser.add_option("-s", "--skip", action="store", type="int", dest="skipFrame", help="Specify skip frame", default="0")

	(options, args) = parser.parse_args()

	if not args:
		parser.error("requires filename such as \"tmp.jpg\"")
		parser.print_help()
		exit()

	width, height = getResolution(options.resolution)

	captureImage(options.captureIndex, width, height, args[0], options.skipFrame)
	cv2.destroyAllWindows()


#!/bin/python

# This script the images containing the instructions formats in
# ../raw/instruction-format-*.png
# and creates png's for each of the instructions.

import os
import Image

files = ["instruction-formats-1.png",
"instruction-formats-2.png",
"instruction-formats-3.png",
"instruction-formats-4.png",
"instruction-formats-5.png"]

# This is easier to do in matlab, use ifParser.m
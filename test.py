from __future__ import print_function

import sys
from random import random
from operator import add

from pyspark.sql import SparkSession

lines = sc.textFile("employee.txt")
lineLengths = lines.map(lambda s: len(s))
totalLength = lineLengths.reduce(lambda a, b: a + b)
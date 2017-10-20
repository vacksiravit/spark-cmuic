from __future__ import print_function

import sys
from random import random
from operator import add

from pyspark.sql import SparkSession

lines = sc.textFile("salary.txt")
lineLengths = lines.map(lambda s: len(s))

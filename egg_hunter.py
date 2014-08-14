#!/usr/bin/env python
from __future__ import division
import numpy as np
import scipy
from matplotlib import pylab
import pymorph
import mahotas
from scipy import ndimage
import sys

if __name__ == "__main__":
	filename = sys.argv[1]
	dna = pymorph
	T = mahotas.thresholding.otsu(dna)
	pylab.imshow(dna > T)
	pylab.show()
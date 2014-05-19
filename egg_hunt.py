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
	image = mahotas.imread(filename)
	image = ndimage.gaussian_filter(image, 16)
	rmax = pymorph.regmax(image)
	seeds,nr_eggs = ndimage.label(rmax)
	print nr_eggs
	threshold = mahotas.thresholding.otsu(image)
	dist_trans = ndimage.distance_transform_edt(image > threshold)
	dist_trans = dist_trans.max() - dist_trans - dist_trans.min()
	dist_trans = dist_trans/float(dist_trans.ptp()) * 255
	dist_trans = dist_trans.astype(np.uint8)
	eggs = pymorph.cwatershed(dist_trans, seeds)
	pylab.imshow(eggs)
	pylab.savefig(filename + ".out.png", format='png')
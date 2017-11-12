# -*- coding: utf-8 -*-
r"""
AnyMocap Features
===============================

A collection of small models that show-off special features of the
*AnyMocap* framework.

``Application/MocapExamples/SpecialFeatures``

This includes:

* offset to forceplates
* individual cutoff frequencies for markers
* normalization with respect to gait cycle events
* using time-varying weight for markers
* plus more.

"""
import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()

gallery.plot("../images/force_plate_offset.jpg")
gallery.show()
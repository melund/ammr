# -*- coding: utf-8 -*-
r"""
Bench Press
===============================

A full-body model doing push-ups with assumed drivers.

**Main file:** ``Application/Examples/BenchPress/BenchPress.Main.any``

The model of a bench press exercise is developed from the free posture model.
The bench is simulated by reaction forces between the head, thorax, pelvis,
feet and the ground.

"""


import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/BenchPress.jpg")
gallery.show()

#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# This application is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio DRM module. Place your Python package
description here (python/__init__.py).
'''

# ----------------------------------------------------------------
# Temporary workaround for ticket:181 (swig+python problem)
import sys
_RTLD_GLOBAL = 0
try:
    from dl import RTLD_GLOBAL as _RTLD_GLOBAL
except ImportError:
    try:
	from DLFCN import RTLD_GLOBAL as _RTLD_GLOBAL
    except ImportError:
	pass

if _RTLD_GLOBAL != 0:
    _dlopenflags = sys.getdlopenflags()
    sys.setdlopenflags(_dlopenflags|_RTLD_GLOBAL)
# ----------------------------------------------------------------


# import swig generated symbols into the drm namespace
from drm_swig import *

# import any pure python here
from mlc_factory import make_mlc
from drm_mlc_4qam_bc import drm_mlc_4qam_bc
from drm_mlc_16qam_bc import drm_mlc_16qam_bc
from drm_mlc_64qam_sm_bc import drm_mlc_64qam_sm_bc
# Receiver
from md_sel_cc import md_sel_cc
from fsync_cc import fsync_cc
from framer_cc import framer_cc
from phase_sync_cc import phase_sync_cc
from drm_equalizer_cc import drm_equalizer_cc
from decoder_c import decoder_c

#

# ----------------------------------------------------------------
# Tail of workaround
if _RTLD_GLOBAL != 0:
    sys.setdlopenflags(_dlopenflags)      # Restore original flags
# ----------------------------------------------------------------

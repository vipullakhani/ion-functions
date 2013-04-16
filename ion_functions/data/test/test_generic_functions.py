#!/usr/bin/env python

"""
@package ion_functions.test.generic_functions
@file ion_functions/test/generic_functions.py
@author Christopher Mueller
@brief Unit tests for generic_functions module
"""

from nose.plugins.attrib import attr
from ion_functions.test.base_test import BaseUnitTestCase

import numpy as np
from ion_functions.data import generic_functions as gfunc


@attr('UNIT', group='func')
class TestGenericFunctionsUnit(BaseUnitTestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_magnetic_declination(self):
            """
            Test magnetic_declination function.
    
            Some values based on those defined in the WMM document,
            WMM2010testvalues.pdf which accompanies the software.  Others
            were created and checked using online calculators.
            
            Implemented by Stuart Pearce, April 2013
            """
    
            lat = np.array([45.0, 45.0, 80.0, 0.0, -80.0, 80.0, 0.0, -80.0])
            lon = np.array([-128.0, -128.0, 0.0, 120.0, 240.0, 0.0, 120.0, 240.0])
            z = np.array([0.0, 1000.0, 0.0, 0.0, 0.0, 100000.0, 100000.0, 100000.0])
            timestamp = np.array([3575053740.7382507,  # 2013-04-15 22:29:00 UTC
                                  3575053740.7382507,
                                  3471292800.0,        # 2010-01-01 UTC
                                  3471292800.0,
                                  3471292800.0,
                                  3471292800.0,
                                  3471292800.0,
                                  3471292800.0])
            zflag = np.array([-1, -1, -1, -1, -1, 1, 1, 1])
            output = []
            for ii in range(len(lat)):
                out_ = gfunc.magnetic_declination(lat[ii],lon[ii],z[ii],
                                                  timestamp[ii],zflag[ii])
                output.append(out_)
            output = np.array(output)
            
            check_values = np.array([16.46093044096720,
                                     16.46376239313584,
                                     -6.13,
                                     0.97,
                                     70.21,
                                     -6.57,
                                     0.94,
                                     69.62])
            self.assertTrue(np.allclose(output, check_values, rtol=0, atol=1e-2))
    
    
    def test_ntp_to_unix_time(self):
            """
            Test ntp_to_unix_time function.
    
            Timestamp Values gathered from various internet sources
            including the NTP FAQ and HOWTO.
            
            Implemented by Stuart Pearce, April 2013
            """
    
            ntp_timestamps = np.array([3176736750.7358608,
                                       3359763506.2082224,
                                       3575049755.4380851])
    
            output = gfunc.ntp_to_unix_time(ntp_timestamps)
            
            check_values = np.array([967747950.735861,
                                     1150774706.2082224,
                                     1366060955.438085])
            self.assertTrue(np.allclose(output, check_values, rtol=0, atol=1e-6))
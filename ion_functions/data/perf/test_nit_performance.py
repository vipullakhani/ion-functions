#!/usr/bin/env python
from ion_functions.data.perf.test_performance import PerformanceTestCase, a_deca
from ion_functions.data.nit_functions import ts_corrected_nitrate
import numpy as np


class TestNITPerformance(PerformanceTestCase):

    def test_ts_corrected_nitrate(self):

        wllower = 217
        wlupper = 240
        cal_temp = 20.082039358135848
        dark_value = np.array([909])
        ctd_t = np.array([20])
        ctd_sp = np.array([0.0000])
        wl = np.array([189.71, 190.5, 191.29, 192.08, 192.87, 193.66, 194.45, 195.25, 196.04, 196.83, 197.62, 198.41, 199.2, 200, 200.79, 201.58, 202.38, 203.17, 203.96, 204.76, 205.55, 206.35, 207.14, 207.94, 208.73, 209.53, 210.33, 211.12, 211.92, 212.72, 213.51, 214.31, 215.11, 215.91, 216.7, 217.5, 218.3, 219.1, 219.9, 220.7, 221.5, 222.3, 223.1, 223.9, 224.7, 225.5, 226.3, 227.1, 227.9, 228.7, 229.51, 230.31, 231.11, 231.91, 232.71, 233.52, 234.32, 235.12, 235.93, 236.73, 237.53, 238.34, 239.14, 239.95, 240.75, 241.56, 242.36, 243.17, 243.97, 244.78, 245.58, 246.39, 247.19, 248, 248.81, 249.61, 250.42, 251.23, 252.03, 252.84, 253.65, 254.46, 255.26, 256.07, 256.88, 257.69, 258.5, 259.3, 260.11, 260.92, 261.73, 262.54, 263.35, 264.16, 264.97, 265.78, 266.58, 267.39, 268.2, 269.01, 269.82, 270.63, 271.44, 272.25, 273.07, 273.88, 274.69, 275.5, 276.31, 277.12, 277.93, 278.74, 279.55, 280.36, 281.18, 281.99, 282.8, 283.61, 284.42, 285.23, 286.05, 286.86, 287.67, 288.48, 289.3, 290.11, 290.92, 291.73, 292.55, 293.36, 294.17, 294.98, 295.8, 296.61, 297.42, 298.24, 299.05, 299.86, 300.68, 301.49, 302.3, 303.11, 303.93, 304.74, 305.56, 306.37, 307.18, 308, 308.81, 309.62, 310.44, 311.25, 312.06, 312.88, 313.69, 314.5, 315.32, 316.13, 316.95, 317.76, 318.57, 319.39, 320.2, 321.02, 321.83, 322.64, 323.46, 324.27, 325.08, 325.9, 326.71, 327.53, 328.34, 329.15, 329.97, 330.78, 331.59, 332.41, 333.22, 334.03, 334.85, 335.66, 336.48, 337.29, 338.1, 338.92, 339.73, 340.54, 341.36, 342.17, 342.98, 343.79, 344.61, 345.42, 346.23, 347.05, 347.86, 348.67, 349.48, 350.3, 351.11, 351.92, 352.74, 353.55, 354.36, 355.17, 355.98, 356.8, 357.61, 358.42, 359.23, 360.04, 360.86, 361.67, 362.48, 363.29, 364.1, 364.91, 365.72, 366.53, 367.34, 368.16, 368.97, 369.78, 370.59, 371.4, 372.21, 373.02, 373.83, 374.64, 375.45, 376.26, 377.07, 377.88, 378.68, 379.49, 380.3, 381.11, 381.92, 382.73, 383.54, 384.34, 385.15, 385.96, 386.77, 387.58, 388.38, 389.19, 390, 390.81, 391.61, 392.42, 393.23, 394.03, 394.84, 395.64])
        eno3 = np.array([-0.03411199, -0.01018159, -0.00318933, -0.00894908, -0.01104624, -0.00006145, 0.01586057, -0.0051615, -0.00467014, -0.00593588, -0.00733024, -0.00227615, -0.01284824, -0.00004967, -0.0190399, 0.0062002, -0.01347323, 0.00809096, 0.00450973, 0.00140898, 0.00351332, 0.00329296, 0.00442724, 0.00423925, 0.0040111, 0.00406529, 0.00386114, 0.00372506, 0.00356287, 0.00334277, 0.00323825, 0.00304123, 0.00284314, 0.00265964, 0.00249591, 0.00232651, 0.00212433, 0.00195766, 0.00177127, 0.00160284, 0.00148095, 0.00131054, 0.00116577, 0.00103722, 0.00092505, 0.00081846, 0.00070704, 0.00062786, 0.0005408, 0.00045861, 0.00039183, 0.00033631, 0.00028581, 0.00023696, 0.00020634, 0.0001623, 0.00013849, 0.0001106, 0.00008422, 0.00007712, 0.00006064, 0.00004194, 0.00003498, 0.00002304, 0.00001489, 0.00001549, 0.00000664, -0.00000298, 0.00000547, -0.00000196, -0.00001164, -0.00000058, -0.00000664, -0.00001163, -0.00001466, -0.00000173, 0.00000439, -0.00000963, -0.0000064, -0.00000075, -0.00000889, -0.00000176, -0.00000712, 0.00000662, 0.00000394, 0.00000894, 0.00001376, 0.00000623, 0.00001416, 0.0000144, 0.00000821, 0.00002575, 0.00002124, 0.00003059, 0.00002591, 0.00002037, 0.00003129, 0.0000337, 0.000026, 0.00004509, 0.00004023, 0.00004651, 0.00005051, 0.00003921, 0.00003022, 0.00004689, 0.00004727, 0.00004996, 0.00004095, 0.00005855, 0.0000599, 0.00006063, 0.00005822, 0.00005213, 0.00006594, 0.00006247, 0.00006047, 0.00005656, 0.00007531, 0.00006451, 0.0000822, 0.00007228, 0.00006814, 0.00006654, 0.00007889, 0.00007828, 0.00008047, 0.00008416, 0.0000884, 0.00008343, 0.00008895, 0.00008391, 0.00009165, 0.00010465, 0.00009701, 0.00009468, 0.0001052, 0.00009904, 0.00009963, 0.00010066, 0.00010178, 0.00010181, 0.00010078, 0.00010369, 0.00010319, 0.00010516, 0.00010371, 0.00011073, 0.00010365, 0.0001088, 0.00011818, 0.00010986, 0.00010841, 0.0001037, 0.00012087, 0.00012238, 0.00012106, 0.00012231, 0.00012042, 0.00013205, 0.00012391, 0.00013543, 0.00012665, 0.00013488, 0.00013687, 0.00014296, 0.00015111, 0.00014599, 0.00014179, 0.00013916, 0.0001494, 0.00013625, 0.00013862, 0.00014173, 0.00015215, 0.00013674, 0.00016678, 0.00015353, 0.00015307, 0.00015747, 0.00014916, 0.00015459, 0.00014347, 0.00014341, 0.00016133, 0.00016349, 0.00016972, 0.00018286, 0.00018341, 0.00017463, 0.00018584, 0.00016787, 0.00018983, 0.00017584, 0.00018486, 0.00020235, 0.00019586, 0.00017831, 0.00016939, 0.00019697, 0.00018981, 0.00019976, 0.00019253, 0.00019274, 0.00021425, 0.00019833, 0.00021862, 0.00018352, 0.00020482, 0.00018786, 0.00018572, 0.00019685, 0.00019666, 0.00021307, 0.00020684, 0.00021551, 0.0002102, 0.0001949, 0.00022761, 0.00018531, 0.0002354, 0.00021047, 0.0002229, 0.0002377, 0.00023918, 0.00021833, 0.00024802, 0.0002537, 0.00022211, 0.00025345, 0.00023181, 0.00020176, 0.00021726, 0.00020704, 0.00021012, 0.00022049, 0.00022717, 0.00021809, 0.00024546, 0.00024071, 0.00027593, 0.00026214, 0.00027633, 0.00025597, 0.00027758, 0.00024742, 0.00025206, 0.00023885, 0.00025827, 0.00030827, 0.00024759, 0.0003046, 0.0003129, 0.00026685, 0.00028302, 0.00027792])
        eswa = np.array([0.05180226, 0.01601277, 0.02252629, 0.01441802, 0.02213719, -0.00037942, 0.00106569, 0.00246742, 0.00524106, -0.0003689, 0.01021176, -0.00036366, 0.02486347, -0.00035838, 0.0682417, 0.06253262, 0.08762439, 0.06923902, 0.06912265, 0.06509374, 0.05695105, 0.0495771, 0.0424733, 0.03620625, 0.03070004, 0.02574593, 0.0215775, 0.01797804, 0.01483676, 0.01216502, 0.00988781, 0.0079794, 0.00641764, 0.00513366, 0.00402245, 0.00317328, 0.00250482, 0.00195535, 0.00153819, 0.0012029, 0.00093943, 0.00073445, 0.00058934, 0.00046178, 0.00036742, 0.00029976, 0.00023502, 0.00018475, 0.00016917, 0.00013935, 0.00012877, 0.00009708, 0.00008702, 0.00006751, 0.0000543, 0.00005498, 0.00004588, 0.00003683, 0.00003364, 0.00002535, 0.00000982, 0.00001744, 0.00001012, 0.00000462, 0.00001025, 0.00000288, 0.00000515, 0.00000146, -0.00000578, -0.00000575, 0.00000437, -0.00000555, -0.00000365, -0.00000356, 0.00000006, -0.00000257, -0.00001922, 0.00000276, 0.00000469, -0.00000369, 0.00000927, 0.0000002, 0.00000544, 0.00000054, 0.00000105, -0.00000326, 0.0000053, -0.00000038, -0.00000056, 0.00000654, 0.00001416, 0.0000044, 0.00001286, -0.00000192, 0.00000659, 0.00001726, 0.00000773, 0.0000137, 0.00001381, 0.00000617, 0.00002658, 0.00000563, -0.00000411, 0.00001998, 0.00004065, 0.00003279, 0.00002604, 0.00003852, 0.00002272, 0.00002229, 0.00001692, 0.00003197, 0.00004142, 0.000034, 0.00003256, 0.00004102, 0.00003399, 0.00005039, 0.00003795, 0.00005075, 0.00003751, 0.00004616, 0.00004937, 0.00004812, 0.00004453, 0.00004571, 0.00003732, 0.00003589, 0.00004682, 0.00005973, 0.00006285, 0.00005804, 0.00006537, 0.0000464, 0.00008124, 0.00005819, 0.00005502, 0.00007971, 0.00006856, 0.00007526, 0.00007793, 0.00007181, 0.00006083, 0.00008294, 0.00007609, 0.00008437, 0.00008565, 0.00008441, 0.00009433, 0.00008639, 0.00008995, 0.0001001, 0.00010124, 0.000116, 0.00010066, 0.00011784, 0.00010537, 0.00011174, 0.00011137, 0.0001115, 0.00012041, 0.0001093, 0.00012107, 0.00011595, 0.00012756, 0.00012817, 0.00012547, 0.0001244, 0.00013607, 0.00013081, 0.00013377, 0.0001452, 0.00013674, 0.00014875, 0.0001472, 0.00015914, 0.00014811, 0.0001605, 0.00014614, 0.00015805, 0.00016785, 0.00017213, 0.0001886, 0.00018458, 0.00016965, 0.00016942, 0.00017847, 0.00014929, 0.00017984, 0.00016957, 0.0001919, 0.00020499, 0.00018274, 0.00021345, 0.00019917, 0.00018581, 0.00022166, 0.00022915, 0.00023291, 0.0002218, 0.00023669, 0.00022478, 0.00023863, 0.00022902, 0.000219, 0.00025989, 0.00024008, 0.00024547, 0.00024427, 0.00024826, 0.00025647, 0.00024107, 0.00025013, 0.0002528, 0.00027643, 0.00025758, 0.00030102, 0.00028716, 0.00026521, 0.0003198, 0.00027929, 0.00027451, 0.00026086, 0.00024033, 0.00027327, 0.00024272, 0.00026349, 0.00029115, 0.00030297, 0.00029137, 0.00030819, 0.00034227, 0.00035306, 0.00033793, 0.00035977, 0.0003195, 0.00032722, 0.0003337, 0.00032211, 0.00032313, 0.0003051, 0.00030897, 0.00032207, 0.00032395, 0.00034471, 0.00033295, 0.00035061, 0.00036662, 0.00035713, 0.00034403, 0.00039216, 0.00032109, 0.00038396, 0.00038684, 0.00036283, 0.00036494])
        di = np.array([52, 45, 34, 46, 44, 11, 29, 31, 26, 32, 49, 22, 81, 411, 1440, 3738, 7024, 10670, 14035, 17003, 19732, 22359, 24937, 27451, 29707, 31576, 32915, 33451, 33223, 32392, 31065, 29593, 28218, 27006, 26039, 25486, 25267, 25403, 25896, 26731, 28004, 29598, 31576, 33920, 36535, 39376, 42245, 45009, 47512, 49417, 50663, 51043, 50684, 49596, 48066, 46259, 44338, 42444, 40756, 39282, 37973, 37012, 36254, 35795, 35572, 35608, 35909, 36465, 37294, 38429, 39854, 41489, 43325, 45326, 47349, 49414, 51219, 52767, 53874, 54358, 54239, 53537, 52185, 50384, 48219, 45801, 43362, 40971, 38687, 36584, 34722, 33038, 31612, 30347, 29348, 28545, 27907, 27472, 27226, 27135, 27221, 27444, 27850, 28455, 29198, 30112, 31113, 32309, 33530, 34895, 36269, 37647, 38909, 40014, 40942, 41595, 41971, 42056, 41795, 41302, 40514, 39588, 38503, 37370, 36215, 35092, 33994, 33037, 32175, 31354, 30619, 29996, 29446, 28965, 28625, 28247, 28002, 27842, 27700, 27652, 27658, 27704, 27803, 27999, 28181, 28497, 28800, 29205, 29657, 30100, 30600, 31168, 31717, 32288, 32898, 33470, 33997, 34557, 35048, 35509, 35881, 36128, 36343, 36426, 36351, 36129, 35729, 35183, 34550, 33763, 32898, 31981, 30990, 30022, 29067, 28077, 27127, 26170, 25234, 24398, 23556, 22762, 21981, 21236, 20508, 19824, 19192, 18582, 18009, 17440, 16950, 16449, 15999, 15592, 15208, 14835, 14534, 14217, 13919, 13670, 13452, 13246, 13085, 12934, 12807, 12704, 12620, 12534, 12479, 12442, 12417, 12398, 12412, 12416, 12477, 12516, 12592, 12679, 12769, 12896, 13032, 13094, 13120, 13114, 13129, 13097, 13130, 13181, 13172, 13203, 13197, 13183, 13181, 13135, 13144, 13049, 12907, 12662, 12421, 12166, 11921, 11660, 11430, 11165, 10976, 10771, 10587, 10368, 10133, 9950, 9832, 9696, 9573, 9159, 8518, 7866])
        frame_type = np.array(['SLB', 'SLB', 'SLB', 'SDB'])
        data_in = np.array([965, 942, 971, 960, 953, 963, 956, 979, 977, 966, 978, 990, 992, 1175, 1919, 3841, 7050, 10949, 14799, 18269, 21360, 24299, 27089, 29794, 32240, 34221, 35613, 36129, 35899, 35000, 33584, 32039, 30573, 29270, 28297, 27713, 27472, 27594, 28123, 29013, 30322, 31994, 34076, 36528, 39298, 42232, 45281, 48168, 50750, 52720, 53987, 54381, 53975, 52813, 51192, 49297, 47234, 45268, 43513, 41934, 40561, 39554, 38757, 38257, 38008, 38017, 38342, 38920, 39745, 40923, 42384, 44073, 45973, 48020, 50109, 52233, 54142, 55680, 56765, 57275, 57089, 56309, 54889, 52998, 50736, 48234, 45668, 43190, 40855, 38645, 36706, 34960, 33484, 32202, 31146, 30322, 29672, 29193, 28951, 28834, 28919, 29172, 29591, 30186, 30950, 31842, 32896, 34101, 35388, 36776, 38156, 39559, 40853, 41986, 42905, 43575, 43976, 44018, 43744, 43228, 42413, 41457, 40336, 39174, 38000, 36838, 35732, 34716, 33796, 32968, 32224, 31554, 30999, 30525, 30137, 29802, 29557, 29333, 29207, 29153, 29121, 29179, 29294, 29461, 29658, 29969, 30300, 30708, 31156, 31634, 32140, 32679, 33271, 33828, 34459, 35018, 35601, 36138, 36629, 37093, 37482, 37750, 37968, 38036, 37937, 37697, 37296, 36729, 36075, 35289, 34400, 33478, 32477, 31494, 30496, 29521, 28533, 27553, 26647, 25748, 24881, 24065, 23276, 22522, 21814, 21088, 20475, 19833, 19243, 18679, 18161, 17642, 17178, 16768, 16372, 16039, 15686, 15365, 15094, 14830, 14610, 14400, 14217, 14065, 13930, 13792, 13715, 13652, 13602, 13556, 13535, 13525, 13541, 13529, 13587, 13624, 13705, 13774, 13890, 13989, 14103, 14206, 14229, 14225, 14235, 14216, 14215, 14267, 14270, 14277, 14292, 14256, 14221, 14217, 14173, 14131, 13972, 13697, 13459, 13214, 12973, 12718, 12453, 12227, 12002, 11799, 11611, 11393, 11144, 10947, 10855, 10734, 10573, 10162, 9527, 8705])

        stats = []
        # create 10000 data packets
        data_in = np.tile(data_in, (a_deca, 1))
        ctd_t = np.tile(ctd_t, (a_deca, 1))
        ctd_sp = np.tile(ctd_sp, (a_deca, 1))
        dark_value = np.tile(dark_value, (a_deca, 1))
        frame_type = np.tile(frame_type, 2500)

        # timing test
        self.profile(stats, ts_corrected_nitrate, wllower, wlupper,
                     cal_temp, wl, eno3, eswa, di, dark_value,
                     ctd_t, ctd_sp, data_in, frame_type)

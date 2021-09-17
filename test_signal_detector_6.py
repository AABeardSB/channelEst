#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: power test
# Author: Steven Sharp
# GNU Radio version: 3.8.0.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import pmt
import random
import time
import threading
import numpy as np



class untitled(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "power test")

        ##################################################
        # Variables
        ##################################################
#        self.variable_function_probe_17 = variable_function_probe_17 = 0
#        self.variable_function_probe_16 = variable_function_probe_16 = 0
#        self.variable_function_probe_15 = variable_function_probe_15 = 0
#        self.variable_function_probe_14 = variable_function_probe_14 = 0
#        self.variable_function_probe_13 = variable_function_probe_13 = 0
#        self.variable_function_probe_12 = variable_function_probe_12 = 0
#        self.variable_function_probe_11 = variable_function_probe_11 = 0
#        self.variable_function_probe_10 = variable_function_probe_10 = 0
        self.variable_function_probe_9 = variable_function_probe_9 = 0
        self.variable_function_probe_8 = variable_function_probe_8 = 0
        self.variable_function_probe_7 = variable_function_probe_7 = 0
        self.variable_function_probe_6 = variable_function_probe_6 = 0
        self.variable_function_probe_5 = variable_function_probe_5 = 0
        self.variable_function_probe_4 = variable_function_probe_4 = 0
        self.variable_function_probe_3 = variable_function_probe_3 = 0
        self.variable_function_probe_2 = variable_function_probe_2 = 0
        self.variable_function_probe_1 = variable_function_probe_1 = 0
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.source_amp = source_amp = 0.05
        self.samp_rate = samp_rate = 166000000 #166 MHz, twice the bandwidth of our 10 freq's
        self.noise_amp = noise_amp = 0.01
        self.freq_4 = freq_4 = 0
        self.freq_3 = freq_3 = 0
        self.freq_2 = freq_2 = 0
        self.freq_1 = freq_1 = 0
        self.freq_0 = freq_0 = 0

        ##################################################
        # Blocks
        ##################################################
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_1 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_2 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_3 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_4 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_5 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_6 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_7 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_8 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_9 = blocks.probe_signal_f()
#        self.blocks_probe_signal_x_10 = blocks.probe_signal_f()
#        self.blocks_probe_signal_x_11 = blocks.probe_signal_f()
#        self.blocks_probe_signal_x_12 = blocks.probe_signal_f()
#        self.blocks_probe_signal_x_13 = blocks.probe_signal_f()
#        self.blocks_probe_signal_x_14 = blocks.probe_signal_f()
#        self.blocks_probe_signal_x_15 = blocks.probe_signal_f()
#        self.blocks_probe_signal_x_16 = blocks.probe_signal_f()
#        self.blocks_probe_signal_x_17 = blocks.probe_signal_f()
        
        def _variable_function_probe_0_probe():
            while True:

                val = self.blocks_probe_signal_x_0.level()
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()

        def _variable_function_probe_1_probe():
            while True:

                val = self.blocks_probe_signal_x_1.level()
                try:
                    self.set_variable_function_probe_1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_1_thread = threading.Thread(target=_variable_function_probe_1_probe)
        _variable_function_probe_1_thread.daemon = True
        _variable_function_probe_1_thread.start()

        def _variable_function_probe_2_probe():
            while True:

                val = self.blocks_probe_signal_x_2.level()
                try:
                    self.set_variable_function_probe_2(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_2_thread = threading.Thread(target=_variable_function_probe_2_probe)
        _variable_function_probe_2_thread.daemon = True
        _variable_function_probe_2_thread.start()

        def _variable_function_probe_3_probe():
            while True:

                val = self.blocks_probe_signal_x_3.level()
                try:
                    self.set_variable_function_probe_3(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_3_thread = threading.Thread(target=_variable_function_probe_3_probe)
        _variable_function_probe_3_thread.daemon = True
        _variable_function_probe_3_thread.start()

        def _variable_function_probe_4_probe():
            while True:

                val = self.blocks_probe_signal_x_4.level()
                try:
                    self.set_variable_function_probe_4(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_4_thread = threading.Thread(target=_variable_function_probe_4_probe)
        _variable_function_probe_4_thread.daemon = True
        _variable_function_probe_4_thread.start()

        def _variable_function_probe_5_probe():
            while True:

                val = self.blocks_probe_signal_x_5.level()
                try:
                    self.set_variable_function_probe_5(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_5_thread = threading.Thread(target=_variable_function_probe_5_probe)
        _variable_function_probe_5_thread.daemon = True
        _variable_function_probe_5_thread.start()

        def _variable_function_probe_6_probe():
            while True:

                val = self.blocks_probe_signal_x_6.level()
                try:
                    self.set_variable_function_probe_6(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_6_thread = threading.Thread(target=_variable_function_probe_6_probe)
        _variable_function_probe_6_thread.daemon = True
        _variable_function_probe_6_thread.start()

        def _variable_function_probe_7_probe():
            while True:

                val = self.blocks_probe_signal_x_7.level()
                try:
                    self.set_variable_function_probe_7(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_7_thread = threading.Thread(target=_variable_function_probe_7_probe)
        _variable_function_probe_7_thread.daemon = True
        _variable_function_probe_7_thread.start()

        def _variable_function_probe_8_probe():
            while True:

                val = self.blocks_probe_signal_x_8.level()
                try:
                    self.set_variable_function_probe_8(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_8_thread = threading.Thread(target=_variable_function_probe_8_probe)
        _variable_function_probe_8_thread.daemon = True
        _variable_function_probe_8_thread.start()

        def _variable_function_probe_9_probe():
            while True:

                val = self.blocks_probe_signal_x_9.level()
                try:
                    self.set_variable_function_probe_9(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_9_thread = threading.Thread(target=_variable_function_probe_9_probe)
        _variable_function_probe_9_thread.daemon = True
        _variable_function_probe_9_thread.start()

        def _variable_function_probe_10_probe():
            while True:

                val = self.blocks_probe_signal_x_10.level()
                try:
                    self.set_variable_function_probe_10(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
#        _variable_function_probe_10_thread = threading.Thread(target=_variable_function_probe_10_probe)
#        _variable_function_probe_10_thread.daemon = True
#        _variable_function_probe_10_thread.start()

        def _variable_function_probe_11_probe():
            while True:

                val = self.blocks_probe_signal_x_11.level()
                try:
                    self.set_variable_function_probe_11(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
#        _variable_function_probe_11_thread = threading.Thread(target=_variable_function_probe_11_probe)
#        _variable_function_probe_11_thread.daemon = True
#        _variable_function_probe_11_thread.start()

        def _variable_function_probe_12_probe():
            while True:

                val = self.blocks_probe_signal_x_12.level()
                try:
                    self.set_variable_function_probe_12(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
#        _variable_function_probe_12_thread = threading.Thread(target=_variable_function_probe_12_probe)
#        _variable_function_probe_12_thread.daemon = True
#        _variable_function_probe_12_thread.start()

        def _variable_function_probe_13_probe():
            while True:

                val = self.blocks_probe_signal_x_13.level()
                try:
                    self.set_variable_function_probe_13(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
#        _variable_function_probe_13_thread = threading.Thread(target=_variable_function_probe_13_probe)
#        _variable_function_probe_13_thread.daemon = True
#        _variable_function_probe_13_thread.start()

        def _variable_function_probe_14_probe():
            while True:

                val = self.blocks_probe_signal_x_14.level()
                try:
                    self.set_variable_function_probe_14(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
#       _variable_function_probe_14_thread = threading.Thread(target=_variable_function_probe_14_probe)
#       _variable_function_probe_14_thread.daemon = True
#       _variable_function_probe_14_thread.start()

        def _variable_function_probe_15_probe():
            while True:

                val = self.blocks_probe_signal_x_15.level()
                try:
                    self.set_variable_function_probe_15(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
#        _variable_function_probe_15_thread = threading.Thread(target=_variable_function_probe_15_probe)
#        _variable_function_probe_15_thread.daemon = True
#        _variable_function_probe_15_thread.start()

        def _variable_function_probe_16_probe():
            while True:

                val = self.blocks_probe_signal_x_16.level()
                try:
                    self.set_variable_function_probe_16(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
#        _variable_function_probe_16_thread = threading.Thread(target=_variable_function_probe_16_probe)
#        _variable_function_probe_16_thread.daemon = True
#        _variable_function_probe_16_thread.start()

        def _function_probe_17_probe():
            while True:

                val = self.blocks_probe_signal_x_17.level()
                try:
                    self.set_function_probe_17(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
#        _function_probe_17_thread = threading.Thread(target=_function_probe_17_probe)
#        _function_probe_17_thread.daemon = True
#        _function_probe_17_thread.start()

        self.fft_vxx_0 = fft.fft_vcc(10, True, window.blackmanharris(10), True, 1) # 18 -> 10
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 10) # 18 -> 10
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 10) # 18 -> 10
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(5, 1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_2 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_3 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_4 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_5 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_6 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_7 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_8 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_9 = blocks.complex_to_mag_squared(1)
#        self.blocks_complex_to_mag_squared_10 = blocks.complex_to_mag_squared(1)
#        self.blocks_complex_to_mag_squared_11 = blocks.complex_to_mag_squared(1)
#        self.blocks_complex_to_mag_squared_12 = blocks.complex_to_mag_squared(1)
#        self.blocks_complex_to_mag_squared_13 = blocks.complex_to_mag_squared(1)
#        self.blocks_complex_to_mag_squared_14 = blocks.complex_to_mag_squared(1)
#        self.blocks_complex_to_mag_squared_15 = blocks.complex_to_mag_squared(1)
#        self.blocks_complex_to_mag_squared_16 = blocks.complex_to_mag_squared(1)
#        self.blocks_complex_to_mag_squared_17 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_0, source_amp, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_1, source_amp, 0, 0)
        self.analog_sig_source_x_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_2, source_amp, 0, 0)
        self.analog_sig_source_x_3 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_3, source_amp, 0, 0)
        self.analog_sig_source_x_4 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_4, source_amp, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_amp, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 5))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_1, 4))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_add_xx_1, 3))
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_sig_source_x_4, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_1, 0), (self.blocks_probe_signal_x_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_2, 0), (self.blocks_probe_signal_x_2, 0))
        self.connect((self.blocks_complex_to_mag_squared_3, 0), (self.blocks_probe_signal_x_3, 0))
        self.connect((self.blocks_complex_to_mag_squared_4, 0), (self.blocks_probe_signal_x_4, 0))
        self.connect((self.blocks_complex_to_mag_squared_5, 0), (self.blocks_probe_signal_x_5, 0))
        self.connect((self.blocks_complex_to_mag_squared_6, 0), (self.blocks_probe_signal_x_6, 0))
        self.connect((self.blocks_complex_to_mag_squared_7, 0), (self.blocks_probe_signal_x_7, 0))
        self.connect((self.blocks_complex_to_mag_squared_8, 0), (self.blocks_probe_signal_x_8, 0))
        self.connect((self.blocks_complex_to_mag_squared_9, 0), (self.blocks_probe_signal_x_9, 0))
#        self.connect((self.blocks_complex_to_mag_squared_10, 0), (self.blocks_probe_signal_x_10, 0))
#        self.connect((self.blocks_complex_to_mag_squared_11, 0), (self.blocks_probe_signal_x_11, 0))
#        self.connect((self.blocks_complex_to_mag_squared_12, 0), (self.blocks_probe_signal_x_12, 0))
#        self.connect((self.blocks_complex_to_mag_squared_13, 0), (self.blocks_probe_signal_x_13, 0))
#        self.connect((self.blocks_complex_to_mag_squared_14, 0), (self.blocks_probe_signal_x_14, 0))
#        self.connect((self.blocks_complex_to_mag_squared_15, 0), (self.blocks_probe_signal_x_15, 0))
#        self.connect((self.blocks_complex_to_mag_squared_16, 0), (self.blocks_probe_signal_x_16, 0))
#        self.connect((self.blocks_complex_to_mag_squared_17, 0), (self.blocks_probe_signal_x_17, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 4), (self.blocks_complex_to_mag_squared_4, 0))
        self.connect((self.blocks_vector_to_streams_0, 9), (self.blocks_complex_to_mag_squared_9, 0))
   #     self.connect((self.blocks_vector_to_streams_0, 13), (self.blocks_complex_to_mag_squared_13, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_complex_to_mag_squared_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 6), (self.blocks_complex_to_mag_squared_6, 0))
 #       self.connect((self.blocks_vector_to_streams_0, 10), (self.blocks_complex_to_mag_squared_10, 0))
#        self.connect((self.blocks_vector_to_streams_0, 14), (self.blocks_complex_to_mag_squared_14, 0))
#        self.connect((self.blocks_vector_to_streams_0, 16), (self.blocks_complex_to_mag_squared_16, 0))
#        self.connect((self.blocks_vector_to_streams_0, 17), (self.blocks_complex_to_mag_squared_17, 0))
        self.connect((self.blocks_vector_to_streams_0, 2), (self.blocks_complex_to_mag_squared_2, 0))
        self.connect((self.blocks_vector_to_streams_0, 7), (self.blocks_complex_to_mag_squared_7, 0))
#        self.connect((self.blocks_vector_to_streams_0, 11), (self.blocks_complex_to_mag_squared_11, 0))
        self.connect((self.blocks_vector_to_streams_0, 5), (self.blocks_complex_to_mag_squared_5, 0))
        self.connect((self.blocks_vector_to_streams_0, 3), (self.blocks_complex_to_mag_squared_3, 0))
        self.connect((self.blocks_vector_to_streams_0, 8), (self.blocks_complex_to_mag_squared_8, 0))
#        self.connect((self.blocks_vector_to_streams_0, 12), (self.blocks_complex_to_mag_squared_12, 0))
#        self.connect((self.blocks_vector_to_streams_0, 15), (self.blocks_complex_to_mag_squared_15, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_streams_0, 0))

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0

    def get_variable_function_probe_1(self):
        return self.variable_function_probe_1

    def set_variable_function_probe_1(self, variable_function_probe_1):
        self.variable_function_probe_1 = variable_function_probe_1

    def get_variable_function_probe_2(self):
        return self.variable_function_probe_2

    def set_variable_function_probe_2(self, variable_function_probe_2):
        self.variable_function_probe_2 = variable_function_probe_2

    def get_variable_function_probe_3(self):
        return self.variable_function_probe_3

    def set_variable_function_probe_3(self, variable_function_probe_3):
        self.variable_function_probe_3 = variable_function_probe_3

    def get_variable_function_probe_4(self):
        return self.variable_function_probe_4

    def set_variable_function_probe_4(self, variable_function_probe_4):
        self.variable_function_probe_4 = variable_function_probe_4

    def get_variable_function_probe_5(self):
        return self.variable_function_probe_5

    def set_variable_function_probe_5(self, variable_function_probe_5):
        self.variable_function_probe_5 = variable_function_probe_5

    def get_variable_function_probe_6(self):
        return self.variable_function_probe_6

    def set_variable_function_probe_6(self, variable_function_probe_6):
        self.variable_function_probe_6 = variable_function_probe_6

    def get_variable_function_probe_7(self):
        return self.variable_function_probe_7

    def set_variable_function_probe_7(self, variable_function_probe_7):
        self.variable_function_probe_7 = variable_function_probe_7

    def get_variable_function_probe_8(self):
        return self.variable_function_probe_8

    def set_variable_function_probe_8(self, variable_function_probe_8):
        self.variable_function_probe_8 = variable_function_probe_8

    def get_variable_function_probe_9(self):
        return self.variable_function_probe_9

    def set_variable_function_probe_9(self, variable_function_probe_9):
        self.variable_function_probe_9 = variable_function_probe_9

#    def get_variable_function_probe_10(self):
#        return self.variable_function_probe_10
#
#    def set_variable_function_probe_10(self, variable_function_probe_10):
#        self.variable_function_probe_10 = variable_function_probe_10
#
#    def get_variable_function_probe_11(self):
#        return self.variable_function_probe_11
#
#    def set_variable_function_probe_11(self, variable_function_probe_11):
#        self.variable_function_probe_11 = variable_function_probe_11
#
#    def get_variable_function_probe_12(self):
#        return self.variable_function_probe_12
#
#    def set_variable_function_probe_12(self, variable_function_probe_12):
#        self.variable_function_probe_12 = variable_function_probe_12
#
#    def get_variable_function_probe_13(self):
#        return self.variable_function_probe_13
#
#    def set_variable_function_probe_13(self, variable_function_probe_13):
#        self.variable_function_probe_13 = variable_function_probe_13
#
#    def get_variable_function_probe_14(self):
#        return self.variable_function_probe_14
#
#    def set_variable_function_probe_14(self, variable_function_probe_14):
#        self.variable_function_probe_14 = variable_function_probe_14
#
#    def get_variable_function_probe_15(self):
#        return self.variable_function_probe_15
#
#    def set_variable_function_probe_15(self, variable_function_probe_15):
#        self.variable_function_probe_15 = variable_function_probe_15
#
#    def get_variable_function_probe_16(self):
#        return self.variable_function_probe_16
#
#    def set_variable_function_probe_16(self, variable_function_probe_16):
#        self.variable_function_probe_16 = variable_function_probe_16
#
#    def get_variable_function_probe_17(self):
#        return self.variable_function_probe_17
#
#    def set_variable_function_probe_17(self, variable_function_probe_17):
#        self.variable_function_probe_17 = variable_function_probe_17

    def get_source_amp(self):
        return self.source_amp

    def set_source_amp(self, source_amp):
        self.source_amp = source_amp
        self.analog_sig_source_x_1.set_amplitude(self.source_amp)
        self.analog_sig_source_x_0.set_amplitude(self.source_amp)
        self.analog_sig_source_x_2.set_amplitude(self.source_amp)
        self.analog_sig_source_x_3.set_amplitude(self.source_amp)
        self.analog_sig_source_x_4.set_amplitude(self.source_amp)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_4.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)

    def get_freq_4(self):
        return self.freq_4

    def set_freq_4(self, freq_4):
        self.freq_4 = freq_4
        self.analog_sig_source_x_4.set_frequency(self.freq_4)

    def get_freq_3(self):
        return self.freq_3

    def set_freq_3(self, freq_3):
        self.freq_3 = freq_3
        self.analog_sig_source_x_3.set_frequency(self.freq_3)

    def get_freq_2(self):
        return self.freq_2

    def set_freq_2(self, freq_2):
        self.freq_2 = freq_2
        self.analog_sig_source_x_2.set_frequency(self.freq_2)

    def get_freq_1(self):
        return self.freq_1

    def set_freq_1(self, freq_1):
        self.freq_1 = freq_1
        self.analog_sig_source_x_1.set_frequency(self.freq_1)

    def get_freq_0(self):
        return self.freq_0

    def set_freq_0(self, freq_0):
        self.freq_0 = freq_0
        self.analog_sig_source_x_0.set_frequency(self.freq_0)

def argument_parser():
    parser = ArgumentParser()
    return parser

def main(top_block_cls=untitled, options=None):
    if options is None:
        options = argument_parser().parse_args()
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)
    
    tb.start()
    
    all_error = [0 for x in range(160)] # range: match number of files ran through NN validation. Also in range below
    for j in range(160):                            #Begin loop
        freq_list = [2.412E9,2.417E9,2.422E9,2.427E9,2.432E9,2.437E9,2.442E9,2.447E9,2.452E9,2.462E9]   #list of all 2.4Ghz wifi center freqs. Was kHz before?
        Teach_list = [0 for i in range(10)]               # set up teaching list
        freq_pick=[]                                                                   # set up freq picked list

        time.sleep(1)
        tb.lock()                               # Lock flowgraph to change params

        ### Define frequencies and lists
        n = random.sample(freq_list, 5)
        bins = 10 #orig:18 (number of bins to match the number of frequencies in list)
        freq_pick = n
        for i in range(5):
           for k in range(10):
               if freq_pick[i] == freq_list[k]:
                   Teach_list[k] = 1            # designates a used channel for that frequency spot, else for open channel = 0

        
        mag_sqs = [0 for i in range(bins)]
        print("freq_pick" + str(freq_pick))
        print("Teach_list" + str(Teach_list))
        

        ### Set frequencies to new selected values
        tb.set_freq_0(freq_list[0])
        tb.set_freq_1(freq_list[1])
        tb.set_freq_2(freq_list[2])
        tb.set_freq_3(freq_list[3])
        tb.set_freq_4(freq_list[4])

        ### Fill mag_sqs list
        mag_sqs[0] = tb.blocks_probe_signal_x_0.level() # Bin 1
        mag_sqs[1] = tb.blocks_probe_signal_x_1.level() # Bin 2
        mag_sqs[2] = tb.blocks_probe_signal_x_2.level() # Bin 3
        mag_sqs[3] = tb.blocks_probe_signal_x_3.level() # Bin 4
        mag_sqs[4] = tb.blocks_probe_signal_x_4.level() # Bin 5
        mag_sqs[5] = tb.blocks_probe_signal_x_5.level() # Bin 6
        mag_sqs[6] = tb.blocks_probe_signal_x_6.level() # Bin 7
        mag_sqs[7] = tb.blocks_probe_signal_x_7.level() # Bin 8
        mag_sqs[8] = tb.blocks_probe_signal_x_8.level() # Bin 9
        mag_sqs[9] = tb.blocks_probe_signal_x_9.level() # Bin 10
        #mag_sqs[10] = tb.blocks_probe_signal_x_10.level() # Bin 11
        #mag_sqs[11] = tb.blocks_probe_signal_x_11.level() # Bin 12
        #mag_sqs[12] = tb.blocks_probe_signal_x_12.level() # Bin 13
        #mag_sqs[13] = tb.blocks_probe_signal_x_13.level() # Bin 14
        #mag_sqs[14] = tb.blocks_probe_signal_x_14.level() # Bin 15
        #mag_sqs[15] = tb.blocks_probe_signal_x_15.level() # Bin 16
        #mag_sqs[16] = tb.blocks_probe_signal_x_16.level() # Bin 17
        #mag_sqs[17] = tb.blocks_probe_signal_x_17.level() # Bin 18

        ### Find open frequencies
        print("initial mag-squared list: ")
        print(mag_sqs)
        # sort magnitudes-squared from smallest to largest
        sorted_mags = sorted(mag_sqs)[0:5] # 5 used, 5 free
        print("sorted: ")
        print(sorted_mags)
        # Find the bins associated with those mags-squared, then find their freq: The frequency range is (not sure now: 15M). Each of the
        # 10 bins has a range of (not sure:0.83 MHz). So the frequency they register could be anywhere in that range, not just the
        # center frequency. 
        
        
        channel_bool = [1 for i in range(10)]
        # whatever index element is in the lowest mag list, that index in frequency list gets put in open freq list
        for i in range(10):
            if mag_sqs[i] in sorted_mags:
                
                channel_bool[i] = 0
                #open_guess.append(freq_list[i]) 
            
        print("Identified channels:" + str(channel_bool))    
        
        ### Calculate Error
        num_wrong = 0
        
        for i in range(10):
            if channel_bool[i] is not Teach_list[i]:
                
                num_wrong +=1
        print("Number wrong: " + str(num_wrong))

        all_error[j] = float(num_wrong) / 10.0
 
        #print(all_error)
        
        # open_guess = np.array(open_guess) # change from lists to numpy arrays
        # Teach_list = np.array(Teach_list)
        # error = np.abs(open_guess - Teach_list)
    
        tb.unlock()                             # Unlock flowgraph
        time.sleep(1)    
                                                
        print("End of loop")        # End of loop 
        
    print("Error Matrix: " + str(all_error))
        
    all_error = np.array(all_error) # change from lists to numpy arrays
    avg_error = np.mean(all_error) # Average all the elements in "error" to one mean value
    print("Avg. Error: " + str(avg_error))        




    print("After loop")
    time.sleep(1)
    sys.exit()


if __name__ == '__main__':
    main()

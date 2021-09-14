#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Data Files Generator
# Author: Ashley Beard
# GNU Radio version: 3.8.0.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import gr, blocks
import pmt
import random
from random import sample
import time

class data_files_gen(gr.top_block):

    def __init__(self, filename='New_Text_Document_(3).txt'):
        gr.top_block.__init__(self, "Data Files Generator")

        ##################################################
        # Parameters
        ##################################################
        self.filename = filename

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100e6 #166 MHz, twice the bandwidth of our 10 freq's
        self.freq_0 = freq_0 = 1
        self.freq_1 = freq_1 = 1
        self.freq_2 = freq_2 = 1
        self.freq_3 = freq_3 = 1
        self.freq_4 = freq_4 = 1
        self.source_amp = source_amp = 0.05 # SNR = 5
        self.noise_amp = noise_amp = 0.01
        
        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=None)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, filename, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_0, source_amp, 0, 0)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_1, source_amp, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_2, source_amp, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_3, source_amp, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_4, source_amp, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_0, 0))


    #Get and set amplitudes for each block
    def get_source_amp(self):
        return self.source_amp
    def set_source_amp(self, source_amp):
        self.source_amp = source_amp
        self.analog_sig_source_x_0.set_amplitude(self.source_amp)
        self.analog_sig_source_x_0_0.set_amplitude(self.source_amp)
        self.analog_sig_source_x_0_0_0.set_amplitude(self.source_amp)
        self.analog_sig_source_x_0_0_0_0.set_amplitude(self.source_amp)
        self.analog_sig_source_x_0_0_0_0_0.set_amplitude(self.source_amp)

    def get_noise_amp(self):
        return self.noise_amp
    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)
        
    #Get and set frequencies for each block
    def get_freq_0(self):
        return self.freq_0
    def set_freq_0(self, freq_0):
        self.freq_0 = freq_0
        self.analog_sig_source_x_0_0_0_0_0.set_frequency(self.freq_0)

    def get_freq_1(self):
        return self.freq_1
    def set_freq_1(self, freq_1):
        self.freq_1 = freq_1
        self.analog_sig_source_x_0_0_0_0.set_frequency(self.freq_1)

    def get_freq_2(self):
        return self.freq_2
    def set_freq_2(self, freq_2):
        self.freq_2 = freq_2
        self.analog_sig_source_x_0_0_0.set_frequency(self.freq_2)

    def get_freq_3(self):
        return self.freq_3
    def set_freq_3(self, freq_3):
        self.freq_3 = freq_3
        self.analog_sig_source_x_0_0.set_frequency(self.freq_3)

    def get_freq_4(self):
        return self.freq_4
    def set_freq_4(self, freq_4):
        self.freq_4 = freq_4
        self.analog_sig_source_x_0.set_frequency(self.freq_4)

    #Same sample rate for every block
    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_filename(self):
        return self.filename
    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_sink_0.open(self.filename)

    def pause(self, timer): # Do nothing until the timer is up
        flag = 0
        while (flag == 0):
            if (timer.remainingTime() == 0):
              flag = 1

def argument_parser():
    parser = ArgumentParser()
    return parser


def main(top_block_cls=data_files_gen, options=None):
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
    
    for j in range(800):                            #Begin loop

        freq_list = [2412000000,2417000000,2422000000,2427000000,2432000000,2437000000,2442000000,2447000000,2452000000,2462000000] #list of all 2.4Ghz wifi center freqs (although registers as kHz)
        Teach_list = [2412000000,2417000000,2422000000,2427000000,2432000000,2437000000,2442000000,2447000000,2452000000,2462000000]               # set up teaching list
        freq_pick=[]                                                                   # set up freq picked list

        time.sleep(0.5)   # 0.5 second 
        tb.lock()                               # Lock flowgraph to change params

 
        n = random.sample(freq_list, 5)
        freq_pick = n
        Teach_list = [x for x in freq_list if x not in freq_pick]
        print("freq_pick" + str(freq_pick))
        print("Teach_list" + str(Teach_list))
            
        file_name_teach = str("Teach_"+str(j) +".txt")      # makes a file handle -> file is generated where ever this is run
        tb.set_filename(str("Feature_List_" + str(j) + ".txt"))
        f= open(file_name_teach,"w+")                           # opens/makes file
        f.write("This is Teaching file number: " +  str(j) + "\n")      # write first line of teaching file we can change this to be more discriptive        
        f.write(str(Teach_list[0]) + ",")
        f.write(str(Teach_list[1]) + ",")
        f.write(str(Teach_list[2]) + ",")
        f.write(str(Teach_list[3]) + ",")
        f.write(str(Teach_list[4]))                                     # writes teaching list
        f.close()
        
        tb.set_freq_0(freq_pick[0])
        print(freq_pick[0])
        tb.set_freq_1(freq_pick[1])
        tb.set_freq_2(freq_pick[2])
        tb.set_freq_3(freq_pick[3])
        tb.set_freq_4(freq_pick[4])
        
        
        tb.unlock()                             # Unlock flowgraph
        time.sleep(1)   # 1 seconds

                                                # End of loop
        print("End of loop")

    print("After loop")
    time.sleep(0.5)   # 0.5 second
    sys.exit()
    

if __name__ == '__main__':
    main()

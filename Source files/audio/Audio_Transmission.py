#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: lenovo
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import soapy
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class Audio_Transmission(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Audio_Transmission")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.qpsk = qpsk = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j], [0, 1, 2, 3],
        4, 2, 2, 1, 1).base()
        self.nfilts = nfilts = 32
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_cma( qpsk, 100e-6, 4).base()
        self.timing_loop_bw = timing_loop_bw = 62.8e-3
        self.time_offset = time_offset = 1
        self.samp_rate = samp_rate = 1024000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.phase_bw = phase_bw = 62.8e-3
        self.noise_volt = noise_volt = 0
        self.freq_offset = freq_offset = 0
        self.freq = freq = 2450000000
        self.excess_bw = excess_bw = 0.5
        self.const = const = 1
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0, 0.2, 0.01, 62.8e-3, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, "Timing: BW", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._timing_loop_bw_win)
        self._phase_bw_range = Range(0, 1, 0.01, 62.8e-3, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, "Phase: Bandwidth", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._phase_bw_win)
        self._time_offset_range = Range(0.999, 1.001, 10e-6, 1, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, "Timing Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._time_offset_win)
        self.soapy_bladerf_source_0 = None
        dev = 'driver=bladerf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_bladerf_source_0 = soapy.source(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_bladerf_source_0.set_sample_rate(0, samp_rate)
        self.soapy_bladerf_source_0.set_bandwidth(0, 0.0)
        self.soapy_bladerf_source_0.set_frequency(0, freq)
        self.soapy_bladerf_source_0.set_frequency_correction(0, 0)
        self.soapy_bladerf_source_0.set_gain(0, min(max(20.0, -1.0), 60.0))
        self.soapy_bladerf_sink_0 = None
        dev = 'driver=bladerf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_bladerf_sink_0 = soapy.sink(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_bladerf_sink_0.set_sample_rate(0, samp_rate)
        self.soapy_bladerf_sink_0.set_bandwidth(0, 0.0)
        self.soapy_bladerf_sink_0.set_frequency(0, freq)
        self.soapy_bladerf_sink_0.set_frequency_correction(0, 0)
        self.soapy_bladerf_sink_0.set_gain(0, min(max(20.0, 17.0), 73.0))
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=100,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=100,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
            1024,
            100,
            -1,
            1,
            "",
            1,
            None # parent
        )

        self.qtgui_histogram_sink_x_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(False)
        self.qtgui_histogram_sink_x_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_histogram_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self._noise_volt_range = Range(0, 1, 0.01, 0, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, "'noise_volt'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_volt_win)
        self._freq_offset_range = Range(-0.1, 0.1, 1e-3, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, "Frequency Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_offset_win)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_loop_bw, rrc_taps, nfilts, nfilts/2, 1.5, 2)
        self.digital_linear_equalizer_0 = digital.linear_equalizer(15, 2, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, arity, False)
        self._const_range = Range(1, 10, 1, 1, 200)
        self._const_win = RangeWidget(self._const_range, self.set_const, "constant", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._const_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/shevi/Documents/GNU radio/audio/sending voice.wav', False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            'C:\\Users\\receiver.wav',
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=samp_rate,
        	quad_rate=samp_rate,
        	tau=75e-6,
        	max_dev=5e+3,
        	fh=-1.0,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=samp_rate,
        	audio_decimation=1,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_histogram_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.digital_linear_equalizer_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_linear_equalizer_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.soapy_bladerf_sink_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.soapy_bladerf_source_0, 0), (self.rational_resampler_xxx_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Audio_Transmission")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.soapy_bladerf_sink_0.set_sample_rate(0, self.samp_rate)
        self.soapy_bladerf_source_0.set_sample_rate(0, self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps(self.rrc_taps)

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.soapy_bladerf_sink_0.set_frequency(0, self.freq)
        self.soapy_bladerf_source_0.set_frequency(0, self.freq)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity




def main(top_block_cls=Audio_Transmission, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

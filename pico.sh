#!/bin/bash
pico2wave -w /tmp/out.wav "$*" && mplayer /tmp/out.wav &> /tmp/pico.log

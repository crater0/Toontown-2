// Filename: config_windisplay.h
// Created by:  drose (20Dec02)
//
////////////////////////////////////////////////////////////////////
//
// PANDA 3D SOFTWARE
// Copyright (c) Carnegie Mellon University.  All rights reserved.
//
// All use of this software is subject to the terms of the revised BSD
// license.  You should have received a copy of this license along
// with this source code in a file named "LICENSE."
//
////////////////////////////////////////////////////////////////////

#ifndef CONFIG_WINDISPLAY_H
#define CONFIG_WINDISPLAY_H

#include "pandabase.h"
#include "filename.h"
#include "notifyCategoryProxy.h"
#include "configVariableBool.h"

NotifyCategoryDecl(windisplay, EXPCL_PANDAWIN, EXPTP_PANDAWIN);

extern ConfigVariableBool responsive_minimized_fullscreen_window;
extern ConfigVariableBool hold_keys_across_windows;
extern ConfigVariableBool do_vidmemsize_check;
extern ConfigVariableBool auto_cpu_data;
extern ConfigVariableBool ime_composition_w;
extern ConfigVariableBool ime_aware;
extern ConfigVariableBool ime_hide;
extern ConfigVariableBool request_dxdisplay_information;

extern EXPCL_PANDAWIN ConfigVariableBool swapbuffer_framelock;

extern EXPCL_PANDAWIN void init_libwindisplay();

#endif

# Copyright 2013 Ben Vanik. All Rights Reserved.
{
  'sources': [
    'assert.h',
    'atomic.h',
    'byte_order.h',
    'common.h',
    'config.h',
    'core.h',
    'emulator.cc',
    'emulator.h',
    'export_resolver.cc',
    'export_resolver.h',
    'logging.cc',
    'logging.h',
    'malloc.cc',
    'malloc.h',
    'memory.cc',
    'memory.h',
    'platform.cc',
    'platform.h',
    'platform_includes.h',
    'string.cc',
    'string.h',
    'types.h',
    'xbox.h',
    'xenia.h',
  ],

  'includes': [
    'apu/sources.gypi',
    'core/sources.gypi',
    'cpu/sources.gypi',
    'dbg/sources.gypi',
    'gpu/sources.gypi',
    'kernel/sources.gypi',
  ],
}

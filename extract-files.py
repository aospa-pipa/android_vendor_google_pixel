#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 Paranoid Android
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import ExtractUtils
from extract_utils_pixel.module import ExtractUtilsPixelModule


module = ExtractUtilsPixelModule()

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

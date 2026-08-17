#
# SPDX-FileCopyrightText: 2026 Paranoid Android
# SPDX-License-Identifier: Apache-2.0
#

from os import path

from extract_utils.module import ExtractUtilsModule
from extract_utils.utils import remove_dir_contents

class ExtractUtilsPixelModule(ExtractUtilsModule):
    def __init__(self):
        super().__init__(
            device='pixel',
            vendor='google',
            device_rel_path=path.join('vendor', 'google', 'pixel'),
        )

    def cleanup(self):
        for proprietary_file in self.proprietary_files:
            vendor_path = self.proprietary_file_vendor_path(proprietary_file)
            remove_dir_contents(vendor_path)

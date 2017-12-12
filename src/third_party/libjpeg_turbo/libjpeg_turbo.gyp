# Copyright 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# We got 'libjpeg_turbo' and 'src/libjpeg.gyp' from Chromium. 'src/libjpeg.gyp'
# has set up the dependency to 'yasm', but does not include all files
# which 'mod_pagespeed' needs. The additional files are included here.
{
      'targets': [
        {
          'target_name': 'libjpeg_turbo',
          'type': 'none',
          'direct_dependent_settings': {
            'defines': [
              'USE_SYSTEM_LIBJPEG',
            ],
          },
          'link_settings': {
            'libraries': [
              '-ljpeg',
            ],
          },
        }
      ],
}

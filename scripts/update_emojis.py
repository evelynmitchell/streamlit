#!/usr/bin/env python

# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2025)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Update the list of emojis in `lib/streamlit/emojis.py.

This script requires the emoji package to be installed: pip install emoji.
"""

import os
import re

from emoji.unicode_codes import EMOJI_DATA
from streamlit.emojis import ALL_EMOJIS

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EMOJI_SET_REGEX = re.compile(r"### EMOJIS START ###(.+?)### EMOJIS END ###", re.DOTALL)
EMOJIS_SCRIPT_PATH = os.path.join(BASE_DIR, "lib", "streamlit", "emojis.py")

emoji_unicodes = set(EMOJI_DATA.keys())

print(f"Existing emoji collection: {len(ALL_EMOJIS)}")
print(f"New emoji collection:  {len(emoji_unicodes)}")

generated_code = f"""### EMOJIS START ###
ALL_EMOJIS = {{{", ".join([f'"{emoji}"' for emoji in sorted(emoji_unicodes)])}}}
### EMOJIS END ###"""

with open(EMOJIS_SCRIPT_PATH, "r") as file:
    script_content = file.read()

updated_script_content = re.sub(EMOJI_SET_REGEX, generated_code, script_content)

with open(EMOJIS_SCRIPT_PATH, "w") as file:
    file.write(updated_script_content)

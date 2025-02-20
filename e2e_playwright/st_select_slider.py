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

import numpy as np
import pandas as pd

import streamlit as st
from streamlit import runtime


def format_option(option):
    return f"Color: {option}"


w1 = st.select_slider(
    "Label 1 (format_func with key and help)",
    value=("orange", "blue"),
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    format_func=format_option,
    key="first_select_slider",
    help="Help in a select slider",
)
if "first_select_slider" in st.session_state:
    st.write("Value 1:", st.session_state.first_select_slider)
st.write("Value 1:", w1)

w2 = st.select_slider(
    "Label 2 (no default)",
    options=np.array([1, 2, 3, 4, 5]),
)
st.write("Value 2:", w2)

w3 = st.select_slider(
    "Label 3 (default with ints and series)",
    value=[2, 5],
    options=pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9]),
)
st.write("Value 3:", w3)

w4 = st.select_slider(
    "Label 4 (default with pandas df)",
    value=5,
    options=pd.DataFrame(
        {
            "first column": [1, 2, 3, 4, 5],
            "second column": [10, 20, 30, 40, 50],
        }
    ),
)
st.write("Value 4:", w4)

w5 = st.select_slider(
    "Label 5 (disabled)",
    value=("orange", "blue"),
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    disabled=True,
)
st.write("Value 5:", w5)

w6 = st.select_slider(
    "Label 6 (hidden visibility)",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    label_visibility="hidden",
)

st.write("Value 6:", w6)


w7 = st.select_slider(
    "Label 7 (collapsed visibility)",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    label_visibility="collapsed",
)

st.write("Value 7:", w7)

if runtime.exists():

    def on_change():
        st.session_state.select_slider_changed = True
        st.write("Hello world")

    st.select_slider(
        "Label 8 (on change)",
        options=np.array([1, 2, 3, 4, 5]),
        key="select_slider8",
        on_change=on_change,
    )
    st.write("Value 8:", st.session_state.select_slider8)
    st.write("Select slider changed:", "select_slider_changed" in st.session_state)

with st.expander("Expander", expanded=True):
    w9 = st.select_slider(
        label="Label 9 (expander)",
        options=["foo", "bar", "baz", "This is a very, very long option"],
        value="This is a very, very long option",
    )

    st.write("Value 9:", w9)

with st.form(key="my_form", clear_on_submit=True):
    selection = st.select_slider(
        label="Label 10 (form)",
        options=np.array([1, 2, 3, 4, 5]),
    )
    st.form_submit_button("Submit")

st.write("select_slider-in-form selection:", str(selection))


@st.fragment
def test_fragment():
    selection = st.select_slider(
        label="Label 11 (fragment)",
        options=np.array([1, 2, 3, 4, 5]),
    )
    st.write("select_slider-in-fragment selection:", str(selection))


test_fragment()

st.select_slider(
    "Label 12 -> :material/check: :rainbow[Fancy] _**markdown** `label` _support_",
    options=np.array([1, 2, 3, 4, 5]),
)

if "runs" not in st.session_state:
    st.session_state.runs = 0
st.session_state.runs += 1
st.write("Runs:", st.session_state.runs)

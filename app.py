import streamlit as st

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

st.markdown("""# This is a header
## This is a sub header
### This is H3
This is line count {}
This is text""".format(line_count))

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

import datetime

d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

def get_data():
    return pd.DataFrame(
            np.random.randn(3, 3),
            columns=['a', 'b', 'c'])

@st.cache
def get_cached_data():
    return get_data()

st.write("Uncached dataframe")
df1 = get_data()
df1

st.write("Cached dataframe")
df2 = get_cached_data()
df2

import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache
def get_data():
    return pd.read_csv("https://raw.githubusercontent.com/LinneaLager/Prophet_Covid_19/main/df_prophet.csv")

df = get_data()
st.title("Förutsäg utvecklingen för COVID-19 och dess smittospridning")
st.markdown("Welcome to this in-depth introduction to [Streamlit](www.streamlit.io)! For this exercise, we'll use an Airbnb [dataset](http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv) containing NYC listings.")
st.header("Customary quote")
st.markdown("> I just love to go home, no matter where I am, the most luxurious hotel suite in the world, I love to go home.\n\n—Michael Caine")
st.header("Airbnb NYC listings: data at a glance")
st.markdown("The first five records of the Airbnb data we downloaded.")
st.dataframe(df.head())
st.header("Caching our data")
st.markdown("Streamlit has a handy decorator [`st.cache`](https://streamlit.io/docs/api.html#optimize-performance) to enable data caching.")
st.code("""
@st.cache
def get_data():
    url = "https://raw.githubusercontent.com/LinneaLager/Prophet_Covid_19/main/df_prophet.csv"
    return pd.read_csv(url)
""", language="python")
st.markdown("_To display a code block, pass in the string to display as code to [`st.code`](https://streamlit.io/docs/api.html#streamlit.code)_.")
with st.echo():
    st.markdown("Alternatively, use [`st.echo`](https://streamlit.io/docs/api.html#streamlit.echo).")

#t.header("Where are the most expensive properties located?")
#st.subheader("On a map")
#st.markdown("The following map shows the top 1% most expensive Airbnbs priced at $800 and above.")
#st.map(df.query("price>=800")[["latitude", "longitude"]].dropna(how="any"))
#st.subheader("In a table")
#st.markdown("Following are the top five most expensive properties.")
#st.write(df.query("price>=800").sort_values("price", ascending=False).head())

#st.subheader("Selecting a subset of columns")
#st.write(f"Out of the {df.shape[1]} columns, you might want to view only a subset. Streamlit has a [multiselect](https://streamlit.io/docs/api.html#streamlit.multiselect) widget for this.")
#defaultcols = ["name", "host_name", "neighbourhood", "room_type", "price"]
#cols = st.multiselect("Columns", df.columns.tolist(), default=defaultcols)
#st.dataframe(df[cols].head(10))

st.header("What is the distribution of property price?")
st.write("""Select a custom price range from the side bar to update the histogram below displayed as a Plotly chart using
[`st.plotly_chart`](https://streamlit.io/docs/api.html#streamlit.plotly_chart).""")
values = st.sidebar.slider("Price range", float(df.y.min()), float(df.y.clip(upper=1000.).max()), (50., 300.))
f = px.histogram(df.query(f"price.between{values}"), x="ds", nbins=15, title="Price distribution")
f.update_xaxes(title="Price")
f.update_yaxes(title="No. of listings")
st.plotly_chart(f)

#st.header("What is the distribution of availability in various neighborhoods?")
#st.write("Using a radio button restricts selection to only one option at a time.")
#st.write("💡 Notice how we use a static table below instead of a data frame. \
#Unlike a data frame, if content overflows out of the section margin, \
#a static table does not automatically hide it inside a scrollable area. \
#Instead, the overflowing content remains visible.")
#neighborhood = st.radio("Neighborhood", df.neighbourhood_group.unique())
#show_exp = st.checkbox("Include expensive listings")
#show_exp = " and price<200" if not show_exp else ""


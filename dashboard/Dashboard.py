import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_bywindspeed_df(df):
    bywindspeed_df = df.groupby(by="season", as_index=False).agg({
        "windspeed": "mean"
    }).sort_values(by="windspeed", ascending=False)
    

    return bywindspeed_df

def create_byweathersit_df(df):
    byweathersit_df = df.groupby(by="season", as_index=False).agg({
        "weathersit": "mean"
    }).sort_values(by="weathersit", ascending=True)

    return byweathersit_df

# def create_windspeedmean_df(df):
#     windspeedmean_df = df[["instant", "windspeed"]].groupby("windspeed")["instant"].mean().reset_index
#     index = windspeedmean_df.index
#     windspeedmean_df = pd.DataFrame({"windspeed": index, "avg speed": windspeedmean_df})
#     return windspeedmean_df

# def create_weathersitmean_df(df):
#     weathersitmean_df = df[["instant", "weathersit"]].groupby("weathersit")["instant"].mean().reset_index
#     index = weathersitmean_df.index
#     weathersitmean_df = pd.DataFrame({"weathersit": index, "avg weathersit": weathersitmean_df})
#     return weathersitmean_df

all_df = pd.read_csv("main_data.csv")

bywindspeed_df = create_bywindspeed_df(all_df)
byweathersit_df = create_byweathersit_df(all_df)
# windspeedmean_df = create_windspeedmean_df(all_df)
# weathersitmean_df = create_weathersitmean_df(all_df)

st.header('Submission Dashboard :sparkles:')

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(30, 30))
    colors = ["#EF4040", "#90CAF9", "#D3D3D3", "#E3651D"]
    
    sns.barplot(
        x="season", 
        y="windspeed", 
        data=bywindspeed_df.sort_values(by="windspeed", ascending=False),
        palette = colors,
        ax=ax
    )
    ax.set_title("Rata rata kecepatan angin per Musim", loc="center", fontsize=100)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=100)
    ax.tick_params(axis='y', labelsize=100)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(31, 30))
    colors = ["#BED754", "#90CAF9", "#F4CE14", "#5272F2"]
    
    sns.barplot(
        x="season", 
        y="weathersit",
        data=byweathersit_df.sort_values(by="weathersit", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title("Rata rata cuaca per Musim", loc="center", fontsize=100)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=100)
    ax.tick_params(axis='y', labelsize=100)
    st.pyplot(fig)

# st.subheader('Windspeed')

# fig = plt.figure(figsize=(10,5))
# plt.plot(
#     bywindspeed_df["season"],
#     bywindspeed_df["windspeed"],
#     marker='o',
#     linewidth=2,
#     color="#72BCD4"
# )
# plt.title("Rata rata kecepatan angin per Musim", loc="center", fontsize=25)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.xlabel('Musim', fontsize=18)
# plt.ylabel('Kecepatan Angin (m/s)', fontsize=18)
# plt.legend(['Angin'])
# plt.grid()
# st.pyplot(fig)



# st.subheader('Weathersit')

# fig = plt.figure(figsize=(10,5))
# plt.plot(
#     byweathersit_df["season"],
#     byweathersit_df["weathersit"],
#     marker='o',
#     linewidth=2,
#     color="#72BCD3"
# )
# plt.title("Rata rata cuaca per Musim", loc="center", fontsize=25)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.xlabel('Musim', fontsize = 18)
# plt.ylabel('Perubahan Cuaca', fontsize = 18)
# plt.grid()
# st.pyplot(fig)

st.caption('Copyright © Ryan Gading Abdullah 2023')
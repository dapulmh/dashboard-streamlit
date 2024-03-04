import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np


def get_by_weathersit(df):
    data_by_weathersit = df.groupby(by="weathersit").agg({
        "cnt": "sum"
    })
    data_by_weathersit.rename(columns={
        "cnt": "count_customer"
    }, inplace=True)
    return data_by_weathersit


def get_by_season(df):
    data_by_season = df.groupby(by="season").agg({
        "cnt": "sum"
    })
    data_by_season.rename(columns={
        "cnt": "count_customer"
    }, inplace=True)
    return data_by_season


day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

day_data_by_weathersit = get_by_weathersit(day_df)
day_data_by_season = get_by_season(day_df)

hour_data_by_weathersit = get_by_weathersit(hour_df)
hour_data_by_season = get_by_season(hour_df)

st.title("Pengaruh Keadaan Cuaca dan Musim terkait Jumlah Customer")
st.subheader("Created by : Daffa Maulana Haekal")


tab1, tab2 = st.tabs(["Dataset Day", "Dataset Hour"])

with tab1:

    colors = ["#7fff00", "#ffcc00", "#ff9900", "#ff0000"]
    labels = ['1: Clear, Few clouds, Partly cloudy, Partly cloudy', '2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist', '3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
              '4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog']

    st.header("Berdasarkan Dataset Day.csv")

    plt.figure(figsize=(14, 8))

    bars = sns.barplot(
        y=day_data_by_weathersit["count_customer"],
        x=day_data_by_weathersit.index,
        data=day_data_by_weathersit.sort_values(
            by="count_customer", ascending=False),
        palette=colors
    )
    plt.title("Number of Customer by Weather Situation",
              loc="center", fontsize=24)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='x', labelsize=12)
    plt.show()

    for i, label in enumerate(labels):
        plt.plot([], [], color=colors[i], label=label)

    plt.legend()

    st.pyplot(plt)

    st.text("""    Bisa dilihat berdasarkan analisis untuk dataset Day.csv, keadaan cuaca 
    berpengaruh sekali terhadap jumlah pelanggan peminjaman sepeda dimana pengunjung 
    tertinggi berada pada saat cuaca cerah dan sedikit berawan""")

    colors = ["#445B89", "#8D6AA9", "#FFD082", "#3F9E6E"]
    labels = ['1:springer', '2:summer', '3:fall', '4:winter']

    plt.figure(figsize=(14, 8))

    bars = sns.barplot(
        y=day_data_by_season["count_customer"],
        x=day_data_by_season.index,
        data=day_data_by_season.sort_values(
            by="count_customer", ascending=False),
        palette=colors
    )
    plt.title("Number of Customer by Season", loc="center", fontsize=24)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='x', labelsize=12)
    plt.show()

    for i, label in enumerate(labels):
        plt.plot([], [], color=colors[i], label=label)

    plt.legend()

    st.pyplot(plt)

    st.text("""    Bisa dilihat berdasarkan analisis untuk dataset Day.csv, keadaan 
    musim cukup berpengaruh akan tetapi tidak sesignifikan keadaan cuaca terhadap 
    peningkatan jumlah pelanggan peminjaman sepeda. Pengunjung tertinggi berada
    pada saat musim fall""")


with tab2:
    st.header("Berdasarkan Dataset Hour.csv")

    colors = ["#7fff00", "#ffcc00", "#ff9900", "#ff0000"]
    labels = ['1: Clear, Few clouds, Partly cloudy, Partly cloudy', '2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist', '3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
              '4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog']

    plt.figure(figsize=(14, 8))

    bars = sns.barplot(
        y=hour_data_by_weathersit["count_customer"],
        x=hour_data_by_weathersit.index,
        data=hour_data_by_weathersit.sort_values(
            by="count_customer", ascending=False),
        palette=colors
    )
    plt.title("Number of Customer by Weather Situation",
              loc="center", fontsize=24)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='x', labelsize=12)
    plt.show()

    for i, label in enumerate(labels):
        plt.plot([], [], color=colors[i], label=label)

    plt.legend()

    st.pyplot(plt)

    st.text("""    Bisa dilihat berdasarkan analisis untuk dataset Hour.csv, hubungannya sama 
    dengan dataset Day.csv dimana keadaan cuaca berpengaruh sekali terhadap jumlah pelanggan 
    peminjaman sepeda dimana pengunjung tertinggi berada pada saat cuaca cerah dan 
    sedikit berawan""")

    colors = ["#445B89", "#8D6AA9", "#FFD082", "#3F9E6E"]
    labels = ['1:springer', '2:summer', '3:fall', '4:winter']

    plt.figure(figsize=(14, 8))

    bars = sns.barplot(
        y=hour_data_by_season["count_customer"],
        x=hour_data_by_season.index,
        data=hour_data_by_season.sort_values(
            by="count_customer", ascending=False),
        palette=colors
    )
    plt.title("Number of Customer by Season", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='y', labelsize=12)
    plt.show()

    for i, label in enumerate(labels):
        plt.plot([], [], color=colors[i], label=label)

    plt.legend()

    st.pyplot(plt)

    st.text("""    Bisa dilihat berdasarkan analisis untuk dataset Hour.csv, 
    hubungannya sama dengan dataset Day.csv keadaan musim cukup berpengaruh 
    akan tetapi tidak sesignifikan keadaan cuaca terhadap jumlah pelanggan 
    peminjaman sepeda. Pengunjung tertinggi berada pada saat musim fall""")

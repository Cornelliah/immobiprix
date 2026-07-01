import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

data_geoloc = pd.read_csv("data_geoloc.csv")

center_lat = data_geoloc["latitude"].mean()
center_lon = data_geoloc["longitude"].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=14)

for _, row in data_geoloc.iterrows():
    try:
        lat = float(row["latitude"])
        lon = float(row["longitude"])

        
        popup_text = f"""
        <b>Type :</b> {row['type_bien']}<br>
        <b>Surface :</b> {row['surface_m2']} m²<br>
        <b>Pièces :</b> {row['nb_pieces']}<br>
        <b>Chambres :</b> {row['nb_chambres']}<br>
        <b>Étage :</b> {row['etage']}<br>
        <b>DPE :</b> {row['dpe']}<br>
        <b>Code postal :</b> {row['code_postal']}
        """

        folium.Marker(
            location=[lat, lon],
            icon=folium.Icon(color="red", icon="home"),
            popup=folium.Popup(popup_text, max_width=300)
        ).add_to(m)

    except (ValueError, TypeError):
        st.warning(f"Coordonnées invalides pour : {row}")

st_data = st_folium(m, width=725)

import streamlit as st
import folium
import pandas as pd
from pages.accueil import page_accueil
from pages.estimation import page_estimation
from streamlit_folium import st_folium



pages = [
    st.Page(page_accueil, title="Accueil", default=True),
    st.Page(page_estimation, title="Estimation"),
    st.Page("pages/carte.py", title="Carte")
]


pg = st.navigation(pages)

pg.run()




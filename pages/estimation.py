import streamlit as st
import joblib
from pred import ft_pred

def page_estimation():
    st.title("Estimer le prix d'un bien")

    encoder_type = joblib.load("utils/encoder_type.joblib")
    encoder_etage = joblib.load("utils/encoder_etage.joblib")

    types_bien = list(encoder_type.classes_)
    etages = list(encoder_etage.classes_)
    dpe = ["A","B","C","D","E","F","G"]

    st.selectbox("Types de bien", types_bien, key="Types de bien")
    st.number_input("Surface en m2", key="Surface en m2")
    st.number_input("Nombre de pièces", key="Nombre de pièces")
    st.number_input("Nombre de chambres", key="Nombre de chambres")
    st.selectbox("Etage", etages, key="Etage")
    st.selectbox("DPE", dpe, key="dpe")
    st.number_input("Code postal", key="Code postal")

    def lancer_prediction():
        infos = {
            "type_bien": st.session_state["Types de bien"],
            "surface_m2": st.session_state["Surface en m2"],
            "nb_pieces": st.session_state["Nombre de pièces"],
            "nb_chambres": st.session_state["Nombre de chambres"],
            "etage": st.session_state["Etage"],
            "dpe": st.session_state["dpe"],
            "code_postal": st.session_state["Code postal"],
        }
        st.session_state["resultat"] = ft_pred(infos)

    st.button("Estimer le prix", on_click=lancer_prediction)

    if "resultat" in st.session_state:
        st.success(f"Prix estimé : {st.session_state['resultat']:.0f} €")

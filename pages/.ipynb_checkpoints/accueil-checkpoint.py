import streamlit as st

def page_accueil():
    st.title("🏡 Estimation Immobilière")
    st.subheader("Obtenez une estimation fiable et instantanée de votre bien")

    st.markdown("---")

   
    st.markdown("""
    ### 📌 À propos de l'application

    Cette application vous permet d’estimer le prix d’un bien immobilier à partir de ses caractéristiques
    (type de logement, surface, nombre de pièces, étage, DPE, code postal…).

    Elle s’appuie sur un **modèle de machine learning** entraîné sur des données réelles du marché,
    ainsi que sur des **encodages automatiques** pour traiter les informations catégorielles.
    """)

    st.markdown("---")

   
    st.markdown("###  Fonctionnalités principales")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 📊 Estimation")
        st.write("Remplissez un formulaire simple et obtenez une estimation instantanée.")

    with col2:
        st.markdown("#### 🗂️ Modèle ML")
        st.write("Le prix est calculé grâce à un modèle entraîné sur des données du marché.")

    with col3:
        st.markdown("#### 🧭 Navigation")
        st.write("Accédez facilement aux différentes pages grâce au menu intégré.")

    st.markdown("---")

   
    # Comment ça marche
    st.markdown("""
    ### 🧠 Comment ça marche ?
    1. Vous remplissez les caractéristiques du bien  
    2. Le modèle analyse les données  
    3. Une estimation personnalisée est générée  
    """)

    st.markdown("---")
    st.caption("Application développée dans le cadre d’un projet de data science.")

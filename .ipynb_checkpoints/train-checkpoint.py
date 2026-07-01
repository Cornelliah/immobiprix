import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
import joblib


def load_data(csv_path="data.csv"):
    return pd.read_csv(csv_path)


def encode_columns(data):

    encoder_type = LabelEncoder()
    data["type_bien"] = encoder_type.fit_transform(data["type_bien"])

    encoder_etage = LabelEncoder()
    data["etage"] = encoder_etage.fit_transform(data["etage"].astype(str))

    mapping_dpe = {
        "A": 1, "B": 2, "C": 3,
        "D": 4, "E": 5, "F": 6, "G": 7
    }
    data["dpe"] = data["dpe"].map(mapping_dpe)

    return data, encoder_type, encoder_etage


def extract_target(data):
    return data["prix_eur"]


def ft_train():
    print("Chargement du dataset...")
    data = load_data()
    data = data[data["prix_eur"]<5000000]

    print("Encodage des colonnes...")
    data, encoder_type, encoder_etage = encode_columns(data)

    print("Extraction de la target...")
    y = extract_target(data)

    
    cols_to_drop = ["Unnamed: 0", "url", "latitude", "longitude", "prix_eur", "prix_m2", "adresse"]
    X = data.drop(columns=[c for c in cols_to_drop if c in data.columns])
    X = X.fillna(-100000)

  
    model = GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        random_state=42
    )
    model.fit(X, y)

    
    joblib.dump(encoder_etage, "utils/encoder_etage.joblib")
    joblib.dump(encoder_type, "utils/encoder_type.joblib")
    joblib.dump(model, "utils/model.joblib")

    print("Modèle et encoders sauvegardés dans utils/")


if __name__ == "__main__":
    ft_train()

import pandas as pd
import joblib

def ft_pred(infos_bien):
    
    encoder_etage = joblib.load("utils/encoder_etage.joblib")
    encoder_type = joblib.load("utils/encoder_type.joblib")

    model = joblib.load("utils/model.joblib")

    mapping_dpe = {
        "A": 1, "B": 2, "C": 3,
        "D": 4, "E": 5, "F": 6, "G": 7
    }

    df = pd.DataFrame([{
        "type_bien": infos_bien["type_bien"],
        "surface_m2": infos_bien["surface_m2"],
        "nb_pieces": infos_bien["nb_pieces"],
        "nb_chambres": infos_bien["nb_chambres"],
        "etage": str(infos_bien["etage"]),
        "dpe": infos_bien["dpe"],
        "code_postal":infos_bien["code_postal"]
    }])

    df["type_bien"] = encoder_type.transform(df["type_bien"])
    df["etage"] = encoder_etage.transform(df["etage"])
    df["dpe"] = df["dpe"].map(mapping_dpe)

    df = df.fillna(-100000)

    estimation = model.predict(df)[0]

    return estimation

if __name__ == "__main__":
    infos_test = {
        "type_bien": "Appartement à vendre",
        "surface_m2": 50,
        "nb_pieces": 3,
        "nb_chambres": 2,
        "etage": "1 étages",
        "dpe": "A",
        "code_postal":75011.0
    }
   
    estimation = ft_pred(infos_test)
    print("Prix estimé :", estimation)

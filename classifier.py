# https://scikit-learn.org/0.21/documentation.html
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report


def classify(is_kaylee):
    file_label_map = {
        "kaylee_sweet_control_RESTING.csv": "resting 😌",
        "kaylee_water_SWEAT.csv": "sweat 😅💦",
        "kaylee_sweet_SWEET.csv": "post glucose 🤤",
    } if is_kaylee else {
        "jason_gsr_data_RESTING.csv": "resting 😌",
        "jason_drums_gsr_SWEAT.csv": "sweat 😅💦",
        "jason_sweet_SWEET.csv": "post glucose 🤤",
    }

    df_list = []
    for csv_path, label in file_label_map.items():
        tmp = pd.read_csv(csv_path)
        tmp["state"] = label
        df_list.append(tmp[["GSR", "state"]])

    df = pd.concat(df_list, ignore_index=True)

    X = df[["GSR"]]
    y = df["state"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    return clf

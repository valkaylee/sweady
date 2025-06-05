import pandas as pd
import measure
import classifier

if __name__ == "__main__":
    measure.measure()

    clf = classifier.classify(True)

    new_df = pd.read_csv("gsr_data.csv")
    new_X = new_df[["GSR"]]
    new_df["predicted_state"] = clf.predict(new_X)

    most_common = new_df["predicted_state"].mode()[0]
    print(f"Predicted state: {most_common}")

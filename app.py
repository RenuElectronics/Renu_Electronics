from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the Excel file
df = pd.read_excel("data.xlsx")

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        engineer = request.form.get("engineer", "").strip().lower()
        rnp = request.form.get("rnp", "").strip().lower()

        # Create a filtered DataFrame
        filtered_df = df.copy()

        if engineer:
            filtered_df = filtered_df[filtered_df["Engineer Name"].astype(str).str.lower() == engineer]
        if rnp:
            filtered_df = filtered_df[filtered_df["RNP No."].astype(str).str.lower() == rnp]

        results = filtered_df.to_dict(orient="records")

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

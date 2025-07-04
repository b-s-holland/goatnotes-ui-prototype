from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/preview", methods=["POST"])
def preview():
    selected_option = request.form.get("output_type")
    return render_template("preview.html", output_type=selected_option)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

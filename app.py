from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get(
        "https://api.artic.edu/api/v1/artworks?fields=id,title,image_id,date_start,artist_display,date_display,main_reference_numb&page=1&limit=25"
    )

    if response.status_code == 200:
        data = response.json()
        artworks_list = data.get('data', [])
    else:
        artworks_list = []

    return render_template("index.html", artworks=artworks_list)

@app.route('/artwork/<int:id>')
def artworkDetail(id):
    # FIXED API URL
    response = requests.get(
        f"https://api.artic.edu/api/v1/artworks/{id}?fields=id,title,image_id,date_start,short_description,artist_display,date_display,main_reference_numb"
    )

    if response.status_code == 200:
        artwork = response.json().get('data', {})
        return render_template('artworks.html', artwork=artwork)
    else:
        return "Artwork not found", 404

if __name__ == "__main__":
    app.run(debug=True)

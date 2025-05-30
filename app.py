from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    # Get artworks from the Art Institute of Chicago API
    response = requests.get("https://api.artic.edu/api/v1/artworks?fields=id,title,image_id,date_start,artist_display,date_display,main_reference_numb&page=1&limit=25")
    
    if response.status_code == 200:
        data = response.json()
        artworks_list = data.get('data', [])
    else:
        artworks_list = []

    return render_template("index.html", artworks=artworks_list)

# route for atrwork detail page
@app.route('/artwork/<int:id>')
def artworkDetail(id):
    response = requests.get(f"https://api.artic.edu/api/v1/artworks?fields=id,title,image_id,date_start,artist_display,date_display,main_reference_numb&page=1&limit=25/{id}")

    if response.status_code == 200:
        data = response.json()
        artworkData = data.get("data", {})
        imgId = artworkData.get("image_id")
        url = f"https://www.artic.edu/iiif/2/{imgId}/full/843,/0/default.jpg" if imgId else None
    else:
        artworkData = {}
        url = None

    return render_template("artworks.html", artwork=artworkData, image_url=url)
    
if __name__ == "__main__":
    app.run(debug=True)
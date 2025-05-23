from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    # Get artworks from the Art Institute of Chicago API
    response = requests.get("https://api.artic.edu/api/v1/artworks")
    
    if response.status_code == 200:
        data = response.json()
        """for art in data.get('data', {}):
            image_id = art.get('image_id')
            title = art.get('title')
            artist = art.get('artist_title')"""
        """artworks_list = data.get('data', [])  # Use 'data' key based on API structure
    else:
        artworks_list = []"""

    """if image_id:
        image_url = f"https://www.artic.edu/iiif/2/{image_id}/full/843,/0/default.jpg"
    else:
        image_url = None"""

    artworks_list = data['data']

    return render_template("index.html", artworks=artworks_list)
@app.route("/artworks/<int:id>")
def artworkDetail():
    response = requests.get(f"https://api.artic.edu/api/v1/artworks/{id}")
    data = response.json()
    artworkData = data.get("data", {})
    imgId = artworkData.get("image_id")
    url = f"https://www.artic.edu/iiif/2/{imgId}/full/843,/0/default.jpg"
    render_template("/", artwork = {
        'url': url
    })
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
from energy_scraper import EnergyScraper

app = Flask(__name__)
CORS(app)


@app.route('/data')
def get_data():
    scraper = EnergyScraper()
    data = scraper.create_dictionary()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

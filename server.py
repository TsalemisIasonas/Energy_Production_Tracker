from flask import Flask, jsonify
from energy_scraper import EnergyScraper

app = Flask(__name__)


@app.route('/data')
def get_data():
    scraper = EnergyScraper()
    data = scraper.scrape_data()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

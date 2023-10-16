from flask import Flask, jsonify, render_template, request, redirect
import hashlib


app = Flask(__name__)

url_database = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    if request.method == 'POST':
        long_url = request.json.get('long_url')
        
        short_url = generate_short_url(long_url)
        
        url_database[short_url] = long_url
        return jsonify({"short_url": short_url})

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_database.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "Short URL not found", 404

def generate_short_url(long_url):
    md5_hash = hashlib.md5(long_url.encode()).hexdigest()
    short_url = md5_hash[-6:]
    return short_url

if __name__ == "__main__":
    app.run(debug=True)

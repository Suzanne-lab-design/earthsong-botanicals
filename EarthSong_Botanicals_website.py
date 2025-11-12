
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to EarthSong Botanicals</h1><p>Healing through sound, herbs, and nature.</p>'

@app.route('/services')
def services():
    return '<h2>Our Healing Services</h2><ul><li>Sound Healing</li><li>Herbal Remedies</li><li>Healing Garden</li></ul>'

@app.route('/contact')
def contact():
    return '<h2>Contact Us</h2><p>Email: info@earthsongbotanicals.com</p>'

if __name__ == '__main__':
    app.run(debug=True)

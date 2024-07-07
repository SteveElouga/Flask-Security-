from flask import Flask, jsonify, Blueprint

app = Flask(__name__)
app.config.from_object("config")
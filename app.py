from flask import Flask, render_template
import os

app = Flask(__name__)

FOOD_ITEMS = [
    {"name": "Cheesy Burger", "price": "$12", "img": "https://source.unsplash.com/400x300/?burger"},
    {"name": "Pepperoni Pizza", "price": "$18", "img": "https://source.unsplash.com/400x300/?pizza"},
    {"name": "Spicy Tacos", "price": "$10", "img": "https://source.unsplash.com/400x300/?tacos"},
    {"name": "Sushi Platter", "price": "$25", "img": "https://source.unsplash.com/400x300/?sushi"}
]

@app.route('/')
def home():
    env_name = os.environ.get("ENV", "Localhost")
    return render_template('index.html', items=FOOD_ITEMS, env=env_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
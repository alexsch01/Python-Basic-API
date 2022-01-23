from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100))


@app.route('/')
def index():
    return "Hello World"

@app.route('/items')
def get_items():
    items = []
    for item in Item.query.all():
        items.append({'name': item.name,
                      "description": item.description})
    return {'items': items}

@app.route('/items/<id>')
def get_item(id):
    item = Item.query.get_or_404(id)
    return {'name': item.name,
            'description': item.description}

@app.route('/items', methods=['POST'])
def add_item():
    item = Item(name=request.json["name"],
                description=request.json["description"])
    db.session.add(item)
    db.session.commit()
    return {'id': item.id}

@app.route('/items/<id>', methods=["DELETE"])
def delete_item(id):
    item = Item.query.get(id)
    if item is None:
        return {"error": "not found"}
    db.session.delete(item)
    db.session.commit()
    return {"message": "successful"}

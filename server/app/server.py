import os

_PORT = os.environ.get('PORT') or "4003"

def run():
    from app import app, db, resources
    db.create_all()
    app.run(host='0.0.0.0', port=_PORT)

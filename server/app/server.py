def run():
    from app import app, db, resources
    db.create_all()
    app.run(host='0.0.0.0')

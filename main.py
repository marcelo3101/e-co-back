from app import create_app, db

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
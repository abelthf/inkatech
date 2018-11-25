# services/users/manage.py


from flask.cli import FlaskGroup

from project import app, db     # nuevo


cli = FlaskGroup(app)


# nuevo
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session()


if __name__ == '__main__':
    cli()

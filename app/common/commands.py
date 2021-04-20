def register_commands(app, db):
    """
    Register the commands.

    :param app:
    :param db:
    :return:
    """
    @app.cli.command('setupdb')
    def setupdb_command():
        """
        Setup the DB from the SQLAlchemy model structure.
        :return:
        """
        db.create_all()

from app.common.app import create_app
from app.common.routes import register_routes

(app, db) = create_app()
register_routes(app)

if __name__ == '__main__':
    app.run('0.0.0.0')

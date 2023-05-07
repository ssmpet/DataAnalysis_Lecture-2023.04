from flask import Flask
from views import main_views
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# import config

# db = SQLAlchemy()
# migrate = Migrate()

app = Flask(__name__)
# app.config.from_object(config)

#ORM
# db.init_app(app)
# migrate.init_app(app, db)


app.register_blueprint(main_views.bp)

if __name__ == '__main__':
    app.run(debug=True)

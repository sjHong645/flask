from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()
    
# 블루프린트 등록
def create_app() : 
    app = Flask(__name__)
    app.config.from_object(config) # config.py 파일에 작성한 항목을 읽기 위해 추가한 코드 

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models # flask의 migrate 기능을 인식하기 위해 추가된 코드

    # blueprint
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    
    return app
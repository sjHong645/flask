from flask import Flask

# 기존 pybo 함수 코드 
""" app = Flask(__name__)

@app.route('/')
def hello_pybo() : 
    return 'Hello, Pybo!' """

# 애플리케이션 팩토리 적용
""" def create_app() : 
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo() : 
        return 'Hello, Pybo!'
    
    return app """
    
# 블루프린트 등록
def create_app() : 
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app
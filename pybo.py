from flask import Flask

# 기존 pybo 함수 코드 
""" app = Flask(__name__)

@app.route('/')
def hello_pybo() : 
    return 'Hello, Pybo!' """
    
# 이걸 애플리케이션 팩토리를 적용하기 위해서 아래와 같이 수정했다.
def create_app() : 
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo() : 
        return 'Hello, Pybo!'
    
    return app
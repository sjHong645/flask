from flask import Blueprint

# main은 블루프린트의 별칭
# bp 객체 생성시 사용된 __name__은 모듈명인 "main_views" 가 인수로 전달된다.
# url_prefix는 라우팅 함수의 애너테이션 URL 앞에 기본적으로 붙일 접두어 URL을 의미
# ex. url_prefix = '/main'이라고 하면
# hello_pybo 함수를 호출하는 URL은 localhost:5000/ 가 아니라 localhost:5000/main/ 이 된다. 
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo() : 
    return 'Hello, Pybo!'

@bp.route('/')
def index() : 
    return 'Pybo Index'
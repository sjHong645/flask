# 2. Flask 애플리케이션 팩토리

- chapter1의 pybo.py에서 만든 플라스크 앱
```
app = Flask(__name__)
```
Flask는 `app 객체`를 사용해서 여러가지 설정을 진행한다. 

하지만, 이런식으로 app 객체를 전역으로 사용하면 프로젝트의 규모가 커질수록 문제가 발생할 확률이 높아진다.  
대표적으로 `순환 참조(circular import)오류`가 발생할 수 있다. 

`순환 참조`란 A 모듈이 B 모듈을 참조하고 B 모듈이 다시 A 모듈을 참조하는 경우를 의미한다. 

그러면 이 문제를 어떻게 해결할 수 있을까? `application factory`를 사용하라고 권한다. 

## 2-1. pybo.py를 `__init__.py` 파일로 변경 

기존 변수 설정에서 `FLASK_APP=pybo`로 설정했었다. 
지금은 pybo 디렉토리를 만들어서 그 안에 `__init__.py`에 `pybo.py`의 내용을 그대로 복사 + 붙여넣기를 했다. 

여기서 `__init__.py`의 위치가 아닌 `pybo 디렉토리`의 위치에서 `flask run`을 실행하면 기존처럼 flask 개발 서버가 동작한다. 

## 2-2. 애플리케이션 팩토리 적용 

`pybo\__init__.py`를 아래와 같이 수정한다.

```
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app
```

`create_app 함수`가 app 객체를 생성해서 반환하도록 코드를 수정했다.  
여기서 사용된 `create_app 함수`가 `애플리케이션 팩토리`이다. 

다른 이름을 사용하면 정상적으로 동작하지 않는다. `create_app`은 Flask 내부에서 정의된 함수이름이기 때문이다. 

## 2-3 블루프린트로 라우팅 함수 관리하기 

- 라우팅 함수란? 
`@app.route('/')`와 같은 장식자로 URL를 매핑하는 함수를 말한다. 

기존 방식대로라면 새로운 URL 매핑이 필요할 때 마다 라우팅 함수를 `create_app 함수` 안에 계속 추가해야 한다. 그렇게 되면 create_app 함수는 엄청나게 크고 복잡한 함수가 될 것이다. 

이런 문제를 해결하기 위해서 `블루프린트(Blueprint)`를 사용할 것이다. 

`flask의 블루프린트(blueprint)`란 URL과 함수의 매핑을 관리하기 위해 사용되는 도구(클래스)를 의미한다. 이걸 가지고 라우팅 함수를 체계적으로 관리할 수 있다. 

### 블루프린트 생성 

1. `pybo/views 디렉토리` 아래에 `main_views.py` 파일 생성
2. 아래와 같이 코드 작성
```
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo() : 
    return 'Hello, Pybo!'
```

### 블루프린트 등록 

이제 flask 앱에 이전에 작성했던 블루프린트를 등록해보자. `pybo/__init__.py` 파일을 다음과 같이 수정함 

```
def create_app() : 
    app = Flask(__name__)

    # 이 부분으로 수정함 
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app
```

이렇게 수정하고 나서 flask를 동작시키면 `hello_pybo 함수`가 잘 동작하는 걸 확인할 수 있다. 

### 블루프린트에 라우팅 함수 추가 

블루프린트가 제대로 동작하는지 확인하기 위해 라우팅 함수를 수정하겠다. 

- hello_pybo 함수의 URL 매핑을 `/`에서 `/hello`로 변경
- index 함수를 추가해 `/`로 매핑

```
(...) main_views.py의 앞 부분

@bp.route('/hello')
def hello_pybo() : 
    return 'Hello, Pybo!'

@bp.route('/')
def index() : 
    return 'Pybo Index'
```

### 블루프린트 동작 확인 

flask를 실행하고 url을 각각 입력했을 때 각 URL에 따른 화면이 출력된다는 걸 확인할 수 있다. 


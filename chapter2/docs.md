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

### 애플리케이션 팩토리 적용 

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
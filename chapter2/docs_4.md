# 4. 모델로 데이터 처리하기 

지금 만들고 있는 건 질문/답변 게시판이다. 질문이나 답변을 작성하면 데이터가 생성된다.
그러므로 데이터를 저장, 조회, 수정하는 등의 기능을 구현해야 한다. 

웹 서비스는 데이터를 처리할 때 대부분 DB를 사용한다. 

DB를 이용하기 위해서는 2가지 방법이 있다. 

- 직접 SQL 쿼리를 작성
- ORM을 이용 

둘 다 장/단점은 있지만 ORM의 가장 큰 장점은 sql 쿼리문을 작성하지 않고 python 문법만으로 DB에 접근해서 작업할 수 있다는 점이다. 

## 1. 플라스크 ORM 라이브러리 사용하기 

파이썬 ORM 중 가장 많이 사용하는 건 `SQLAlchemy`이다.  
그리고 python 모델을 이용해 테이블을 생성하고 컬럼을 추가하는 등의 작업을 할 수 있게 해주는 `Flask-Migrate 라이브러리`도 사용해보자. 

### ORM 라이브러리 설치

Flask-Migrate 라이브러리를 설치하면 SQLAlchemy도 함께 설치된다. 
```
pip install flask-migrate
```

### 설정 파일 추가하기 

ORM을 적용하기 위해서 DB 설정이 필요하다. config.py 파일에 아래의 코드를 작성하자.

```
import os

BASE_DIR = os.path.dirname(__file__)

# 데이터베이스 접속 주소 
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# SQLAlchemy의 이벤트를 처리하는 옵션. 여기서는 필요하지 않아서 False로 비활성화함 
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

`SQLALCHEMY_DATABASE_URI` 설정에 의해 `SQLite DB를 사용`하고 
DB파일은 프로젝트 `홈 디렉토리 바로 밑에 pybo.db 파일로 저장`된다. 

### 발생할 수 있는 오류 상황

```
(flask) C:\devtool\python-study\flask> flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current directory.
```

이 오류가 발생한 이유는 플라스크를 실행하는 기본앱을 잘못설정했기 때문에 발생한다. 
커맨드 환경에서 `FLASK_APP` 변수를 잘못 설정해줬기 때문이다. 

ex. FLASK_APP = pybo 라고 설정했다고 하자. 
1. `flask 명령어`를 실행하는 위치에 `pybo.py` 파일에 flask 서버를 실행할 수 있는 코드가 있어야 한다.
2. 또는 `pybo/__init__.py`에 flask 서버를 실행할 수 있는 코드가 있어야 한다.

### ORM 적용하기 

[ORM 적용한 `__init__.py` 커밋 링크]()

### db 초기화하기

아래 명령어 실행. 그러면 해당 명령어를 실행한 위치에 migrations 폴더가 자동으로 생성됨(폴더 아래에 있는 파일들은 Flask-Migrate 라이브러리가 내부적으로 사용하는 거라서 자세히 살펴보지는 않는다)

```
flask db init 
```

이 명령어는 최초에 한 번만 수행하면 된다. 

- DB 관리 명령어
| 명령어 | 설명 | 
| --- | --- | 
| `flask db migrate` | 모델을 새로 생성하거나 변경할 때 사용 (실행하면 작업파일이 생성됨) | 
| `flask db upgrade` | 모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용 (위에서 생성된 작업파일을 실행하여 데이터베이스를 변경) | 

## 2. 모델 만들기 

파이보는 `질문 답변 게시판`이기 때문에 `질문`과 `답변`에 해당하는 모델이 있어야 한다. 
- 모델 : 데이터를 다룰 목적으로 만든 파이썬 클래스 

### 모델 속성 구상 

- 질문 모델

| 속성명 | 설명 | 
| --- | --- | 
| id | 질문 데이터의 고유 번호 |
| subject | 질문 제목 |
| content | 질문 내용 |
| create_date | 질문 작성일시 |

- 답변 모델 
| 속성명 | 설명 | 
| --- | --- | 
| id | 답변 데이터의 고유 번호 |
| question_id | 질문 데이터의 고유번호 |
| content | 답변 내용 |
| create_date | 답변 작성일시 |

### 질문 모델 생성 

구상한 속성을 가지고 모델을 정의해보자. 

1. pybo 디렉터리에 모델을 정의하기 위한 models.py 생성
2. 질문 모델 Question 클래스를 작성하자. 

### 답변 모델 생성 

질문 모델을 참조하는 외래키 설정을 위해서 다음과 같은 내용을 추가해야 한다.

- 질문 모델을 참조하기 위한 변수 question 
```
question = db.relationship('Question', backref=db.backref('answer_set'))
```
- db.relationship의 매개변수 
    1. Question : 참조할 모델 이름
    2. backref : 역참조 설정
        - 역참조 : 쉽게 말해 `질문`에서 `답변`을 거꾸로 참조하는 것 
        - ex. 어떤 질문에 해당하는 객체가 `a_question`일 때
            - `a_question.answer_set`와 같은 코드로 해당 질문에 대한 답변들을 참조가능

- 외래키 설정 
```
question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'CASCADE'))
```

1. 앞서 설정한 `question`의 `id 속성`을 참조하는 외래키
2. 삭제 옵션은 `CASCADE`로 설정

## 3. 모델을 이용해 테이블 자동으로 생성하기 

모델을 구상하고 생성했으니까 flask의 migrate 기능을 이용해서 DB의 테이블을 생성해보자. 

### 모델 import 

- [모델을 이용한 테이블 생성 커밋]()



# 플라스크 개발 기초공사

## 학습목표
- 블루프린트를 이용한 라우트 함수 관리
- flask orm을 사용한 db 제어
- pybo 게시판에 질문 목록과 상세 조회 기능 추가 

## 프로젝트 구조 
```
├── pybo/
│      ├─ __init__.py
│      ├─ models.py
│      ├─ forms.py
│      ├─ views/
│      │   └─ main_views.py
│      ├─ static/
│      │   └─ style.css
│      └─ templates/
│            └─ index.html
└── config.py
```

### models.py : DB를 처리하는 파일 

ORM을 지원하는 SQLAlchemy를 사용한다. SQLAlchemy는 모델 기반으로 DB를 처리한다.  
아직은 잘 모르겠지만 이후 프로젝트를 진행하면서 알아보도록 하자. 

## forms.py : 서버에 전송된 폼을 처리하는 파일 

웹 브라우저에서 서버로 전송한 폼을 처리할 때 `WTForms 라이브러리`를 사용한다. 
이 역시 모델 기반으로 폼을 처리해서 폼 클래스를 정의할 forms.py가 필요하다. 

## view 디렉토리 : 화면을 구성

chapter1의 pybo.py에 작성했던 hello_pybo 함수의 역할은 화면구성이었다.  
views 디렉토리에는 바로 이런 함수들로 구성된 뷰 파일들을 저장한다. 

## static 디렉토리 : css, js, image 파일을 저장하는 디렉토리 

## templates 디렉토리 : html 파일을 저장하는 디렉토리 

## config.py : 파이보 프로젝트를 설정하는 파일 

프로젝트의 환경변수, DB 등의 설정을 이 파일에 저장한다. 
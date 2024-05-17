# 5. 질문 목록과 질문 상세 기능 만들기 
pybo의 핵심 기능을 만들어보자. 

## 1. 질문 목록 만들기 

### 게시판 질문 목록 출력하기 

- main_views.py 파일 수정 

``` python
from flask import Blueprint, render_template

from pybo.models import Question

@bp.route('/')
def index() : 

    # 질문 목록 데이터를 query를 사용해서 얻어냈다.
    # 이때, 데이터 정렬 순서는 작성일시 기준으로 역순이다. 
    question_list = Question.query.order_by(Question.create_date.desc())
    
    # render_template를 이용해서 템플릿 화면을 렌더링했다. 
    # question/question_list.html 라는 템플릿 파일에 
    # 변수 question_list를 사용할 건데 여기에 사용할 변수 값은 앞서 정의한 question_list이다. 
    return render_template('question/question_list.html', question_list = question_list)
``` 

### 질문 목록 템플릿 작성하기 

그러면 질문 목록을 출력할 `question/question_list.html` 파일을 만들어줘야 한다. 

- 파일의 저장 경로 : pybo/templates 폴더
    - 해당 폴더에 question 폴더 생성 ⇒ question_list.html 파일 생성

- question_list.html 파일 내용

``` html 
<!-- 질문 목록 -->
{% if question_list %}
    <ul>
    {% for question in question_list %}
        <li><a href="/detail/{{ question.id }}/">{{ question.subject }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>질문이 없습니다.</p>
{% endif %}
```


## 2. 질문 상세 기능 만들기 

## 3. 블루프린트로 기능 분리하기 
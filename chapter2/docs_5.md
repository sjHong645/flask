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

1. 템플릿 태그 : `{%`와 `%}`로 둘러싸인 문장 
    - `{% if question_list %}` : `render_template` 메소드를 통해 question_list라는 데이터를 전달받았는지 확인한다. 
    - {% for question in question_list %} : question_list 데이터에 있는 각각의 항목들을 for문을 통해 순차접근한다. 

### 플라스크에서 자주 사용하는 템플릿 태그 

1. 조건문 태그 

python의 if, elif, else 문과 유사하게 사용한다. 이때, 반드시 조건문 태그는 `{% endif %}`로 닫아줘야 한다. 

```
{% if 조건문1 %}
    <p>조건문1에 해당하면 실행</p>
{% elif 조건문2 %}
    <p>조건문2에 해당하면 실행</p>
{% else %}
    <p>조건문1, 2 모두 해당하지 않으면 실행</p>
{% endif %}
```

2. 반복문 태그 

python의 for문과 유사하다. 마찬가지로 `{% endfor %}`로 닫아줘야 한다. 

```
{% for item in list %}
    <p>순서: {{ loop.index }} </p>
    <p>{{ item }}</p>
{% endfor %}
```

- 반복문 안에서 사용할 수 있는 loop 객체 
| loop 객체의 속성 | 설명 | 
| --- | --- | 
| loop.index | 반복 순서, 1부터 1씩 증가 |
| loop.index0 | 반복 순서, 0부터 1씩 증가 |
| loop.first | 반복 순서가 첫 번째 순서이면 True 아니면 False |
| loop.last | 반복 순서가 마지막 순서이면 True 아니면 False |

3. 객체 태그 

- 객체를 출력하는 템플릿 태그 
    - `{{ 객체 }}`
    - 속성 출력 : `{{ 객체.속성 }}`

[자세한 내용](https://jinja.palletsprojects.com/en/2.11.x/templates/)

## 2. 질문 상세 기능 만들기 

1번 실습을 통해 만든 질문 목록 페이지에서 링크를 누르면 오류메시지가 나타난다. 

```
Not Found

The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
```

말 그대로 내가 요청한 페이지(http://localhost:5000/detail/2/)의 URL이 정의되지 않아서 발생한 오류다. 
이번에는 질문의 제목과 내용이 표시되도록 해보자. 

### 라우팅 함수 

질문 목록 링크 : http://localhost:5000/detail/2/ => Question 모델 데이터 중 id값이 2인 데이터를 조회하라는 뜻 

여기에 대응할 수 있도록 `main_views.py` 파일에 라우팅 함수를 추가한다. 

``` python
@bp.route('/detail/<int:question_id>/')
def detail(question_id) : 
    question = Question.query.get(question_id) # Question 모델 데이터 중 URL를 통해 전달받은 id값의 데이터를 조회한다. 
    
    # 조회한 데이터를 question/question_detail.html 파일이 전달받는다. 
    return render_template('question/question_detail.html', question = question) 
```

즉, http://localhost:5000/detail/2/ 페이지를 요청받으면 

main_views.py의 detail 메소드 실행 => 매개변수 question_id에는 2라는 값이 전달된다. 

### 질문 상세 템플릿 작성하기 

이제 `question/question_detail.html` 파일을 만들자. 

``` html
<h1>{{ question.subject }}</h1>
<div>
    {{ question.content }}
</div>
```

이제 flask를 실행하고 나서 링크를 클릭하면 원하는 화면이 출력될 것이다. 

### 404 에러 페이지 표시하기 

- http://localhost:5000/detail/30/ 페이지를 요청하면... 빈 페이지가 나온다. 

원래는 question_id 값을 잘못 썼기 때문에 404 오류가 발생해야 하는데 아무것도 보이지 않는 빈 페이지가 나온다. 

존재하지 않는 페이지를 요청받았을 때 빈 페이지 대신 404 오류 페이지를 표시하도록 하기 위해서 detail 함수를 아래와 같이 수정하자.

``` py
@bp.route('/detail/<int:question_id>/')
def detail(question_id) : 

    # get대신 get_or_404 메소드를 사용함으로써 원하는 기능으로 수정했다. 
    question = Question.query.get_or_404(question_id)
    
    return render_template('question/question_detail.html', question = question)
```

## 3. 블루프린트로 기능 분리하기 
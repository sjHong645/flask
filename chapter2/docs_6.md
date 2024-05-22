# 6. 답변 등록 기능 만들기 

이번에는 질문에 답변을 등록하고 보여주는 기능을 만든다. 

## 1. 답변 저장하기 

- 구현할 기능
1. 텍스트 창(textarea) : 질문 상세 화면에 답변을 입력하기 위한 곳
2. `<답변등록> 버튼` : 이 버튼을 누르면 텍스트 창에 입력된 답변이 저장되도록 할 것임

### 답변 등록 버튼 만들기 

question_detail.html 파일

- 답변 저장 URL 
    - form 태그의 action 속성에서 지정
    - `답변등록` 버튼을 누르면 POST 방식으로 action에서 지정한 URL이 호출된다.
``` html
<h1>{{ question.subject }}</h1>
<div>
    {{ question.content }}
</div>
<form action = "{{ url_for('answer.create', question_id = question.id)}}" method = "post">
    <textarea name = "content" id = "content" rows = 15></textarea>
    <input type = "submit" value = "답변등록">
</form>
```

이 상태에서 flask를 실행하고 질문 목록을 클릭하면... 당연히 500번 오류가 발생한다. 아직 `answer라는 이름의 블루프린트 파일`을 작성하지 않았기 때문이다. 

### 답변 블루프린트 만들기 

답변을 관리하는 블루프린트를 만들자. `views/answer_views.py`파일을 만들고 아래와 같이 코드를 작성한다.

``` python
from datetime import datetime 

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

# ex. http://locahost:5000/answer/create/2/ 페이지를 요청받으면
# question_id값에는 2가 전달된다. 
# 질문 상세 템플릿의 form 엘리먼트를 POST 방식으로 지정했기에 같은 방식으로 지정한다. 
@bp.route('/create/<int:question_id>', method = ('POST', ))
def create(question_id) : 
    # form 엘리먼트를 통해 전달된 데이터들은 해당 메소드에서 request 객체로 얻을 수 있다. 
    # request 객체를 얻을 수 있도록 html 파일에서 action을 설정했다.     
    question = Question.query.get_or_404(question_id)

    # POST 폼 방식으로 전송된 데이터 항목 중 name 속성이 content인 값을 저장함
    # <textarea name = "content" id = "content" rows = 15></textarea> 부분 
    content = request.form['content']  
    answer = Answer(content = content, create_date = datetime.now())

    # question.answer_set은 
    # models.py에서 Question과 Answer 모델을 backref을 통해 연결 설정했다. 
    # 그 부분을 이용한 코드이다. 
    question.answer_set.append(answer)
    db.session.commit()

    # 다른 방법
    # Answer 모델을 직접 사용해 답변 저장하기 
    '''
    answer = Answer(question = question, content = content, create_date = datetime.now())
    db.session.add(answer)
    '''
    
    # 답변 생성 이후에 화면을 상세 화면으로 이동하도록 redirect 함수를 사용했다. 
    return redirect(url_for('question.detail', question_id = question_id))
```

### 답변 블루프린트 등록하기 

답변 블루프린트를 `__init__.py`에 등록하자. 

``` python
# blueprint
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
```
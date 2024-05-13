# __init__.py 파일에서 생성한 SQLAlchemy 객체 db 
from pybo import db 


# 질문 모델 
# db.Model 클래스를 상속해서 모델 클래스를 만든다. 
class Question(db.Model) : 
    
    # 모델을 이루는 속성들을 각각 컬럼으로 구현했다. 
    # (컬럼의 데이터 타입, primary_key 여부)를 설정할 수 있다. 
    # nullable도 설정가능(기본값 = false)
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), primary_key = False)
    content = db.Column(db.Text(), primary_key = False)
    create_date = db.Column(db.DateTime(), primary_key = False)
    

# 답변 모델

class Answer(db.Model) : 
    
    id = db.Column(db.Integer, primary_key = True)
    
    # docs_4.md에 나와있듯 질문 데이터의 고유 번호를 의미한다. 
    # 모델을 서로 연결하기 위해서 db.ForeignKey()를 추가했다. 
    # 여기서는 질문 모델과 답변 모델을 서로 연결함 
    
    # 아래에 추가된 속성 question의 id값을 참조한다. 
    # 이때, 삭제 옵션은 CASCADE이다. 질문을 삭제하면 그 질문에 달린 답변도 삭제된다. 
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'CASCADE'))
    
    # Answer 모델에서 Question 모델을 참조하기 위해 추가된 속성값 
    # backref는 역참조 설정이라고 한다. 
    # 역참조란 쉽게 말해 Question에서 Answer를 거꾸로 참조하는 것을 의미한다. 
    # 하나의 질문에 여러 답변이 달릴 때 역참조는 이 질문에 달린 답변들을 참조할 수 있게 한다.
    
    # ex. 어떤 질문에 해당하는 객체가 a_question이라고 하자.
    # 그러면 a_question.answer_set과 같은 코드로 해당 질문에 달린 답변들을 참조할 수 있다. 
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), primary_key = False)
    create_date = db.Column(db.DateTime(), primary_key = False)
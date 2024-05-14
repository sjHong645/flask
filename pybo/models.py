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
    
    # Answer 모델에서 Question 모델을 참조하기 위해 추가된 속성값 
    question = db.relationship('Question', backref=db.backref('answer_set'))
    
    # question 객체의 id값을 참조하는 외래키 속성 question_id
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'CASCADE'))
    content = db.Column(db.Text(), primary_key = False)
    create_date = db.Column(db.DateTime(), primary_key = False)
# coding: utf-8
from flask import Flask
app = Flask(__name__) #flask instance 형성
app.debug=True
@app.route('/')     #url 루트 경로로 접속했을때의 처리, @는 파이썬에서 디자인패턴중 decorator 패턴을 사용하겠다는것을 의미
def hello_world():      #결과 적으로 루트 경로로 들어갔을때 어떤것을 실행 시킬것인지
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
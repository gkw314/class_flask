from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

# 다른 경로에 대한 라우트
# 127.0.0.1:5000/about
@app.route('/about')
def about():
    return 'This is the about page.'

# 127.0.0.1:5000/project
@app.route('/project')
def project():
    return 'The project page'

# 동적인 URL 파라미터 사용
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

# URL에 변수 및 타입 지정
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'


# POST 요청 날리는법
# (1) post man
# (2) requests
import requests
@app.route('/test')
def test():
    url = 'http://localhost:5000/submit'
    data ='test data'
    response = requests.post(url=url, data=data)
    
    return response


# 다양한 HTTP 메소드 지원
@app.route('/submit', methods=['POST', 'GET', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("----POST method----", requests.data)

    return Response("success 성공성공", status=200)

    # if request.method == 'POST':
    #     return 'POST method.'
    # else:
    #     return 'GET method.'


if __name__ == '__main__':
    app.run()
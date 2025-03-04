from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 템플릿에 전달할 데이터
    data = {
        'title': 'Flask Jinja Template',
        'user': 'gkw',
        'is_admin': True,
        'items': ['Item 11', 'Item 22', 'Item 33']
    }

    # render_template을 사용하여 템플릿 파일을 렌더링
    # rendering 할 html 파일명 입력
    # html로 넘겨줄때 데이터 입력
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
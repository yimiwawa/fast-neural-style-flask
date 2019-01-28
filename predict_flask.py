# encoding:utf-8
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
import os
import datetime
import random
import online_eval
import json


def config():
    flk = Flask(__name__)
    flk.config['SECRET_KEY'] = 'hard to guess'
    return flk


# gevent的猴子魔法
# monkey.patch_all()
app = config()
app.config['JSON_AS_ASCII'] = False

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
UPLOAD_PIC_PATH = 'imgs/'
GENERATE_PIC_PATH = 'static/generated/'
MODEL_PATH = 'models/'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def create_uuid():  # 生成唯一的图片的名称字符串，防止图片显示时的重名问题
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
    randomNum = random.randint(0, 100)  # 生成的随机整数n，其中0<=n<=100
    if randomNum <= 10:
        randomNum = str(0) + str(randomNum)
    uniqueNum = str(nowTime) + str(randomNum)
    return uniqueNum


@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def generate_pic():
    # receive and save picture
    f = request.files['pic']
    if not (f and allowed_file(f.filename)):
        return "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"
    fn = create_uuid() + '.' + f.filename.rsplit('.', 1)[1]
    update_path = os.path.join(UPLOAD_PIC_PATH, fn)
    f.save(update_path)

    # receive style model
    mode = request.form.get('mode')
    model_path = os.path.join(MODEL_PATH, mode + '.ckpt-done')

    # generate picture's path
    generated_file = os.path.join(GENERATE_PIC_PATH, fn)
    result = online_eval.generation(update_path, model_path, generated_file)
    
    # show pic
    if result is not None:
        return json.dumps(result)
    return json.dumps("NONE")


if __name__ == '__main__':
    # http_server = WSGIServer(('127.0.0.1', 8777), app)
    http_server = WSGIServer(('10.129.0.242', 8877), app)
    http_server.serve_forever()
    #app.run('10.129.0.242', 8877)

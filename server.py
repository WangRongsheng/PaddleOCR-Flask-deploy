import os
import cv2
import time
import yaml
import uuid
import json
from datetime import timedelta
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from paddleocr import PaddleOCR,draw_ocr
from werkzeug import run_simple

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(hours=1)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(fname):
    return '.' in fname and fname.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg']

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route('/ocr', methods=['POST', 'GET'])
def detect():
    file = request.files['file']
    if file and allowed_file(file.filename):
        ext = file.filename.rsplit('.', 1)[1]
        random_name = '{}.{}'.format(uuid.uuid4().hex, ext)
        savepath = os.path.join('caches', secure_filename(random_name))
        file.save(savepath)
        # time-1
        t1 = time.time()
        img = cv2.imread(savepath)
        img_result = ocr.ocr(img)
        # time-2
        t2 = time.time()
        
        '''
        识别结果将以列表返回在img_result，根据具体需求进行改写
        '''
        results = []
        for i in range(len(img_result)):
            results.append(img_result[i][1][0])

        return jsonify({
            '服务状态': 'success',
            '识别结果': results,
            '识别时间': '{:.4f}s'.format(t2-t1)
        })
    return jsonify({'服务状态': 'faild'})

if __name__ == '__main__':
    ocr = PaddleOCR(use_angle_cls=True,use_gpu=False) # 查看README的参数说明
    app.run(host='127.0.0.1', port=8090, debug=True, threaded=True, processes=1)
    '''
    app.run()中可以接受两个参数，分别是threaded和processes，用于开启线程支持和进程支持。
    1.threaded : 多线程支持，默认为False，即不开启多线程;
    2.processes：进程数量，默认为1.
    '''
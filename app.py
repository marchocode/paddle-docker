from paddleocr import PaddleOCR
from flask import Flask, request, flash
from werkzeug.utils import secure_filename
import os,json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'  # 上传文件保存到当前文件夹
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 设置上传文件最大为16MB

# paddleocr --image_dir ./imgs/11.jpg --use_angle_cls true --use_gpu false

@app.route('/', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        flash('No file part')
        return "<p>No file part</p>";

    file = request.files['file']
    # 如果用户没有选择文件，浏览器也会提交一个空的部分而不带文件名
    if file.filename == '':
        flash('No file part')
        return "<p>No file part</p>";

    filename = secure_filename(file.filename)
    target = os.path.join(app.config['UPLOAD_FOLDER'], filename);
    file.save(target)

    ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)  # need to run only once to download and load model into memory
    result = ocr.ocr(target, cls=True)

    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)

    return app.response_class(
        response=json.dumps(result, ensure_ascii=False),
        status=200,
        mimetype='application/json')
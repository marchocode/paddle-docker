FROM paddlepaddle/paddle:2.6.1

WORKDIR /home
COPY 11.jpg .

RUN mkdir upload
RUN pip install paddleocr
RUN paddleocr --image_dir ./11.jpg --use_angle_cls true --use_gpu false
RUN pip install gunicorn

COPY app.py .
COPY enterpoint.sh .
RUN chmod +x enterpoint.sh

ENTRYPOINT ["./enterpoint.sh"]
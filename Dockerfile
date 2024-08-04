FROM paddlepaddle/paddle:3.0.0b1-gpu-cuda11.8-cudnn8.6-trt8.5

WORKDIR /home
COPY 11.jpg .

RUN mkdir upload
RUN pip install paddleocr gunicorn

COPY app.py .
COPY enterpoint.sh .
RUN chmod +x enterpoint.sh

ENTRYPOINT ["./enterpoint.sh"]
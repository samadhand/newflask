FROM python
WORKDIR /src
RUN pip install flask
COPY . .
EXPOSE 8000
CMD python server.py

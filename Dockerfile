FROM python:latest
WORKDIR /PycharmProjects/proiect_sincretic
COPY source.py .
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "source.py", "hexagon.py"]
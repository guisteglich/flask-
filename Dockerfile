FROM python:3
COPY . /app
RUN pip install Flask && pip install request && pip install jsonify
WORKDIR /app
CMD python api.py
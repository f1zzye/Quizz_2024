FROM python:3.12

RUN apt update
RUN mkdir /quizez

WORKDIR /quizez

COPY ./src ./src
COPY commands ./commands

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["bash"]

    # docker run --rm -it -d --name quiz_cont quiz_image

    # docker run --rm -it -d --name quiz_cont quiz_image

    # docker run --rm -it -d -p 8010:8000 -v ~/Desktop/Quizz_2024/src/:/quizez/src --name quiz_cont quiz_image

    # docker run --rm -it -d -p 8010:8000 -v ~/Desktop/Quizz_2024/src/:/quizez/src --name quiz_cont quiz_image python src/manage.py runserver 0:8000

    # docker run --rm -it -p 8010:8000 -v ~/Desktop/Quizz_2024/src/:/quizez/src --name quiz_cont quiz_image ./commands/start_server.sh

# CMD ["python", "src/manage.py", "runserver", "0:8000"]
FROM python:bullseye
RUN useradd amigos
RUN mkdir -p /usr/src/app/bewise_first
WORKDIR /usr/src/app/bewise_first
COPY . /usr/src/app/bewise_first/
RUN pip3 install poetry
RUN poetry install -n --without dev
RUN chmod +x /usr/src/app/bewise_first/boot.sh
ENTRYPOINT ["./boot.sh"]
EXPOSE 8080
FROM python:3.11.3-slim-bullseye as python
LABEL authors="vincentdavis"

ENTRYPOINT ["top", "-b"]
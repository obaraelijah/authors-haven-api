ARG PYTHON_VERSION=3.11.2-bullseye

FROM python:${PYTHON_VERSION} as python


FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=production

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements .
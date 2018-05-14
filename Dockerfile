ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

ADD . /app

CMD python setup.py test --addopts "--doctest-modules --junitxml=test_results.xml"

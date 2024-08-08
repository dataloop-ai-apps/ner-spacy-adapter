FROM docker.io/dataloopai/dtlpy-agent:cpu.py3.10.opencv
USER root
RUN apt update && apt install -y curl gpg software-properties-common

USER 1000
WORKDIR /tmp
ENV HOME=/tmp
RUN pip install spacy
RUN python -m spacy download en_core_web_sm

# docker build -t gcr.io/viewo-g/piper/agent/runner/apps/spacy-ner-adapter:0.1.0 -f Dockerfile .
# docker push gcr.io/viewo-g/piper/agent/runner/apps/spacy-ner-adapter:0.1.0
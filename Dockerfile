FROM hub.dataloop.ai/dtlpy-runner-images/cpu:python3.10_opencv
USER 1000
WORKDIR /tmp
ENV HOME=/tmp
RUN pip install spacy "pandas>=2.1"
RUN python -m spacy download en_core_web_sm
# docker build -t gcr.io/viewo-g/piper/agent/cpu/ner-spacy-adapter:0.1.6 -f Dockerfile .
# docker push gcr.io/viewo-g/piper/agent/cpu/ner-spacy-adapter:0.1.6
FROM frolvlad/alpine-miniconda3 as builder

MAINTAINER Pascal Pellmont <pascal.pellmont.3@css.ch>
MAINTAINER Lukas Schmid <lukas.schmid@css.ch>

# Part of base-image
COPY data/environment.yml /app/
RUN conda env create --file app/environment.yml -p /env

# Current part
COPY data/requirements.txt /app/
WORKDIR /app
RUN source activate /env && pip install -r requirements.txt
COPY data /app/
RUN source activate /env && tox && pip install .

FROM frolvlad/alpine-miniconda3

MAINTAINER Lukas Schmid
COPY --from=builder /env /env
COPY data/datasets/trainingset.csv /app/datasets/
COPY data/runtrain.py /app/

WORKDIR /app
RUN adduser --system trainer
RUN chown -R trainer /app
USER trainer
RUN source activate /env && mkdir model && python runtrain.py

FROM frolvlad/alpine-miniconda3 as builder

MAINTAINER Pascal Pellmont <pascal.pellmont.3@css.ch>
MAINTAINER Lukas Schmid <lukas.schmid@css.ch>

# Actually part of base-image
COPY ["data/environment.yml", "/app/"]
RUN conda env create --file app/environment.yml -p /env

# Now correct part
COPY ["data", "/app/"]
WORKDIR /app
RUN source activate /env && tox && pip install -r requirements.txt && pip install .

FROM frolvlad/alpine-miniconda3

MAINTAINER Lukas Schmid
COPY --from=builder /env /env
WORKDIR /app
RUN adduser --system trainer
USER trainer
CMD source activate /env && python runtrain.py

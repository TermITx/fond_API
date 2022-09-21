FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends build-essential r-base r-cran-randomforest python3.6 python3-pip python3-setuptools python3-dev
COPY requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

#RUN Rscript -e "install.packages('data.table')"
RUN Rscript --vanilla init.R

# expose the port that uvicorn will run the app on
ENV PORT=8000
EXPOSE 8000

# execute the command python main.py (in the WORKDIR) to start the app
CMD ["python", "main.py"]


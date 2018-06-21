FROM python:3.6

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install Linux dependencies
RUN apt-get update && apt-get install -y libssl-dev

# Copy over requirements
COPY requirements.txt .
# Install python dependencies
RUN pip install -r requirements.txt

COPY langnet ./langnet/

COPY tests ./tests/
COPY main.py ./main.py/

#COPY setup.py .
#COPY README.md .

#RUN pip install -e .

WORKDIR /app
#RUN python main.py
#CMD [ "python", "./main.py"]
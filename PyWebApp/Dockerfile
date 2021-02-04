# base image
FROM python:3-windowsservercore 

# create directory
WORKDIR /user/src/app

# copy over the requirements file and run pip install to install the packages into your container
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --user

COPY . .

ENTRYPOINT ["python", "./app.py"]

EXPOSE 80

# local development
# ENTRYPOINT ["python", "./app.py", "--host=0.0.0.0"]

# local development (flask)
#EXPOSE 5000 











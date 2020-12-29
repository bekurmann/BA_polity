# pull official alpine base image for python
FROM python:3.8-slim

################################################
# set work directory
################################################
WORKDIR /usr/src/polity

################################################
# set environment variables
################################################
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

################################################
# update repository & install dependencies  ####
################################################
RUN apt-get update && \
    # pipenv
    apt-get install -y --no-install-recommends pipenv \
    # uwsgi
    build-essential \
    # dependencies gdal & postgis
    binutils libproj-dev gdal-bin python-gdal python3-gdal \
    && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

################################################
# pipenv
################################################
COPY ./Pipfile .
COPY ./Pipfile.lock .
# install django dependencies from pipfile
RUN pipenv install --system --deploy --ignore-pipfile

################################################
# copy polity project to /usr/src/app
################################################
COPY ./polity .

################################################
# copy entrypoint + adjust permissions
################################################
COPY ./entrypoint.sh .
RUN chmod +x /entrypoint.sh

CMD ["/usr/src/polity/entrypoint.sh"]



# (-p flag = create all directories)
# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static

# # add non-root user
# RUN adduser --disabled-password --disabled-login polity
# # own relevant directories
# RUN chown -R polity:polity /vol
# RUN chown -R polity:polity /polity
# RUN chown -R 755 /vol/web

# # switch user
# USER polity
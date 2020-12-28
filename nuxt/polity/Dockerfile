#########
# FINAL #
#########


# pull official base image
FROM node:12.18.3-alpine3.9 as builder

# set work directory
WORKDIR /polity

# install dependencies and avoid `node-gyp rebuild` errors
COPY ./package.json .
RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && apk del .gyp

# copy our react project
COPY . .

# run
RUN npm install
RUN npm run build

# expose port
EXPOSE 3000

# environment
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

# install serve
RUN npm start

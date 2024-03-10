ARG NODE_VERSION=16.14-alpine
FROM node:${NODE_VERSION} as node

FROM node as client-local-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./package*.json .

RUN npm install

RUN chmod a+rwx /app/node_modules 

RUN mkdir /app/node_modules/.cache && chmod -R 777 /app/node_modules/.cache

COPY . ${APP_HOME}

CMD ["npm","start"]
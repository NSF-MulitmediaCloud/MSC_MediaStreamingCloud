FROM node:16-alpine3.11

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH


COPY streaming/package.json ./
COPY streaming/package-lock.json ./

RUN npm install --silent

RUN npm install react-scripts@4.0.3 -g --silent


COPY ./streaming/ ./


EXPOSE 3000

CMD ["npm","start"]

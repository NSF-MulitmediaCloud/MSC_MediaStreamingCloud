FROM node:16-alpine3.11

WORKDIR /app

COPY ./streaming ./

RUN npm install --production

RUN npm install @material-ui/core



EXPOSE 3000

CMD ["node","index.js"]

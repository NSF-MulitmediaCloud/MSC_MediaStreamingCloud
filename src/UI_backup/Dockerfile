FROM node:16-alpine3.11

WORKDIR /app

COPY ./js/package.json ./js/package-lock.json ./

RUN npm install --production

COPY ./js .

EXPOSE 3000

CMD ["node","index.js"]

FROM node:lts-alpine
RUN npm install -g http-server

WORKDIR /app
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install 
COPY . .
RUN npm run build
EXPOSE 7070
RUN chown -R node /app
USER node

CMD ["http-server", "dist"]

FROM node:16-slim

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . ./

# Сборка проекта Nuxt в продакшен
RUN npm run build

EXPOSE 3000
ENV PORT 3000

# Запуск в режиме продакшена (SSR)
CMD ["npm", "run", "start"]

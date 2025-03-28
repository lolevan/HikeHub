FROM node:16-slim

WORKDIR /app
# для панели управления (CSR)
COPY package.json package-lock.json ./
RUN npm install

COPY . ./

# Сборка проекта Nuxt в продакшен
RUN npm run build

EXPOSE 3001
ENV PORT 3001

# Запуск в режиме продакшена
CMD ["npm", "run", "start"]

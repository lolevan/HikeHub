FROM node:14

WORKDIR /app
# для панели управления (CSR)
COPY package.json package-lock.json ./
RUN npm install

COPY . ./

# Сборка проекта Nuxt в продакшен
RUN npm run build

EXPOSE 3000

# Запуск в режиме продакшена
CMD ["npm", "run", "start"]

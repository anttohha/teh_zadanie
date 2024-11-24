# Этап 1: Стадия разработки
FROM node:18-alpine AS development

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json в контейнер
COPY package.json package-lock.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код проекта в контейнер
COPY . .

# Открываем порт для локальной разработки
EXPOSE 3000

# Запускаем приложение в режиме разработки
CMD ["npm", "run", "dev"]

# Этап 2: Стадия продакшн
FROM node:18-alpine AS production

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только необходимые файлы (package.json и package-lock.json)
COPY package.json package-lock.json ./

# Устанавливаем только продакшн-зависимости
RUN npm install --production

# Копируем исходный код для продакшн-сборки
COPY . .

# Строим проект для продакшн-окружения
RUN npm run build

# Открываем порт для продакшн-сервера
EXPOSE 3000

# Запускаем приложение в продакшн-режиме
CMD ["npm", "start"]

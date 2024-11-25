# Stage 1: Install dependencies
FROM node:18-alpine AS deps

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package.json package-lock.json ./

# Устанавливаем зависимости
RUN npm ci --frozen-lockfile

# Stage 2: Development environment
FROM node:18-alpine AS dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем node_modules из предыдущего этапа
COPY --from=deps /app/node_modules ./node_modules

# Копируем весь проект (исключая файлы из .dockerignore)
COPY . .

# Устанавливаем переменную окружения для разработки
ENV NODE_ENV=development

# Открываем порт для разработки
EXPOSE 3000

# Команда для запуска в режиме разработки
CMD ["npm", "run", "dev"]

# Stage 3: Production environment
FROM node:18-alpine AS prod

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем node_modules из этапа deps
COPY --from=deps /app/node_modules ./node_modules

# Копируем весь проект
COPY . .

# Строим приложение для продакшена
RUN npm run build

# Устанавливаем переменную окружения для продакшена
ENV NODE_ENV=production

# Открываем порт для продакшена
EXPOSE 3000

# Команда для запуска в режиме продакшена
CMD ["npm", "start"]

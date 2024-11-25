# Stage 1: Install dependencies
FROM node:18-alpine AS deps
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package.json package-lock.json ./

# Устанавливаем зависимости
RUN npm ci

# Stage 2: Build application
FROM node:18-alpine AS builder
WORKDIR /app

# Копируем файлы проекта и зависимости
COPY . .
COPY --from=deps /app/node_modules ./node_modules

# Собираем Next.js-приложение
RUN npm run build

# Stage 3: Production image
FROM node:18-alpine AS production
WORKDIR /app

# Устанавливаем только production-зависимости
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Копируем собранное приложение
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

# Указываем переменную окружения для Next.js
ENV NODE_ENV production

# Порт, на котором будет запускаться приложение
EXPOSE 3000

# Команда запуска
CMD ["npm", "start"]

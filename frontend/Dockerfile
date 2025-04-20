# frontend/Dockerfile
FROM node:22-alpine AS dev

# Set legacy OpenSSL provider AND Node options
ENV NODE_OPTIONS="--openssl-legacy-provider --max-old-space-size=4096"
ENV CI=true

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]

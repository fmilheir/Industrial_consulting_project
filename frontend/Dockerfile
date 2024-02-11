# Build stage
FROM node:18 AS build

# Set working directory
WORKDIR /app


# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install all dependencies, including devDependencies necessary for the build
RUN npm install

# Copy the rest of the frontend codebase into the image
COPY . .

# Build the project using vue-cli-service
RUN npm run build

# Production stage (for serving the built Vue app)
FROM node:18-alpine AS production

# Set working directory
WORKDIR /app

# Copy the built Vue.js app from the previous stage
COPY --from=build /app/dist /app

# Expose the port for our frontend
EXPOSE 8080

# Create serve.js at the root
COPY server.js .

# Simple command to start a lightweight Node.js HTTP server 
CMD ["node", "server.js"] 
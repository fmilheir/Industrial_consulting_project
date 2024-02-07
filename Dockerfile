# Use Node.js version 18 as the base image 
FROM node:18 AS build

# Set the working directory inside the container 
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . . 

# Build the Vue.js application
RUN npm run build 

# Use nginx as the base image for serving the static files 
FROM nginx:alpine

# Copy the built Vue.js application from the previous stage to the nginx directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]

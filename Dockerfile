FROM nginx:alpine
COPY website/static/index.html /usr/share/nginx/html/
COPY website/static/Panchase-eco-tourism /usr/share/nginx/html/Panchase-eco-tourism/
COPY website/static/images /usr/share/nginx/html/images/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
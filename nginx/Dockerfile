FROM nginx:alpine

EXPOSE 1443

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY dhparam.pem /etc/nginx/dhparam.pem

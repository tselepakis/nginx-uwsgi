FROM nginx:1.15-alpine

RUN rm /etc/nginx/conf.d/*.conf

COPY ./sites/*.conf /etc/nginx/conf.d/

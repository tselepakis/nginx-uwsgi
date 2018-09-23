# uWSGI and Nginx

This project is a simple setup to experiment with deploying python apps with uWSGI and Nginx.

# Setup

We have a simple setup of containerized Nginx and uWSGi communicating over a unix socket connection.

# Notes

## uSWGI
* No default timeout on the worker
* Time in the logs refers to the time worker spent to serve it. So, if the request made in 00:00 and the worker start processing it at 00:05 and finished at 00:10, the time log will be 5 secs, but the request took 10 secs
* Timestamp refers to the time the request reached uWSGi

Log sample:
```
web_1    | [pid: 11|app: 0|req: 3/8] 172.18.0.1 () {42 vars in 627 bytes} [Sun Sep 23 10:47:35 2018] GET /?sleep=5 => generated 57 bytes in 5005 msecs (HTTP/1.1 200) 2 headers in 79 bytes (1 switches on core 0)
```
So, for the above sample the worker start processing the request at `10:47:35` and finished 5 secs later
in `10:47:40`.

## Nginx

* Default timeout is 60 secs
* client_max_body_size can be defined in specific location (TBT)
* Timestamp refers to the finish time of the request processing

Log sample:
```
nginx_1  | 172.18.0.1 - - [23/Sep/2018:10:47:40 +0000] "GET /?sleep=5 HTTP/1.1" 200 57 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0"
```
So, for the above sample Nginx inform us that the request was finished at `10:47:40`


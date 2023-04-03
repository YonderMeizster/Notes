# HTTP 1.1

Стоит вспомнить, что строка подключения (request line) при использовании 
HTTP 1.0 была достаточна для того, чтобы сервер её обработал. То есть имя
запрашиваемого ресурса ни в коей мере не важно. А из этого можно сделать вывод о
том, что HTTP 1.0 был разработан с мыслью о том, что на одном хосте может
располагаться только один сайт (порт по- умолчанию то один, восьмидесятый).

HTTP 1.1 нивилирует это ограничение и вводит такое определение как виртуальные
хосты. В этой версии протокола помимо обязательной request line обязателен еще и
заголовок host. По этому заголовку сервер определяет, какой домен необходим
клиенту.

Значит, подобный запрос не должен ассоциироваться с ответом 200?
```
ser@coding:~$ telnet google.com 80
Trying 216.58.210.142...
Connected to google.com.
Escape character is '^]'.
HEAD / HTTP/1.1
```

Как- бы да, но на самом деле не со всем. Веб- сервер гугл, в данном случае,
обнаружит отсутствие заголовка host и вернет сайт по умолчанию. К примеру, такое
поведение можно настроить в Nginx. Соответствие стандарту требует указания
заголовка host.

```
HEAD / HTTP/1.1
host: google.com    

HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-qd-N0jGfkacIm-nM0POcRQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
Date: Mon, 03 Apr 2023 20:16:13 GMT
Expires: Wed, 03 May 2023 20:16:13 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

```

Сразу стоит отметить вот какую штуку: при использовании http 1.1 соединение не
закрывается после того, как клиент получил ответ. По всей видимости, это было
реализовано, когда стало ясно, что человечество активно исползует http для
потоковой передачи кусоков больших данных. Избавление от закрытия-открытия
соединения было сделано в целях снижения инфраструктурных расходов. Для этого в
протокол http 1.1 был введен механизм KeepAlive (Что он делает- понятно).

А вообще- то можно и принудительно закрыть соединение, для этого необходимо
указать заголовок: 'connection: close'.

```
HEAD / HTTP/1.1
host: google.com
connection: close

HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-iYYOrPNrMG24zSAOt7yXsQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
Date: Mon, 03 Apr 2023 20:26:21 GMT
Expires: Wed, 03 May 2023 20:26:21 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Connection: close

Connection closed by foreign host.
```

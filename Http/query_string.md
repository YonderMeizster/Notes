# Передача данных query string

query string - параметры, находящиеся в request line. Представляют собой
последовательность парметров ключ=значение, разделенные знаком амперсант &

```
POST /login?key=value HTTP/1.1

# или

GET /?key1=value1&key2=value2 HTTP/1.1
```

query string не имеет никакого отношения к GET запросам, хоть зачастую их и
называют get- параметрами. Получается, что get-параметры- параметры,
передаваемые через URL в запросе (через request line), вместе с ними можно
передать и параметры в теле запроса.

Query string используются при работе с формами на так называемую выборку данных.
К примеру, запрос в поисковой строке приведет к посещению такого url:

```
https://www.google.com/search?q=погода+в+москве& ...
```
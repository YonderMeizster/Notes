# Cookies

Куки позволяют впихнуть "сохранение состояния" в протокол без сохранения
состояния, каковым и является http.

```
user@coding:~$ curl --head https://ya.ru
HTTP/2 302 
location: https://ya.ru/?nr=1&redirect_ts=1680639628.00000
date: Tue, 04 Apr 2023 20:20:28 GMT
nel: {"report_to": "network-errors", "max_age": 100, "success_fraction": 0.001, "failure_fraction": 0.1}
x-content-type-options: nosniff
set-cookie: yandex_csyr=1680639628:1; Path=/; Domain=ya.ru; Expires=Wed, 03 Apr 2024 20:20:28 GMT; Secure
set-cookie: is_gdpr=0; Path=/; Domain=.ya.ru; Expires=Thu, 03 Apr 2025 20:20:28 GMT
set-cookie: is_gdpr_b=CPzoGBDvrwEoAg==; Path=/; Domain=.ya.ru; Expires=Thu, 03 Apr 2025 20:20:28 GMT
set-cookie: _yasc=gsULGolKH0jZIYSkZZdS2SYTZ2otWgKQ4gxzheGkQPEMFy78lwAgZyBhDSsvfg==; domain=.ya.ru; path=/; expires=Fri, 01-Apr-2033 20:20:28 GMT; secure
set-cookie: i=qekvpBlessuHd1pT1sXmfhT/pHjAfQz2l/XSCaYoixhtkyMBPI8GAjfWp2R2PGnxVp28hmuydaeTr4igEzSycb0LKPQ=; Expires=Thu, 03-Apr-2025 20:20:28 GMT; Domain=.ya.ru; Path=/; Secure; HttpOnly
set-cookie: yandexuid=9863468991680639628; Expires=Thu, 03-Apr-2025 20:20:28 GMT; Domain=.ya.ru; Path=/; Secure
p3p: policyref="/w3c/p3p.xml", CP="NON DSP ADM DEV PSD IVDo OUR IND STP PHY PRE NAV UNI"
expires: Tue, 04 Apr 2023 20:20:28 GMT
x-yandex-req-id: 1680639628801665-14477189235286346899-balancer-l7leveler-kubr-yp-vla-78-BAL-2916
last-modified: Tue, 04 Apr 2023 20:20:28 GMT
accept-ch: Sec-CH-UA-Platform-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA, Sec-CH-UA-Full-Version-List, Sec-CH-UA-WoW64, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Platform, Sec-CH-UA-Full-Version, Viewport-Width, DPR, Device-Memory, RTT, Downlink, ECT
report-to: { "group": "network-errors", "max_age": 100, "endpoints": [{"url": "https://dr.yandex.net/nel", "priority": 1}, {"url": "https://dr2.yandex.net/nel", "priority": 2}]}
cache-control: no-cache,no-store,max-age=0,must-revalidate
```

Вот такой запрос был отправлен к yandex через curl. В ответ яндкс вернул
несколько заголовков set-cookie. Это именно те куки, которые запоминает браузер
и затем при новых запросах будет их пристыковывать в качестве заголовков.

Каждый заголовок set-cookie выставляет одну куку, при этом сама кука состоит из
нескольких пар ключ=значение, разделенных точкой с запятой.

>set-cookie: yandexuid=9863468991680639628; Expires=Thu, 03-Apr-2025 20:20:28 GMT; Domain=.ya.ru; Path=/; Secure

О предназначении Secure: такая кука устанавливается только если была передана по
HTTPS. А вот Domain и Path отвечают за область видимости куки.

## Сессионные куки

Такая кука кхранится лишь в оперативной памяти и пропадет после закрытия веб-
страницы

## Постоянные куки

Такие куки сохраняются в постоянное хранилище браузера и "подтягиваются" сайтом
даже после перезагрузки ЭВМ.

При этом через аттрибуты кук, такие как expires= ... или MAX-AGE= ... можно
управлять длиной их жизни.

С клиента на сервер все куки поступают в виде одного заголовка "cookie:".
Разделенные точкой с запятой.
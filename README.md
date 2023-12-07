# Утилита "DNServer"

Запуск: будучи в папке "DNServer", введите в командной строке\
`python main.py` и сервер запустится!

## Взаимодействие
С помощью DNS-клиента отправьте запрос на localhost(127.0.0.1) и получите ответ от сервера.

Пример: dig google.com @127.0.0.1

## Подробности реализации
UDP поддерживает, TCP - нет. Поддерживает только "A" - тип записи.
Есть кэширование, с учетом времни жизни.
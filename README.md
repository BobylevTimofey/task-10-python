# Задание 10 технологии программирования
1)Сделал профилирование
# для filter.py
![профилирование filter.py](https://github.com/BobylevTimofey/task-10-python/blob/main/report%20profile%20filter.jpg)
# для old_filter.py
![профилирование old_filter.py](https://github.com/BobylevTimofey/task-10-python/blob/main/report%20profile%20old_filter.jpg)

Из скриншотов видно, что функция apply_filter выполнилась почти в 1000 раз быстрее. Это связано с тем, что операции numpy лучще оптимизированы и поэтому намного быстре импиративного программирования. Конечно, сам файл filter.py выполнялся дольше из-за ввода данных.

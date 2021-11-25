# Задание 10 технологии программирования

# Сделал профилирование

# Для filter.py
![профилирование filter.py](https://github.com/BobylevTimofey/task-10-python/blob/main/report%20profile%20filter.jpg)

# Для old_filter.py
![профилирование old_filter.py](https://github.com/BobylevTimofey/task-10-python/blob/main/report%20profile%20old_filter.jpg)

Из скриншотов видно, что функция **apply_filter**(не учитывая ввод данных) выполнилась почти в 18 раз быстрее. Это связано с тем, что операции **numpy** лучще оптимизированы и поэтому намного быстрее импиративного программирования. Конечно, сам файл **filter.py** выполнялся дольше из-за ввода данных. Поэтому выполним аналогичный код **filter.py**, но без ввода данных и с теми же настройками, что для **old_filter.py**.

# для filter_with_filename.py
![профилирование filter_with_filename.py](https://github.com/BobylevTimofey/task-10-python/blob/main/report%20profile%20filter_with_filename.jpg)

Видим, что действительно без ввода данных программа работает быстрее, файл **filter_with_filename.py** выполнился примерно в 8.5 раз быстрее чем старый фильтр.

Давайте сравним результаты работы наших фильтров. Для старого фильтра и фильтра без ввода данных размер мозайки = 10px и 5 градаций серого, а для фильтра с вводом данных размер мозайки = 10px и 10 градаций серого.

# Изначальное изображение
![Изначальное изображение](https://github.com/BobylevTimofey/task-10-python/blob/main/cat%20test%20photo.jpg)

# Изображения, полученные в результате работы фильтров 

# Для старого фильтра
![результат старого фильтра](https://github.com/BobylevTimofey/task-10-python/blob/main/result_old_filter.jpg)

# Результат фильтра без ввода данных
![результат фильтра без ввода данных](https://github.com/BobylevTimofey/task-10-python/blob/main/result_filter_with_filename.jpg)

# Результат фильтра с вводом данных
![результат фильтра с вводом данных](https://github.com/BobylevTimofey/task-10-python/blob/main/result_filter.jpg)

К функциям написал документацию. Доктест сделал только для нахождения среднего, так как другие функции ничего не возвращают. В доктесте написал два теста один верный и один не верный. Докстесты запустил с помощью **PyCharm**, но пробовал и с помощью терминала. Ниже представлен скриншот с результатом доктеста запущенного с **PyCharm**

# Результаты доктеста
![результаты доктеста](https://github.com/BobylevTimofey/task-10-python/blob/main/doctest.jpg)

Через отладчик вывел на экран ширину и высоту изображения, а также тип изображения. Также в отладчике вывел значения ширины блока и количество градаций серого.

# Скриншот отладчика
![результаты отладчика](https://github.com/BobylevTimofey/task-10-python/blob/main/debug%20info.jpg)








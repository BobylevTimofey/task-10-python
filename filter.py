from PIL import Image
import numpy as np


def apply_filter():
    """
    Принимает вводимые параметры, применяет фильтр и возвращает измененное фильтром изображение
    :return: измененное фильтом изображение
    """
    path_img = input("Введите путь к фото, которое хотите преобразовать:")
    img = Image.open(path_img)
    output_name = input("Введите название фото - результата:")
    mosaic_size = int(input("Введите размер мозайки в пикселях:"))
    count_gradations = int(input("Введите количество градаций серого:"))
    data_img = np.array(img)
    size_img = data_img.shape

    for x in range(0, size_img[0], mosaic_size):
        for y in range(0, size_img[1], mosaic_size):
            paint_cell(data_img, x, y, mosaic_size, count_gradations)

    res = Image.fromarray(data_img)
    path_output = path_img[0:path_img.rindex('\\') + 1]
    res.save(f"{path_output}{output_name}")


def find_average_brightness_cell(arr, px_width, px_height, mosaic_size):
    """
    Находит среднюю ярскость пикселей
    :param arr: массив с пикселями
    :param px_width: позияия по ширине
    :param px_height: позиция по высоте
    :param mosaic_size: размер мозайки
    :return: среднюю яркость пикселей в мозайке
    >>> find_average_brightness_cell(np.array([[[1,1,1],[1,1,1]],[[1,1,1],[1,1,1]]]),0,0,2)
    1.0
    >>> find_average_brightness_cell(np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]]),0,0,2)
    1.0
    """
    return np.average(arr[px_width:px_width + mosaic_size, px_height: px_height + mosaic_size])


def paint_cell(arr, px_width, px_height, mosaic_size, count_gradations):
    """
    Перекрашивает пиксели
    :param arr: массив с пикселями
    :param px_width: позияия по ширине
    :param px_height: позиция по высоте
    :param mosaic_size: размер мозайки
    :param count_gradations: количество градаций серого
    :return: перекрашенные пиксели в мозайке
    """
    average_brightness = find_average_brightness_cell(arr, px_width, px_height, mosaic_size)
    gradations = 255 // count_gradations
    px_brightness = average_brightness // gradations * gradations
    arr[px_width:px_width + mosaic_size, px_height:px_height + mosaic_size, ][:] = px_brightness


if __name__ == "__main__":
    apply_filter()

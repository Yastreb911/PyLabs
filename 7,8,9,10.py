# Прописать в консоли pip install pillow для работы модулей
# импортируем модули
from PIL import Image # Работа с фото
from PIL import ImageFont # Работа со шрифтами
from PIL import ImageDraw # Создание новых фото
from PIL import ImageFilter #  Работа с фильтрами
from PIL.ExifTags import TAGS # Работа с exif тэгами
import os
import csv
import json



def PictShowing(path): # 7.1 Выводим фото на экран
    # Подготовьте любой графический файл для выполнения практической работы.
    # Напишите программу, которая открывает и выводит этот файл на экран.
    # Получите и выведите в консоль информацию о размере изображения, его формате, его цветовой модели.
    picture = Image.open(path) # Открываем фото в переменной
    picture.show() # Выводим фото на экран

def PictPrintInfo(path): # 7.1 Печать информации о фото
    picture = Image.open(path)  # Открываем фото в переменной
    print(picture.filename)  # Отображаем путь к фото в коноли
    print(picture.format) # Выводим информацию о формате фото
    print(picture.size) # Выводим информацию о размере фото
    print(picture.mode) # Выводим информацию о цветовой схеме фото
    print(type(picture))
    exifdata = picture.getexif() # Выводим информацию о дате, устройстве захвата и т.д.
    for tagid in exifdata: # Парсим exif данные
        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        print(f"{tagname:25}: {value}")
    print(picture.__dict__)

def PictTransp(path): # 7.2 Отзеркаливание фото
    # Напишите программу, которая создаёт уменьшенную в три раза копию изображения.
    # Получите горизонтальный и вертикальный зеркальный образ изображения.
    # Сохраните изображения в текущую папку под новым именем.
    picture = Image.open(path)  # Открываем фото в переменной
    picture = picture.reduce(3)  # уменьшаем фото в 3 раза
    picture.show()  # Выводим фото на экран
    picture = Image.open(path)  # Открываем фото в переменной
    picture = picture.transpose(0) # Зеркалим фото по горизонтали
    picture.show()
    picture = Image.open(path)  # Открываем фото в переменной
    picture = picture.transpose(5) # Зеркалим фото по вертикали
    picture.show()

def PictFilterRGB(path): # 7.3 Наложить фильтр (альтернативный способ методом изменения очерёдности цветовых каналов)
    picture = Image.open(path) # Открываем фото в переменной
    r, g, b = picture.split() # Раскладываем фото на цветовые каналы
    picture = Image.merge(mode="RGB", bands=(r, b, g)) # Собираем цветовые каналы в другой очередности
    picture.show() # Выводим фото на экран
    picture.save("redacted.JPG")  # Сохраняем фото

def PictSharp(): # 7.3 9.1(Модифицировать) 9.2 (Модифицировать) Наложить фильтр
    # Подготовьте 5 графических файлов с именами 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg.
    # Напишите программу, которая применит ко всем этим файлам сразу любой фильтр (кроме размытия,
    # т.к. он рассматривался на лекции).
    # Сохраните изображения в новую папку под новыми именами.
    # 9.1 - Модифицируйте программу из практики 7.3 (7 лабораторная работа ) или создайте заново:
    # обработать любой операцией все картинки в заданной папке, используя для обхода файлов в папке модуль os (или Pathlib).
    # При этом каталог для итоговых (обработанных) изображений должен тоже создаваться с помощью модуля os или Pathlib.
    # 9.2 - Модифицировать программу из практики 9.1, добавив проверку типа (расширения) файла,
    # если в папке хранятся разные типы файлов, а вам нужно обработать только заданные (jpg, png).
    # Модификация 9.1:
    if not os.path.isdir("LabFiles/Redacted"): # Проверяем существование каталога
        os.mkdir("LabFiles/Redacted")  # Создаём новый каталог в случае его отсутствия.
    ListOfFiles = os.listdir("LabFiles") # Добавляем все файлы корневого каталога в переменную список
    for format in ListOfFiles:  # Читаем список в переменную "формат" с помощью цикла
        # Модификация 9.2
        if ".jpg" in format or ".png" in format: # Ищем файлы с нужными расширениями. Если раширение подошло:
            # Выполяем 7.3
            picture = Image.open(format) # Открываем фото в переменной по значению из списка
            picture = picture.filter(ImageFilter.SHARPEN) # Накладываем фильтр повышения резкости
            picture.show() # Выводим фото на экран
            picture.save(str("LabFiles/Redacted/NEW___") + str(format))  # Добавляем "NEW___" к имени файла и сохраняем его.

def watermarkPict(input_image_path, output_image_path, watermark_image_path, positionX, positionY): # 7.4 Наложение водяного знака
    # Напишите программу, которая добавляет на изображение водяной знак.
    base_image = Image.open(input_image_path) # Открываем исходное фото в переменной
    watermark = Image.open(watermark_image_path) # Открываем водяной знак в переменной
    width, height = base_image.size # Читаем размеры исходника в переменную
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0)) # Создаём новое фото с размерами исходника (прозрачное RGBA)
    transparent.paste(base_image, (0, 0)) # Накладываем на него исходник
    transparent.paste(watermark, (positionX, positionY), mask=watermark) # Накладываем водяной знак на новое фото
    transparent.show() # Отображаем получившийся файл
    transparent.save(output_image_path) # Сохраняем получившийся файл

def PictCrop(path, x1, y1, x2, y2): # 8.1 Обрезка фото
    # Скачайте любую открытку из интернета, определите область,
    # которую Вам нужно вырезать из данного изображения (обрезать текст, часть фото и т.д.).
    # Напишите программу, которая выполнит эту операцию.
    # Сохраните изображения в текущую папку под новым именем.
    picture = Image.open(path)  # Открываем фото в переменной
    print(picture.size) # Печатаем размеры фото (для удобства подгонки размеров вырезаемой области)
    picture = picture.crop((x1, y1, x2, y2)) # Обрезаем фото по заданным координатам.
    picture.show() # Открываем обрезанное фото
    picture.save("Открытка ОБРЕЗАНО.png") # Сохраняем обрезанное фото под новым именем.

# Словари для 8.2 и 8.3
# Словарь праздник - путь к фото открытки к празднику
CelebsPath = {"новый год": "LabFiles/Открытки/6.JPEG", "день рождения": "LabFiles/Открытки/7.JPG", "23 февраля": "LabFiles/Открытки/8.JPG", "8 марта": "LabFiles/Открытки/9.JPG"}
# Словарь праздник - его склонение
CelebsText = {"новый год": "Новым годом, ", "день рождения": "Днём рождения, ", "23 февраля": "23-ем февраля, ", "8 марта": "8-ым марта, "}
# Словарь праздник - координаты текста по Х для открытки
CelebsCoordX = {"новый год": 350, "день рождения": 620, "23 февраля": 200, "8 марта": 220}
# Словарь праздник - координаты текста по У для открытки
CelebsCoordY = {"новый год": 500, "день рождения": 900, "23 февраля": 500, "8 марта": 165}

def  Congrats(celeb, conname): # 8.2 8.3(Модифицировать)
    # Создайте словарь, содержащий перечень пары «Название праздника – имя_файла с открыткой к нему».
    # Спросите у пользователя, к какому празднику ему нужна открытка и выведите нужную открытку наэкран.
    # 8.3 - Модифицируйте задачу 8.1 так: спросите еще у пользователя,
    # имя того, кого он хочет поздравить, добавьте на заданную открытку
    # текст «…., поздравляю!», где вместо …. вставьте полученное
    # имя (выведите его разным цветом и шрифтами, посередине вверху или внизу фото).
    # Найдите в сети интернет решение, как сделать надпись жирным текстом (по умолчанию, такого параметра нет).
    # Сохраните новую открытку в файл с расширением png.
    path = CelebsPath.get(celeb) # Получаем путь к открытке
    print("Путь к файлу - "+ str(path)) # Выводим путь (отладка)
    ConText = CelebsText.get(celeb) # Получаем текст поздравления
    print("Текст поздравления - "+ str(ConText)) # Выводим текст поздравления (отладка)
    CelebCoordX = CelebsCoordX.get(celeb) # Получаем координаты по Х
    print("Координаты текста по Х - "+ str(CelebCoordX)) # Выводим координаты по Х (отладка)
    CelebCoordY = CelebsCoordY.get(celeb) # Получаем координаты по У
    print("Координаты текста пл У - "+ str(CelebCoordY)) # Выводим координаты по У (отладка)
    print("Имя получателя - "+ str(conname)) # Выводим имя получателя (отладка)
    font_fname = '/fonts/Arial/arial.ttf'  # Прописываем путь к основеому шрифту
    font_fname_bold = '/fonts/Arial/arialbd.ttf'  # Прописываем путь к жирному шрифту
    font_size = 70  # Устанавливаем размер шрифта
    font = ImageFont.truetype(font_fname, font_size)  # Устанавливаем стиль для обычного текста
    font_bold = ImageFont.truetype(font_fname_bold, font_size)  # Устанавливаем стиль для жирного текста
    with Image.open(path) as picture: # Открываем изображение в переменной
        draw = ImageDraw.Draw(picture) # Создаём но новое фото в объекте draw
        draw.text(xy=(CelebCoordX, CelebCoordY), text="Поздравляю с ", font=font, fill=(0, 255, 0)) # Пишем зелёным шрифтом
        TL = font.getlength("Поздравляю с ") # Вычисляем длинну написанного текста указанным шрифтом
        draw.text(xy=(CelebCoordX + TL, CelebCoordY), text=ConText + " ", font=font, fill=(0, 0, 255)) # Пишем Голубым шрифтом
        TL = TL + font.getlength(ConText) # Вычисляем длинну написанного текста указанным шрифтом
        draw.text(xy=(CelebCoordX + TL, CelebCoordY), text=conname, font=font_bold, fill=(255, 0, 0)) # Пишем Красным шрифтом
    picture.show() # Вывоим полученное изображение на экран
    picture.save("Открытка с " + str(ConText) + ".png")# Сохраняем полученное изображение
def Pokupki(path): # 9.3 Работа с CSV файлами
    # Имеется файл с данными в формате csv:
    # Продукт,Количество,Цена
    # Молоко,2,80
    # Сыр,1,500
    # Хлеб,2,70
    # Напишите программу, которая считывает данные из этого файла,
    # подсчитывает итоговую сумму расходов и выводит данные в виде:
    # Нужно купить:
    # Молоко - 2 шт. за 80 руб.
    # Сыр - 1 шт. за 500 руб.
    # Хлеб - 2 шт. за 70 руб.
    # Итоговая сумма: 800 руб.
    print("Нужно купить")
    Price=0 # Будущая итоговая цена
    with open(path, encoding='utf-8') as r_file: # Открываем файл в переменной "r_file"
        file_reader = csv.reader(r_file, delimiter=";") # Создаем объект reader, указываем символ-разделитель ";"
        count = 0 # Счётчик строк, чтобы первая строка не считалась в в переменную
        for row in file_reader: # Построчно читаем файл в переменную "row"
            if count != 0: # Проверяем, что читается не первая строка файла
                Price = int(Price) + (int(row[2]) * int(row[1])) # К предыдущей цене добавляем новую цену, умноженную на кол-во штук
                # Цена =    Цена   + (цена товара * кол-во штук)
                print(f' {row[0]} - {row[1]} шт. за {row[2]} руб.')
            # Печать   имя товара - кол-во   шт за    цена    руб.
            count += 1 # Увеличиваем счётчик строк
    print(f' Итоговая сумма {Price} Руб.') # выводим итоговую цену

def JSON(path): # 10.1 10.2 Работа с JSON Файлами
    # 10.1 Имеется файл JSON с информацией о продуктах:
    # {
    #  "products": [
    # {
    # "name": "Шоколад",
    # "price": 50,
    # "available": true,
    # "weight": 100
    # },
    # {
    # "name": "Кофе",
    # "price": 100,
    # "available": false,
    # "weight": 250
    # },
    # {
    # "name": "Чай",
    # "price": 70,
    # "available": true,
    # "weight": 50
    # }
    #  ]
    # }
    # Напишите программу, которая считывает информацию из этого файла и выводит ее на экран в виде:
    # Название: Шоколад
    # Цена: 50
    # Вес: 100
    # В наличии
    # Название: Кофе
    # Цена: 100
    # Вес: 250
    # Нет в наличии!
    # Название: Чай
    # Цена: 70
    # Вес: 50
    # В наличии
    with open(path, encoding='utf-8') as JsonFile: # Открываем файл в переменной JsonFile
        reader = json.load(JsonFile) # Читаем файл в переменную
    print(reader)
    print(type(reader))
    ProductsList = reader.get("products") # Словарь продукты содержми список из словарей
    print(ProductsList) # Смотрим список словарей
    print(type(ProductsList))
    ProductsDict = ProductsList[1] # Берём для проверки первый словарь из списка
    print(ProductsDict) # Получаем продукты из первого словаря
    print(type(ProductsDict))
    # То есть структура файла следующая:
    # Продукты(Словарь)                reader
    #   1. Продукты: Список            ProductsList
    #          1. Словарь              ProductsDict
    #          2. Словарь              ProductsDict
    #          3. Словарь              ProductsDict
    # Теперь выполним все те же действия для остальных словарей
    ProductsListLen = (len(ProductsList)) # Узнаём количество элементов в списке
    count = 0
    while count != ProductsListLen:
        ProductsDict = ProductsList[count]  # Берём словарь из списка
        print(f' Название: {ProductsDict.get("name")}')  # Получаем имя продукта из словаря
        print(f' Цена: {ProductsDict.get("price")}')  # Получаем имя продукта из словаря
        print(f' Вес: {ProductsDict.get("weight")}') # Получаем вес продукта из списка
        if ProductsDict.get("available") == True: # Проверяем наличие продукта
            print("В наличии")
        if ProductsDict.get("available") == False:
            print("Нет в наличии!")
        print(" ") # Добавляем пустую строку между позициями
        count += 1 # Следующий цикл
    # 10.2 Модифицируйте программу 10.1 – добавьте в нее код,
    # который добавляет данные в файл JSON (спрашивает их у пользователя) и потом также выводить содержимое итогового файлана экран.
    name = input("Название: ")
    price = input("Цена: ")
    weight = input("Вес: ")
    available = input("Наличие (0 - нет, 1 - есть: ")
    if available == "0":
        available = False
    if available == "1":
        available = True
        # Проверяем корректность значений
    if name != "" and name.isdigit() == False and price.isdigit() == True and weight.isdigit() == True and (available == True or available == False):
        # Создаём словарь из новых данных
        NewDict = {"name": name, "price": price, "weight": weight, "available": available}
        print(NewDict)
        ProductsList.append(NewDict) # Добавляем в конец списка новый словарь
        reader = {"products": ProductsList} # Обновляем ридер новыми данными
        with open(path, 'r+', encoding='utf-8') as JsonFileWrite:  # Открываем файл для записи в переменной JsonFile
            JsonFileWrite.write(json.dumps(reader, sort_keys = False, indent = 4, ensure_ascii = False, separators = (',', ': ')))
    else:
        print("Введены неверные значения!")
def TXT(path, OutputPath): #10.3 Работа с TXT файлами
    # 10.3 Создание русско-английского словаря.
    # Имеется файл en-ru.txt, в котором находятся строки англорусского словаря в таком формате:
    # cat - кошка
    # dog - собака
    # home - домашняя папка, дом
    # mouse - мышь, манипулятор мышь
    # to do - делать, изготавливать
    # to make – изготавливать
    # и т.п.
    # Требуется создать русско-английский словарь и вывести его в файл ru-en.txt в таком формате:
    # делать – to do
    # дом – home
    # домашняя папка – home
    # изготавливать – to do, to make
    # кошка – cat
    # манипулятор мышь – mouse
    # мышь – mouse
    # собака – dog
    with open(path, encoding='utf-8') as TXTFile: # Открываем файл
        file_reader = csv.reader(TXTFile, delimiter="-")  # Создаем объект reader, указываем символ-разделитель ";"
        RuEn={} # Создаём словарь для будущих значений рус-англ
        for row in file_reader:  # Построчно читаем файл в переменную "row"
            ru="" # Обнуляем ключ словаря
            for parse in row[1]: # Разбираем русское слово
                if parse == ",": # Если есть запятая, эначит имеем пару русских значений
                    # А значит нужно и 2 ключа или бльше
                    addons = {ru: row[0]} # Записываем слово, найденное до запятой в переменную и аглийское значение к нему
                    RuEn.update(addons) # Добавляем полученную пару в наш словарь
                    parse="" # Обнуляем переменные, чтобы следующее значение было записано без предыдущего
                    ru = ""
                ru += str(parse) # Записываем найденные во время разбора символы, если не наткнулись на запятую
                # иначе переменная остаётся пустой (из-за обнуления, по условию выше)
            if ru != "": # Если после разбора переменной остались символы - значит, это последний ключ в строке или единственный (запятых не было и условие не выполнилось)
                addons = {ru: row[0]} # Записываем слово, найденное до запятой в переменную и аглийское значение к нему
                RuEn.update(addons) # Добавляем полученную пару в наш словарь
            print(RuEn)
        RuList=list(RuEn.keys()) # Создаём список из русскоязычных ключей
        RuList.sort() # Сортируем полученный список по алфавиту
        print(RuList)
        with open(OutputPath, 'w+', encoding='utf-8') as TXTFile:  # Открываем файл для записи в переменной
            RuListLen=len(RuList) # узнаём количество элементов в списке
            count = 0
            while count != RuListLen:
                TXTFile.write(f' {RuList[count]} - {RuEn.get(RuList[count])}\n') # Записываем ключ - эначение в новый файл
                count += 1

MyLabs = input("Номер лабы: ")
if MyLabs == "7.1":
    PictShowing("LabFiles/first.jpg") # 7.1 Отобразить любое изображение
    PictPrintInfo("LabFiles/first.jpg") # 7.1 Отобразить информацию о фото
if MyLabs == "7.2":
    PictTransp("LabFiles/first.jpg") # 7.2 Отзеркаливание изображения
if MyLabs == "7.3" or MyLabs == "9.1" or MyLabs == "9.2":
    PictFilterRGB("first.jpg") # 7.3 Наложить фильтр (альтернативный способ)
    PictSharp() # 7.3 Наложить фильтр (альтернативный способ)
if MyLabs == "7.4":
    watermarkPict("1.jpg", "11s.png", "yastreb.ico", 3008, 2200) # 7.4 Накладываем водяной знак на фото:
    # Очерёдность:исходник/выходной файл/файл с водяным знаком/позиция
if MyLabs == "8.1":
    PictCrop("LabFiles/открытка.png", 239, 37, 1280, 853) # 8.1 Обреззка фото
if MyLabs == "8.2" or MyLabs == "8.3":
    Congrats(input("Назовите праздник"), input("Имя получателя"))
if MyLabs == "9.3": # Работа с CSV файлами
    Pokupki("LabFiles/Pokupki.csv")
if MyLabs == "10.1" or MyLabs == "10.2": # Работа с JSON файлами
    JSON('LabFiles/Products.JSON')
if MyLabs == "10.3": # Работа с TXT файлами
    TXT("LabFiles/en-ru.txt", "ru-en.txt")
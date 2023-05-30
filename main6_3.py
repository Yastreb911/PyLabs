Langs={"Китайский": "1", "Французкий": "2", "Немецкий": "3", "Английский": "4", "Русский": "5", "Хинди": "6"}
Studs={"Иванов": "135", "Петров": "134", "Сидоров": "24", "Паронько": "12345", "Зубрилкин": "34", "Хулиганов": "5", "Полиглотов": "12345", "Кодер": "4",}
StudsKeys=Studs.keys() # Получаем Ключи-имена студентов
print(StudsKeys) # Это пригодится для создания списка всех языков, которые знают студенты
StudsLangs=[] #Создаём список из всех языков, которые знают студенты
for Student in StudsKeys:
    StudsLangs.append(Studs.get(Student)) # Получаем список из индексов языков
print(StudsLangs)
# Теперь избавимся от повторов. Для этого сначала склеим все языки в одной переменной
LangsCount=""
for Temp in StudsLangs:
    LangsCount += str(Temp) # Склеиваем все индексы в один большой
print (LangsCount)
# Мы получили длинное число. Убираем из него повторяющиеся элементы
Temp = 9
# Создаём цикл. Если номер цикла совпадёт с числом в переменной - выписываем число и немедленно
# переходим к следующему шагу цикла
Temp2=""
while Temp >=0:
    for Temp1 in LangsCount:
        if int(Temp1) == int(Temp):
            Temp2 += Temp1
            break
    Temp -=1
LangsCount=Temp2
print(LangsCount) # Мы получили индексы всех известных языков
# Теперь выведем колиество этих различных языков
print(len(LangsCount))
# Создаём список из языков, которые знают студенты.
# Для удобства взаимодействия поменяем ключ и значение местами в словаре языков
LangsRevers = dict(zip(Langs.values(), Langs.keys()))
print(LangsRevers) # Теперь можно выполнять поиск по индексу в новом словаре
# Теперь распарсим переменную LangsCount, где хранятся индексы языков и Вытащим нужные языки из словаря
KnownLangs=[] # Список для известных языков
for Temp in LangsCount:
    KnownLangs.append(LangsRevers.get(Temp))
print(KnownLangs)
# Отсортируем получившийся список
KnownLangs.sort()
print(KnownLangs)
# Теперь выведем список студентов, которые знают введённый язык
SrcLang = input("Введите интересующий язык")
# Для этого в словаре найдём соответствующий указанному языку индекс
SrcLangIndex = Langs.get(SrcLang)
print(SrcLangIndex) # Мы вытащили индекс интересующего языка
# Для удобства так же перевернём словарь со студентами
StudsRevers = dict(zip(Studs.values(), Studs.keys()))
print(StudsRevers)
Final=[]
# Теперь разберём ключи-индексы, присвоенные студентам и найдём в них соответствующий нашему
for Temp in StudsRevers: # За один цикл получаем все языки, которые знает студент
    for Temp1 in Temp: # А в этом подцыкле проверяем, есть ли среди всех них нужный нам
        if Temp1 == SrcLangIndex: # Если нашли совпадения - Добавляем студента по ключу из перевёрнутого словаря
            Final.append(StudsRevers.get(Temp))
print(Final)
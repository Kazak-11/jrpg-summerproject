import mapModule as maps
import entityModule as entitys

size = int(input())

map = maps.gen(size) #Генерация простейшей карты
entMap = maps.gen(size)
player = entitys.Player(entMap, 0, 0)
bear = entitys.Bear(entMap, 0,1)
chest = entitys.Chest(entMap, 3,3, 0)
trader = entitys.Trader(entMap, 4,4, 0)
entList = [bear,chest, trader] #Первичная генерация тестовых сущностей
image = maps.over(map, entMap)
maps.print_array(image)

a = 1
while a == 1: #игровой цикл
    player.action(image) #Происходит ход игрока
    for entity in entList: #Для каждой сущности в листе происходит ход
        entity.turn()
    image = maps.over(map, entMap) #Накладывание карты с сущностями на карту с местностью
    maps.print_array(image) #Выдает игровую карту

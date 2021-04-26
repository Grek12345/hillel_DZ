# Дан список:
# [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3,9, 4.0+5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]
a = [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3,9, 4.0+5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]

# 1.1 Исключить из внутренних вложенних списков "мусор" - обекти у которих тип данних в меньшенстве по сравнению с превалирующим типом.
for i in range(len(a)-1, -1, -1):
    for j in range(len(a[i])-1, -1, -1):
        if type(a[i][j]).__name__ in ('NoneType', 'complex'):
            del a[i][j]

print(a)


# 1.2 Сделать три копии основного списка.
import copy
a = [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3,9, 4.0+5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]
b = [*a]
c = copy.copy(a)
d = copy.deepcopy(a)


# 1.3 Приобразовать єти копии таким образом, чтоби каждая копия:
# не имела "мусора" (п.2.1);
for i in range(len(b)-1, -1, -1):
    for j in range(len(b[i])-1, -1, -1):
        if type(b[i][j]).__name__ in ('NoneType', 'complex'):
            del b[i][j]
print(b)

for i in range(len(c)-1, -1, -1):
    for j in range(len(c[i])-1, -1, -1):
        if type(c[i][j]).__name__ in ('NoneType', 'complex'):
            del c[i][j]
print(c)

for i in range(len(d)-1, -1, -1):
    for j in range(len(d[i])-1, -1, -1):
        if type(d[i][j]).__name__ in ('NoneType', 'complex'):
            del d[i][j]
print(d)

# не содержала вложености: внутренние списки должни бить расскрити;
bx = []
for i in range(0, len(b)):
    for j in range(0, len(b[i])):
        bx.append(b[i][j])
print(bx)

cx = []
for i in range(0, len(c)):
    for j in range(0, len(c[i])):
        cx.append(c[i][j])
print(cx)

dx = []
for i in range(0, len(d)):
    for j in range(0, len(d[i])):
        dx.append(d[i][j])
print(dx)

# каждая из копий имела єлементи списка только определенного типа данних - [int], [float], [str].
for i in range(len(bx)-1, -1, -1):
    if type(bx[i]).__name__ != 'int':
        del bx[i]
print(bx)

for i in range(len(cx)-1, -1, -1):
    if type(cx[i]).__name__ != 'float':
        del cx[i]
print(cx)

for i in range(len(dx)-1, -1, -1):
    if type(dx[i]).__name__ != 'str':
        del dx[i]
print(dx)

# 1.4 Решение Задачи 2 должно бить полностью автоматизировано - не иметь hardcode.
# Єто позволит при каких-либо модификациях исходного списка, не меняю кода программи каждий раз получать привильное решение.
#
# 1.5 Задача 2 содержит такие єлементи Python програмирования:
#
# цикли (возможно вложеность циклов)
# проверка типа данних;
# определение длини списка;
# условний оператор, чтоби исключить "мусор";
# копирование списка;
# "спред" оператор;
# приведение типа данних к нужному;
# вивод результата в виде принта.


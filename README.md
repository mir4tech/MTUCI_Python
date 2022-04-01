# MTUCI_Python

# Задания

### Задание 1: <a class="anchor" id="task1"></a>
Все пункты нужно ввыполнить с использованием ТОЛЬКО срезов
* Получите подстроку 'string' из строки test_string
* Получите подстроку 'Just' из строки test_string
* Получите подстроку 'simple' из строки test_string
* Получите каждый 5 символ из строки test_string
* Получите каждый 3 символ из строки test_string, начиная с конца.

test_string = 'Just a simple string'

### Задание 2: <a class="anchor" id="task3"></a>

Написать функцию, которая будет приниметь одно значение с логическими типы, а затем ковертировать их в строковые 'True' и 'False' и возвращать эти значения.

### Задание 3: <a class="anchor" id="task3"></a>

Написать функцию, которая будет приниметь одно значение - список. Вычислить разницу между максимальным и минимальным значением и вернуть его.

### Задание 4: <a class="anchor" id="task4"></a>

Написать функцию, которая будет принимать одно значение - число. Функция должна возвращать список всех четных чисел в диапозоне от 1 до полученного числа. В этом задании нужно использовать list comprehension.

### Задание 5: <a class="anchor" id="task2"></a>

Напишите функцию, который имеет два аргумента - x и y. Функция должна выводить координатный угол, в котором находятся координаты (x, y). 
Точки внутри координатного угла I имеют положительные абсциссы и ординаты.
Точки внутри координатного угла II имеют отрицательные абсциссы и положительные ординаты.
Точки внутри координатного угла III имеют отрицательные абсциссы и ординаты
Точки внутри координатного угла IV имеют положительные абсциссы и отрицательные ординаты.

### Задание 6: <a class="anchor" id="task2"></a>

Напишите функцию, которая принимает одно значение - число . Функция должна возвращать строку - полученное число в двоичном виде

### Задание 7:<a class="anchor" id="task5"></a>

Написать функцию, которая будет принимать одно значение - список. Список содержит числа. Все числа, кроме двух, повторяются как минимум два раза. Вернуть список из этих двух неповторяющихся чисел

### Задание 8: <a class="anchor" id="task2"></a>

Напишите функцию, которая принимает два значения - числа **num**, **length** (основное число, количество умножений). Функция должна возвращать список перемножений числа **num** **length** раз. Пример: test_function(7, 5) ➞ [7, 14, 21, 28, 35]

### Задание 9: <a class="anchor" id="task6"></a>

Написать функцию, которая будет принимать одно значение - строку. Функция должна возвращать представление полученной строки закодированной азбукой Морзе. Входная строка может содержать буквы как нижнего, так и верхнего регистра. Междк всеми словами присутствует пробел

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

### Задание 10: <a class="anchor" id="task6"></a>

Написать функцию, которая будет принимать одно значение - список. Функция должна возвращать самое частое значение в списке (встречается > N/2). Пример: test_function(["A", "A", "A", "B", "C", "A"]) ➞ "A"

### Задание 11: 
Создайте функцию для выполнения основных арифметических операций, которая применяет сложение, вычитание, умножение и деление к строковому значению (например, "12 + 24" или "23-21" или "12 // 12" или "12 * 21").

Здесь у нас есть 1 число, за которым следует пробел, затем оператор, за которым следует другой пробел, и 2 число. Возвращаемое значение должно быть числом.

Применение функции eval() не допускается. В случае деления, всякий раз, когда второе число равно "0", возвращайте -1.

### Задание 12: 
Напишите функцию, которая принимает список списков и возвращает значение всех символов в нем, где каждый символ добавляет или отнимает что-то от общего балла. Значения символов:

* \# = 5
* О = 3
* Х = 1
* ! = -1
* !! = -3
* !!! = -5

Если итоговый результат отрицательный, верните 0 (например, 3 ``#``, 3 ``!!``, 2 ``!!!`` и ``X`` будет (5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) = -3, так что верните 0.

### Задание 13: <a class="anchor" id="task7"></a>

Написать функцию, которая будет принимать одно значение - строку. Функция определяет свободные и занятые участки пляжа. Строка состоит из двух символов 0 - свободный участок, 1 - занятый участок. Из-за недавних ограничений новый человек не может занять место рядом с другим. Должно быть одно свободное место между двумя людьми, отдыхающими на пляже. Функци должна вернуть число - количество новых людей, которые могут воспользоваться местами на пляже.

### Задание 14: <a class="anchor" id="task7"></a>

Написать функцию, которая будет принимать одно значение - строку или список. Необходимо зашифровать строку. Первый элемент строки - код буквы в ascii (например 'a' = 97, a 'A' = 65). Следующий элемент - закодированная с помощью таблицы разница между текущим и предыдущим символом, итд. Если подается список - необходимо расшифровать его. Алгоритм такой же - первое число перекодируется в соответствием с таблицей ascii, второй символ - сумма первого и второго числа перекодированная с помощью таблицы ascii.

test_function("Hello") ➞ [72, 29, 7, 0, 3]

test_function([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

### Задание 15:
Создайте функцию, которая определяет, может ли c каждого места в концертном заде видеть сцену. С места можно увидеть сцену, если значение этого места (указано во входном списке) строго больше, чем значение перед ним.

Каждый может увидеть сцену в примере ниже:

``[[1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 2, 2],
 [5, 5, 5, 5, 4, 4],
 [6, 6, 7, 6, 5, 5]]``

Не все видят сцену:

``[[1, 2, 3, 2, 1, 1], 
  [2, 4, 4, 3, 2, 2], 
  [5, 5, 5, 10, 4, 4], 
  [6, 6, 7, 6, 5, 5]]``

Функция должна возвращать True, если абсолютно все видят сцену, ичане False

### Задание 16:
Создать функции, которая будет строить лестницу, используя знаки ‘_’ и ‘#’. Положительное значение обозначают, что направление лестницы направленно вверх и вниз для отрицательных значений.
Пример

``staircase(3) ➞ "__#\n_##\n###"
__#
_##
###``

``staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
______#
_____##
____###
___####
__#####
_######
#######``

``staircase(2) ➞ "_#\n##"
_#
##``

``staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
########
_#######
__######
___#####
____####
_____###
______##
_______#``

Замечания:
Возвращаемая строка дополняется символом перехода на новую строку \n

### Задание 17:

Имеется строк из символов в нижнем регистре ascii[["a".."z"]]. Нужно сократить строку следующим образом: берется пара соседних символов и если они одинаковы, то они удаляются. Например aab должно превратится в b.
Нужно удалить как можно больше символов. Если результирующая строка пустая, нужно вернуть "Empty String"

Пример:

``super_reduced_string("aaabccddd") ➞ "abd"``

### Задание 18:

Создать функцию, которая вернет ближайшую к текущей странице главу. Если две главы одинаково близко, то выбирается та, которая находится на большей по порядку странице.
Пример

``nearest_chapter({
  "Chapter 1" : 1,
  "Chapter 2" : 15,
  "Chapter 3" : 37
}, 10) ➞ "Chapter 2"``


``nearest_chapter({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200) ➞ "The End?"``


``nearest_chapter({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3) ➞ "Chapter 1b"``

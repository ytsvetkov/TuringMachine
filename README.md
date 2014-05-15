TuringMachine
=============

Tова е(или ще се опита да стане) имплементация на класическата машина на Тюринг. Всеки потребител ще има възможност да пише програми за нея, да ги изпълнява и да види визуално как работи машината, на която се базира модерния компютър.


##Основна функционалност
В основата си, ще може да изпълнява следния набор от инструкции:
>1. read
2. write
3. NOP(no operation)
4. move/shift left
5. move/shift right
6. change state



Като допълнение ще бъде реализиранa и възможността за ползване на:
>1. стек
2. регистри


Недетерминизма също ще бъде реализиран като ще има възможност да бъде изключен т.е. използването на инструкция която води до недерминистично поведение ще предизвиква грешка, караща програмата да спре и да изведе подходящо съобщение за настъпилата грешка.


##Интерфейс
Ще има два интерфейса:
>1. конзолен - основен и минималистичен(surprise, surprise), който разбирасе ще поддържа вече изброената функционалност
2. графичен - изпълнен от пъстри нюанси и цветове, с лесен за ползване от ежедневния потребител интерфейс т.е. бутончета и козола за писане на инструкции.

Към графичния интерфейс ще бъде свързана и най-съществената част от проекта - визуализажията на машината. Като цяло ще се визуализира лента, разбита на клетки и глава под формата на стрелка, която ще сочи къде се намира в даден момент главата на машината. Тъй като все още липвса имплементация, в груб вид, идеята може да се илюстрира от полимеризацията на:
[идея1](http://www.rutherfordjournal.org/images/TAHC_Turing_machine.jpg)
[идея2](http://community.middlebury.edu/~molinick/103%20Lectures/Lecture_30_Folder/Image10.gif)
[идея3](http://astarmathsandphysics.com/university-maths-notes/logic/university-maths-notes-logic-turing-machines-html-m4d0ef97a.gif)

Естетиката на MaicrosoftPaint ще бъде минимизарана максимално, в идеалния случай няма да присъства.
Преместването на главата ще представлява плавна анимация в която стрелаката (т.е. сочещия инструмен a.k.a. главата) ще се "плъзва" наляво или надясно, в зависимост от изпълняваната инструкция.


##Помощ за потребителя
Тъй като ползването на програмата се свежда до писане на програми, желателно е да има парсър който да преглежда написания код и при наличието на синтактични грешки, любезно да подканва поправянео им като за целта ще предоставя информация за това на кой ред и къде в интсрукция е възникнал проблем. Отрстаняването на семантични грешки е теоретично невъзможно но програмиста ще даде всичко от себе си за предостави антична форма на засичане на грешки преди изпълнение и дебъгване.

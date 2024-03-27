Efekt trójwymiarowości:

Przyjęłam wektor padania światła o parametrach [0.5, 1.5, 3]. 

Następnie dla każdego punktu wyznaczyłam różnicę między jego wysokością a wysokością punktu bezpośrednio nad nim oraz punktu po lewej stronie. Pozwoliło to na wyznaczenie wektorów vectortoup oraz vectortoleft, których iloczyn wektorowy jest wektorem prostopadłym do zbocza.

vector to left = [dist ance_to_next_point 0, difference to left*100000]

vector to up = [0, dist ance_to_next difference to up*100000]

Pomnożenie różnicy wysokości przez większą liczbę pozwala uzyskać efekt głębszych cieni. 

Iloczyn skalarny wektora padania światła oraz wektora normalnego po ich wcześniejszym znormalizowaniu jest cosinusem kąta pomiędzy wektorami, który przekazuję jako parametr value do funkcji wyznaczającej gradient HSV.

![image](https://github.com/anroszkiewicz/map-coloring/assets/111358119/9729e405-1a46-4a12-ae9d-65405caf9a05)


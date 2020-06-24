import matplotlib.pyplot as plt
import numpy as np
import math

#Исходные данные
data = [0, 0.5, 1, 1.5, 2, 2.5,
        3, 3.5, 4, 4.5, 5, 5.5,
        6, 6.5, 7, 7.5, 8, 8.5,
        9, 9.5, 10, 10.5, 11,
        11.5, 12, 12.5, 13,
        13.5, 14, 14.5, 15]
temp1 = [-6.48773984052241, -5.50310960547532, -4.19047508431161,
         17.480265650133, 38.156783622165, 37.1697020341714,
         40.0051495866111, 41.3885159919645, 64.5386848731954,
         81.3788118954882, 122.554168607724, 203.622134166765,
         264.516840109667, 377.207341853305, 530.27411941004,
         723.738467853529, 1047.60068001725, 1456.37114954243,
         2014.2907567928, 2805.83889544656, 3941.38897855703,
         5480.51641232266, 7657.94478592193, 10695.4883721303,
         14897.7373687716, 20786.8613399812, 29047.8310624743,
         40505.7636146707, 56528.4572682974, 78906.6426107198,
         110146.063624971]
appX    = np.arange(0, 15, 0.5)         	

#Функция для поиска коэффициентов по методу наименьших квадратов для экпоненты
def mnk(x, y):
	sumX = np.sum(x)
	sumY = np.sum(y)
	LnY = list(map(lambda i: np.log(np.abs(i)), y))
	sumLnY = sum(LnY)
	sumX2 = sum(list(map(lambda i: i**2, x)))
	sumXY = sum(list(map(lambda i,j: i*j, x,LnY)))	
	A = (len(x) * sumXY - sumX * sumLnY )/(len(x) * sumX2 - sumX ** 2)
	B = (sumLnY - A * sumX ) / len(x)
	B = np.exp(B)
	print("Необходимая функция - ", B, "e^(", A, "x)")
	return [A, B]

#Функция для поиска значений y в зависимости от x и параметров a,b(literally "y=be^{ax}")
def getY(x, params):
	return (params[1])*np.exp(x*params[0])

#Находим a, b
coefs = mnk(data, temp1)

#Заполняем массив значениями 
temp2 = []
for i in appX:
	temp2.append(getY(i, coefs))

#Рисуем графики
plt.plot(appX, temp2, ".-",label = 'Аппроксимация')
plt.plot(data, temp1, "--", label = 'Исходные данные')
plt.xlabel('X', fontsize=15, color='blue')
plt.ylabel('Y', fontsize=15, color='blue')
plt.legend()
plt.show()
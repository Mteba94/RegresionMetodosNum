
from statistics import linear_regression
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

#Leer datos de excel
datos = pd.read_excel("Prueba.xlsx")
#datos = pd.read_excel("Superior.xlsx")
datos.head()
#print(datos)
#print(datos.keys())
#print(datos.feature_names)

#asignar valores a los ejes
#X = datos['MES/AÑO']
X = datos.iloc[:,0].values
#y = datos[2021]
#y = datos['ANIO']
y = datos.iloc[:,1].values

#convertir el array
X = X.reshape(-1,1)

#calcular valores de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = linear_model.LinearRegression()

lr.fit(X_train, y_train)

Y_pred = lr.predict(X_test)


#mostrar los datos por grafica
plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.xlabel('Mes')
plt.ylabel('Precio')
plt.title("Regresion Lineal")
plt.show()

print('Ecuacion del modelo:')
print('y = ',lr.coef_, ' x = ', lr.intercept_)

print('Precision del modelo:')
print(lr.score(X_train, y_train))
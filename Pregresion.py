import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

datos = pd.read_excel("Prueba.xlsx")
#print(datos.head)

r_l = smf.ols(formula="MES~ANIO", data=datos).fit()

#print(r_l.summary())

predic = r_l.predict(pd.DataFrame(datos["ANIO"]))

datos.plot(kind="scatter", x = "ANIO", y = "MES")
plt.plot(pd.DataFrame(datos["ANIO"]), predic, c="red", linewidth=2)
plt.show()

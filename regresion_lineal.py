
import numpy as np  
import pandas as pd  
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
from sklearn.metrics import mean_squared_error, r2_score  
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")

data = {
    "altura": [150, 160, 170, 180, 190, 155, 165, 175, 185, 195],
    "genero": [0, 0, 0, 1, 1, 0, 0, 1, 1, 1], # 0 = mujer, 1 = hombre
    "peso": [50, 55, 60, 70, 80, 52, 58, 75, 85, 90]
}

df = pd.DataFrame(data)


X = df[["altura", "genero"]] 
y = df["peso"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test
                       
#evaluar
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Coeficientes:", modelo.coef_)
print("Intercepto:", modelo.intercept_)
print("Error cuadrático medio (MSE):", mse)
print("Coeficiente de determinación (R^2):", r2)

def genero_a_texto(genero):
    return "M" if genero == 1 else "F"

def nueva_persona(altura, genero):
    persona = np.array([[altura, genero]])
    peso_predicho = modelo.predict(persona)
    return print(f"altura: {altura} Genero: {genero_a_texto(genero)} peso estimado: {peso_predicho[0]:.2f} kg") 

nueva_persona(165, 1)
nueva_persona(170, 0)
nueva_persona(180, 1)
nueva_persona(175, 0)
nueva_persona(190, 1)
nueva_persona(155, 0)
nueva_persona(150, 1)
nueva_persona(195, 0)
nueva_persona(185, 1)
nueva_persona(160, 0)

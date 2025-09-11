import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Carregar dataset Iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Mostrar primeiras linhas
print("Exemplo de dados:")
print(X.head())

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliar modelo
accuracy = model.score(X_test, y_test)
print(f"Acurácia do modelo: {accuracy:.2f}")

# Importância das features
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.sort_values().plot(kind='barh')
plt.title("Importância das variáveis")
plt.tight_layout()
plt.show()
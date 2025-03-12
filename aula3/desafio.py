import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

# Carregando o dataset Wine
data = load_wine()

# Criando um DataFrame com os dados
df = pd.DataFrame(data.data, columns=data.feature_names)

# Adicionando a coluna de rótulos (target)
df['target'] = data.target

# Separando as features (X) e o target (y)
X = df.drop('target', axis=1)  # Removendo a coluna 'target' do DataFrame
y = df['target']  # Apenas a coluna 'target'

# Dividindo os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalizando as features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Implementando o classificador KNN
k = 5  # Exemplo de valor para k
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Calculando as métricas
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Exibindo os resultados
print("Acurácia:", accuracy)
print("Matriz de Confusão:\n", conf_matrix)
print("Precisão:", precision)
print("Recall:", recall)
print("F1-Score:", f1)

# 🌱 FarmTech Solutions – Fase 4: Assistente Agrícola Inteligente

##  Sobre o Projeto

O FarmTech Solutions é um projeto desenvolvido com o objetivo de aplicar conceitos de Inteligência Artificial, Ciência de Dados, Banco de Dados e Agricultura Cognitiva para auxiliar a tomada de decisão no agronegócio.

Nesta fase foi desenvolvido um Assistente Agrícola Inteligente capaz de armazenar dados agrícolas, treinar modelos preditivos e gerar previsões de produtividade com recomendações automáticas de manejo agrícola.

A solução integra sensores simulados, banco de dados relacional, Machine Learning e dashboard analítico interativo, permitindo transformar dados em informações úteis para gestores agrícolas.

---

#  Objetivos

O projeto foi desenvolvido com os seguintes objetivos:

- Simular a coleta de dados agrícolas por sensores IoT.
- Armazenar dados em banco de dados relacional SQLite.
- Aplicar técnicas de Machine Learning supervisionado.
- Prever produtividade agrícola utilizando regressão.
- Gerar recomendações automáticas de manejo.
- Disponibilizar análises através de dashboard interativo.
- Demonstrar a aplicação prática da Inteligência Artificial no agronegócio.

---

#  Conceito de Agricultura Cognitiva

A Agricultura Cognitiva combina sensores, dados, algoritmos e sistemas inteligentes para auxiliar produtores rurais na tomada de decisões.

Neste projeto, os dados agrícolas são utilizados para alimentar modelos de Inteligência Artificial capazes de identificar padrões e gerar previsões relacionadas à produtividade agrícola.

Essa abordagem permite reduzir desperdícios, otimizar recursos e aumentar a eficiência da produção.

---

#  Arquitetura da Solução

```text
Sensores IoT Simulados
          ↓
   Geração dos Dados
          ↓
 CSV + Banco SQLite
          ↓
 Pré-processamento
          ↓
 Machine Learning
          ↓
 Treinamento
          ↓
 Avaliação
          ↓
 Modelo .PKL
          ↓
 Dashboard Streamlit
          ↓
 Previsões e Recomendações
````

---

#  Tecnologias Utilizadas

## Linguagem

* Python

## Banco de Dados

* SQLite

## Ciência de Dados

* Pandas
* NumPy

## Machine Learning

* Scikit-Learn
* Joblib

## Visualização

* Streamlit
* Matplotlib
* Seaborn

---

#  Estrutura do Projeto

```text
assistente-agricola-inteligente/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── dados_agricolas.csv
│   └── dados_agricolas.db
│
├── models/
│   ├── modelo_produtividade.pkl
│   └── metricas.json
│
└── src/
    ├── data_generator.py
    ├── database.py
    ├── treinar_modelo.py
    ├── menu.py
    └── main.py
```

---

#  Banco de Dados

O projeto utiliza SQLite para armazenar os dados agrícolas gerados pelos sensores simulados.

Tabela principal:

```sql
CREATE TABLE sensores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    umidade REAL,
    pH REAL,
    temperatura REAL,
    irrigacao REAL,
    fertilizante REAL,
    produtividade REAL,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

O banco de dados permite:

* Persistência dos dados.
* Consulta histórica.
* Integração com Machine Learning.
* Simulação de ambiente IoT.

---

#  Base de Dados

Foi utilizada uma base agrícola simulada contendo aproximadamente 1000 registros.

Variáveis utilizadas:

| Variável      | Descrição                            |
| ------------- | ------------------------------------ |
| Umidade       | Umidade do solo (%)                  |
| pH            | Acidez do solo                       |
| Temperatura   | Temperatura ambiente (°C)            |
| Irrigação     | Volume de irrigação aplicado         |
| Fertilizante  | Quantidade de fertilizante utilizada |
| Produtividade | Rendimento estimado da cultura       |

---

#  Machine Learning

Foi implementado um modelo de Regressão Linear utilizando a biblioteca Scikit-Learn.

## Variáveis de Entrada

* Umidade
* pH
* Temperatura
* Irrigação
* Fertilizante

## Variável Alvo

* Produtividade

## Divisão dos Dados

* 80% Treinamento
* 20% Teste

O modelo treinado é salvo automaticamente para reutilização no dashboard.

```python
joblib.dump(modelo, MODELO_PATH)
```

---

#  Pipeline de Machine Learning

```text
Coleta dos Dados
        ↓
Armazenamento CSV e SQLite
        ↓
Tratamento dos Dados
        ↓
Treino/Teste
        ↓
Treinamento
        ↓
Avaliação
        ↓
Modelo Treinado
        ↓
Dashboard
```

---

#  Métricas de Avaliação

O desempenho do modelo é avaliado utilizando métricas clássicas de regressão.

## MAE

Mean Absolute Error (Erro Médio Absoluto).

Representa a média dos erros absolutos entre valores previstos e reais.

## MSE

Mean Squared Error (Erro Médio Quadrático).

Penaliza erros maiores ao elevar a diferença ao quadrado.

## RMSE

Root Mean Squared Error.

Versão interpretável do MSE na mesma escala da variável alvo.

## R²

Coeficiente de Determinação.

Indica a capacidade do modelo de explicar a variabilidade dos dados.

---

#  Dashboard Interativo

O dashboard foi desenvolvido utilizando Streamlit.

Funcionalidades disponíveis:

* Visualização dos dados.
* Indicadores agrícolas.
* Estatísticas descritivas.
* Heatmap de correlação.
* Tendência de produtividade.
* Simulador de produtividade.
* Recomendações automáticas.
* Previsões em tempo real.

---

#  Recomendações Inteligentes

Com base nos valores informados pelo usuário, o sistema pode recomendar:

###  Irrigação

Aumento da irrigação quando a umidade estiver abaixo do ideal.

###  Correção de Solo

Correção do pH quando identificado desequilíbrio.

### Fertilização

Sugestões de aumento da fertilização.

###  Temperatura

Monitoramento de possíveis condições de estresse térmico.

###  Condições Favoráveis

Identificação de cenários adequados para cultivo.

---

#  Como Executar

## Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## Executar Menu

```bash
python src/menu.py
```

---

## Executar Dashboard

```bash
streamlit run app.py
```

---

#  Fluxo de Execução

1. Criar banco de dados.
2. Gerar dados agrícolas.
3. Armazenar CSV e SQLite.
4. Treinar modelo de IA.
5. Avaliar métricas.
6. Salvar modelo treinado.
7. Abrir dashboard.
8. Realizar previsões.

---
#  Funcionalidades Implementadas

## Gestão de Dados

* Geração automática de dados.
* Armazenamento em CSV.
* Armazenamento em SQLite.

## Inteligência Artificial

* Regressão Linear.
* Treinamento supervisionado.
* Persistência do modelo.
* Avaliação por métricas.

## Dashboard

* Indicadores.
* Heatmap.
* Scatter Plot.
* Tendência de produtividade.
* Simulações.
* Recomendações.

---

#  Resultados Obtidos

O projeto demonstrou a viabilidade da utilização de Inteligência Artificial para análise de dados agrícolas.

A integração entre banco de dados, Machine Learning e visualização permitiu transformar dados em informações estratégicas para apoio à tomada de decisão.

---

#  Conclusão

O Assistente Agrícola Inteligente permitiu aplicar conceitos de Ciência de Dados, Inteligência Artificial e Agricultura Cognitiva em um cenário prático.

A solução demonstra como dados agrícolas podem ser utilizados para gerar previsões, identificar padrões e fornecer recomendações que contribuem para uma produção mais eficiente, sustentável e orientada por dados.

Além disso, o projeto reforça a importância da integração entre coleta de dados, armazenamento estruturado, aprendizado de máquina e visualização analítica para o futuro do agronegócio.

---

#  Integrantes

* Gabriele Brito Rocha Menezes
* Gilenisson Santos

# FarmTech Solutions – Fase 4: Assistente Agrícola Inteligente

## Introdução

A Fase 4 do projeto FarmTech Solutions tem como objetivo aplicar conceitos de Inteligência Artificial e Ciência de Dados ao contexto agrícola, transformando dados em informações úteis para apoiar a tomada de decisão no campo.

Nesta etapa, foi desenvolvido um protótipo de Assistente Agrícola Inteligente capaz de analisar dados agrícolas, prever a produtividade de uma cultura e fornecer recomendações de manejo agrícola por meio de técnicas de Machine Learning e visualização interativa de dados.

A solução integra banco de dados, aprendizado supervisionado e dashboard analítico, representando um exemplo prático de Agricultura Cognitiva, na qual sensores, dados e algoritmos trabalham juntos para otimizar a produção agrícola.

---

## Objetivos do Projeto

O projeto foi desenvolvido com os seguintes objetivos:

* Armazenar dados agrícolas simulados em uma base estruturada.
* Aplicar técnicas de Machine Learning supervisionado utilizando regressão.
* Prever a produtividade agrícola com base em fatores ambientais e operacionais.
* Gerar recomendações automáticas de irrigação e manejo do solo.
* Disponibilizar análises e previsões em um dashboard interativo desenvolvido com Streamlit.
* Demonstrar a aplicação prática da Inteligência Artificial no agronegócio.

---

## 🛠 Tecnologias Utilizadas

* Python
* Pandas
* Scikit-Learn
* Streamlit
* Matplotlib
* Seaborn
* Joblib

---

## Estrutura do Projeto

```text
assistente-agricola-inteligente/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── dados_agricolas.csv
│
├── models/
│   └── modelo_produtividade.pkl
│
└── src/
    ├── data_generator.py
    ├── treinar_modelo.py
    ├── main.py
    └── menu.py
```

---

## Base de Dados

Foi utilizada uma base de dados agrícolas simulada contendo aproximadamente 1000 registros.

As variáveis utilizadas foram:

| Variável      | Descrição                            |
| ------------- | ------------------------------------ |
| Umidade       | Umidade do solo (%)                  |
| pH            | Nível de acidez do solo              |
| Temperatura   | Temperatura ambiente (°C)            |
| Irrigação     | Volume de irrigação aplicado         |
| Fertilizante  | Quantidade de fertilizante utilizada |
| Produtividade | Rendimento estimado da cultura       |

Esses dados representam condições agrícolas utilizadas para treinamento e validação do modelo preditivo.

---

## Modelo de Machine Learning

Foi implementado um modelo de Regressão Linear utilizando a biblioteca Scikit-Learn.

### Variáveis de Entrada

* Umidade
* pH
* Temperatura
* Irrigação
* Fertilizante

### Variável Alvo

* Produtividade

O conjunto de dados foi dividido em:

* 80% para treinamento
* 20% para teste

Após o treinamento, o modelo foi salvo em formato `.pkl` para utilização no dashboard.

---

## Avaliação do Modelo

O desempenho do modelo foi avaliado utilizando métricas amplamente empregadas em problemas de regressão:

* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE (Root Mean Squared Error)
* R² (Coeficiente de Determinação)

Essas métricas permitem analisar a precisão das previsões realizadas pelo modelo e verificar sua capacidade de generalização.

---

## Dashboard Interativo

O dashboard foi desenvolvido utilizando Streamlit e oferece uma interface amigável para gestores agrícolas.

### Funcionalidades

* Visualização dos dados agrícolas.
* Exibição de métricas gerais da base.
* Mapa de correlação entre variáveis.
* Gráfico de distribuição da produtividade.
* Previsão interativa de produtividade.
* Recomendações automáticas de manejo agrícola.

O sistema permite que o usuário informe valores relacionados às condições do campo e receba previsões em tempo real.

---

## Recomendações Inteligentes

Com base nos valores informados pelo usuário, o sistema fornece sugestões de manejo agrícola, incluindo:

* Recomendação de irrigação quando a umidade está abaixo do ideal.
* Sugestão de correção do solo quando o pH está inadequado.
* Orientações relacionadas à fertilização.
* Indicação de condições favoráveis para cultivo quando os parâmetros estão equilibrados.

Essas recomendações auxiliam o produtor rural na tomada de decisões mais eficientes e sustentáveis.

---

## Como Executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar o dashboard

```bash
streamlit run app.py
```

---

## Resultados Obtidos

O projeto demonstrou que técnicas de Machine Learning podem ser aplicadas com sucesso para prever indicadores agrícolas e apoiar a tomada de decisão no campo.

A integração entre análise de dados, regressão e dashboard interativo permitiu transformar dados agrícolas em informações úteis para planejamento e gestão da produção.

---

## Conclusão

O desenvolvimento do Assistente Agrícola Inteligente permitiu aplicar conceitos de Inteligência Artificial, Ciência de Dados e Agricultura Cognitiva em um cenário prático.

A solução mostrou como dados agrícolas podem ser utilizados para gerar previsões e recomendações que contribuem para uma produção mais eficiente, sustentável e orientada por dados.

Além disso, o projeto reforçou a importância da integração entre coleta de dados, modelos preditivos e visualização de informações para apoiar gestores agrícolas na tomada de decisões.

---

## 👥 Integrantes

* Gabriele Brito
* Gilenisson Santos

# Análise de Avaliações de Produtos da Sephora com NLP e Visualizações

Este projeto tem como objetivo analisar milhares de avaliações de produtos de beleza da Sephora, respondendo a perguntas-chave sobre popularidade, percepção do cliente, tópicos mais discutidos e sentimentos atribuídos pelos usuários. Utilizando técnicas de NLP e análise exploratória, buscamos insights que podem ajudar a empresa em estratégias de marketing e desenvolvimento de produto.

---

## Perguntas de Negócio

- Quais são os produtos com mais avaliações?
- Quais produtos e marcas são os mais bem avaliados?
- Qual é o sentimento geral das avaliações por tipo de produto?
- Quais são os principais tópicos mencionados nas avaliações?
- Quais tópicos apresentam mais sentimentos positivos ou negativos?

---

## Dados

O projeto utiliza dois datasets:

- `df_info`: Informações dos produtos (nome, marca, nota, número de avaliações, etc.)
- `dfs_reviews`: Lista com diversos DataFrames contendo as avaliações textuais e metadados (nota, recomendação, data, etc.)

### Pré-processamento
- Remoção de colunas irrelevantes (`Unnamed: 0`)
- Eliminação de valores nulos nas colunas críticas (rating, reviews, review_text, etc.)
- Tokenização, limpeza e normalização dos textos

---

## Análise Exploratória (EDA)

### Produtos mais populares e melhor avaliados

![Top 20 produtos mais avaliados](INSERIR_CAMINHO_IMAGEM1)
![Top 20 produtos com melhores notas](INSERIR_CAMINHO_IMAGEM2)

💡 Os produtos mais populares não são os mais bem avaliados, sugerindo que nichos específicos têm maior aceitação, enquanto produtos populares sofrem com a média diluída.

---

### Marcas mais populares vs. melhor avaliadas

![Top 20 marcas mais avaliadas](INSERIR_CAMINHO_IMAGEM3)
![Top 20 marcas com melhores notas](INSERIR_CAMINHO_IMAGEM4)

💡 O padrão se repete com as marcas — as mais avaliadas não são as mais bem avaliadas. Marcas de nicho com público fiel se destacam positivamente.

---

### Distribuição de Notas

![Histograma de notas](INSERIR_CAMINHO_IMAGEM5)

💡 A distribuição é enviesada à direita. A maioria das avaliações possui notas altas, evidenciando alta satisfação geral dos clientes.

---

### Nuvem de Palavras

![Wordcloud das avaliações](INSERIR_CAMINHO_IMAGEM6)

💡 Termos relacionados a “skin”, “cream”, “hydrating”, “love”, “good” predominam. Reforça o sucesso da linha de skincare e o sentimento positivo.

---

### Análise Temporal

![Evolução temporal das avaliações](INSERIR_CAMINHO_IMAGEM7)

💡 Há uma queda abrupta nas notas em 2020 e posterior recuperação. Pode refletir questões externas (como pandemia) ou mudanças de produto/marketing.

---

## Processamento de Linguagem Natural (NLP)

### Sentimento

![Sentimento dos top 20 produtos](INSERIR_CAMINHO_IMAGEM8)

💡 Entre os 20 produtos mais avaliados, mais de 60% das avaliações são negativas — com exceção de apenas dois produtos.

---

### Tópicos com BERTopic

- Foram extraídos **50 tópicos únicos** com a técnica BERTopic para reduzir redundância.

#### Tópicos mais comentados

![Tópicos mais comentados](INSERIR_CAMINHO_IMAGEM9)

💡 Predominam tópicos relacionados a skincare — hidratantes, protetores, séruns, etc.

#### Tópicos mais positivos

![Tópicos mais positivos](INSERIR_CAMINHO_IMAGEM10)

💡 Os mesmos tópicos populares também são os mais bem avaliados.

#### Tópicos mais negativos

![Tópicos mais negativos](INSERIR_CAMINHO_IMAGEM11)

💡 Reclamações giram em torno de:
- Marca “NuFace”
- Tamanho das amostras
- Mudança de fórmula
- Reações alérgicas

---

## Insights e Ações Recomendadas

### Para o time de marketing:
- Potencializar campanhas com os produtos e tópicos mais bem avaliados — especialmente os de **skincare**
- Dar visibilidade a produtos de nicho bem avaliados

### Para o time de produtos/parceiros:
- Investigar o **Trinity + Eye and Lip Enhancer** e outros com baixa aceitação
- Considerar **revisar as amostras** distribuídas
- **Reportar às marcas** problemas sobre fórmulas ou reações alérgicas

---

## Conclusão

A Sephora apresenta uma excelente curadoria de produtos, com altíssimos índices de satisfação dos consumidores. O domínio dos produtos de skincare nas avaliações revela uma oportunidade de reforçar esse segmento. A análise de sentimentos e tópicos provou ser uma ferramenta eficaz para entender dores e desejos dos clientes em escala.

---

## Melhorias Futuras

- Implementar paralelização no cálculo de sentimento para reduzir tempo de execução
- Realizar análise por faixa etária (caso dados estejam disponíveis)
- Construir um dashboard interativo com Streamlit ou Power BI
- Classificação automática de reviews em categorias (skincare, perfume, maquiagem)

---

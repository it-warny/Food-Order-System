import pandas as pd
print("Pandas importado como o alias: pd")

print("\nLista dos 5 primeiros registos do DataFrame 'títulos_df':")
titulos_df = pd.read_csv("M5_05_imdb_titulos.csv")
print(titulos_df.head())

print("\nLista dos 5 primeiros registos do DataFrame 'elenco_df':")
elenco_df = pd.read_csv("M5_05_imdb_elenco.csv")
print(elenco_df)

print("\nTotal de registos do DataFrame 'titulo_df':")
print(titulos_df.shape)

print("\nTotal de registos do DataFrame 'elenco_df':")
print(elenco_df.shape)

print("\nLista dos 5 últimos registos do DataFrame 'titulos_df':")
print(titulos_df.sort_values(by='year').head(5))

print("\nLista dos títulos que contém 'Dracula' no título e sua quantidade:")
filmes_dracula = titulos_df[titulos_df["title"].str.contains("Dracula", case=False, na=False)]
print(filmes_dracula)
print(f"Quantidade de filmes: {filmes_dracula.shape[0]}!")

print("\nLista dos 10 títulos mais comuns:")
dez_titulos_mais_comuns = titulos_df["title"].value_counts().head(10)
print(dez_titulos_mais_comuns)

print("\nAno do primeiro filme de 'Romeu and Juliet':")
romeu_e_julieta = titulos_df[titulos_df["title"].str.contains("Romeo and Juliet", case=False, na=False)]
primeiro_romeu = romeu_e_julieta.sort_values("year").head(1).iloc[0]
print(f"Temos o registo do primeiro filme de '{primeiro_romeu["title"]}' no ano de {primeiro_romeu["year"]}")

print("\nLista de todos os filmes que contém 'Exorcist' no título em ordem crescente:")
filme_exorcist = titulos_df[titulos_df["title"].str.contains("exorcist", case=False, na=False)].sort_values(by="year")
print(filme_exorcist.to_string(index=False)) # Usei o .to_string(index=False) para mostrar somente as colunas sem o index

filmes_1950 = titulos_df[titulos_df["year"] == 1950]
print(f"\nTemos um total de {filmes_1950.shape[0]} filmes produzidos no ano de 1950!")

filmes_1950_a_1959 = titulos_df[(titulos_df["year"] >= 1950) & (titulos_df["year"] <= 1959)]
print(f"\nTemos um total de {filmes_1950_a_1959.shape[0]} filmes produzidos entre os anos 1950 e 1959.")

print(f"\nLista de papeis da trilogia 'The Godfather' e a quantidade de vezes que apareceram:")
godfather_filmes = elenco_df[elenco_df["title"].str.contains("the godfather", case=False, na=False)]
contagem_por_ator = godfather_filmes.groupby("character").size().reset_index(name="quantidade")
print(contagem_por_ator)

print("\nRelação do elenco completo de todos os filmes do Drácula no ano 1958.")
dracula_1958 = elenco_df[(elenco_df["title"] == "Dracula") & (elenco_df["year"] == 1958)].sort_values(by="n")
print(dracula_1958)

bruce_wayne = elenco_df[elenco_df["character"].str.contains("bruce wayne", case=False, na=False)]
print(f"\nBruce Wayne teve {bruce_wayne.shape[0]} papéis.")

robert_de_niro = elenco_df[elenco_df["name"].str.contains("robert de niro", case=False, na=False)]
# robert_de_niro = elenco_df[elenco_df["name"] == "Robert De Niro"] # Seria uma segunda opção para solução desta questão
print(f"\nRobert de Niro teve {robert_de_niro.shape[0]} papéis em sua carreira.")

print("\nLista de papéis do Charlton Heston na década de 60, ordenado pelo ano.")
charlton_heston = elenco_df[(elenco_df["name"] == "Charlton Heston") & (elenco_df["n"] == 1) & (elenco_df["year"] >= 1960) & (elenco_df["year"] <= 1969)].sort_values(by="year", ascending=False)
print(charlton_heston)

atores_50s = elenco_df[(elenco_df["type"] == "actor") & (elenco_df["year"] >= 1950) & (elenco_df["year"] <= 1959)]
print(f"\nNúmero de papéis para atores na década de 50: {atores_50s.shape[0]}")

atrizes_50s = elenco_df[(elenco_df["type"] == "actress") & (elenco_df["year"] >= 1950) & (elenco_df["year"] <= 1959)]
print(f"\nNúmero de papéis para atrizes na década de 50: {atrizes_50s.shape[0]}")


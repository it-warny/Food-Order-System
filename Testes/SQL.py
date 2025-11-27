import sqlite3

conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()


##### Como criar tabelas no DB
cursor.execute("""
CREATE TABLE IF NOT EXISTS utilizadores (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
idade INTEGER NOT NULL,
genero TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome_produto TEXT NOT NULL,
preco REAL,
stock INTEGER
);
""")

### Dados para tabela produtos
nome_produto = "Computador Portátil"
preco = 1250.50
stock = 50

### Dados para tabela utilizadores
utilizadores = ["Warny", "Fernanda", "Gorette", "Junior"]
idades = [39, 27, 65, 21]
genero = ["Masculino", "Feminino", "Feminino", "Masculino"]
dados_para_inserir = zip(utilizadores, idades, genero) # Usei um zip() para criar os matches de utilizadores, idades e genero

####### C - criar (CREATE) R - ler (SELECT) U - atualizar (UPDATE) D - deletar (DELETE)

##### C (CREATE) - Basicamente criamos uma variável e atribuimos o comando "INSERT INTO name_table (dados_a inserir) VALUE (? para cada dado inserido);"

sql_query = "INSERT INTO produtos (nome_produto, preco, stock) VALUES (?, ?, ?);"
cursor.execute(sql_query, (nome_produto, preco, stock))

print(f"""Foi inserido no BD os seguintes dados:
Prdduto: {nome_produto}
Preço: {preco}
Stock: {stock}
""")

sql_query_2 = "INSERT INTO utilizadores (nome, idade, genero) VALUES (?, ?, ?);"
cursor.executemany(sql_query_2, dados_para_inserir) # Usei desta forma para testar inserir multiplos dados de uma só vez. Super pratico
conexao.commit() # Sempre após o C (CREATE) U (UPDATE) D (DELETE), deve-se fazer o conexao.commit() para salvar o que foi feito

##### R (SELECT) - Selecionamos basicamente o que queremos de onde queremos (cursor.execute("SELECT * FROM nome_tabela WHERE condição_do_filtro")

cursor.execute("SELECT * FROM utilizadores WHERE genero = 'Masculino'") ### Usamos o * para pegar a tabela inteira na "mão" do cursor
dados_selecionados = cursor.fetchall() ### Usamos o cursor.fetchall para pegar todos os itens da tabela e os atribuir a alguma variável
print("Somente os utilizadores masculinos:")
for line in dados_selecionados:
    print(f"ID: {line[0]} | Nome: {line[1]} | Idade: {line[2]} | Gênero: {line[3]}")

print()

cursor.execute("SELECT * FROM utilizadores") ### Eu realmente preciso "pegar" novamente com o cursor e depois dar o comando do cursor.fetch(o que eu quiser)
for line in cursor: ### Depois que usar o cursor para selecionar o que quer, o cursor se torna iterável, simplificando e muito o loop do for
    print(f"ID: {line[0]} | Nome: {line[1]} | Idade: {line[2]} | Gênero: {line[3]}")


##### U (UPDATE) - Usamos o comando cursor.execute("UPDATE nome_tabela SET o_que_vai_alterar WHERE onde_vai_alterar (tipo filtro)"
######### NUNCA esquecer do WHERE para não alterar tudo sem querer

sql_query_3 = "UPDATE produtos SET preco = ? WHERE id = ?;"
valor_pc_atualizado = 1350
id_pc = 1

### Forma usando as variáveis
cursor.execute(sql_query_3,(valor_pc_atualizado, id_pc))
conexao.commit()

### Forma atualizando dois ou mais valores e usando a forma direta sem variável
cursor.execute("UPDATE produtos SET preco = ?, stock = ? WHERE id = ?;",(2000, 75, 1))
conexao.commit()

##### D (DELETE) - Bem parecido com a sintaxe do UPDATE, aqui fazemos: cursor.execute("DELETE FROM nome_tabela WHERE condição;"
######### NUNCA esquecer do WHERE para não apagar tudo sem querer

### Usando o DELETE para apagar uma linha específica
cursor.execute("DELETE FROM produtos WHERE id = ?;",(1,))
conexao.commit()

conexao.close()


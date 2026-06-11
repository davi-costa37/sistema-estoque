📦 Gerenciador de Estoque Simples (Python & SQLite)
Este projeto é uma biblioteca/módulo em Python desenvolvido para gerenciar o estoque de produtos de forma local e simplificada. 
Ele utiliza o banco de dados SQLite, o que elimina a necessidade de configurações complexas de servidores externos, já que os dados são salvos diretamente em um arquivo local (estoque.db).

⚙️ Funcionalidades
O script fornece todas as operações essenciais para o controle de mercadorias (CRUD e controle de fluxo):

Criação Automática do Banco: Cria a tabela de produtos caso ela ainda não exista.

Cadastro de Produtos: Insere novos itens com nome, quantidade inicial e preço.

Consulta e Busca: * Listagem completa de todos os produtos cadastrados.

Busca inteligente por nome utilizando o operador LIKE (busca parcial).

Movimentação de Estoque: Funções específicas para dar entrada (somar) ou saída (subtrair) na quantidade de itens de forma segura.

Exclusão: Remove um produto do catálogo permanentemente através do seu ID único.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Banco de Dados: SQLite3 (Módulo nativo do Python, sem necessidade de instalações adicionais).

📄 Licença
Este projeto está sob a licença MIT.

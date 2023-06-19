FASTER CLI
Descrição
O projeto FASTER CLI tem como objetivo criar uma Interface de Linha de Comando (CLI) para facilitar o desenvolvimento de projetos em Python.

Comandos
cli start: Cria a estrutura básica de um projeto Python.
cli run <nome_script>: Executa um script Python especificado, que deve estar configurado no arquivo config.json.
cli activate: Ativa o ambiente virtual.
cli entity <nome_entidade>: Cria uma entidade com o nome especificado.
cli entity <nome_entidade> mod <nome_modulo>: Cria uma entidade com o nome especificado dentro do módulo especificado.
cli module <nome_modulo>: Cria um módulo com o nome especificado.
cli module <nome_modulo> sub <nome_submodulo>: Cria um submódulo com o nome especificado dentro do módulo especificado.
cli dto <nome_entidade>: Cria um DTO com o nome especificado.
cli dto <nome_entidade> mod <nome_modulo>: Cria um DTO com o nome especificado dentro do módulo especificado.
cli install <nome_biblioteca>: Instala uma biblioteca Python especificada e atualiza o arquivo requirements.txt.
cli help: Exibe a lista de comandos disponíveis.
Benefícios
Simplifica a configuração de um projeto Python ao gerar as pastas e arquivos necessários.
Fornece comandos convenientes para criar entidades, módulos, submódulos, DTOs e instalar bibliotecas.
Ajuda a otimizar o processo de desenvolvimento e promove a organização do código.
Solução
O FASTER CLI oferece uma solução simplificada para o desenvolvimento de projetos Python, automatizando tarefas repetitivas e fornecendo uma interface conveniente para operações comuns. O objetivo é melhorar a produtividade e a manutenção do código, ao padronizar as estruturas de projeto e automatizar tarefas rotineiras.

Utilizando o FASTER CLI em qualquer diretório do Windows
Para utilizar o FASTER CLI de qualquer diretório no Windows, você pode adicionar o diretório em que o arquivo faster.bat está localizado ao caminho do sistema (PATH). Siga as instruções abaixo:

Copie o arquivo faster.bat para um diretório de sua escolha (por exemplo, C:\faster).
Clique com o botão direito do mouse no ícone "Meu Computador" (ou "Este Computador") e selecione "Propriedades".
Na janela de propriedades do sistema, clique em "Configurações avançadas do sistema".
Na guia "Avançado", clique no botão "Variáveis de Ambiente".
Na seção "Variáveis do Sistema", selecione a variável "Path" e clique em "Editar".
Na janela "Editar Variável de Ambiente", clique em "Novo" e insira o caminho completo para o diretório onde o arquivo faster.bat está localizado (por exemplo, C:\faster).
Clique em "OK" em todas as janelas para salvar as alterações.
Agora você pode abrir uma nova janela do prompt de comando (ou reiniciar o prompt de comando existente) e usar o comando faster de qualquer diretório para executar o FASTER CLI.
Licença
Este projeto está licenciado sob a Licença MIT.
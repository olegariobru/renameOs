# RenameOS — Renomeação por CSV

Script Python para renomear arquivos em lote, acrescentando um sufixo definido em um CSV e preservando a extensão.

Esta é a versão por linha de comando. A aplicação com interface gráfica está em [renameOSnew](https://github.com/olegariobru/renameOSnew).

## Funcionalidades

- Leitura de correspondências entre nome original e sufixo.
- Renomeação dos arquivos encontrados na pasta configurada.
- Preservação da extensão.
- Exibição das operações realizadas e dos arquivos ignorados.

## Tecnologias

Python 3, pandas e módulo `os`.

## Como executar

```bash
git clone https://github.com/olegariobru/renameOs.git
cd renameOs
python -m pip install pandas
```

Edite `Desktop/RenameScript/renameOs.py` e ajuste as variáveis `pasta` e `csv_path` para a pasta e o CSV que deseja utilizar.

O CSV deve conter exatamente as colunas `nome_original` e `sufixo`. Não inclua a extensão em `nome_original`.

```csv
nome_original,sufixo
documento-a,revisado
documento-b,2026
```

Nesse exemplo, `documento-a.pdf` se torna `documento-a_revisado.pdf`.

Execute:

```bash
python Desktop/RenameScript/renameOs.py
```

## Verificação e limites

Execute primeiro sobre uma pasta com cópias de arquivos. O script realiza renomeações diretamente e ainda não oferece simulação, rollback ou tratamento completo de conflitos.

Não há testes automatizados no repositório.

## Próximos passos

- Receber caminhos por argumentos de linha de comando.
- Incluir modo de simulação.
- Validar conflitos antes de renomear.
- Registrar operações e permitir reversão.

## Como contribuir

Abra uma issue com o problema ou a melhoria proposta. Para enviar código, crie um fork e uma branch, mantenha a alteração focada e abra um pull request explicando o resultado e como verificou o funcionamento.

## Licença

Este repositório ainda não contém um arquivo `LICENSE`. A licença de uso e redistribuição precisa ser formalizada pelo autor.

## Autor

[Bruno Olegário](https://github.com/olegariobru) · [LinkedIn](https://www.linkedin.com/in/bolgarimacedo/)

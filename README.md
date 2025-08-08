# 📝 RenameOS

Este projeto é um script em Python para renomear arquivos de uma pasta mantendo o nome original e adicionando um sufixo específico definido em um arquivo CSV.

---

## 📌 Funcionalidade
- Lê um arquivo CSV contendo:
  - O nome original do arquivo (sem extensão)
  - O novo sufixo que deve ser adicionado
- Renomeia todos os arquivos de uma pasta de forma automatizada
- Mantém a extensão original dos arquivos
- Funciona com milhares de arquivos (testado com mais de 12.000)

---

## 📂 Estrutura esperada

/RenameOS
├── renomear.py # Script principal
├── nomes.csv # Lista de nomes originais e sufixos
├── /pasta_imagens # Pasta contendo os arquivos a serem renomeados


---

## 📄 Formato do CSV

O arquivo `nomes.csv` deve ter a seguinte estrutura:

| original   | sufixo            |
|------------|-------------------|
| 123456678  | PPSCFJGV20250808   |
| 098765433  | PPSCFJGV202400900971 |

⚠ **Importante:** Não inclua extensão nos nomes originais no CSV.

---

## 🚀 Como usar

1. Coloque todos os arquivos que deseja renomear dentro da pasta `pasta_imagens`.
2. Crie o arquivo `nomes.csv` com os nomes originais e sufixos(Novos).
3. Execute o script:

```
python renomear.py
```

🛠 Requisitos
Python 3.x instalado

Biblioteca pandas (para ler o CSV)

Para instalar:
```
pip install pandas

```

📜 Licença
Este projeto está licenciado sob a licença MIT - sinta-se livre para usar e modificar.

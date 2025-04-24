# 📇 ContatON CLI

Um sistema de gerenciamento de contatos no terminal, feito com Python puro e muito carinho — totalmente modularizado e persistente, pensado para refletir práticas de desenvolvimento profissional. Ideal para aprendizado e evolução prática de conceitos fundamentais de programação.

---

## 🚀 Sobre o Projeto

O **ContatON CLI** é uma aplicação de linha de comando que permite:

- Cadastrar contatos
- Listar contatos cadastrados em formato visual de ficha
- Armazenar e carregar os dados automaticamente com uso de JSON
- Usar identificadores únicos (UUID) para evitar conflitos
- Organizar o código em módulos reutilizáveis e legíveis

Este projeto foi pensado como parte de um processo de aprendizado ativo, simulando como seria construir um sistema simples dentro de uma equipe real, com divisão de responsabilidades e evolução por sprints.

---

## 👱️ Estrutura do Projeto

```
ContatON/
├── data/
│   └── contatos.json         # Base de dados com os contatos cadastrados
├── scripts/
│   ├── main.py               # Ponto de entrada da aplicação
│   └── utils.py              # Funções auxiliares organizadas de forma modular
├── README.md                
└── requirements.txt          # Dependências
```

---

## ⚙️ Funcionalidades

- [x] Cadastro de contatos com validações (nome, telefone, e-mail)
- [x] Formatação automática do telefone
- [x] Identificação única por UUID
- [x] Listagem estilizada no terminal com fichas visuais
- [x] Armazenamento automático dos dados
- [x] Modularização completa em múltiplos arquivos
- [x] Projeto pronto para expansão com busca, exclusão, etc.

---

## 🧪 Exemplo de Execução

```bash
===== Menu ContatON =====
1 - Cadastrar novo contato
2 - Listar todos os contatos
3 - Sair

Nome: Mario
Telefone: 21999999999
E-mail: mario@email.com

Contato Mario cadastrado com sucesso.
Contato salvo em data/contatos.json com sucesso.

===== Lista de Contatos =====
==============================
🔹 Contato
Nome:     Mario
Telefone: (21) 99999-9999
E-mail:   mario@email.com
==============================
```

---

## 🧠 Tecnologias e Conceitos Aplicados

- Python 3.x
- Estruturas de decisão e repetição
- Funções e escopo
- Manipulação de arquivos (`open`, `json`, `os`)
- Identificadores únicos com `uuid`
- Modularização de código
- Organização de projetos
- Boas práticas de versionamento com Git

---

## 👨‍💻 Autor

Desenvolvido por **Mario**, um eterno curioso em transição de carreira para tecnologia, apaixonado por desenvolvimento, automação e projetos com impacto real.

---

## 📌 Status do Projeto

> **Concluído o MVP (Produto Mínimo Viável).**
>
> Próximas funcionalidades (em planejamento):
> - 🔍 Busca por nome ou e-mail
> - 📝 Edição e exclusão de contatos
> - 💡 Exportação de dados (CSV ou PDF)
> - 🌐 Versão Web com Flask ou Streamlit
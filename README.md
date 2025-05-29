# The Orders and Tasks Project Django

Projeto em Python com funcionalidades diversas, incluindo módulos para core, orders, tasks e uma estrutura de testes com cobertura completa.  
Utiliza ferramentas de qualidade de código como Black, Flake8 e isort integradas via hooks de pré-commit.

---

Feito com <3 por Thayna Santana

## Qualidade de código
O projeto utiliza os seguintes linters e formatadores
- Black - formatação automatica do código.
- Flake8 - verificação de estilo e erros
- isort - organização dos imports
Estes sao configurados como hooks de pre-commit para manter o codigo limpo.

## Tecnologias Utilizadas

- **Python 3.x** — linguagem principal do projeto  
- **Django Rest Framework** — criação da API RESTful  
- **django_rq** — gerenciamento de tarefas assíncronas com Redis como backend  
- **Kafka** — sistema de mensageria para eventos e comunicação assíncrona  
- **pytest** — framework para testes unitários e de integração  
- **Black, Flake8, isort** — ferramentas para formatação, análise estática e organização do código  
- **Clean Code & SOLID** — princípios adotados para manter o código legível, manutenível e extensível  
- **TDD/BDD** — desenvolvimento orientado a testes e comportamento para garantir qualidade e confiabilidade  

## Estrutura do projeto
the-project/
├── core/                # Módulos centrais
├── orders/              # Lógica relacionada a pedidos
├── tasks/               # Tarefas e serviços
├── tests/               # Testes unitários e integração
├── config/              # Configurações do projeto
├── requirements.txt     # Dependências do Python
├── README.md            # Este arquivo
└── ...

## Como rodar localmente

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/the-project.git
cd the-project
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

3. Instale as dependencias:
```bash
pip install -r requirements.txt
```

4. Rode os testes para garantia de que está tudo funcionando:
```bash
pytest
```

## Licença
Este projeto está licenciado sob licença MIT. Veja o arquivo LICENSE para mais detalhes.
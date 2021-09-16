# api-wikipedia

API foi desenvolvida em Flask com o objetivo de realizar buscas na wikipedia e retornar este conteudo em um JSON.

## Rotas

Rotas da API:

| URL | Métodos | Descrição |
| -------- | ------------- | --------- |
| `/api/v1/search=&lang=` | GET | Pesquisa perguntas na wikipedia e retorna um JSON. |

Paramêtros:

| Parâmetro | Tipo de valor | Default | Obrigatório | Descrição |
| -------- | ------------- | ---------- | --------- | --------- |
| search | str | null | Sim | Pergunta |
| lang | str | null | Sim | Linguagem da pesquisa |

Exemplo:

`api-wikipedia.herokuapp.com/api/v1/search=Google&lang=pt`

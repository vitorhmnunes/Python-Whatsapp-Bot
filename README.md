# Python-Whatsapp-Bot

## Visão Geral da aplicação
### Arquivo data treatment
- Por meio do Pandas, obtém dados de uma planilha .xlsm e os filtra de acordo com a necessidade do cliente
- Filtro de dados:
  - Cria outro dataframe, somente com os dados necessários
  - Descarta alguns clientes por uma idade pré determinada

### APP
- Adquire os dados separados no arquivo data treatment
- Pega os dados sensíveis do .env
- Cria as mensagens a serem enviadas pelo bot (têm que ser insseridas pelo adm)
- Faz a conexão com a API Whapi Cloud
- Envia as mensagens para os clientes

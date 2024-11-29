# Chat Bot
Um chatbot que permite o envio de arquivos PDF e responde a perguntas baseadas no conteúdo desses documentos. Ele utiliza o modelo [Roberta](https://huggingface.co/deepset/roberta-base-squad2-distilled) como núcleo para realizar tarefas de question answering.

# Dependências
Para executar o projeto, é necessário:
- Python 3.12 ou superior.
- `pip`, o gerenciador de pacotes do Python.
As bibliotecas necessárias estão listadas no arquivo requirements.txt.

# Instalação
- Certifique-se de ter o Python e o pip instalados.
- Instale as dependências executando o comando abaixo no terminal:

```bash
pip install -r requirements.txt
```


# Execução
Após a instalação das dependências, inicie o servidor com o comando:

```bash
flask run --port 4000
```

## Alteração de Porta ou Host
- Para usar outra porta, substitua 4000 pelo número desejado.
- Para definir outro host, adicione o parâmetro --host, por exemplo:

```bash
flask run --host X.X.X.X --port 4000
```

Quando o servidor iniciar, você verá uma mensagem como:

```bash
Running on http://127.0.0.1:4000
```

Acesse este endereço no navegador para usar a interface gráfica do chatbot.


# Uso

1. Envie um ou mais arquivos PDF para o chatbot por meio da interface gráfica.
2. Faça perguntas baseadas no conteúdo dos documentos enviados.

# Observação
O tempo de resposta pode variar. Caso o processamento não utilize uma GPU, as respostas podem levar mais tempo.
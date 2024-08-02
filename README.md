## Sobre o projeto

O zero_fastapi se trata de uma implementação relativamente básica de uma API Rest com FastAPI.
Se trata de uma lista TODO (à fazer), onde você pode cadastrar tarefas, adicionar descrição, 
mudar status, etc, além de uma autenticação completa de usuários. Você pode conferir a documentação
[aqui](https://zero-fastapi.fly.dev/redoc).

## Como usar

Você pode utilizar diretamente a url `https://zero-fastapi.fly.dev/` para testes.
Caso queira utilizar sua própria infraestrutura, basta ter o Docker instalado.
Então, execute o seguinte comando:

```bash
docker compose up
```

Ressaltando que você precisará definir suas variáveis de ambientes no arquivo .env:

```plain
DATABASE_URL="SUA_URL"
SECRET_KEY="your-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Graças ao SQLAlchemy, você pode utilizar praticamente qualquer banco de dados apenas alterando
a variável de conexão. Incrível, né?

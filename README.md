# jenkins-ci

Uma implementação do jenkins pipeline de fácil utilização.

## Utilização

Use o comando do docker-compose para criar as imagens (a segunda imagem leva cerca de 4 minutos para finalizar).

```bash
docker-compose build
````

Após a construção das imagens, suba as imagens com o comando do docker-compose.

```bash
docker-compose up -d
````
As configurações padrão das imagens estão no arquivo docker-compose.yml. 

## Considerações

As imagens utilizam duas pastas compartilhadas, ./shared/master e ./shared/slave. Todas as configurações e arquivos do jenkins ficam nessas pastas.

A pasta ./shared/slave contém as pastas de arquivos dos jobs do jenkins.
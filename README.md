# Labirinto

Geração de solução dado um labirinto, utilizando métodos de buscas.

## Metodos de Buscas

Utilizamos os seguintes metodos de buscas:

- [Busca em Largura](https://pt.wikipedia.org/wiki/Busca_em_largura)
- [Busca em Profundidade](https://pt.wikipedia.org/wiki/Busca_em_profundidade)
- [Custo Uniforme](http://conteudo.icmc.usp.br/pessoas/sandra/G2_t2/Busca.html)
- [Gulosa (Greedy)](https://pt.wikipedia.org/wiki/Algoritmo_guloso)
- [A*](https://pt.wikipedia.org/wiki/Algoritmo_A*)

## Estrutura dos Arquivos

Temos uma pequena estrutura básica de arquivos.

- base
    - bases.py (Guarda todos os metodos que serão utilizados em toda a aplicação, como por exemplo, caregar a imagem)
    - functions.py (Guarda todos os metodos de busca e suas implementações com o gerenciador de tempo de execução)
- labirintos
    - Todas as imagens de teste do nosso labirinto
- resolv
    - Contem as Imagens com a resposta, separadas pelo metodo de busca


## TODO
- [x] Implementar Leitura de Imagem e Arrays
- [ ] Documentar
- [x] Refatorar Código p/ Melhor desempenho
- [x] Busca em Largura
- [x] Busca em Profundidade
- [ ] Custo Uniforme
- [ ] Gulosa (Greedy)
- [ ] A*
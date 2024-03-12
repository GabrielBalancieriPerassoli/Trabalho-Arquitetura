Professor: Anderson Faustino da Silva, Dr.

Nome: Gabriel Balancieri Perassoli RA: 135854 
Nome: Gabriel Bertolini RA: 132766
Nome: Matheus Dinon Leite RA: 132856

O tradutor foi desenvolvido utilizando todos os recursos disponíveis ao nosso alcance.

Embora reconheçamos que nosso nível de aprendizado impõe certas limitações ao projeto, empenhamo-nos ao máximo em testar nosso programa exaustivamente, em busca de torná-lo plenamente funcional – mantendo, é claro, os elementos presentes na arquitetura do computador IAS. 

Agradecemos a compreensão.

DO FUNCIONAMENTO
Para utiilizar o tradutor: enquanto estiver no diretório principal (Trabalho-Arquitetura-main), execute no terminal:
"python ias.py <arquivo de entrada> <endereço em que começam as instruções>", sem as aspas.
Para ler, por exemplo, o programa de teste (teste.ias), execute:
"python ias.py teste.ias 3", sem as aspas.

Algumas recomendações:

1. A memória vai de 0 a N. Quando for se referir a um endereço, leve em consideração que eles se referem à memória (que começa em 0), e não às linhas do arquivo de texto de entrada (que começa em 1). No exemplo abaixo, a instrução JUMP M(8) não saltará para a instrução STOR M(2) – que apesar de estar na 8.ª linha, é o endereço de memória 7 – e sim para o endereço de memória 8 (9.ª linha), que está vazio.
0  20
1  15
2  0
3  0
4  LOAD M(0)
5  JUMP M(8)
6  SUB M(1)
7  STOR M(2)

2. Não deixe espaços vazios na memória. Estes podem causar comportamentos imprevistos no funcionamento do programa. No exemplo baixo, o endereço 4 está vazio, impossibilitando a leitura correta do arquivo de entrada.
0  20
1  15
2  0
3  0
4  
5  LOAD M(0)
6  SUB M(1)
7  JUMP M(8)
8  STOR M(2)
9  STOR M(3)

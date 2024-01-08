********* README *********

Fizemos o trabalho, e acreditamos que está funcionando corretamente, testamos várias vezes, tentamos fazer o mais realista possível com o computador IAS e com o conhecimento que tinhamos, tendo em vista que tivemos apenas algoritmos (lógica de programação), mas sabemos que fazer ficar 100% ainda não conseguimos desenvolver.

Devido ao nosso atual nível de aprendizado, reconhecemos algumas limitações como o código ainda pode ser otimizado para melhor desempenho, além de limitações na implementação de algoritmos complexos devido à falta de experiência na resolução de problemas avançados.

Algumas recomendações para o funcionamento:

1 - A memória vai de 0 até N, no caso quando for dar um JUMP você tera que colocar uma posição de memória a menos por exemplo, pois as linhas de memória no txt começam em 1:

0 - 20
1 - 15
2 - 0
3 - 0
4 - LOAD M(0)
5 - SUB M(1)
6 - JUMP M(8)
7 - STOR M(2)
8 - STOR M(3)

2 - Não de enter's na memória (txt), isso pode acarretar algum erro no nosso código que não conseguimos tratar, por exemplo:

0 - 20
1 - 15
2 - 0
3 - 0
4 - 
5 - LOAD M(0)
6 - SUB M(1)
7 - JUMP M(8)
8 - STOR M(2)
9 - STOR M(3)
10 - 

Alguns programas para testar no nosso tradutor:

1) Fatorial:

6
1
0
LOAD M(0)
STOR M(2)
LOAD M(0)
SUB M(1)
STOR M(0)
LOAD MQ,M(0)
LOAD M(0)
SUB M(1)
SUB M(1)
JUMP +M(14)
JUMP M(18)
MUL M(2)
LOAD MQ
STOR M(2)
JUMP M(5)
LOAD M(2)

2) Contador:

1
1
10
LOAD M(0)
ADD M(1)
STOR M(0)
SUB M(2)
JUMP +M(9)
JUMP M(3)
LOAD M(0)

3) Encontrar o maior número entre os 3 números:

8
10
15
0
LOAD M(0)       
SUB M(1)        
JUMP +M(8)
JUMP M(12) 
LOAD M(0)
SUB M(2)
JUMP +M(16) 
JUMP M(22) 
LOAD M(1)
SUB M(2) 
JUMP +M(19)
JUMP M(22) 
LOAD M(0)
STOR M(3)
JUMP M(25)
LOAD M(1)
STOR M(3)
JUMP M(25)
LOAD M(2)
STOR M(3)
JUMP M(25)
LOAD M(3)

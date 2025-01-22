Esse código é para solucionar quebras cabeças do Bing, como por exemplo: https://www.bing.com/spotlight/imagepuzzle?form=ML2BF0&OCID=ML2BF0&PUBL=RewardsDO&PROGRAMNAME=BingDailyOfferIN&CREA=ML2BF0

Esse código resolve QUALQUER PLUZZE no esquema 0 a 8 onde 0 é o vazio:

123 <br>
456 <br>
780 <br>

Digite a primeira linha (3 dígitos separados por espaço):
> 0 1 2 (entrada)
> 
Primeira linha: [0, 1, 2]
> 
Digite a segunda linha (3 dígitos separados por espaço):
> 3 4 5 (entrada)
> 
Segunda linha: [3, 4, 5]
> 
Digite a terceira linha (3 dígitos separados por espaço):
> 6 7 8 (entrada)
> 
Terceira linha: [6, 7, 8]
> 
Estado inicial: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Você confirma esta sequência? [0, 1, 2, 3, 4, 5, 6, 7, 8] (s/n):

Solução encontrada! Número de movimentos necessários: 22
Passo 1:
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]

Passo 2:
[1, 0, 2]
[3, 4, 5]
[6, 7, 8]

Passo 3:
[1, 4, 2]
[3, 0, 5]
[6, 7, 8]

Passo 4:
[1, 4, 2]
[0, 3, 5]
[6, 7, 8]

Passo 5:
[1, 4, 2]
[6, 3, 5]
[0, 7, 8]

Passo 6:
[1, 4, 2]
[6, 3, 5]
[7, 0, 8]

Passo 7:
[1, 4, 2]
[6, 3, 5]
[7, 8, 0]

Passo 8:
[1, 4, 2]
[6, 3, 0]
[7, 8, 5]

Passo 9:
[1, 4, 2]
[6, 0, 3]
[7, 8, 5]

Passo 10:
[1, 4, 2]
[0, 6, 3]
[7, 8, 5]

Passo 11:
[1, 4, 2]
[7, 6, 3]
[0, 8, 5]

Passo 12:
[1, 4, 2]
[7, 6, 3]
[8, 0, 5]

Passo 13:
[1, 4, 2]
[7, 0, 3]
[8, 6, 5]

Passo 14:
[1, 0, 2]
[7, 4, 3]
[8, 6, 5]

Passo 15:
[1, 2, 0]
[7, 4, 3]
[8, 6, 5]

Passo 16:
[1, 2, 3]
[7, 4, 0]
[8, 6, 5]

Passo 17:
[1, 2, 3]
[7, 4, 5]
[8, 6, 0]

Passo 18:
[1, 2, 3]
[7, 4, 5]
[8, 0, 6]

Passo 19:
[1, 2, 3]
[7, 4, 5]
[0, 8, 6]

Passo 20:
[1, 2, 3]
[0, 4, 5]
[7, 8, 6]

Passo 21:
[1, 2, 3]
[4, 0, 5]
[7, 8, 6]

Passo 22:
[1, 2, 3]
[4, 5, 0]
[7, 8, 6]

Pressione Enter para sair...

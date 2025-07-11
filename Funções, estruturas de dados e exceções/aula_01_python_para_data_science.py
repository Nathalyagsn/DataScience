# -*- coding: utf-8 -*-
"""Aula 01 - Python para Data Science.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iikV_gwpLV_MfXpLXyxepSFdIYtir9x3

# <font color=green> PYTHON PARA DATA SCIENCE
---

## <font color=green> 1. BIBLIOTECAS
---

## 1.1 Instalação e importação de bibliotecas

Na linguagem Python utiliza-se bastante o conceito de bibliotecas como um conjunto de módulos e funções úteis para o usuário. Elas facilitam em reduzir o uso de códigos no projeto, mantendo apenas o necessário para a tarefa que desejamos realizar.

### Instalando uma biblioteca

Para instalar ou atualizar uma biblioteca no Python, podemos recorrer ao `pip` que é um gerenciador de bibliotecas no Python.
"""

# Instalando a biblioteca matplotlib pelo pip
!pip install matplotlib

# Instalando uma versão específica do matplotlib
!pip install matplotlib==3.6.2

"""Existe também o PYPI que é um repositório de bibliotecas Python que traz as bibliotecas mais utilizadas pela comunidade junto a informações de como usar e acesso as documentações de cada uma delas.

- PYPI ([https://pypi.org/](https://pypi.org/))

### Importando uma biblioteca
"""

# Importando uma biblioteca sem alias
import matplotlib

matplotlib.__version__

# Importando uma biblioteca com alias
import matplotlib.pyplot as plt

plt.show()

"""## 1.2 Utilizando pacotes/bibliotecas

- Documentação do Python (https://docs.python.org/pt-br/3/)

#### Exemplo 1: Vamos testar a biblioteca Matplotlib para um exemplo de médias de estudantes de uma classe.

(https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
"""

import matplotlib.pyplot as plt

estudantes = ["João", "Maria", "José"]
notas = [8.5, 9, 6.5]

plt.bar(x = estudantes, height = notas)

"""#### Exemplo 2: Vamos selecionar aleatoriamente um aluno para apresentar o seu trabalho de ciência de dados usando a biblioteca Random

(https://docs.python.org/pt-br/3/library/random.html)
"""

estudantes_2 = ["João", "Maria", "José", "Ana"]

# Importando uma função específica de uma biblioteca
from random import choice

"""<font color=green>**Dica:**</font> Você pode notar ao longo de nossa prática a importância de recorrer a documentação para aprender como utilizar um método ou pacote na linguagem Python.

O método `help()`, por exemplo, retorna uma descrição sobre uma variável, método ou classe.

https://docs.python.org/pt-br/3/library/functions.html?#help
"""

help(choice)

estudante = choice(estudantes_2)
estudante

"""## <font color=green> 2. FUNÇÕES
---

Na linguagem Python, as **funções** são sequências de instruções que executam tarefas específicas, podendo ser reutilizadas em diferentes partes do código. Elas podem receber parâmetros de entrada (que podemos chamar de *inputs*) e também retornar resultados.

## 2.1 Built-in function

O interpretador do Python já possui uma série de funções embutidas que podem ser invocadas a qualquer momento. Algumas que vamos utilizar ao longo desse curso são: type(), print(), list(), zip(), sum(), map() etc.

***Documentação:***
https://docs.python.org/pt-br/3/library/functions.html

#### **Situação 1:**

A escola em que estamos construindo o nosso case de dados compartilhou os dados das notas de um estudante para que pudéssemos calcular a média deste em até uma casa decimal.

Os dados recebidos correspondem a um dicionário com as chaves indicando o trimestre em questão e os valores das notas de cada trimestre do estudante em uma dada matéria.
"""

# Notas do(a) estudante
notas = {'1º Trimestre': 8.5, '2º Trimestre': 7.5, '3º Trimestre': 9}
notas

# Calculando a soma

# Usando a função embutida sum()

# Usando a função embutida len()

# calculando a média

"""*Arredondar a média usando round():*

https://docs.python.org/pt-br/3/library/functions.html#round
"""





"""## 2.2 Criando funções

Depois de explorarmos a built-in functions e aprendermos como utilizar algumas delas, você pode se deparar com a necessidade de resolver um problema específico em que elas não serão o suficiente.

Nesse ponto, precisaremos criar as nossas próprias funções, ainda mais se precisarmos utilizá-las em mais partes de nossos códigos.

### Funções sem parâmetros

#### Formato padrão:

```python
def <nome>():
  <instruções>
```
"""





"""### Funções com parâmetros

#### Formato padrão:

```python
def <nome>(<param_1>, <param_2>, ..., <param_n>):
  <instruções>
```
"""







"""#### **Situação 2:**

Recebemos uma demanda de calcular a média de um estudante a partir de uma lista, sendo possível alterar a quantidade de notas, sem impedir que o cálculo seja refeito.

Os dados recebidos, desta vez, correspondem a uma lista contendo apenas as notas de um estudante em uma dada matéria.

**Vamos resolver esse desafio?**

Para facilitar o nosso entendimento do processo vamos aplicar às notas de apenas um estudante, mas você pode testar outros casos para treinar.
"""

# Notas do(a) estudante
notas = [8.5, 9.0, 6.0, 10.0]











"""<font color=red>**Atenção!**</font>
Quando utilizamos funções precisamos prestar atenção a uma propriedade chamada **escopo de uma função**

Ela determina onde uma variável pode ser utilizada dentro do código. Por exemplo, uma variável criada dentro de uma função existirá apenas dentro da função. Ou seja, encerrando a execução da função, a variável não estará disponível para o usuário no restante do código.
"""



"""## 2.3 Funções que retornam valores

#### Formato padrão:

```python
def <nome>(<param_1>, <param_2>, ..., <param_n>):
  <instruções>
  return resultado
```

Retomando a atividade anterior, podemos retornar e salvar o valor da média da seguinte forma:
"""

# Notas do(a) estudante
notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
  calculo = sum(lista) / len(lista)
  ...





"""#### **Situação 3:**

Recebemos uma nova demanda, desta vez, de calcular a média de um estudante a partir de uma lista e retornar tanto a média quanto a situação do estudante ("Aprovado(a)" se a nota for maior ou igual a 6.0, caso contrário, será "Reprovado(a)").

Além disso, precisamos exibir um pequeno texto em que indicamos a média do(a) estudante e qual a situação. Os dados recebidos correspondem a uma lista contendo apenas as notas de um estudante em uma dada matéria.

**Vamos resolver esse desafio?**

Para facilitar o nosso entendimento do processo vamos aplicar as notas de apenas um estudante, mas você pode testar outros casos para treinar.
"""

# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.0]











print(f'O(a) estudante atingiu uma média de {} e foi {}.')

"""## 2.4 Funções lambda

Também chamadas de funções anônimas, são funções que não precisam ser definidas, ou seja não possuem um nome, e descrevem em uma única linha os comandos que desejamos aplicar.

https://docs.python.org/pt-br/3/reference/expressions.html?#lambda

#### Formato padrão:

```python
lambda <variavel>: <expressao>
```

#### **Situação 4:**

Nesta nova demanda, precisamos criar uma calculadora simples da média ponderada de notas de uma dada matéria. Vamos requisitar ao usuário a entrada das 3 notas (N1, N2, N3) do estudante e devolver a média ponderada deste estudante. Os pesos das notas são de, respectivamente 3, 2, 5.

Precisamos exibir um pequeno texto em que indicamos a média do(a) estudante.

**Vamos resolver esse desafio?**
"""

# Comparando uma função de qualitativo no formato de função para função anônima

# Testando a mesma função para uma função lambda

"""**Partindo para nosso problema:**"""

# Recebendo as notas e calculando a média ponderável
N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))

...

# Exibindo a média
print(f'O(a) estudante atingiu uma média de {}')

"""### Mapeando valores

#### Formato padrão:

```python
map(<lambda function>, <iterador>)
```

#### **Situação 5:**

Recebemos mais uma demanda, desta vez, para criar uma pequena função que pudesse adicionar qualitativo (pontuação extra) às notas do trimestre dos estudantes da turma que ganhou a gincana de programação promovida pela escola. Cada estudante receberá o qualitativo de 0.5 acrescido à média.

Os dados recebidos correspondem a uma lista contendo as notas de alguns estudantes e uma variável com o qualitativo recebido.

**Vamos resolver esse desafio?**

Para facilitar o nosso entendimento do processo vamos aplicar o qualitativo às notas de 5 estudantes, mas você pode testar outros casos para treinar.
"""

# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5



# Não conseguimos aplicar o lambda em listas direto, é necessário
# utilizarmos junto a ela a função map



"""## <font color=green> 3. ESTRUTURA DE DADOS COMPOSTAS
---

## 3.1 Estruturas aninhadas

Aprendemos anteriormente a manipular listas, tuplas e dicionários para trabalhar com uma sequência ou coleção de valores sejam numéricos, categóricos, etc. Nessa aula, vamos aprofundar em outra situação comum para a pessoa cientista de dados que é trabalhar com esses tipos de estruturas aninhadas, ou seja, quando possuímos por exemplo listas dentro de uma lista.

### Lista de listas

#### Formato padrão:

```python
[[a1, a2,...,an], [b1, b2,...,bn], ..., [n1, n2,...,nn]]
```

#### **Situação 6:**

Recebemos a demanda de transformar uma lista com o nome e as notas dos três trimestres de estudantes em uma lista simples com os nomes separados das notas e uma lista de listas com as três notas de cada estudante separadas umas das outras. Os dados recebidos correspondem a uma lista com os nomes e as respectivas notas de cada estudante.

**Vamos resolver esse desafio?**

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.
"""

notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]













"""### Lista de tuplas

#### Formato padrão:

```python
[(a1, a2,...,an), (b1, b2,...,bn), ..., (n1, n2,...,nn)]
```

#### **Situação 7:**

Nesta nova demanda, precisamos gerar uma lista de tuplas com os nomes dos estudantes e o código ID de cada um para a plataforma de análise dos dados. A criação do código consiste em concatenar a primeira letra do nome do estudante a um número aleatório de 0 a 999. Os dados recebidos correspondem a uma lista dos nomes de cada estudante.

**Vamos resolver esse desafio?**

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.
"""

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
estudantes

from random import randint

def gera_codigo():
  return str(randint(0,999))



"""## 3.2 List comprehension

É uma forma simples e concisa de criar uma lista. Podemos aplicar condicionais e laços para criar diversos tipos de listas a partir de padrões que desejamos para a nossa estrutura de dados.

https://docs.python.org/pt-br/3/tutorial/datastructures.html?#list-comprehensions

#### Formato padrão:

```python
[exressão for item in lista]
```

#### **Situação 8:**

Recebemos a demanda de criar uma lista com as médias dos estudantes da lista de listas que criamos na Situação 6. Lembrando que cada lista da lista de listas possui as três notas de cada estudante.

**Vamos resolver esse desafio?**

**Dica:** Utilize o formato:
```python
[exressão for item in lista]
```
"""

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
  '''

  calculo = sum(lista) / len(lista)

  return calculo



"""#### **Situação 9:**

Agora, precisamos utilizar as médias calculadas no exemplo anterior, pareando com o nome dos estudantes. Isto será necessário para gerar uma lista que selecione aqueles estudantes que possuam uma média final maior ou igual a 8 para concorrer a uma bolsa para o próximo ano letivo. Os dados recebidos correspondem a uma lista de tuplas com os nomes e códigos dos estudantes e a lista de médias calculadas logo acima.

**Vamos resolver esse desafio?**

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.

**Dica:** Utilize o formato:
```python
[expr for item in lista if cond]
```

"""

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# Gerando a lista de nomes (extraindo da tupla)

"""<font color=green>**Dica:**</font> Para conseguirmos parear as médias e nomes facilmente, podemos recorrer a mais uma built-in function: `zip()`

Ela recebe um ou mais iteráveis (lista, string, dict, etc.) e retorna-os como um iterador de tuplas onde cada elemento dos iteráveis são pareados.
"""



# Gerando a lista de pessoas candidatas a bolsa

"""#### **Situação 10:**

Recebemos duas demandas a respeito desse projeto com as notas dos estudantes:
- Criar uma lista da situação dos estudantes em que caso se sua média seja maior ou igual a 6 receberá o valor "Aprovado" e caso contrário receberá o valor "Reprovado".
- Gerar uma lista de listas com:
  - Lista de tuplas com o nome dos estudantes e seus códigos
  - Lista de listas com as notas de cada estudante
  - Lista com as médias de cada estudante
  - Lista da situação dos estudantes de acordo com as médias

Os dados que utilizaremos são os mesmos que geramos nas situações anteriores (`nomes`, `notas`, `medias`).

**Vamos resolver esse desafio?**

Para seguirmos o processo, vou deixar logo abaixo as estruturas de dados que já produzimos.

**Dica:** Para a lista das situações utilize o formato:
```python
[resultado_if if cond else resultado_else for item in lista]
```
"""

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]



"""**Dica:** Para gerar a lista de listas do enunciado podemos utilizar o formato a seguir
```python
[expr for item in lista de listas]
```
"""



"""<font color=green>**Dica:**</font> Podemos recorrer a forma mais simples de geração de listas de lista com o uso direto dos colchetes sem necessitar de utilizar as expressões e o laço for na  abrangência de listas"""



"""## 3.3 Dict comprehension

É uma forma simples e concisa de criar ou modificar um dicionário. Podemos aplicar condicionais e laços para criar diversos tipos de dicionários a partir de padrões que desejamos para a nossa estrutura de dados e com o suporte de iteráveis como listas ou sets.

https://peps.python.org/pep-0274/

#### Formato padrão:

```python
{chave: valor for item in lista}
```

#### **Situação 11:**

Agora, a nossa demanda consiste em gerar um dicionário a partir da lista de listas que criamos na Situação 10 para passar para a pessoa responsável por construir as tabelas para a análise dos dados.
- As chaves do nosso dicionário serão as colunas identificando o tipo de dado
- Os valores serão as listas com os dados correspondentes àquela chave.

**Vamos resolver esse desafio?**

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.

**Dica:** Utilize o formato

```python
{chave: valor for item in lista}
```
"""

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

# Colunas com os tipos dos dados (exceto nome)
coluna = ["Notas", "Média Final", "Situação"]

...

# Vamos por fim adicionar o nome dos estudantes, extraindo apenas seus nomes da lista de tuplas

"""## <font color=green> 4. LIDANDO COM EXCEÇÕES
---

Podemos notar em nosso caminho até aqui a existência de alguns erros e exceções na execução de algum comando. Como uma pessoa cientista de dados ou programador, você precisará estar atento a essas situações para evitar bugs ou problemas em seus códigos e análises que possam afetar a experiência tanto do usuário quanto a eficiência da sua análise.

Existem basicamente duas formas distintas de erros: os **erros de sintaxe** e as **exceções**.

Exceções são erros detectados durante a execução e que quebram o fluxo do programa encerrando-o caso não sejam tratadas.  

Vamos aprender a identificar e tratar algumas das exceções aqui, mas é sempre importante mergulhar na documentação para pesquisar e verificar quais se enquadram nos seus projetos.

**Documentação sobre erros e exceções:** https://docs.python.org/3/tutorial/errors.html

## 4.1 Tratando Exceções

O tratamento das exceções contribui estabelecendo um fluxo alternativo para a execução do código evitando a interrupção dos processos inesperadamente.

Existe uma série de exceções e a partir do comportamento que queremos e dos erros que queremos tratar é possível construir um caminho para o usuário ou fornecer mais detalhes sobre aquela exceção.

- Hierarquia das Exceções (https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

### Try ... Except

```python
try:
  # código a ser executado. Caso uma exceção seja lançada, pare imediatamente
except <nome_da_excecao as e>:
  # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa
```

#### **Situação 12:**

Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.

Caso o(a) estudante não esteja matriculado(a) na turma devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma".

Vamos trabalhar nesse exemplo com a exceção **Key Error** que interromperá o processo desse pedaço do código.

**Vamos testar esse primeiro tratamento?**
"""

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}







"""### Adicionando o Else

```python
try:
  # código a ser executado. Caso uma exceção seja lançada, pare imediatamente
except:
  # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa
else:
  # Se não houver uma exeção lançada pelo try, rode essa parte
```

#### **Situação 13:**

Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.

Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante.

Vamos trabalhar nesse exemplo com a exceção **Key Error** que interromperá o processo desse pedaço do código.

**Vamos testar esse tratamento?**
"""

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}



"""### Adicionando o finally

```python
try:
  # código a ser executado. Caso uma exceção seja lançada, pare imediatamente
except:
  # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa
else:
  # Se não houver uma exeção lançada pelo try, rode essa parte
finally:
  # Rode essa parte (com ou sem exceção)
```

#### **Situação 14:**

Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.

Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante. Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada.

Vamos trabalhar nesse exemplo com a exceção **Key Error** que interromperá o processo desse pedaço do código.

**Vamos testar esse tratamento?**
"""

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}



"""## 4.2 Raise

Uma outra forma de trabalhar com as exceções em seu código, é criar as suas próprias exceções para determinados comportamentos que deseja em seu código.

Para isso, utilizamos a palavra-chave `raise` junto ao tipo de exceção que deseja lançar e uma mensagem a ser exibida.

```python
raise NomeDoErro("mensagem_desejada")
```

#### **Situação 15:**

Você criou uma função para calcular a média de um estudante em uma dada matéria passando em uma lista as notas deste estudante.

Você pretende tratar 2 situações:
- Se a lista possuir um valor não numérico o cálculo de média não será executado e uma mensagem de "Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!" será exibida.
- Caso a lista tenha mais de 4 notas, será lançada uma exceção do tipo **ValueError** informando que "A lista não pode possuir mais de 4 notas."

Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada.

**Vamos resolver esse desafio?**
"""

def media(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
  '''

  calculo = sum(lista) / len(lista)

  ...

  return calculo










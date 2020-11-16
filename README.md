# 🤓 Análise de Algoritmos

## Contents

- [Atividade](#atividade)
  - [Entrada](#entrada)
  - [Saída](#saída)
  - [Tempo de Execução](#tempo-de-execução)
  - [Análise](#análise)
- [Installation and Usage](#installation-and-usage)
  - [System Installation and Usage](#system-installation-and-usage)
  - [Docker Installation and Usage](#docker-installation-and-usage)
- [Contributing](#contributing)
- [LICENSE](#license)

## Atividade

O objetivo dessa avaliação é analisar o desempenho dos diferentes algoritmos de ordenação, para isso deverá ser criado um [Jupyter Notebook](https://jupyter.org/) com a implementação em python dos algoritmos analisados.

4 ALGORITMOS DE ORDENAÇÃO SENDO:

- 2 Algoritmos vistos em Algoritmos e Estrutura de Dados:
- 1 dos mais simples (insertion sort, selection sort e bubble sort)
- 1 dos mais complexos (quicksort, heapsort e mergesort).
- 2 Algoritmos que não foram vistos nas aulas;

Para cada algoritmo vocês devem medir através do código quanto tempo ele levou para ordenar um conjunto de números.

### Entrada

Vocês receberam 7 arquivos de números que devem ser lidos, ordenados e registrados o tempo de ordenação para cada um dos arquivos (os arquivos encontram-se na pasta `data`):

- Arquivo com **MIL** números desordenados;
- Arquivo com **CINCO MIL** números desordenados;
- Arquivo com **DEZ MIL** números desordenados;
- Arquivo com **VINTE MIL** números desordenados;
- Arquivo com **CINQUENTA MIL** números desordenados;
- Arquivo com **SETENTA E CINCO MIL** números desordenados;
- Arquivo com **CEM MIL** números desordenados;

### Saída

Vocês devem preencher a seguinte tabela e gerar gráficos comparativos para os algoritmos:

- Gráfico do tamanho da entrada x o Tempo para cada Algoritmo
- Gráfico que mostre a cada "rodada" os tempos pela quantidade (arquivos) os de todos algoritmos implementados

### Tempo de Execução

Limite de tempo para execução e testes de **5 minutos**.

O tempo de execução NÃO pode incluir o tempo de leitura, ele deve marcar APENAS o tempo de ORDENAÇÃO.

Os tempos precisam ser medidos utilizando o MESMO computador de preferência sem nenhuma outra coisa aberta para que a comparação seja mais próxima da realidade.

### Análise

Para cada algoritmo implementado o aluno deve escrever uma análise da complexidade temporal e espacial do algoritmo, essa análise deverá ser escrita no próprio notebook deve conter as informações como:

- Qual o melhor caso?
- Qual o pior caso?
- Qual o caso médio?

O aluno também deve gerar entradas adicionais com os números organizados de forma a simular o pior e o melhor caso e gerar novos gráficos comparativos em relação ao tempo utilizado para ordenação!

## Installation and Usage

To proceed with a system installation, go to the [System Installation and Usage section](#system-installation-and-usage). Otherwise, if you rather use [Docker](https://www.docker.com), please refer to the [Docker Installation and Usage section](#docker-installation-and-usage).

### System Installation and Usage

To install the **project's system installation pre-requisites**, please follow the instructions in the links below:

- [Python 3.8](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

#### Installing dependencies

First, change your current working directory to the project's root directory and bootstrap the project:

```bash
# change current working directory
$ cd <path/to/cs-algorithm-analysis>

# install project dependencies
$ make bootstrap
```

>_**Note**: this command installs dependencies with [venv](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments). This module creates and manages virtual environments -- meaning that it will work isolated from your global Python installation._

#### Running

In order to run the application, use the following command:

```bash
# runs the application using makefile and venv
$ make run
# or '$ ./venv/bin/python3 scripts/main.py'
```

>_**Note**: this command will run different sorting algorithms for various input files. This make take a while, so you might want to grab a coffee in the meantime!_

Finally, an image with the sorting analysis will be saved in `path/to/cs-algorithm-analysis/figures`.

### Docker Installation and Usage

To install the **project's Docker installation pre-requisites**, please follow the instructions in the link below:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker-compose](https://docs.docker.com/compose/install/)

> _**Note**: if you're using a Linux system, please take a look at [Docker's post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)!_

#### Building the container

Once you have `Docker` and `Docker-compose`, change your current working directory to this repository then build and run the container:

```bash
# start the container in the background of your terminal
$ docker-compose up --detach
```

At this point, [Jupyter Notebook](https://jupyter.org) will be running at: `http://localhost:8888`

#### Installing new packages

There are a few ways you may install packages to the container. It'll depend on your goal and needs.

##### Pip

If you need to do update or add packages via `pip`, execute the following command **inside your jupyter notebook**:

```bash
import sys

# install a pip package in the current Jupyter kernel
!{sys.executable} -m pip install <package>
```

> _**note**_: the `!` notation is used to run `pip` directly as a shell command from the notebook. Also, take a look [here](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/) to see why you should NOT use `!pip install <package>`.

##### Conda

If you need to do update or add packages via `conda`, execute the following command **inside your jupyter notebook**:

```bash
import sys

# install a conda package in the current Jupyter kernel
!conda install --yes --prefix {sys.prefix} <package>
```

> _**note**_: the `!` notation is used to run `conda` directly as a shell command from the notebook. Also, take a look [here](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/) to see why you should NOT use `!conda install --yes <package>`.

##### System

To add or update system packages, you will need `root` user permissions. To achieve this, use the following command:

```bash
# execute the container's shell
$ docker exec -it --user root scipy_notebook /bin/bash

# install a package to the system the container runs on
$ sudo apt install <package>
```

### Wrapping up

Once you're done, you may remove what was created by `docker-compose up`:

```bash
# change current working directory
$ cd <path/to/cs-algorithm-analysis>

# stop containers and removes containers, networks, volumes, and images created by `docker-compose up`
$ docker-compose down
```

## Contributing

We are always looking for contributors of **all skill levels**! If you're looking to ease your way into the project, try out a [good first issue](https://github.com/lcbm/cs-algorithm-analysis/labels/good%20first%20issue).

If you are interested in helping contribute to the project, please take a look at our [Contributing Guide](CONTRIBUTING.md). Also, feel free to drop in our [community chat](https://gitter.im/lcbm/community) and say hi. 👋

Also, thank you to all the [people who already contributed](https://github.com/lcbm/cs-algorithm-analysis/graphs/contributors) to the project!

## License

Copyright © 2020-present, [CS Algorithm Analysis Contributors](https://github.com/lcbm/cs-algorithm-analysis/graphs/contributors).
This project is [ISC](LICENSE) licensed.

# VERSIONAMENTO DE CODIGO COM GIT E GITHUB



---

## Sistema de controle de versão 

**Controlam as versões de um arquivo ao longo do tempo** 
- Registra o histórico de atualizações de um arquivo;
- Gerencia quais foram as alterações, a data, autor, etc.;
- Organização, controle e segurança.


---


## Tipos de sistema de controle de versão

- VCS CENTRALIZADO (CVCS)
	- EX: CVS, Subversion.
	-  O controle e feito apenas por um servidor onde vai estar alocado todos os arquivos do projeto podendo ter problemas caso o servidor fique fora do ar você não consegue salvar o seu projeto ou caso voce nao tenha um backup e algum arquivo for corrompido voce acaba perdendo esse projeto.
- VCS DISTRIBUIDO (DVCS)
	- EX: Git, Mercurial.
	- Cada banco de versão é duplicado localmente. Além do servidor que voce ira ficar conectado irá ter uma espécie de backup local que te da alternativas caso esse servidor esteja fora do ar. 



---
## O que é Git ?

**É um Sistema de Controle de Versão Distribuído.**

- Gratuito e Open Source (Código Aberto);
- Ramificações (branching) e fusões (merging) eficientes;
- Leve e rápido.

---
## Fluxo básico do Git 

```bash
$ git init  
→ Cria um repositorio local.

$ git add . 
→ Adiciona todo conteudo no repositório local, para ser um conteúdo especifíco basta alterar o . e colocar o nome do arquivo.

$ git commit -m "mensagem"
→ Salva as alterações no repositório

$ git remote add origin  https://github.com/username/nome-do-repositorio.git
→ Indica qual caminho do para o repositório remoto que deseja.

$ git push → “empurra” as alterações do repositório local para o remoto.

$ git status → visualização de todos os arquivos que que foram adicionados ou não ao repositório 
```

---

## O que é GitHub ?

**É uma plataforma de hospedagem de código para controle de versão com git, e colaboração.**

- Comunidade ativa
- Utilizado mudialmente
- mascote "Octocat"




# Clonando repositórios

``` bash
$ git clone https://github.com/username/nome-do-repositorio
```

# Salvando Alterações no Repositório Local

``` bash
$ git add . → adiciona todos os arquivos no repositorio local.

$ git commit -m "message" → salva alterações do repositorio 
```
# Desfazendo um repositório local

``` bash
$ rm -rf .git
```
# Restaurar ultima versão de um arquivo

``` bash
$ git restore nome_do_arquivo
```
# Historico de commit

- Com esse comando você consegue indentificar o **hash** do commit, nada mais é que o número identificador do commit.
```bash
$ git log 

$ git reflog
→ Histórico mais completo dos commits 
```
# Alterar mensagem do ultimo commit 

``` bash
$ git commit --amend (voce entra no editor e assim pode editar sua mensagem )
    -aperte Esc e :wq para salvar e sair do editor

$ git commit --amend –m "nova mensagem" 
→ Editar mensagem sem entrar no editor.
```
# Desfazer seu ultimo commit

``` bash
$ git reset --soft hash 
→ retorna a um ponto onde os arquivos já estão adicionados há sua area de preparação.

$ git reset --mixed hash 
→ retorna a um ponto onde os arquivos ainda não estão adicionados há sua area de preparação, esse é o comando padrão do reset:

→ git reset hash 

$ git reset --hard hash 
→ ignora os arquivos do commit anterior deletando ele.

```
- Alterações como essas é indicado que sejam feitas antes de serem enviadas ao repositório remoto, caso ao contrario é melhor fazer um novo commit alterando os erros cometidos para não haver conflitos.
# Atualização de versão
- Se esá trabalhando em um código com mais de uma pessoa onde constantemente ele sofre alterações ou você fez alterações no seu repositorório remoto e indicado que sempre atualize seu repositório local, para trazer e mesclar respositorio local basta usar o comando:

``` bash
$ git pull 
→ “puxa” as alterações do repositório remoto para o local (busca e mescla).
    - :wq para salvar atualização do arquivo e fechar editor 
```
# BRANCH

- Imagine em um cenário onde varias pessoas precisam fazer a manutenção de um código, seria instável todas elas mexerem na branch principal (main), podendo ocorrer diversos erros, sendo assim é mais prático criar uma nova branch fazer as alterações necessárias e depois mesclar a branch principal (main):

``` bash
$ git checkout -b nome_da_branch
→ cria uma  ramificação da branch principal
```
- Após fazer as alterações necessárias na sua nova branch basta fazer o fluxo padrão de adicionar e salvar do git:
``` bash
$ git add . 

$ git commit -m "commit_nova_branch" 
```
- Para mesclar os commits da ramificação com os da branch principal basta usar os seguintes comandos:
``` bash
$ git checkout main 
→ retorna para branch principal. Com este comando voce pode movimentar por todas as branch que quiser basta usar o nome da branch desejada

$ git branch -v
    $ git branch
        → te indica todas as branch
→ te indica o ultimo commit de cada branch

$ git merge branch_que_quer_mesclar 
```
- Para apagar uma branch indesejada basta usar o comando:
``` bash
$ git branch -d branch_que_quer_apagar 
```
# Comandos que podem ajudar no dia a dia 

- Quando voce deseja baixar as alterações feitas no repositorio remoto sem mesclar com seu repositorio local. 

``` bash
$ git fetch origin main
→ baixa todo conteudo do repositorio remoto. 

$ git diff main origin/main
→ compara o repositorio local com o remoto e indica a alteração.

$ git merge origin/main
→ traz todo conteudo do repositorio remoto para o local sem mesclar. 
```

- Quando voce quer clonar uma branch especifica de um repositorio com varias branch.

``` bash
$ git clone https://github.com/username/nome-do-repositorio --branch nome_da_branch --single-branch 
```


# T2 Programação Web
## INF1407 22.2 PUC-Rio
### Theo Caldas (1911078) & Matheus Kulick (1911090)

# Minhoca Louca
Jogo baseado no famoso "Snake". <br>
<a href="https://minhoca-louca-app.herokuapp.com">Clique aqui para acessar a página hospedada!</a><br>

## 1. GDD
Nesse jogo, você é uma minhoca louca que precisa coletar frutas para ganhar pontos. <br>
Ao coletar uma fruta, além de aumentar a pontuação, a cauda da minhoca cresce um pouco. <br>
A minhoca está sempre em movimento e você sempre controla sua direção, à partir da cabeça. <br>
Você perde se a cabeça encostar na cauda ou em uma parede (cantos da tela). <br>

### 1.1 Dificuldades
Antes do início de uma partida, é necessário escolher o nível de dificuldade. <br>
Existem 3 níveis de dificuldade do jogo: Fácil, Médio e Difícil. <br> <br>
Quanto maior a dificuldade, mais para dentro da terra a minhoca está. Logo, sua velocidade aumenta (menor tempo de reação). <br>

### 1.2 Identificação dos Elementos
Dependendo da dificuldade selecionada, diferentes sprites aparecerão. <br>

<br> Mapa (plano de fundo): 
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/mapa_00.png" width="30px" height="30px"/>
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/mapa_01.png" width="30px" height="30px"/>
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/mapa_02.png" width="30px" height="30px"/>
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/mapa_03.png" width="30px" height="30px"/> ou
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/mapTile1.png" width="30px" height="30px"/>

<br> Cabeça da minhoca: 
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/cobra_05.png" width="30px" height="30px"/> ou
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/snakeHead.png" width="30px" height="30px"/>

<br> Corpo da minhoca: 
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/cobra_06.png" width="30px" height="30px"/>
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/cobra_07.png" width="30px" height="30px"/>
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/cobra_08.png" width="30px" height="30px"/> ou
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/snakeBody.png" width="30px" height="30px"/>

<br> Fruta (coletável):
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/fruta_09.png" width="30px" height="30px"/>
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/fruta_10.png" width="30px" height="30px"/>
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/easy/fruta_11.png" width="30px" height="30px"/> ou
<img src="MinhocaLouca/MinhocaLoucaApp/static/MinhocaLoucaApp/img/fruit.png" width="30px" height="30px"/>
<br>

### 1.3 Fluxo de Telas
<img src="fluxograma.png" alt="Fluxograma Minhoca Louca"/>

### 1.4 Autenticação e Leaderboard
O jogador pode jogar anonimamente (como visitante) ou criar uma conta.
Após cada partida, o jogador autenticado (logado em uma conta) terá sua pontuação salva e poderá comparar seu resultado atual com antigos e com outros jogadores na tela de leaderboard. 

### 1.5 Usuário Administrador
O administrador do site tem acesso a todos os placares e pode criar, apagar e atualizar cada um.

# 🤖 Bot de Música para Discord

Um bot de música personalizado feito em Python para tocar músicas do YouTube diretamente em canais de voz no Discord. Ideal para servidores que desejam compartilhar músicas entre amigos, realizar sessões de estudo, treinos ou momentos de descontração.

---

## 🎯 Motivação

A necessidade surgiu de criar um bot leve, funcional e fácil de configurar, com comandos simples, sem depender de bots externos que frequentemente saem do ar ou são limitados.

---

## 🧪 Tecnologias Utilizadas

- **Python 3.11**
- **discord.py v2.3.2**
- **yt-dlp** (para buscar e tocar músicas do YouTube)
- **FFmpeg** (para manipulação de áudio)
- **dotenv** (para variáveis de ambiente)
- **Docker** (para ambiente de execução isolado)

---

## 💻 Instalação Local (Windows)

1. **Clone o projeto**:

```bash
git clone https://github.com/seu-usuario/discord-music-bot.git
cd discord-music-bot
```

2. **Crie o ambiente virtual**:

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências**:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 🛠️ Observações

- O bot precisa que o **`libopus`** esteja carregado corretamente para que o áudio funcione no Discord.
- O `ffmpeg` precisa estar no caminho correto conforme especificado na variável `FFMPEG_PATH`.
- Testado e funcionando perfeitamente em ambientes locais e Docker.

---

## 📄 Licença

Este projeto é de uso livre, mantenha os créditos e contribua caso deseje adicionar novos recursos.


### 🎧 Testar as bibliotecas diretamente pelo terminal

#### 🔽 Baixar e converter um vídeo do YouTube para MP3:

```bash
yt-dlp -x --audio-format mp3 --ffmpeg-location "C:/projetos/bootdiscord/ffmpeg-2025-04-17-git-7684243fbe-full_build/bin" "<URL-DO-YOUTUBE>"
```

> 📌 Substitua `<URL-DO-YOUTUBE>` pelo link do vídeo que você deseja baixar.

#### ▶️ Tocar o arquivo `teste.mp3` via terminal com FFplay:

```bash
ffplay -nodisp -autoexit "teste.mp3"
```

> Certifique-se de que o `teste.mp3` esteja na raiz do projeto e que o `ffplay` esteja no seu PATH ou indique o caminho completo para ele.

## 🗂️ Estrutura Esperada da Pasta do FFmpeg

Certifique-se de extrair corretamente os arquivos `.part01`, `.part02`, `.part03` do pacote do FFmpeg, e organizar a estrutura como abaixo:

```
ffmpeg-2025-04-17-git-7684243fbe-full_build
├───bin
│   ├── ffmpeg.exe
│   ├── ffplay.exe
│   └── ffprobe.exe
├───doc
└───presets
```

Para testar se os programas estão funcionando, execute os seguintes comandos no terminal:

```bash
ffmpeg -version
ffplay -version
ffprobe -version
```

> ✅ Se aparecerem informações sobre cada programa, está tudo funcionando corretamente!

---

## 🔧 Como adicionar FFmpeg ao PATH (opcional)

Se quiser executar `ffmpeg`, `ffplay` e `ffprobe` de qualquer lugar no terminal, siga estes passos:

### 🪟 Windows:

1.1 Copie o caminho completo da pasta `bin`, por exemplo:

```
C:\projetos\bootdiscord\ffmpeg-2025-04-17-git-7684243fbe-full_build\bin
```

1.2 Vá em:
   - Painel de Controle → Sistema e Segurança → Sistema
   - Clique em **"Configurações avançadas do sistema"**
   - Clique em **"Variáveis de Ambiente"**
   - Em "Variáveis do sistema", localize **Path**, clique em **Editar**
   - Clique em **Novo** e cole o caminho

1.3. Clique em OK em todas as janelas e reinicie o terminal.

---

## 📦 Local dos arquivos FFmpeg fracionados

Na raiz do projeto tem as partes `.part01`, `.part02`, `.part03` a partir dos seguintes links:

- [ffmpeg-2025-part01](sandbox:/mnt/data/ffmpeg-2025-04-17-git-7684243fbe-full_build.part01)
- [ffmpeg-2025-part02](sandbox:/mnt/data/ffmpeg-2025-04-17-git-7684243fbe-full_build.part02)
- [ffmpeg-2025-part03](sandbox:/mnt/data/ffmpeg-2025-04-17-git-7684243fbe-full_build.part03)

User o Winrar ou 7zip para decompactar e coloque o conteudo descompactado na pasta:

- ffmpeg-2025-04-17-git-7684243fbe-full_build

```
ffmpeg-2025-04-17-git-7684243fbe-full_build
├───bin
│   ├── ffmpeg.exe
│   ├── ffplay.exe
│   └── ffprobe.exe
├───doc
└───presets
```


4. **Adicione um arquivo `.env` com seu token do bot**:

```env
DISCORD_TOKEN=SEU_TOKEN_AQUI
FFMPEG_PATH=C:/caminho/para/ffmpeg.exe
```

5. **Execute o bot**:

```bash
python main.py
```
---


## 🐧 Instalação Local (Linux)

1. **Clone o projeto**:

```bash
git clone https://github.com/seu-usuario/discord-music-bot.git
cd discord-music-bot
```

2. **Crie o ambiente virtual**:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale o FFmpeg**:

```bash
sudo apt update && sudo apt install ffmpeg
```

4. **Instale as dependências**:

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

5. **Configure o `.env`**:

```env
DISCORD_TOKEN=SEU_TOKEN_AQUI
FFMPEG_PATH=/usr/bin/ffmpeg
```

6. **Execute**:

```bash
python main.py
```

---

## 🐳 Rodando com Docker

1. **Crie o `.env`** (mesmo formato acima)

2. **Construa e rode com Docker Compose**:

```bash
docker-compose up --build
```

> O container cuidará do ambiente e instalará tudo automaticamente.

---

## 🎮 Comandos Disponíveis

| Comando           | Ação                                                   |
|------------------|--------------------------------------------------------|
| `__play <nome>`  | Pesquisa e toca uma música do YouTube                  |
| `__pause`        | Pausa a música atual                                   |
| `__resume`       | Continua a música pausada                              |
| `__stop`         | Para a música e limpa a fila                           |
| `__queue` ou `__list` | Mostra a fila de músicas                        |
| `__next`         | Pula para a próxima música                             |
| `__next <número>`| Pula para a música específica na fila                  |
| `__testlocal`    | Toca `teste.mp3` no canal de voz                       |
| `__testlocalpc`  | Toca `teste.mp3` localmente (no seu computador)        |
| `__help`         | Mostra todos os comandos disponíveis                   |

---

## 🚀 Como Usar

1. Convide o bot para seu servidor com permissões de:
   - Conectar a canais de voz
   - Falar em canais de voz
   - Ler mensagens
   - Usar comandos de aplicação

2. Entre em um canal de voz.

3. Use os comandos diretamente no canal de texto onde o bot está ativado:

```bash
__play Ramones - Pet Semetary
__pause
__resume
__stop
__queue
__next
```

---


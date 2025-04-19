import discord
from discord.ext import commands
import asyncio
import os
from yt_dlp import YoutubeDL

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = None
        self.queue = []
        self.current_index = 0

        self.YDL_OPTIONS = {'format': 'bestaudio'}
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

    def search_yt(self, query):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
                return {'title': info['title'], 'source': info['url']}
            except Exception as e:
                print(f"[Erro na busca]: {e}")
                return None

    async def connect_to_voice(self, ctx):
        if not ctx.author.voice:
            await ctx.send("⚠️ Você precisa estar em um canal de voz.")
            return False
        channel = ctx.author.voice.channel
        if self.vc is None:
            self.vc = await channel.connect()
        elif self.vc.channel != channel:
            await self.vc.move_to(channel)
        return True

    async def play_next(self, ctx=None):
        if self.current_index < len(self.queue):
            song = self.queue[self.current_index]
            source = discord.FFmpegPCMAudio(song['source'], **self.FFMPEG_OPTIONS)
            self.vc.play(
                source,
                after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.bot.loop)
            )
            if ctx:
                await ctx.send(f"▶️ Tocando agora: **{song['title']}**")
            self.current_index += 1
        else:
            if ctx:
                await ctx.send("📭 Fila finalizada.")

    @commands.command()
    async def play(self, ctx, *, query):
        song = self.search_yt(query)
        if not song:
            await ctx.send("❌ Não consegui encontrar a música.")
            return

        self.queue.append(song)
        await ctx.send(f"🎶 Adicionada à fila: **{song['title']}**")

        if not self.vc or not self.vc.is_playing():
            if await self.connect_to_voice(ctx):
                await self.play_next(ctx)

    @commands.command()
    async def pause(self, ctx):
        if self.vc and self.vc.is_playing():
            self.vc.pause()
            await ctx.send("⏸️ Música pausada.")

    @commands.command()
    async def stop(self, ctx):
        if self.vc and self.vc.is_playing():
            self.vc.stop()
            await ctx.send("⏹️ Reprodução parada.")

    @commands.command(name="list")
    async def list_queue(self, ctx):
        if not self.queue:
            await ctx.send("📭 Fila vazia.")
            return

        msg = "**🎵 Fila de músicas:**\n"
        for i, song in enumerate(self.queue):
            pointer = "➡️" if i == self.current_index else "   "
            msg += f"{pointer} `{i+1}.` {song['title']}\n"
        await ctx.send(msg)

    @commands.command()
    async def next(self, ctx, index: int = None):
        if index is not None:
            if 1 <= index <= len(self.queue):
                self.current_index = index - 1
                await ctx.send(f"⏭️ Pulando para a música #{index}: **{self.queue[self.current_index]['title']}**")
            else:
                await ctx.send("❌ Índice inválido na fila.")
                return
        else:
            await ctx.send("⏭️ Pulando para a próxima música.")

        if self.vc and self.vc.is_playing():
            self.vc.stop()
        else:
            await self.play_next(ctx)

    @commands.command()
    async def testlocal(self, ctx):
        if not ctx.author.voice:
            await ctx.send("⚠️ Você precisa estar em um canal de voz.")
            return

        voice_channel = ctx.author.voice.channel
        try:
            if self.vc is None or not self.vc.is_connected():
                print("🔌 Conectando ao canal de voz...")
                self.vc = await voice_channel.connect()
            elif self.vc.channel != voice_channel:
                print("🔁 Movendo para o canal do autor...")
                await self.vc.move_to(voice_channel)
        except Exception as e:
            print(f"[Erro ao conectar ou mover]: {e}")
            await ctx.send(f"[Erro ao conectar ou mover]: {e}")
            return

        mp3_path = "teste.mp3"
        if not os.path.exists(mp3_path):
            await ctx.send(f"❌ Arquivo `{mp3_path}` não encontrado.")
            return

        try:
            if self.vc.is_playing():
                self.vc.stop()
            source = discord.FFmpegPCMAudio(mp3_path)
            self.vc.play(source)
            await ctx.send("▶️ Tocando `teste.mp3` no canal de voz.")
        except Exception as e:
            print(f"[Erro ao tocar]: {e}")
            await ctx.send(f"❌ Erro ao tentar tocar: {e}")

    @commands.command()
    async def testlocalpc(self, ctx):
        os.system('start "" "ffplay" -nodisp -autoexit "teste.mp3"')
        await ctx.send("▶️ Tocando `teste.mp3` no seu PC local (ffplay).")

async def setup(bot):
    await bot.add_cog(Music(bot))

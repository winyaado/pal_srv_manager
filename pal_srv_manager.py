# import

import discord
from discord.ext import commands

import pal_config

class MyBot(commands.Bot):

    def __init__(self, command_prefix):

        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix=command_prefix,
            activity=discord.Game(name=f"パル鯖缶 Vr.{pal_config.Version}"
        ))


    async def on_ready(self):
        # Cogをpropartyのリストからロード
        for cog in pal_config.cog_list:
            try:
                await self.load_extension(cog)
                print(f'Success: Cog loaded ({cog})')
            except Exception as e:
                print(e)
                raise e
        print('----------------')
        print(self.user.name)
        print(self.user.id)
        print('----------------')

if __name__ == '__main__':
    bot = MyBot(command_prefix='/')
    bot.run(pal_config.Discord_Key)
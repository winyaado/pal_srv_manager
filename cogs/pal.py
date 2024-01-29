import pal_config
import pal_msg

from discord.ext import commands
import discord

import subprocess
import psutil


def setup(bot):
    return bot.add_cog(pal_srv_manager(bot))

class pal_srv_manager(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.group(name='pal')
	async def test(self,ctx,cmd):
		# ヘルプ
		if (cmd == 'help'):
			await ctx.reply(f'{pal_msg.helpmsg}')
		# サーバー開始
		if (cmd == 'start'):
			if server_boot_flag():
				await ctx.reply(f'{pal_msg.bootng}')
			else:
				try:
					subprocess.Popen(f'{pal_config.server} {pal_config.serverconfig}')
					await ctx.reply(f'{pal_msg.bootok}')
				except Exception as e:
					await ctx.reply(f'{pal_msg.start_err_e}{e}')
		# サーバー停止
		if (cmd == 'stop'):
			subprocess.Popen(f'taskkill /IM {pal_config.serverexe} /F /T')
			await ctx.reply(f'{pal_msg.stopserver}')
		# サーバーアップデート
		if (cmd == 'update'):
			if server_boot_flag():
				await ctx.reply(f'{pal_msg.update_err_bootserver}')
			else:
				await ctx.reply(f'{pal_msg.update_start}')
				try:
					subprocess.run(f'{pal_config.steamcmd} {pal_config.serverupdatecmd}')
					await ctx.reply(f'{pal_msg.update_end}')
				except Exception as e:
					await ctx.reply(f'{pal_msg.update_err_e}{e}')
def server_boot_flag():
	for process in psutil.process_iter(['name']):
		if process.info['name'] == pal_config.serverexe:
			return True
	return False
	

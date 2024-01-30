import pal_config
import pal_msg

from discord.ext import commands
from discord.ext import tasks
import discord

import subprocess
import psutil

from mcrcon import MCRcon

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
			if server_boot_flag():
				try:
					with MCRcon(pal_config.rcon_ip, pal_config.rcon_passwd, pal_config.rcon_port) as mcr:
						resp = mcr.command(f'Shutdown {pal_config.stoptime} {pal_msg.stopmsg}')
						print(resp)
						await ctx.reply(f'{pal_msg.stopserver}')
				except Exception as e:
					await ctx.reply(f'{pal_msg.stop_err_e}{e}')
					
		# サーバー強制停止
		if (cmd == 'kill'):
			try:
				subprocess.Popen(f'taskkill /IM {pal_config.serverexe} /F /T')
				await ctx.reply(f'{pal_msg.killserver}')
			except Exception as e:
				await ctx.reply(f'{pal_msg.kill_err_e}{e}')	
				
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
		
		# サーバーセーブ
		if (cmd == 'save'):
			try:
				with MCRcon(pal_config.rcon_ip, pal_config.rcon_passwd, pal_config.rcon_port) as mcr:
					resp = mcr.command(f'Save')
					print(resp)
				await ctx.reply(f'{pal_msg.save}')
			except Exception as e:
				await ctx.reply(f'{pal_msg.save_err_e}{e}')
			
		# サーバースタータスの表示
		if (cmd == 'info'):
			try:
				with MCRcon(pal_config.rcon_ip, pal_config.rcon_passwd, pal_config.rcon_port) as mcr:
					resp = mcr.command(f'Info')
					print(resp)
				await ctx.reply(f'{pal_msg.info}{resp}')
			except Exception as e:
				await ctx.reply(f'{pal_msg.info_err_e}{e}')

		# サーバー情報表示モード
		if (cmd == 'activity'):
			try:
				if not activity_update.is_running():
					activity_update.start(self.bot)
					await ctx.reply(f'{pal_msg.activity_start}')
				else:
					activity_update.stop()
					activity = discord.Game(f'{pal_msg.activity_def}')
					await self.bot.change_presence(activity=activity)
					await ctx.reply(f'{pal_msg.activity_stop}')
			except Exception as e:
				await ctx.reply(f'{pal_msg.activity_err_e}{e}')
				
@tasks.loop(seconds=pal_config.activity_update_time)
async def activity_update(bot):
	if server_boot_flag():
		activity = discord.Game(f'パル鯖 Pyr:{server_player()}  Mem:{server_mem_use():.2f}GB') #サーバー情報表示モード　表示項目
	else:
		activity = discord.Game(f'パル鯖 停止中')
	await bot.change_presence(activity=activity)

def server_mem_use():
	pid = 0
	mem = 0
	for process in psutil.process_iter(['name','pid']):
		if process.info['name'] == pal_config.serverexe:
			pid = process.info['pid']
	if (pid != 0):
		palsrv = psutil.Process(pid)
		for process in palsrv.children():
			mem += process.memory_info().rss
	return mem/1024**3

def server_player():
	with MCRcon(pal_config.rcon_ip, pal_config.rcon_passwd, pal_config.rcon_port) as mcr:
		resp = mcr.command(f'ShowPlayers')
	return resp.count('\n')-1

def server_boot_flag():
	for process in psutil.process_iter(['name']):
		if process.info['name'] == pal_config.serverexe:
			return True
	return False
	

	

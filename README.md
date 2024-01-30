# pal_srv_manager
win版palserver 管理用DiscodeBot

# セットアップ
PalWorldSettings.ini 下記設定を追加する  
RCONEnabled=True\n  
adminPassword="任意のパスワード"\n  

pal_config.py 下記項目をサーバーに合わせて書き換える  
Discord_Key #DiscodeBotのトークン  
steamcmd #steamcmdのexe  
serverupdatecmd #palserverアップデート時のコマンド  
server #palserverの実行ファイル  
serverexe #palserverの実行ファイル名  
serverconfig #palserver実行時の引数  
stoptime #サーバー停止時の待機時間(s)  
activity_update_time #アクティビティ領域の更新頻度(s)   
rcon_port #rconポート  
rcon_passwd #PalWorldSettings adminPassword  

上記設定後にpal_srv_manager.pyを実行

# 使い方  
pal 引数  
/pal start :palサーバーを開始します  
/pal stop :{pal_config.py:stoptime}秒後にpalサーバーを通常停止します  
/pal kill :palサーバーを強制停止します  
セーブは行われないのでフリーズした際に利用してください  
/pal save :palサーバーのセーブを実行します  
/pal update :palサーバーの更新を行います  
/pal activity :botのアクティビティ領域での情報表示を切り替えます'

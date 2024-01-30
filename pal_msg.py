import pal_config

helpmsg = f'pal鯖缶ヘルプ\n/pal 引数\n\nstart :palサーバーを開始します\n\nstop :{pal_config.stoptime}秒後にpalサーバーを通常停止します\n\nkill :palサーバーを強制停止します\nセーブは行われないのでフリーズした際に利用してください\n\nsave :palサーバーのセーブを実行します\n\nupdate :palサーバーの更新を行います\n\nactivity :botのアクティビティ領域での情報表示を切り替えます'

bootng = 'palサーバーの起動に失敗しました\nすでにサーバーが起動されています'
bootok = 'palサーバーを起動しました'

stopserver = f'palサーバーへ{pal_config.stoptime}秒後の終了命令を送信しました'
stopmsg = f'Server_shutdown_will_occur_after_{pal_config.stoptime}_seconds' #スペース以降の文字はサーバーメッセージへ送信されない

killserver = 'palサーバーを強制終了しました'

save = 'セーブを実行しました'

info = '現在のサーバー情報\n'

update_err_bootserver = 'palサーバーが起動中のため\nアップデートに失敗しました'
update_start = 'palサーバーのアップデートを開始します'
update_end = 'palサーバーのアップデートが完了しました'

activity_start = 'サーバー情報表示モードへ切り替えました'
activity_stop = 'サーバー情報非表示モードへ切り替えました'
activity_def = f"パル鯖缶 Vr.{pal_config.Version}"

start_err_e = 'palサーバー開始時エラーが発生しました\n'
stop_err_e = 'palサーバー終了時エラーが発生しました\n'
update_err_e = 'アップデートエラーが発生しました\n'
kill_err_e = 'palサーバー強制終了時エラーが発生しました\n'
activity_err_e = 'botアクティビティ変更時にエラーが発生しました\n'
save_err_e = 'セーブ時にエラーが発生しました\n'
info_err_e = 'サーバー情報表示時にエラーが発生しました\n'
import keyboard
import socket

stop = False
def on_key_event(event):
	print(f"Key {event.name} was pressed")
	global stop
	stop = True
def tcp_client(host, port, message):
	# ソケットを作成
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# サーバーに接続
	client_socket.connect((host, port))
	try:

		while True:
			
			# メッセージを送信
			# client_socket.sendall(message.encode('utf-8'))

			# サーバーからのレスポンスを受信
			data = client_socket.recv(1024)
			print(f"Received from server: {data.decode('utf-8')}")
			if stop:
				break
	except Exception as e:
		print(f"Error: {e}")
	client_socket.close()

if __name__ == "__main__":
	# 接続先のホストとポートを指定
	server_host = "192.168.5.3"  # 例: サーバーがローカルホスト上で実行されている場合
	server_port = 4001         # 例: サーバーが使用するポート

	# 送信するメッセージを指定
	buf = "012345678 "
	message_to_send = ""
	for i in range(100):
		message_to_send += buf
	keyboard.on_press_key('a', on_key_event)
	# TCPクライアントを実行
	tcp_client(server_host, server_port, message_to_send)

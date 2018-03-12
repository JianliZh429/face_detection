import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

open_relay_array = [
    [0xFE, 0x05, 0x00, 0x00, 0xFF, 0x00, 0x98, 0x35],
    [0xFE, 0x05, 0x00, 0x01, 0xFF, 0x00, 0xC9, 0xF5]
]
close_relay_array = [
    [0xFE, 0x05, 0x00, 0x00, 0x00, 0x00, 0xD9, 0xC5],
    [0xFE, 0x05, 0x00, 0x01, 0x00, 0x00, 0x88, 0x05]
]

sock.connect(('192.168.1.232', 10000))


def switcher(signal=True):
    print('send modbus data')
    if signal:
        send_modbus_data = bytes(open_relay_array[0])
    else:
        send_modbus_data = bytes(close_relay_array[0])
    sock.sendall(send_modbus_data)
    data = sock.recv(2048)
    return data == send_modbus_data


def close_connection():
    sock.close()

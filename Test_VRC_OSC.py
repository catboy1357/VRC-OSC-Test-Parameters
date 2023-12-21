# requires the python-osc library. If you need to install the modual use:
# "pip install python-osc"
# You can find the values in:
# "~\AppData\LocalLow\VRChat\VRChat\OSC\{userId}\Avatars\{avatarId}.json"
from pythonosc.udp_client import SimpleUDPClient


def get_user_input():
    address = input('Parameter Name:  ')
    data_type = input('Type: 1 int, 2 bool, 3 float:  ')
    value = input('Value Number:  ')
    return address, data_type, value


def parse_data(data_type, value):
    if data_type == '1':
        return int(value)
    elif data_type == '2':
        return bool(int(value))
    elif data_type == '3':
        return float(value)


def send_data(client, path, data):
    print(f'Sent {data} to /avatar/parameters/{path}: {data}')
    client.send_message(f'/avatar/parameters/{path}', data)
    print('\n', '----------------------------', '\n')


def main():
    client = SimpleUDPClient("127.0.0.1", 9000)  # Default VRChat ip & port

    print('Input path, type, and value.')
    print('Parameter names are case sensitive')
    print('Use ctrl + C to exit', '\n')

    while True:
        address, data_type, value = get_user_input()
        data = parse_data(data_type, value)
        send_data(client, address, data)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n', "Exit")

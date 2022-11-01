# requires the python-osc library. If you need to install the modual use:
# "pip install python-osc"
# You can find the values in:
# "~\AppData\LocalLow\VRChat\VRChat\OSC\{userId}\Avatars\{avatarId}.json"
from pythonosc.udp_client import SimpleUDPClient


def main():
    # setup
    ip = "127.0.0.1"
    port = 9000
    client = SimpleUDPClient(ip, port)

    path_ = None
    data_ = None
    data = [None]*3

    # info
    print('Input path, type, and vale.')
    print('Use ctrl + C to exit', '\n')

    # loop
    while True:
        # get info from user
        data[0] = input('Address: string: \n')
        data[1] = input('Type: 1 int, 2 bool, 3 float: \n')
        data[2] = input('value: Num or bool: 1 or 0: \n')

        # parse data
        path_ = data[0]
        if data[1] == '1':
            data_ = int(data[2])
        if data[1] == '2':
            if data[2] == '1':
                data_ = True
            else:
                data_ = False
        if data[1] == '3':
            data_ = float(data[2])

        # sends the data
        print(f'sending /avatar/parameters/{path_} : {data_}')
        client.send_message(f'/avatar/parameters/{str(path_)}', data_)
        print('\n', '----------------------------', '\n')


if __name__ == '__main__':
    main()

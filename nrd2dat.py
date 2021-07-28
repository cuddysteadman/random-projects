import struct

import numpy as np


def process_packet(packet):
    num_values = len(packet)
    crc = 0
    for i in range(int(len(packet) / 4)):
        crc ^= struct.unpack('i', packet[num_values - 4:])[0]
    if crc != 0:
        print("Invalid packet.")
        return
    num_channels = int((num_values - 18 * 4) / 4)
    data_packet = packet[17 * 4:17 * 4 + num_channels * 4]
    data = np.fromstring(data_packet, dtype=np.int32)
    data = data.astype(np.int16)
    return data.tobytes()


def nrd2dat(file_loc, num_channels, new_name): # screen
    new_name += ".dat"
    old_file = open(file_loc, mode='rb')
    nrs_data = old_file.read()
    nrs_data = nrs_data[16384:]
    old_file.close()
    packet_size = num_channels * 4 + 18 * 4
    num_samples = int(len(nrs_data) / packet_size)
    new_file = file_loc[:file_loc.rindex("/") + 1] + new_name
    data = open(new_file, mode='wb')
    # progress_bar = screen['progress']
    # percent = 0.0
    # progress_bar.update_bar(percent)
    for i in range(num_samples):
        # process the packet at index i
        data.write(process_packet(nrs_data[i * packet_size:packet_size * (i + 1)]))
        # if i % int(num_samples / 50) == 0 and i != 0:
            # percent += 0.2
            # progress_bar.update_bar(percent)
    # progress_bar.update_bar(10)
    data.close()


if __name__ == "__main__":
    # sample 10-second dataset
    dat_loc = "/home/wufan/Downloads/10sec.nrd"
    nrd2dat(dat_loc, 32, "10secPy")
    old_file_dat = open("/home/wufan/Downloads/10sec.dat", mode='rb')
    old_data = old_file_dat.read()
    new_file_dat = open("/home/wufan/Downloads/10secPy.dat", mode='rb')
    new_data = new_file_dat.read()
    if old_data == new_data:
        print("Everything went well!")
    else:
        print("Something went wrong. :(")


    # with PythonSimpleGUI
    """
    import PySimpleGUI as sg
    sg.theme('BluePurple')
    layout = [[sg.Text('Welcome to NRD 2 DAT!')],
              [sg.Text('Choose a file to convert: '), sg.Input(key='-IN-'), sg.FileBrowse()],
              [sg.Text('Channel count: '), sg.Input(key='-IN-2-')],
              [sg.Text('New name for your file: '), sg.Input(key='-IN-3-')],
              [sg.Button('Convert'), sg.Button('Exit')],
              [sg.ProgressBar(max_value=10, orientation='h', size=(20, 20), key='progress'), sg.Text("Complete!", visible=False, key='complete')]]

    window = sg.Window('Introduction', layout, size=(1920, 1080))
    while True:
        event, values = window.read()
        if event is 'Exit' or event == sg.WIN_CLOSED:
            break
        if event is 'Browse File':
            sg.FileBrowse()
        if event is 'Convert':
            nrd2dat(str(values['-IN-']), int(str(values['-IN-2-'])), str(values['-IN-3-']), window)
            window['complete'].Update(visible=True)
    window.close()
    """
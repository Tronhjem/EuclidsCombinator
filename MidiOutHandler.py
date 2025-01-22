import time
# import rtmidi

# def MidiExample():
#     midiout = rtmidi.MidiOut()
#     available_ports = midiout.get_ports()
#
#     print(available_ports)
#
#     if available_ports:
#         midiout.open_port(1)
#     else:
#         midiout.open_virtual_port("My virtual output")
#
#     with midiout:
#         note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
#         note_off = [0x80, 60, 0]
#         midiout.send_message(note_on)
#         time.sleep(0.5)
#         midiout.send_message(note_off)
#         time.sleep(0.1)
#
#     del midiout


class MidiOutHandler:
    def __init__(self):
        pass
        # self.midiout = rtmidi.MidiOut()
        # self.available_ports = self.midiout.get_ports()
        #
        # if self.available_ports:
        #     self.midiout.open_port(1) #hardcoded for now to max input
        # else:
        #     self.midiout.open_virtual_port("My virtual output")

    def noteout(self, note, velocity):
        pass
        # note_on = [0x90, note, velocity] # channel 1, middle C, velocity 112
        note_off = [0x80, 60, 0]
        # self.midiout.send_message(note_on)

import rtmidi

class MidiOutHandler:
    def __init__(self):
        self._midiout = rtmidi.MidiOut()
        self._available_ports = self._midiout.get_ports()
    
    def get_ports(self):
        return self._available_ports
        
    def set_port(self, port):
        if self._available_ports:
            self._midiout.open_port(port) 
        else:
            self._midiout.open_virtual_port("My virtual output")

    def noteout(self, note, velocity):
        note_on = [0x90, note, velocity] # channel 1, middle C, velocity 112
        # note_off = [0x80, 60, 0]
        self._midiout.send_message(note_on)

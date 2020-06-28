# Midi Interface by Andrew Li

A Python interface for [MIDIUtil](https://pypi.org/project/MIDIUtil/)



Install with 

```shell
python setup.py install
```

+

You need MIDIUtil, so

```shell
pip install MIDIUtil
```



## Tests

To run a test, use the following command
```shell
py .\tests\test_1.py
```


## Use

To use, import with 

```python
from Midi_interface.Midi import Midi
```



Functions you can use

```python

def set_tempo(self, tempo, time = 0):
    ''' sets tempo of track at a given time given the time and the tempo, defaults to start of track '''
    
def set_track(self, track):
    ''' given new track (int) switch to that track '''
    
def set_instrument(self, instrument_number):
    ''' set the instrument of current track; use this website to find your instrument: https://www.midi.org/specifications/item/gm-level-1-sound-set '''
  
def notes_to_midi(self, string_notes):
    '''
    converts list of notes ie [G3, Ab5, f#2] (supports octives 0 to 9 inclusive)
    to notes interperated by this midi class
    '''
        
def push_notes(self, new_notes, duration):
    ''' 
    given list of note pitch and duraction, push to notes and duraction attribute
    (new note pitch can be a list or a single note, same with duration)
    '''
        
def encode_track(self):
    ''' encodes the entirety of a single track '''

def output_mid(self, name):
    '''
    given mid output name (.mid extension not needed),
    the .mid extension will be added
    *Note if the mid file of the same name already exists, it will be OVERWRITTEN
    '''
```



\* Note, look at the tests if you need examples of how to implement things




## Requires

* [midiutil](https://pypi.org/project/MIDIUtil/)

But will install if you don't have it




## License

MIT

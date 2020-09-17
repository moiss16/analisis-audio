import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave
import thinkplot

waveTelefono = read_wave("telefono.wav")
waveTelefono.plot()
decorate(xlabel="Tiempo (s)")


espectro = waveTelefono.make_spectrum()
espectro.plot()
decorate(xlabel="Hz")


thinkplot.show()
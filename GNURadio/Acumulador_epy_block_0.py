"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Acum',  # Comillas rectas corregidas
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # Variable de estado para guardar el valor acumulado del bloque anterior
        self.last_val = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]       # Señal de entrada
        y0 = output_items[0]     # Señal acumulada de salida
        
        if len(x) > 0:
            # Calculamos la cumsum del bloque actual y le sumamos el arrastre del bloque anterior
            y0[:] = np.cumsum(x) + self.last_val
            # Actualizamos el estado con el último valor de este bloque para el siguiente
            self.last_val = y0[-1]
            
        return len(y0)  # Corregido de 'y' a 'y0' (o len(output_items[0]))

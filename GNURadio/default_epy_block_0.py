import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Diferenciador',  # Nombre que aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # Memoria para guardar la última muestra del bloque anterior
        self.x_anterior = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]     # Señal de entrada
        y0 = output_items[0]   # Señal de salida diferenciada
        
        if len(x) == 0:
            return 0
            
        # Para calcular la diferencia considerando la transición entre buffers:
        # 1. Unimos el último valor procesado antes con el vector actual de entrada
        x_extended = np.insert(x, 0, self.x_anterior)
        
        # 2. Calculamos la diferencia entre elementos consecutivos (np.diff)
        diff = np.diff(x_extended)
        
        # 3. Actualizamos la memoria con la última muestra de este bloque
        self.x_anterior = x[-1]
        
        # Escribimos el resultado en el buffer de salida
        y0[:] = diff
        
        return len(x)

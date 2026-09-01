import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Diferenciador',  
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        
        self.x_anterior = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]     
        y0 = output_items[0]   
        
        if len(x) == 0:
            return 0
            
        x_extended = np.insert(x, 0, self.x_anterior)
        
        diff = np.diff(x_extended)
        
        self.x_anterior = x[-1]
        
        y0[:] = diff
        
        return len(x)

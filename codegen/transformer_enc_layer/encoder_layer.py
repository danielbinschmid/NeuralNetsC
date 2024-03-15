from python.encoder_layer import TransformerEncoderLayer

DIM_FEEDFORWARD=256
D_MODEL = 64
N_HEAD = 4

encoder_layer = TransformerEncoderLayer(
    d_model=D_MODEL,  
    nhead=N_HEAD, 
    dim_feedforward=DIM_FEEDFORWARD, 
    batch_first=True)

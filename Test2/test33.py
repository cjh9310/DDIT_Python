import gc
import torch
from tensorflow.python.keras.saving.save import load_model
from model import Generator


device = 'cuda'  # @param ['cuda', 'cpu']

generator1 = Generator(256, 512, 8, channel_multiplier=2).eval().to(device)
generator2 = Generator(256, 512, 8, channel_multiplier=2).to(device).eval()


gc.collect()
torch.cuda.empty_cache()

mean_latent1 = load_model(generator1, 'D:/workspace_python/Test2/inversion_codes/01.pt')

print(len(mean_latent1))

print(mean_latent1[0].shape)
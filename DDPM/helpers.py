"""Helper functions for the DDPM"""

import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# Helper function to convert float tensor [0, 1] back to displayable image
def tensor_to_image(tensor):
    return (torch.clamp(tensor, 0, 1) * 255).byte().numpy()

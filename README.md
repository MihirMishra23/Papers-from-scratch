Here, I implement various machine learning models from scratch to improve my understanding of them.

## Papers Implemented

### Transformers
**Paper:** "Attention Is All You Need" by Vaswani et al. (2017)

Built an English to Italian translator following tutorial by Umar Jamil: https://www.youtube.com/watch?v=ISNdQcPhsts

Implementation includes the full transformer architecture with multi-head attention, positional encoding, and encoder-decoder structure.

### Binoculars
**Paper:** "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" by Hans et al. (2024)

Implementation of the Binoculars method for detecting AI-generated text using cross-perplexity between two language models. This zero-shot detection method compares perplexity scores to distinguish between human-written and machine-generated content.

### DDPM (Denoising Diffusion Probabilistic Models)
**Paper:** "Denoising Diffusion Probabilistic Models" by Ho et al. (2020)

https://andrewkchan.dev/posts/diffusion.html has an amazing guide on the intuition and math behind diffusion models.

Implementation of Diffusion models to generate an image of Hornet from Silksong. Utilizes an MLP denoising model (eventually replaced with a UNet).

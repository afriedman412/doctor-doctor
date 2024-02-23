from matplotlib import pyplot as plt

from setup import analyzer

path = "cary_testo.pdf"

df = analyzer.analyze(path=path)
df.reset_state()
dp = next(iter(df))

np_image = dp.viz()

plt.figure(figsize=(25, 17))
plt.axis('off')
plt.imshow(np_image)

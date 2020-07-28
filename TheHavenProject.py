import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import math
import random
from pathlib import Path
import imageio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

print("By JUKjacker")

choice = input("Type 2 for 2d, anything else will result in 3d, who cares, just type some stuff: ")
if choice == "2":
    n = random.randint(1, 400)
    u = random.randint(1, 15)

    id = random.randint(1000, 1747)

    frames = input("How many frames: ")
    for a in range(1, int(frames)):
        try:
            b = a/math.pow(math.pow(a, 2) + 1, 0.5)
            print(b)
            x = np.linspace(math.pow(u**2/b, 0.5), b/4*(u**2), n)
            y = np.linspace(math.pow(u**2/b, 0.5), b/4*(u**2), n)
            X, Y = np.meshgrid(x, y)

            Z = X * np.sinc(X ** 2 + Y ** 2)

            plt.pcolormesh(X, Y, Z, cmap="inferno")
            plt.savefig(str(a) + "ID" + str(id) + ".png", dpi=300, bbox_inches='tight')
        except Exception:
            print("gig")

    image_path = Path('C:/Users/Lenon/PycharmProjects/TheHavenProject')
    images = list(image_path.glob('*.png'))
    image_list = []
    for a in range(1, int(frames)):
        image_list.append(imageio.imread(str(a) + "ID" + str(id) + ".png"))
    imageio.mimwrite('Animated2D_Heaven_ID' + str(id) + "_.gif", image_list)
if choice != "2":
    n = random.randint(1, 400)
    u = random.randint(1, 15)
    id = random.randint(1000, 1747)
    frames = input("how many frames bro: ")
    increment = input("an increment bro pls, could be negative: ")
    increment2 = input("another increment bro pls, just positive this time: ")
    for a in range(1, int(frames)):
        new_a = a + int(increment)
        b = new_a / math.pow(math.pow(new_a, 2) + 1, 0.5) + int(increment2)
        x = np.linspace(math.pow(u**2/b, 0.5), b/4*(u**2), n)
        y = np.linspace((math.pow(u, 0.5)*b)**2, b*(4/(math.pow(u, 0.5))))
        X, Y = np.meshgrid(x, y)
        Z = np.sinc(np.sqrt(X ** 2 + Y ** 2))

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(X, Y, Z, cmap="plasma")

        plt.savefig("ID_" + str(id) + "_" + str(a) + ".png", dpi=300, bbox_inches='tight')
        image_path = Path('C:/Users/Lenon/PycharmProjects/TheHavenProject')
        plt.close()
    image_list = []
    for a in range(1, int(frames)):
        image_list.append(imageio.imread("ID_" + str(id) + "_" + str(a) + ".png"))
    imageio.mimwrite('Animated3D_Heaven_ID' + str(id) + "_.gif", image_list)


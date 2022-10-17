import matplotlib.pyplot as plt
import numpy as np


thetas = np.array([-0.28, 9.72, 19.72, 29.72, 39.72, 49.72, 59.72, 69.72, 79.72, 89.72, 99.72, 109.72, 119.72])
Ns = np.array([900, 1011, 819, 779, 702, 621, 553, 470, 437, 378, 346, 313, 298])
N_errors = np.sqrt(0.0001 * Ns * Ns + 1)

one_minus_cos = 1 - np.cos(thetas * np.pi / 180)
one_over_N = 1 / Ns

one_over_N_errors = N_errors / Ns / Ns


def main():
    ### one_over_N = m * one_minus_cos + b
    ### With chi^2 calculated:
    m = 0.00155664
    b = 0.00106738

    x = np.arange(0, 1.5, 0.001)
    y = m * x + b

    plt.figure(figsize=(12, 8))
    plt.plot(x, y * 10000, color='red', lw=2.5)
    plt.errorbar(one_minus_cos, one_over_N * 10000, yerr=one_over_N_errors, color='black', fmt='.', markersize=9)

    plt.xlabel(r"$1 - \cos \theta$", fontsize=24)
    plt.ylabel(r"$\dfrac{1}{N(\theta)} \cdot 10^{-4}$", fontsize=24)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlim([-0.01, 1.51])
    plt.ylim([-0.00003, 35])

    chi2 = 0
    for i in range(0, len(one_over_N_errors)):
        chi2 += ((one_over_N[i] - m * one_minus_cos[i] - b) ** 2) / (one_over_N_errors[i] ** 2) 

    chi2 = int(chi2)
    plt.text(0.02, 32, f"$\chi^2 = {chi2}$", size = 24, bbox=dict(facecolor='white', edgecolor='black', pad=10.0))
    
    plt.grid()
    plt.savefig("./Pictures/N(theta).pdf")
    plt.show()





if __name__ == '__main__':
    main()

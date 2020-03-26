import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as c

# Code for radial wavefunction:
a = c.physical_constants['Bohr radius'][0]


###Code:
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return round(x, 5), round(y, 5), round(z, 5)


def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x * x + y * y + z * z)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return round(r, 5), round(theta, 5), round(phi, 5)


# Test:
# assert statement will throw error if the result is wrong
# no output will be produced for correct results

### Code for angular wavefunction:
def angular_wave_func(m, l, theta, phi):
    def sqrt(v):
        return np.sqrt(v)

    def cos(v):
        return np.cos(v)

    def sin(v):
        return np.sin(v)

    def exp(v):
        return np.exp(v)

    pi = np.pi
    i = complex(0, 1)

    if l == 0 and m == 0:
        y = sqrt(1 / 4 / pi)
        return np.complex(np.round(y, 5))
    elif l == 1:
        if m == 0:
            y = sqrt(3 / 4 / pi) * cos(theta)
            return np.complex(np.round(y, 5))
        if m == 1:
            y = - sqrt(3 / 8 / pi) * sin(theta) * exp(i * phi)
            return np.complex(np.round(y, 5))
        if m == -1:
            y = sqrt(3 / 8 / pi) * sin(theta) * exp(-i * phi)
            return np.complex(np.round(y, 5))
    elif l == 2:
        if m == 0:
            y = sqrt(5 / 16 / pi) * (3 * (cos(theta)) ** 2 - 1)
            return np.complex(np.round(y, 5))
        if m == 1:
            y = - sqrt(15 / 8 / pi) * cos(theta) * sin(theta) * exp(i * phi)
            return np.complex(np.round(y, 5))
        if m == -1:
            y = sqrt(15 / 8 / pi) * cos(theta) * sin(theta) * exp(-i * phi)
            return np.complex(np.round(y, 5))
        if m == 2:
            y = sqrt(15 / 32 / pi) * (sin(theta)) ** 2 * exp(i * 2 * phi)
            return np.complex(np.round(y, 5))
        if m == -2:
            y = sqrt(15 / 32 / pi) * (sin(theta)) ** 2 * exp(-i * 2 * phi)
            return np.complex(np.round(y, 5))
    else:
        return -1


def radial_wave_func(n, l, r):
    sigma = r / a

    if l == 0:
        if n == 1:
            r_1s = 2 * (a / a) ** (1.5) * np.exp(-sigma)
            return round(r_1s, 5)
        elif n == 2:
            r_2s = 1 / 2 / np.sqrt(2) * (a / a) ** (1.5) * (2 - sigma) * np.exp(-sigma / 2)
            return round(r_2s, 5)
        elif n == 3:
            r_3s = 2 / 81 / np.sqrt(3) * (a / a) ** (1.5) * (27 - 18 * sigma + 2 * sigma ** 2) * np.exp(- sigma / 3)
            return round(r_3s, 5)
        else:
            return -1
    elif l == 1:
        if n == 2:
            r_2p = 1 / 2 / np.sqrt(6) * (a / a) ** (1.5) * sigma * np.exp(- sigma / 2)
            return round(r_2p, 5)
        elif n == 3:
            r_3p = 4 / 81 / np.sqrt(6) * (a / a) ** (1.5) * (6 * sigma - sigma ** 2) * np.exp(- sigma / 3)
            return round(r_3p, 5)
        else:
            return -1
    elif l == 2:
        if n == 3:
            r_3d = 4 / 81 / np.sqrt(30) * (a / a) ** (1.5) * sigma ** 2 * np.exp(- sigma / 3)
            return round(r_3d, 5)
        else:
            return -1
    else:
        return -1


def mgrid3d(xstart, xend, xpoints,
            ystart, yend, ypoints,
            zstart, zend, zpoints):
    xr = []
    yr = []
    zr = []
    xval = xstart
    xcount = 0

    # calculate the step size for each axis
    xstep = (xend - xstart) / (xpoints - 1)
    ystep = (yend - ystart) / (ypoints - 1)
    zstep = (zend - zstart) / (zpoints - 1)

    while xcount < xpoints:
        # initialize y points
        # create temporary variable to store x, y and z list
        yval = ystart
        ycount = 0

        xrow = []
        yrow = []
        zrow = []

        while ycount < ypoints:
            # initialize z points
            # create temporary variable to store the inner x, y, and z list
            zval = zstart
            zcount = 0

            innerxrow = []
            inneryrow = []
            innerzrow = []

            while zcount < zpoints:
                # add the points x, y, and z to the inner most list
                innerxrow.append(xval)
                inneryrow.append(yval)
                innerzrow.append(zval)

                # increase z point
                zval += zstep
                zcount += 1
            # add the inner most lists to the second lists
            xrow.append(innerxrow)
            yrow.append(inneryrow)
            zrow.append(innerzrow)

            # increase y point
            yval += ystep
            ycount += 1
        # add the second lists to the returned lists
        xr.append(xrow)
        yr.append(yrow)
        zr.append(zrow)

        # increase x point
        xval += xstep
        xcount += 1

    return [xr, yr, zr]


###Code:
def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    xr, yr, zr = mgrid3d(-roa, roa, Nx, -roa, roa, Ny, -roa, roa, Nz)
    density = []

    i = complex(0, 1)
    for h in range(Nx):
        outerrow = []
        for i in range(Ny):
            innerrow = []
            for j in range(Nz):
                xx = xr[h][i][j]
                yy = yr[h][i][j]
                zz = zr[h][i][j]

                r, theta, phi = cartesian_to_spherical(xx, yy, zz)
                Y_lm = angular_wave_func(m, l, theta, phi)
                Y_lm_neg = angular_wave_func(-m, l, theta, phi)

                if m < 0:
                    Y = (i / np.sqrt(2)) * (Y_lm_neg + Y_lm)
                elif m == 0:
                    Y = Y_lm
                elif m > 0:
                    Y = (1 / np.sqrt(2)) * (Y_lm_neg - Y_lm)

                Y = np.real(Y)
                R_nl = radial_wave_func(n, l, r * a) * Y
                probdensity = np.real(R_nl ** 2)
                wave = round(probdensity, 5)
                innerrow.append(wave)
            outerrow.append(innerrow)
        density.append(outerrow)
    x = np.array(xr)
    y = np.array(yr)
    z = np.array(zr)
    mag = np.array(density)
    return x, y, z, mag


# Code to save the data to a file so that
# you don't have to keep on computing it:

print('Test ')
x, y, z, mag = hydrogen_wave_func(4, 1, -1, 40, 100, 100, 100)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)
print(x, y, z, mag)
x.dump('x_test.dat')
y.dump('y_test.dat')
z.dump('z_test.dat')
mag.dump('den_test.dat')

# Mayavi code:

from mayavi import mlab

mu, sigma = 0, 0.1
x = np.load('x_test.dat', allow_pickle=True)
y = np.load('y_test.dat', allow_pickle=True)
z = np.load('z_test.dat', allow_pickle=True)

density = np.load('den_test.dat', allow_pickle=True)
figure = mlab.figure('DensityPlot')
pts = mlab.contour3d(density, contours=40, opacity=0.4)
mlab.axes()
mlab.show()
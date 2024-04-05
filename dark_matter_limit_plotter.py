import numpy as np
from matplotlib import pyplot as plt
from glob import glob
from scipy.interpolate import interp1d, BSpline, splrep

import mpl_style as mplt
from mpl_style import make_spline, label_line

plt.style.use(['mvstyle', 'one_piece'])

limit_dir = 'Limits_DM/'

def load_data(fname, int_type):

    file = int_type + '_' + limit_dir + fname + '.dat'

    data = np.loadtxt(file, unpack=True)

    return data


def add_limit(ax, int_type, fname, txt_pos, fill=True, ls = '-', halign = 'center', valign = 'top', xshift = 0, yshift = 0, x_end = None):

    fname = glob(int_type + '_' + limit_dir + fname + '*.dat')
    fname = fname[0].rstrip('.dat')
    fname = fname.lstrip(int_type + '_Limits_DM')
    fname = fname.lstrip('/')


    data = load_data(fname, int_type)

    interp = make_spline(data[0], data[1], smoothing=0.01, degree=2)

    # if x_end != None:
    #     x_vals = np.logspace(np.log10(data[0,0]), np.log10(x_end), 100)
    # else:
    x_vals = data[0]

    y_vals = interp(x_vals)

    with plt.rc_context({'lines.linewidth':1}):
        plot = mplt.loglog(ax, x_vals, y_vals, ls=ls)

    if fill:
        ax.fill_between(x_vals, y_vals, 1e-20, color='#E2E2E2', ec="none")

    col = plot.get_lines()[-1].get_color()
    label_line(ax, data, r'\textsf{{{}}}'.format(fname), data[0,txt_pos], halign = halign, xshift = xshift, yshift = yshift, valign=valign, txt_col = col)

def add_all_lims(ax):
    fnames = glob(limit_dir + '*.dat')

    for file in fnames:
        file = file.rstrip('.dat')
        file = file.lstrip('Limits_DM')
        file = file.lstrip('/')
        if file == 'DARWIN':
            add_limit(ax, file, ls = '--', fill = False)
        else:
            add_limit(ax, file)

        
def nu_floor(ax, target, txt_pos, halign = 'center', valign = 'center_baseline', x_end = 1e3):

    data = np.loadtxt(f'Neutrino_Floor/nu_floor_{target}.dat', unpack=True)

    interp = interp1d(data[0], data[1], kind='linear', fill_value='extrapolate')

    if x_end != None:
        x_vals = np.logspace(np.log10(data[0,0]), np.log10(x_end), 100)
    else:
        x_vals = data[0]

    y_vals = interp(x_vals)

    mplt.loglog(ax, x_vals, y_vals, ls = ':')
    col = ax.get_lines()[-1].get_color()
    ax.fill_between(x_vals, y_vals, 1e-56, alpha = 0.3, color = col, ec = 'none')
    label_line(ax, data, r'$\nu\mathsf{-Floor}$', data[0, txt_pos], halign = halign, valign=valign)

def add_DAMA(ax, col = 'C03'):

    data1 = np.loadtxt('DAMA/DAMA_I.dat', unpack=True)
    data2 = np.loadtxt('DAMA/DAMA_Na.dat', unpack=True)
    # print(data)
    mplt.loglog(ax, data1[0], data1[1], color = col)
    ax.fill(data1[0], data1[1], alpha = 0.5, color = col)

    mplt.loglog(ax, data2[0], data2[1], color = col)
    ax.fill(data2[0], data2[1], alpha=0.5, color = col)

    pos1 = 6
    ax.annotate(r'\textsf{DAMA/I}', xy=(data1[0, pos1], data1[1, pos1]), xytext=(-6, 5), textcoords='offset points', size=10, horizontalalignment='center', verticalalignment='bottom', color = col)
    ax.annotate(r'\textsf{DAMA/Na}', xy=(data2[0, pos1], data2[1, pos1]), xytext=(10, 10), textcoords='offset points', size=10, horizontalalignment='center', verticalalignment='bottom', color = col)
    
if __name__ == "__main__":
    
    # data = np.loadtxt('Limits_DM/COSINE-100.dat', unpack=True)

    pass


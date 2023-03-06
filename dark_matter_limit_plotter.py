from turtle import color
import numpy as np
from matplotlib import pyplot as plt
from glob import glob
from scipy.interpolate import interp1d

import mpl_style as mplt

plt.style.use('mvstyle')

limit_dir = 'Limits_DM/'

def load_data(fname):

    file = limit_dir + fname + '.csv'

    data = np.loadtxt(file, unpack=True)

    return data

def label_line(ax, data, label, x, y, halign = 'right', valign = 'center', xshift = 0, yshift = 0, txt_col = 'black', size=6):
    """Add a label to a line, at the proper angle.

    Arguments
    ---------
    line : matplotlib.lines.Line2D object,
    label : str
    x : float
        x-position to place center of text (in data coordinated
    y : float
        y-position to place center of text (in data coordinates)
    color : str
    size : float
    """
    xdata, ydata = data[0], data[1]
    x1 = data[0, np.where(data[0] == x)[0][0]]
    x2 = data[0, np.where(data[0] == x)[0][0] + 1]
    y1 = data[1, np.where(data[1] == y)[0][0]]
    y2 = data[1, np.where(data[1] == y)[0][0] + 1]

    text = ax.annotate(label, xy=(x, y), xytext=(xshift, yshift),
                       textcoords='offset points',
                       size=size,
                       horizontalalignment=halign,
                       verticalalignment=valign, 
                       color = txt_col)

    sp1 = ax.transData.transform_point((x1, y1))
    sp2 = ax.transData.transform_point((x2, y2))

    rise = (sp2[1] - sp1[1])
    run = (sp2[0] - sp1[0])

    slope_degrees = np.degrees(np.arctan2(rise, run))
    text.set_rotation(slope_degrees)
    return text


def add_limit(ax, fname, txt_pos, fill=True, ls = '-', halign = 'center', valign = 'top', xshift = 0, yshift = 0, x_end = None):

    fname = glob(limit_dir + fname + '*.csv')
    fname = fname[0].rstrip('.csv')
    fname = fname.lstrip('Limits_DM')
    fname = fname.lstrip('/')


    data = load_data(fname)

    interp = interp1d(data[0], data[1], kind='linear', fill_value='extrapolate')

    if x_end != None:
        x_vals = np.logspace(np.log10(data[0,0]), np.log10(x_end), 100)
    else:
        x_vals = data[0]

    y_vals = interp(x_vals)

    with plt.rc_context({'lines.linewidth':1}):
        plot = mplt.loglog(ax, x_vals, y_vals, ls=ls)

    if fill:
        ax.fill_between(x_vals, y_vals, 1e-20, color='#ECECEC', ec="none")

    col = plot.get_lines()[-1].get_color()
    label_line(ax, data, fname, data[0,txt_pos], data[1,txt_pos], halign = halign, xshift = xshift, yshift = yshift, valign=valign, txt_col = col)

def add_all_lims(ax):
    fnames = glob(limit_dir + '*.csv')

    for file in fnames:
        file = file.rstrip('.csv')
        file = file.lstrip('Limits_DM')
        file = file.lstrip('/')
        if file == 'DARWIN':
            add_limit(ax, file, ls = '--', fill = False)
        else:
            add_limit(ax, file)

        
def nu_floor(ax, txt_pos, halign = 'center', valign = 'center_baseline', x_end = None):

    data = np.loadtxt('Neutrino_Floor/nu_floor_Xe.csv', unpack=True)

    interp = interp1d(data[0], data[1], kind='linear', fill_value='extrapolate')

    if x_end != None:
        x_vals = np.logspace(np.log10(data[0,0]), np.log10(x_end), 100)
    else:
        x_vals = data[0]

    y_vals = interp(x_vals)

    mplt.loglog(ax, x_vals, y_vals, ls = ':', color = 'C07')
    ax.fill_between(x_vals, y_vals, 1e-56, alpha = 0.3, color = 'C07', ec = 'none')
    label_line(ax, data, r'$\nu\mathsf{-Floor}$', data[0, txt_pos], data[1, txt_pos], halign = halign, valign=valign)

def add_DAMA(ax):

    data1 = np.loadtxt('DAMA/DAMA_I.csv', unpack=True)
    data2 = np.loadtxt('DAMA/DAMA_Na.csv', unpack=True)
    # print(data)
    mplt.loglog(ax, data1[0], data1[1], color = 'C08')
    ax.fill(data1[0], data1[1], alpha = 0.5, color = 'C08')

    mplt.loglog(ax, data2[0], data2[1], color='C08')
    ax.fill(data2[0], data2[1], alpha=0.5, color='C08')

    pos1 = 6
    col = ax.get_lines()[-1].get_color()
    ax.annotate('DAMA/I', xy=(data1[0, pos1], data1[1, pos1]), xytext=(-6, 5), textcoords='offset points', size=6, horizontalalignment='center', verticalalignment='bottom', color = col)
    ax.annotate('DAMA/Na', xy=(data2[0, pos1], data2[1, pos1]), xytext=(10, 10), textcoords='offset points', size=6, horizontalalignment='center', verticalalignment='bottom', color = col)
    
if __name__ == "__main__":
    
    data = np.loadtxt('Limits_DM/COSINE-100.csv', unpack=True)

    fig, ax = plt.subplots()

    x_end = 1e3
    plt.ylim(1e-50, 1e-36)
    plt.xlim(5e-1, x_end)
    # with plt.rc_context({'font.size':10}):
    plt.xlabel(r'$\mathrm{Dark\; Matter\; Mass\;(GeV/}c^2\mathrm{)}$')
    plt.ylabel(r'$\mathrm{Cross\;Section}\;\sigma_{SI}\;\mathrm{(cm}^2\mathrm{)}$')

    # add_all_lims(ax)

    add_limit(ax, 'XENON', -10, yshift = 9)
    add_limit(ax, 'DARWIN', -16, ls = '--', fill= False, yshift = 8, x_end = x_end)
    add_limit(ax, 'Dark Side', -15, yshift = 10,  x_end = x_end)
    add_limit(ax, 'DEAP', -10, xshift = -5, yshift=-1)
    # add_limit(ax, 'SuperCDMS', 9, halign='right', x_end = x_end)
    # next(ax._get_lines.prop_cycler)
    add_limit(ax, 'LZ', -20, yshift = -1, x_end = x_end)
    add_limit(ax, 'Panda', -13, x_end = x_end)
    add_limit(ax, 'COSINE', -12, xshift = -5, yshift = 10, x_end = x_end)
    # add_limit(ax, 'LUX', -20, x_end = x_end)
    add_limit(ax, 'CDMSlite', 5)
    add_limit(ax, 'CREST', -10)



    nu_floor(ax, 8, valign='top', x_end = x_end)

    add_DAMA(ax)


    plt.savefig('DM_limits.pdf')
    # plt.show()


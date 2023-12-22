import numpy as np
from matplotlib import pyplot as plt
from glob import glob
from scipy.interpolate import interp1d, BSpline, splrep

import mpl_style as mplt

plt.style.use(['mvstyle', 'one_piece'])

limit_dir = 'Limits_DM/'

def load_data(fname, int_type):

    file = int_type + '_' + limit_dir + fname + '.dat'

    data = np.loadtxt(file, unpack=True)

    return data


def make_spline(x_data, y_data, smoothing=0.1, degree=3, xscale = 'log', yscale = 'log'):
    '''
    Makes a Bspline rep interolating function. 
    
    Inputs:
    --------
    x_data: range of x values
    y_data: range of y values
    smoothing: amount of smoothing to apply to the data. 's' value in splines
    degree: degree of the fitting polynomial

    Outputs:
    ---------
    An interpolating function over the x values supplied
    '''

    if xscale == 'log' and yscale == 'log':

        lx_data = np.log10(x_data)
        ly_data = np.log10(y_data)

        linterp = splrep(lx_data, ly_data, s=smoothing, k=degree)

        def __interpolating_function(_xx):
            return 10**BSpline(*linterp)(np.log10(_xx))

    else:

        linterp = splrep(x_data, y_data, s=smoothing, k=degree)

        def __interpolating_function(_xx):
            return BSpline(*linterp)(_xx)
    
    return __interpolating_function

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
        ax.fill_between(x_vals, y_vals, 1e-20, color='#ECECEC', ec="none")

    col = plot.get_lines()[-1].get_color()
    label_line(ax, data, fname, data[0,txt_pos], data[1,txt_pos], halign = halign, xshift = xshift, yshift = yshift, valign=valign, txt_col = col)

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

        
def nu_floor(ax, target, txt_pos, halign = 'center', valign = 'center_baseline', x_end = None):

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
    label_line(ax, data, r'$\nu\mathsf{-Floor}$', data[0, txt_pos], data[1, txt_pos], halign = halign, valign=valign)

def add_DAMA(ax):

    data1 = np.loadtxt('DAMA/DAMA_I.dat', unpack=True)
    data2 = np.loadtxt('DAMA/DAMA_Na.dat', unpack=True)
    # print(data)
    mplt.loglog(ax, data1[0], data1[1])
    col = ax.get_lines()[-1].get_color()
    ax.fill(data1[0], data1[1], alpha = 0.5, color = col)

    mplt.loglog(ax, data2[0], data2[1], color = col)
    ax.fill(data2[0], data2[1], alpha=0.5, color = col)

    pos1 = 6
    ax.annotate('DAMA/I', xy=(data1[0, pos1], data1[1, pos1]), xytext=(-6, 5), textcoords='offset points', size=6, horizontalalignment='center', verticalalignment='bottom', color = col)
    ax.annotate('DAMA/Na', xy=(data2[0, pos1], data2[1, pos1]), xytext=(10, 10), textcoords='offset points', size=6, horizontalalignment='center', verticalalignment='bottom', color = col)
    
if __name__ == "__main__":
    
    # data = np.loadtxt('Limits_DM/COSINE-100.dat', unpack=True)

    pass


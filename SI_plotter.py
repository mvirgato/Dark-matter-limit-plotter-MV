
from matplotlib import pyplot as plt

from dark_matter_limit_plotter import *

if __name__ == "__main__":    

    fig, ax = plt.subplots()

    x_end = 1e3
    plt.ylim(1e-50, 1e-36)
    plt.xlim(5e-1, x_end)
    # with plt.rc_context({'font.size':10}):
    plt.xlabel(r'$\mathrm{Dark\; Matter\; Mass\;(GeV/}c^2\mathrm{)}$')
    plt.ylabel(r'$\mathrm{SI\;Dark\;Matter-Nucleon\;Cross\;Section}\;\mathrm{(cm}^2\mathrm{)}$')
    # plt.ylabel(r'$\mathrm{Spin-Independent\;Cross\;Section:}\;\sigma^{SI}_{n\chi}\;\mathrm{(cm}^2\mathrm{)}$')

    # add_all_lims(ax)

    add_limit(ax, 'SI', 'XENON', -10, yshift = 9)
    add_limit(ax, 'SI', 'DARWIN', -16, ls = '--', fill= False, yshift = 8, x_end = x_end)
    # next(ax._get_lines.prop_cycler)
    # next(ax._get_lines.prop_cycler)
    add_limit(ax, 'SI', 'Dark Side', -15, yshift = 10,  x_end = x_end)
    # add_limit(ax, 'SI', 'DEAP', -10, xshift = -5, yshift=-1)
    # add_limit(ax, 'SI', 'SuperCDMS', 9, halign='right', x_end = x_end)
    add_limit(ax, 'SI', 'LZ', -20, yshift = -1, x_end = x_end)
    add_limit(ax, 'SI', 'Panda', -13, x_end = x_end)
    add_limit(ax, 'SI', 'COSINE', -12, xshift = -5, yshift = 10, x_end = x_end)
    # add_limit(ax, 'SI', 'LUX', -20, x_end = x_end)
    add_limit(ax, 'SI', 'CDMSlite', 5)
    add_limit(ax, 'SI', 'CREST', -10)


    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    nu_floor(ax, 'Xe', 8, valign='top', x_end=x_end)


    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    add_DAMA(ax)


    plt.savefig('DM_limits_SI.pdf')
    plt.show()

from matplotlib import pyplot as plt

from dark_matter_limit_plotter import *

if __name__ == "__main__":   

    int = 'SD_p' 

    fig, ax = plt.subplots()

    x_end = 1e3
    plt.ylim(1e-46, 1e-32)
    plt.xlim(5e-1, x_end)
    # with plt.rc_context({'font.size':10}):
    plt.xlabel(r'$\mathrm{Dark\; Matter\; Mass\;(GeV/}c^2\mathrm{)}$')
    plt.ylabel(r'$\mathrm{SD\;Dark\;Matter-Proton\;Cross\;Section}\;\mathrm{(cm}^2\mathrm{)}$')
    # plt.ylabel(r'$\mathrm{Spin-Independent\;Cross\;Section:}\;\sigma^{SI}_{n\chi}\;\mathrm{(cm}^2\mathrm{)}$')

    # add_all_lims(ax)

    add_limit(ax, int, 'XENON', -15, valign = 'top')
    add_limit(ax, int, 'PICO', -10, valign = 'top')
    add_limit(ax, int, 'PICASSO', -10, valign = 'bottom')
    add_limit(ax, int, 'LUX', -5, valign = 'top')
    add_limit(ax, int, 'Panda', -10, valign = 'bottom')
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler) 
    add_limit(ax, int, 'CRESST', -20, valign = 'bottom')


    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    next(ax._get_lines.prop_cycler)
    nu_floor(ax, 'C3F8', 8, valign='top', x_end=x_end)


    # next(ax._get_lines.prop_cycler)
    # next(ax._get_lines.prop_cycler)
    # next(ax._get_lines.prop_cycler)
    # next(ax._get_lines.prop_cycler)
    # next(ax._get_lines.prop_cycler)
    # add_DAMA(ax)


    plt.savefig('plots/DM_limits_SD_p.pdf')
    plt.show()
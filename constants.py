import numpy as np

energy_scale = np.float128(1.e-3) # Sets energy scale relative to MeV i.e. if working in GeV set to 1e-3 as 1 MeV is 1e-3 GeV

# constants
pi      = np.float128(np.pi)                            # Pi
cspeed  = np.float128(299792458.)                       # speed of light m/s
hplanck = np.float128(6.62607015e-34)                   # plancks constant. J s
hbar    = np.float128(6.582119569e-22 * energy_scale)   # reduced plancks  MeV s
Msol    = np.float128(1.989e30)                         # Mass of Sun in kg
GNewt   = np.float128(6.67430e-11)                      # Newtons constant m^3 / kg / s^2
kB      = np.float128(1.380e-23)
kBeV    = np.float128(8.61733034e-11 * energy_scale)    # Boltzmann's constant in MeV/K
echarge = np.float128(0.30286)                          # elementary charge in natural units
vev     = np.float128(246000. * energy_scale)           # Higgs vev
rhoDM   = np.float128(0.4)                              # local DM density in GeV/cm^3
vs      = np.float(230.0)                               # Star rel velocity
vd      = np.float(270.0)                               # DM dispersion velocity
alphaEM = np.float(0.00729927)
GF      = np.float(1.166e-5)                            # Fermi coupling constant
sigmaSB = np.float(np.pi**2 / 60.0)                     # Stefan - Boltzmann in natural units

# conversions
sTOmin       = np.float128(1./60.)                                        # s to min
minTOhr      = np.float128(1./60.)                                        # min to hour
hrTOday      = np.float128(1./24.)                                        # hour to day
dayTOyr      = np.float128(1./365.)                                       # day to year
sTOhr        = np.float128(sTOmin*minTOhr)                                # s to hour
sTOday       = np.float128(sTOhr*hrTOday)                                 # s to day
sTOyr        = np.float128(sTOday*dayTOyr)                                # s to year
yrTOs        = np.float128(1.0 / sTOyr)                                # s to year
mTOcm        = np.float128(100)                                           # m to cm
cmTOm        = np.float128(1. / 100.)                                     # cm to m
kmTOm        = np.float128(1000.)                                         # km to m
mTOkm        = np.float128(1. / 1000.)                                    # m to km
mTOpm        = np.float128(1e12)                                          # m to pm
pmTOm        = np.float128(1e-12)                                         # pm to m
mTOfm        = np.float128(1e15)                                          # m to fm
fmTOm        = np.float128(1e-15)                                         # fm to m
kgTOg        = np.float128(1000)                                          # kg to g
gTOkg        = np.float128(1. / 1000.)                                    # g to kg
PaTOdynpcm2  = np.float128(10)                                            # Pascals to dyne/cm^2
inveVTOm     = np.float128(197.3269788 * fmTOm * energy_scale)            # MeV m
mTOinveV     = np.float128(1. / (197.3269788 * fmTOm * energy_scale))     # (MeV m)^-1
inveVTOs     = np.float128(6.582119514e-22 * energy_scale)                # MeV s
sTOinveV     = np.float128(1. / (6.582119514e-22 * energy_scale))         # (MeV s)^-1
eVTOkg       = np.float128(1.78266191e-30 / energy_scale)                 # kg/MeV
kgTOeV       = 1.0 / eVTOkg                                               # MeV / kg

# Usefule natural unit quantities
GNewt_natural = np.float128(GNewt * mTOinveV**3 / kgTOeV / sTOinveV**2)
Msol_natural  = np.float128( Msol * kgTOeV)

# particle masses
mn    = np.float128(939. * energy_scale)           # neutron mass  MeV
mp    = np.float128(938. * energy_scale)           # proton mass  MeV
me    = np.float128(0.511 * energy_scale)          # electron mass  MeV
mmu   = np.float128(105.66 * energy_scale)         # muon mass  MeV
mtau = np.float128(1776.86 * energy_scale)         # tau mass in MeV
mnu = np.float128(1e-7 * energy_scale)             # neutrino mass

mpionPM = np.float128(139.57061 * energy_scale)      # pi+/- mass in MeV
mpion0  = np.float128(134.98 * energy_scale)         # pi0 mass in MeV
mEta0   = np.float128(547.862 * energy_scale)        # eta0 mass
mKaonPM = np.float128(493.68 * energy_scale)         # K+/- mass
mKaon0  = np.float128(497.61 * energy_scale)         # K0 mass

mL    = np.float128(1115.683 * energy_scale)       # Lambda mass in MeV
mXi0  = np.float128(1314.86 * energy_scale)        # Xi0 mass in MeV
mXim  = np.float128(1321.71 * energy_scale)        # Xim mass in MeV

mU = np.float128(0.00216 * 1e3 * energy_scale)      # u quark mass
mD = np.float128(0.00467 * 1e3 * energy_scale)      # d quark mass
mS = np.float128(0.093 * 1e3 * energy_scale)        # s quark mass
mC = np.float128(1.27 * 1e3 * energy_scale)         # c quark mass
mB = np.float128(4.18 * 1e3 * energy_scale)         # b quark mass
mT = np.float128(172.69 * 1e3 * energy_scale)       # t quark mass

mZ = np.float128(91.1876 * 1e3 * energy_scale)

ye   = np.sqrt(2.0) * me / vev
ymu  = np.sqrt(2.0) * mmu / vev
ytau = np.sqrt(2.0) * mtau / vev
ynu  = np.sqrt(2.0) * mnu / vev


yU = np.sqrt(2.0) * mU / vev
yD = np.sqrt(2.0) * mD / vev
yS = np.sqrt(2.0) * mS / vev
yC = np.sqrt(2.0) * mC / vev
yB = np.sqrt(2.0) * mB / vev
yT = np.sqrt(2.0) * mT / vev

cvU   = 0.266
cvD   = -0.38
cvlep = -0.03783

caU   = 0.519
caD   = -0.527
calep = -0.50123

gnu= np.array([ynu, ynu, ynu, ynu, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
ge = np.array([ye, ye, ye, ye, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
gmu = np.array([ymu, ymu, ymu, ymu, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
gtau = np.array([ytau, ytau, ytau, ytau, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

gl = np.vstack((gnu, gnu, gnu, ge, gmu, gtau))

gU = np.array([yU, yU, yU, yU, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
gD = np.array([yD, yD, yD, yD, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
gS = np.array([yS, yS, yS, yS, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
gC = np.array([yC, yC, yC, yC, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
gB = np.array([yB, yB, yB, yB, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
gT = np.array([yT, yT, yT, yT, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

gq = np.vstack((gU, gD, gS, gC, gB, gT))

mq = np.array([mU, mD, mS, mC, mB, mT])

caq = np.array([caU, caD, caD, caU, caD, caU])
cvq = np.array([cvU, cvD, cvD, cvU, cvD, cvU])

B0 = mpion0**2 / (mU + mD)


Q0FF = np.float128(1.0)


# Numerical settings
_tol = 1e-12
_atol = 0.0
_rtol = 1e-10
_max_iters = 20000
_arg_tol = 1e-5

_mean_filter = 100.

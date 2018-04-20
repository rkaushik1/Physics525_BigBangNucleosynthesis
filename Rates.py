import numpy as np

#ALL_RATES = {1,}

def equation_1_forward(temp, rho):
    return 2.5e4 * rho

def equation_1_backward(temp, rho):
    return 4.68e9 * equation_1_forward(temp, rho) / rho * temp**(3/2.) * np.exp(-25.82 / temp)

def equaton_2_forward(temp, rho):
    return 2.23e3 * rho * temp**(-2./3) * np.exp(-3.72 * temp**(-1./3)) * (1 + 0.112*temp**(1./3) + 3.38*temp**(2./3) + 2.65*temp)

def equation_2_backward(temp, rho):
    return 1.63e10 * equaton_2_forward(temp, rho) / rho * temp**(3./2) * np.exp(-63.75/temp)

def equation_3_forward(temp, rho):
    return rho * (75.5 + 1250*temp)

def equation_3_backward(temp, rho):
    return 1.63e10 * equation_3_forward(temp, rho) / rho * temp**(3./2) * np.exp(-72.62 / temp)

def equaton_4_forward(temp, rho):
    return 7.06e8 * rho

def equation_4_backward(temp, rho):
    return equaton_4_forward(temp, rho) * np.exp(-8.864 / temp)
    
def equation_5_forward(temp, rho):
    return 2.87e4 * rho * temp**(-2./3) * np.exp(-3.87*temp**(-1./3)) * (1 + 0.108*temp**(1./2) + 0.466*temp**(2./3) + 0.352*temp + 0.300*temp**(4./3) + 0.576*temp**(5./3))

def equation_5_backward(temp, rho):
    return 2.59e10 * equation_5_forward(temp, rho) / rho * temp**(3./2) * np.exp(-229.9/temp)

def equation_6_forward(temp, rho):
    return 6.0e3 * rho * temp

def equation_6_backward(temp, rho):
    return 2.6e10 * equation_6_forward(temp, rho) / rho * temp**(3./2) * np.exp(-238.8 / temp)

def equation_7_forward(temp, rho):
    return 3.9e8 * rho * temp**(-2./3) * np.exp(-4.26 * temp**(-1./3)) * (1 + 0.0797*temp**(1./3) + 0.642*temp**(2./3) + 0.440*temp)

def equation_7_backward(temp, rho):
    return 1.73 * equation_7_forward(temp, rho) * np.exp(-37.94/temp) 

def equation_8_forward(temp, rho):
    return equation_7_backward(temp, rho)

def equation_8_backward(temp, rho):
    return 1.73* equation_7_forward(temp, rho) * np.exp(-46.80/temp)

def equation_9_forward(temp, rho):
    return 24.1 * rho * temp**(-2./3) * np.exp(-4.26*temp**(-1./3)) * (temp**(2./3) + 0.685*temp + 0.152*temp**(4./3) + 0.265*temp**(5./3))

def equation_9_backward(temp, rho):
    return 4.5e10 * equation_9_forward(temp, rho) / rho * temp**(3./2) * np.exp(-276.7/temp)

def equation_10_forward(temp, rho):
    return 2.6e9 * rho * temp**(-3./2) * np.exp(-2.99/temp)

def equation_10_backward(temp, rho):
    return 5.5 * equation_10_forward(temp, rho) * np.exp(-213.0/temp)

def equation_11_forward(temp, rho):
    return 1.38e9 * rho * temp**(-3./2) * np.exp(-0.745/temp)

def equation_11_backward(temp, rho):
    return 5.5 * equation_11_forward(temp, rho) * np.exp(-204.1/temp)

def equation_12_forward(temp, rho):
    return 1.19e10 * rho * temp**(-2./3) * np.exp(-12.25*temp**(-1./3)) * (1 + 0.0340*temp**(1./3))

def equation_12_backward(temp, rho):
    return 3.377e-10 * equation_12_forward(temp, rho) * rho * temp**(-3./2) * np.exp(-149.2/temp)

def equation_13_forward(temp, rho):
    return 1.1e9 * rho * temp**(-2./3) * np.exp(-4.87*temp**(-1./3))* (1 + 0.0857*temp**(1./3))

def equation_13_backward(temp, rho):
    return 3.377e-10 * equation_13_forward(temp, rho) *rho * temp**(-3./2) * np.exp(-131.5/temp)

def equation_14_forward(temp, rho):
    return 5.60e9 * rho * temp**(-2./3) * np.exp(-7.72*temp**(-1./3)) * (1 + 0.0540*temp**(1./3))

def equation_14_backward(temp, rho):
    return 3.377e-10 * equation_14_forward(temp, rho) *rho * temp**(-3./2) * np.exp(-140.4/temp)

def equation_15_forward(temp, rho):
    return 3.88e9 * rho * temp**(-2./3) * np.exp(-7.72*temp**(-1./3)) *(1 + 0.0540*temp**(1./3))

def equation_15_backward(temp, rho):
    return 1.59 * equation_15_forward(temp, rho) * np.exp(-166.2/temp)

def equation_16_forward(temp, rho):
    return 4.8e6 * rho * temp**(-2./3) * np.exp(-12.8*temp**(-1./3)) * (1 + 0.0326*temp**(1./3) - 2.19*temp**(2./3) - 0.0499*temp + 0.0258*temp**(4./3) + 0.0150*temp**(5./3))

def equation_16_backward(temp, rho):
    return 1.12e10 * equation_16_forward(temp, rho) / rho * temp**(3./2) * np.exp(-18.42/temp)

def equation_17_forward(temp, rho):
    return 5.60e9 * rho * temp**(-2./3) * np.exp(-7.72*temp**(-1./3)) *(1 + 0.0540*temp**(1./3))

def equation_17_backward(temp, rho):
    return
def equation_18_forward(temp, rho):
    return
def equation_18_backward(temp, rho):
    return
def equation_19_forward(temp, rho):
    return
def equation_19_backward(temp, rho):
    return
def equation_20_forward(temp, rho):
    return
def equation_20_backward(temp, rho):
    return
def equation_21_forward(temp, rho):
    return
def equation_21_backward(temp, rho):
    return
def equation_22_forward(temp, rho):
    return
def equation_22_backward(temp, rho):
    return
def equation_23_forward(temp, rho):
    return
def equation_23_backward(temp, rho):
    return
def equation_24_forward(temp, rho):
    return
def equation_24_backward(temp, rho):
    return
def equation_25_forward(temp, rho):
    return
def equation_25_backward(temp, rho):
    return
def equation_26_forward(temp, rho):
    return
def equation_26_backward(temp, rho):
    return
def equation_27_forward(temp, rho):
    return
def equation_27_backward(temp, rho):
    return
def equation_28_forward(temp, rho):
    return
def equation_28_backward(temp, rho):
    return
def equation_29_forward(temp, rho):
    return
def equation_29_backward(temp, rho):
    return
def equation_30_forward(temp, rho):
    return
def equation_30_backward(temp, rho):
    return
def equation_31_forward(temp, rho):
    return
def equation_31_backward(temp, rho):
    return
def equation_32_forward(temp, rho):
    return
def equation_32_backward(temp, rho):
    return
def equation_33_forward(temp, rho):
    return
def equation_33_backward(temp, rho):
    return
def equation_34_forward(temp, rho):
    return
def equation_34_backward(temp, rho):
    return
def equation_35_forward(temp, rho):
    return
def equation_35_backward(temp, rho):
    return
def equation_36_forward(temp, rho):
    return
def equation_36_backward(temp, rho):
    return
def equation_37_forward(temp, rho):
    return
def equation_37_backward(temp, rho):
    return
def equation_38_forward(temp, rho):
    return
def equation_38_backward(temp, rho):
    return
def equation_39_forward(temp, rho):
    return
def equation_39_backward(temp, rho):
    return
def equation_40_forward(temp, rho):
    return
def equation_40_backward(temp, rho):
    return
def equation_41_forward(temp, rho):
    return
def equation_41_backward(temp, rho):
    return
def equation_42_forward(temp, rho):
    return
def equation_42_backward(temp, rho):
    return
def equation_43_forward(temp, rho):
    return
def equation_43_backward(temp, rho):
    return
def equation_44_forward(temp, rho):
    return
def equation_44_backward(temp, rho):
    return
def equation_45_forward(temp, rho):
    return
def equation_45_backward(temp, rho):
    return
def equation_46_forward(temp, rho):
    return
def equation_46_backward(temp, rho):
    return
def equation_47_forward(temp, rho):
    return
def equation_47_backward(temp, rho):
    return
def equation_48_forward(temp, rho):
    return
def equation_48_backward(temp, rho):
    return
def equation_49_forward(temp, rho):
    return
def equation_49_backward(temp, rho):
    return
def equation_50_forward(temp, rho):
    return
def equation_50_backward(temp, rho):
    return
def equation_51_forward(temp, rho):
    return
def equation_51_backward(temp, rho):
    return
def equation_52_forward(temp, rho):
    return
def equation_52_backward(temp, rho):
    return
def equation_53_forward(temp, rho):
    return
def equation_53_backward(temp, rho):
    return
def equation_54_forward(temp, rho):
    return
def equation_54_backward(temp, rho):
    return
def equation_55_forward(temp, rho):
    return
def equation_55_backward(temp, rho):
    return
def equation_56_forward(temp, rho):
    return
def equation_56_backward(temp, rho):
    return
def equation_57_forward(temp, rho):
    return
def equation_57_backward(temp, rho):
    return
def equation_58_forward(temp, rho):
    return
def equation_58_backward(temp, rho):
    return
def equation_59_forward(temp, rho):
    return
def equation_59_backward(temp, rho):
    return
def equation_60_forward(temp, rho):
    return
def equation_60_backward(temp, rho):
    return
def equation_61_forward(temp, rho):
    return
def equation_61_backward(temp, rho):
    return


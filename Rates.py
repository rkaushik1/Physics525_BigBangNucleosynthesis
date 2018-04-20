import numpy as np

def forward_1(temp, rho):
    return 2.5e4 * rho

def backward_1(temp, rho):
    return 4.68e9 * forward_1(temp, rho) / rho * temp**(3/2.) * np.exp(-25.82 / temp)

def forward_2(temp, rho):
    return 2.23e3 * rho * temp**(-2./3) * np.exp(-3.72 * temp**(-1./3)) * (1 + 0.112*temp**(1./3) + 3.38*temp**(2./3) + 2.65*temp)

def backward_2(temp, rho):
    return 1.63e10 * forward_2(temp, rho) / rho * temp**(3./2) * np.exp(-63.75/temp)

def forward_3(temp, rho):
    return rho * (75.5 + 1250*temp)

def backward_3(temp, rho):
    return 1.63e10 * forward_3(temp, rho) / rho * temp**(3./2) * np.exp(-72.62 / temp)

def forward_4(temp, rho):
    return 7.06e8 * rho

def backward_4(temp, rho):
    return forward_4(temp, rho) * np.exp(-8.864 / temp)
    
def forward_5(temp, rho):
    return 2.87e4 * rho * temp**(-2./3) * np.exp(-3.87*temp**(-1./3)) * (1 + 0.108*temp**(1./2) + 0.466*temp**(2./3) + 0.352*temp + 0.300*temp**(4./3) + 0.576*temp**(5./3))

def backward_5(temp, rho):
    return 2.59e10 * forward_5(temp, rho) / rho * temp**(3./2) * np.exp(-229.9/temp)

def forward_6(temp, rho):
    return 6.0e3 * rho * temp

def backward_6(temp, rho):
    return 2.6e10 * forward_6(temp, rho) / rho * temp**(3./2) * np.exp(-238.8 / temp)

def forward_7(temp, rho):
    return 3.9e8 * rho * temp**(-2./3) * np.exp(-4.26 * temp**(-1./3)) * (1 + 0.0797*temp**(1./3) + 0.642*temp**(2./3) + 0.440*temp)

def backward_7(temp, rho):
    return 1.73 * forward_7(temp, rho) * np.exp(-37.94/temp) 

def forward_8(temp, rho):
    return 7(temp, rho)

def backward_8(temp, rho):
    return 1.73* forward_8(temp, rho) * np.exp(-46.80/temp)

def forward_9(temp, rho):
    return 24.1 * rho * temp**(-2./3) * np.exp(-4.26*temp**(-1./3)) * (temp**(2./3) + 0.685*temp + 0.152*temp**(4./3) + 0.265*temp**(5./3))

def backward_9(temp, rho):
    return 4.5e10 * forward_9(temp, rho) / rho * temp**(3./2) * np.exp(-276.7/temp)

def forward_10(temp, rho):
    return 2.6e9 * rho * temp**(-3./2) * np.exp(-2.99/temp)

def backward_10(temp, rho):
    return 5.5 * forward_10(temp, rho) * np.exp(-213.0/temp)

def forward_11(temp, rho):
    return 1.38e9 * rho * temp**(-3./2) * np.exp(-0.745/temp)

def backward_11(temp, rho):
    return 5.5 * forward_11(temp, rho) * np.exp(-204.1/temp)

def forward_12(temp, rho):
    return 1.19e10 * rho * temp**(-2./3) * np.exp(-12.25*temp**(-1./3)) * (1 + 0.0340*temp**(1./3))

def backward_12(temp, rho):
    return 3.377e-10 * forward_12(temp, rho) * rho * temp**(-3./2) * np.exp(-149.2/temp)

def forward_13(temp, rho):
    return 1.1e9 * rho * temp**(-2./3) * np.exp(-4.87*temp**(-1./3))* (1 + 0.0857*temp**(1./3))

def backward_13(temp, rho):
    return 3.377e-10 * forward_13(temp, rho) *rho * temp**(-3./2) * np.exp(-131.5/temp)

def forward_14(temp, rho):
    return 5.60e9 * rho * temp**(-2./3) * np.exp(-7.72*temp**(-1./3)) * (1 + 0.0540*temp**(1./3))

def backward_14(temp, rho):
    return 3.377e-10 * forward_14(temp, rho) *rho * temp**(-3./2) * np.exp(-140.4/temp)

def forward_15(temp, rho):
    return 3.88e9 * rho * temp**(-2./3) * np.exp(-7.72*temp**(-1./3)) *(1 + 0.0540*temp**(1./3))

def backward_15(temp, rho):
    return 1.59 * forward_15(temp, rho) * np.exp(-166.2/temp)

def forward_16(temp, rho):
    return 4.8e6 * rho * temp**(-2./3) * np.exp(-12.8*temp**(-1./3)) * (1 + 0.0326*temp**(1./3) - 2.19*temp**(2./3) - 0.0499*temp + 0.0258*temp**(4./3) + 0.0150*temp**(5./3))

def backward_16(temp, rho):
    return 1.12e10 * forward_16(temp, rho) / rho * temp**(3./2) * np.exp(-18.42/temp)

def forward_17(temp, rho):
    return 5.28e5 * rho * temp**(-2./3) * np.exp(-8.08*temp**(-1./3)) *(1 + 0.0516*temp**(1./3))

def backward_17(temp, rho):
    return 1.12e10 * forward_17(temp, rho) / rho * temp**(3./2) * np.exp(-18.63/temp)

def forward_18(temp, rho):
    return 6.74e9 * rho * temp

def backward_18(temp, rho):
    return forward_18(temp, rho) * np.exp(-19.07/temp)

def forward_19(temp, rho):
    return 5.19e5 * rho * temp**(-2./3) * np.exp(-10.26*temp**(-1./3)) * (1 + 0.0407*temp**(1./3)) * (1 - np.exp(-1.564/temp))**(-1)

def backward_19(temp, rho):
    return 1.131e10 * forward_19(temp, rho) / rho * temp**(3./2) * np.exp(-1.564/temp)

def forward_20(temp, rho):
    return 1.42e9 * rho * temp**(-2./3) * np.exp(-8.47*temp**(-1./3)) * (1 + 0.0493*temp**(1./3))

def backward_20(temp, rho):
    return 4.64 * forward_20(temp, rho) * np.exp(-201.3/temp)

def forward_21(temp, rho):
    return 1.2e7 * rho * temp

def backward_21(temp, rho):
    return 4.64 * forward_21(temp, rho) * np.exp(-220.4/temp)

def forward_22(temp, rho):
    return 1.1e11 * rho * (temp**(-2./3) * np.exp(-12.04*temp**(-1./3)) + 3.28e-2 * temp**(-3./2) * np.exp(-12.35/temp) + 5.08e-2 * temp**(-3./2) * np.exp(-16.18/temp))

def backward_22(temp, rho):
    return 0.749 * forward_22(temp, rho) * np.exp(-13.32/temp)

def forward_23(temp, rho):
    return 5.08e12 * rho

def backward_23(temp, rho):
    return 0.749 * forward_23(temp, rho) * np.exp(-32.39/temp)

def forward_24(temp, rho):
    return 5.7e3  *rho * temp**(-3./2) * np.exp(-6.44/temp)

def backward_24(temp, rho):
    return 4.06e10 * forward_24(temp, rho) / rho * temp**(3./2) * np.exp(-87.56/temp)

def forward_25(temp, rho):
    return 1.8e-8 * rho**2 * temp**(-3) * (np.exp(-4.32/temp) + 30.3*np.exp(-27.4/temp)) 

def backward_25(temp, rho):
    return 2.05e20 * forward_25(temp, rho) * rho**(-2) * temp**3 * np.exp(-84.42/temp)

def forward_26(temp, rho):
    return 3.97e5 * rho * temp**(-3./2) * (np.exp(-1.74/temp) + 1.96e4*np.exp(-7.18/temp))

def backward_26(temp, rho):
    return 0

def forward_27(temp, rho):
    return 1.06e5 * rho * temp**(-3./2) * np.exp(-5.7/temp) + 2.05e7 * rho * temp**(-2./3)*np.exp(-13.7*temp**(-1./3))(1 + 3.04e-2*temp**(1./3) + 1.19*temp**(2./3) + 0.254*temp)

def backward_27(temp, rho):
    return 2.36e10 * forward_27(temp, rho) / rho * temp**(3./2) * np.exp(-6.65/temp)

def forward_28(temp, rho):
    return 2.2e16 * rho * temp**(-2./3) * np.exp(-31.9/temp)

def backward_28(temp, rho):
    return 3.71 * forward_28(temp, rho) * np.exp(-33.89*temp**(-1./3))
 
def forward_29(temp, rho):
    return 1.06e5 * rho * temp**(-3./2) * np.exp(-4.92/temp) + 2.05e7 * rho * temp**(-2./3)*np.exp(-13.7*temp**(-1./3))(1 + 3.04e-2*temp**(1./3) + 1.19*temp**(2./3) + 0.254*temp)

def backward_29(temp, rho):
    return 8.87e9 * forward_29(temp, rho) / rho * temp**(3./2) * np.exp(-22.25/temp)

def forward_30(temp, rho):
    return 2.34e8 * rho * temp**(-2) * np.exp(-32.2*temp**(-1./3))

def backward_30(temp, rho):
    return 5.2e10 * forward_30(temp, rho) / rho * temp**(3./2) * np.exp(-83.11/temp)

def forward_31(temp, rho):
    return 1.2e17 * rho * temp**(-2./3) * np.exp(-35.6*temp**(-1./3))

def backward_31(temp, rho):
    return 4.29 * forward_31(temp, rho) * np.exp(-111.9/temp)

def forward_32(temp, rho):
    return 1.2e16 * rho * temp**(-2./3) * np.exp(-32.3*temp**(-1./3))

def backward_32(temp, rho):
    return 5.87 * forward_32(temp, rho) * np.exp(-25.72/temp)

def forward_33(temp, rho):
     return 1.34e6 * rho * temp**(-3./2) * np.exp(-5.97/temp) + 8.04e7 * rho * temp**(-2./3)*np.exp(-13.7*temp**(-1./3))(1 + 3.04*temp**(1./3) + 9.58*temp**(2./3) + 2.04*temp)

def backward_33(temp, rho):
     return 1.2e10 * forward_33(temp, rho) / rho * temp**(3./2) * np.exp(-87.61/temp)

def forward_34(temp, rho):
     return 

def backward_34(temp, rho):
     return

def forward_35(temp, rho):
     return

def backward_35(temp, rho):
     return

def forward_36(temp, rho):
     return

def backward_36(temp, rho):
     return

def forward_37(temp, rho):
     return

def backward_37(temp, rho):
     return

def forward_38(temp, rho):
     return

def backward_38(temp, rho):
     return

def forward_39(temp, rho):
     return

def backward_39(temp, rho):
     return

def forward_40(temp, rho):
     return

def backward_40(temp, rho):
     return

def forward_41(temp, rho):
     return

def backward_41(temp, rho):
     return

def forward_42(temp, rho):
     return

def backward_42(temp, rho):
     return

def forward_43(temp, rho):
     return

def backward_43(temp, rho):
     return

def forward_44(temp, rho):
     return

def backward_44(temp, rho):
     return

def forward_45(temp, rho):
     return

def backward_45(temp, rho):
     return

def forward_46(temp, rho):
     return

def backward_46(temp, rho):
     return

def forward_47(temp, rho):
     return

def backward_47(temp, rho):
     return

def forward_48(temp, rho):
     return

def backward_48(temp, rho):
     return

def forward_49(temp, rho):
     return

def backward_49(temp, rho):
     return

def forward_50(temp, rho):
     return

def backward_50(temp, rho):
     return

def forward_51(temp, rho):
     return

def backward_51(temp, rho):
     return

def forward_52(temp, rho):
     return

def backward_52(temp, rho):
     return

def forward_53(temp, rho):
     return

def backward_53(temp, rho):
     return

def forward_54(temp, rho):
     return

def backward_54(temp, rho):
     return

def forward_55(temp, rho):
     return

def backward_55(temp, rho):
     return

def forward_56(temp, rho):
     return

def backward_56(temp, rho):
     return

def forward_57(temp, rho):
     return

def backward_57(temp, rho):
     return

def forward_58(temp, rho):
     return

def backward_58(temp, rho):
     return

def forward_59(temp, rho):
     return

def backward_59(temp, rho):
     return

def forward_60(temp, rho):
     return

def backward_60(temp, rho):
     return

def forward_61(temp, rho):
     return

def backward_61(temp, rho):
     return

def forward_62(temp, rho):
     return

def backward_62(temp, rho):
     return

def forward_63(temp, rho):
     return

def backward_63(temp, rho):
     return

ALL_RATES = {
    'backward_1':backward_1,
    'backward_10':backward_10,
    'backward_11':backward_11,
    'backward_12':backward_12,
    'backward_13':backward_13,
    'backward_14':backward_14,
    'backward_15':backward_15,
    'backward_16':backward_16,
    'backward_17':backward_17,
    'backward_18':backward_18,
    'backward_19':backward_19,
    'backward_2':backward_2,
    'backward_20':backward_20,
    'backward_21':backward_21,
    'backward_22':backward_22,
    'backward_23':backward_23,
    'backward_24':backward_24,
    'backward_25':backward_25,
    'backward_26':backward_26,
    'backward_27':backward_27,
    'backward_28':backward_28,
    'backward_29':backward_29,
    'backward_3':backward_3,
    'backward_30':backward_30,
    'backward_31':backward_31,
    'backward_32':backward_32,
    'backward_33':backward_33,
    'backward_34':backward_34,
    'backward_35':backward_35,
    'backward_36':backward_36,
    'backward_37':backward_37,
    'backward_38':backward_38,
    'backward_39':backward_39,
    'backward_4':backward_4,
    'backward_40':backward_40,
    'backward_41':backward_41,
    'backward_42':backward_42,
    'backward_43':backward_43,
    'backward_44':backward_44,
    'backward_45':backward_45,
    'backward_46':backward_46,
    'backward_47':backward_47,
    'backward_48':backward_48,
    'backward_49':backward_49,
    'backward_5':backward_5,
    'backward_50':backward_50,
    'backward_51':backward_51,
    'backward_52':backward_52,
    'backward_53':backward_53,
    'backward_54':backward_54,
    'backward_55':backward_55,
    'backward_56':backward_56,
    'backward_57':backward_57,
    'backward_58':backward_58,
    'backward_59':backward_59,
    'backward_6':backward_6,
    'backward_60':backward_60,
    'backward_61':backward_61,
    'backward_62':backward_62,
    'backward_63':backward_63,
    'backward_7':backward_7,
    'backward_8':backward_8,
    'backward_9':backward_9,
    'forward_1':forward_1,
    'forward_10':forward_10,
    'forward_11':forward_11,
    'forward_12':forward_12,
    'forward_13':forward_13,
    'forward_14':forward_14,
    'forward_15':forward_15,
    'forward_16':forward_16,
    'forward_17':forward_17,
    'forward_18':forward_18,
    'forward_19':forward_19,
    'forward_1':forward_1,
    'forward_20':forward_20,
    'forward_21':forward_21,
    'forward_22':forward_22,
    'forward_23':forward_23,
    'forward_24':forward_24,
    'forward_25':forward_25,
    'forward_26':forward_26,
    'forward_27':forward_27,
    'forward_28':forward_28,
    'forward_29':forward_29,
    'forward_2':forward_2,
    'forward_3':forward_3,
    'forward_30':forward_30,
    'forward_31':forward_31,
    'forward_32':forward_32,
    'forward_33':forward_33,
    'forward_34':forward_34,
    'forward_35':forward_35,
    'forward_36':forward_36,
    'forward_37':forward_37,
    'forward_38':forward_38,
    'forward_39':forward_39,
    'forward_3':forward_3,
    'forward_4':forward_4,
    'forward_40':forward_40,
    'forward_41':forward_41,
    'forward_42':forward_42,
    'forward_43':forward_43,
    'forward_44':forward_44,
    'forward_45':forward_45,
    'forward_46':forward_46,
    'forward_47':forward_47,
    'forward_48':forward_48,
    'forward_49':forward_49,
    'forward_5':forward_5,
    'forward_50':forward_50,
    'forward_51':forward_51,
    'forward_52':forward_52,
    'forward_53':forward_53,
    'forward_54':forward_54,
    'forward_55':forward_55,
    'forward_56':forward_56,
    'forward_57':forward_57,
    'forward_58':forward_58,
    'forward_59':forward_59,
    'forward_6':forward_6,
    'forward_60':forward_60,
    'forward_61':forward_61,
    'forward_62':forward_62,
    'forward_63':forward_63,
    'forward_7':forward_7,
    'forward_8':forward_8,
    'forward_9':forward_9,
    }

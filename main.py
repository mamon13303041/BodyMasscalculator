B_height=float(input('please eneter your height'))
B_weight=float(input('please enter your weight'))
B_height=B_height/100
Mass_calu=B_weight/(B_height)**2
print('your body mass index {}'.format(Mass_calu))
if Mass_calu!=0:
    if (Mass_calu<=16):
        print('Severe Thinness	')
    elif (Mass_calu<=25):
        print('Normal')
    elif (Mass_calu<=30):
        print('Severe Thinness	')
    elif (Mass_calu<=35):
        print('Obse Class 1')
    else:
        print('Overweighted person')
else:
    print('please input valid details ')




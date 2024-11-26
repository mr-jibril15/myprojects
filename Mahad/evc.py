haraaga = 185
code = input('code :')
if code.startswith('*770#'):
    print('-EVCPLUS')
    print('')
    pin = input('Fadlan geli PIN-kaaga (Enter PIN) : ')
    if pin.digit() and len(pin) == 4:
        print('EVCPlus')
        print('1.Itus Haraaga\n2.Kaarka hadalka \n3.Bixi Biil\n4.U wareeji EVCPlus\n5.Warbixin Kooban\n6.Salaam Bank\n7.Maareynta\n8.Bill Payment')
        print('')
        a = input('Dooro adeega aad rabto : ')
        if a == '1':
            print(f'Haraagaga waa :{haraaga}')
        elif a == '4':
            print('')
            num = input('Fadlan Geli Mobile-ka : ')
            if num.startswith('61') and len(num) == 9 and num.isdigit():
                print('')
                lacagta = input('Fadlan Geli Lacagta : ')
                if lacagta.isdigit() and float(lacagta) > haraaga:
                    print('')
                    print(f'Ma hubtaa inaad ${lacagta} u wareejisid 252{num}\n1.Haa\n2.Maya'),
                    pr = input(':')
                    if pr == '1':
                        print(f'waxaad wareejisay ${lacagta} waxaana uwareejisay number-ka 252{num}')
                    else:
                        print('Try again')
                else:
                    print('Try again')
            else:
                print('Try again')
        else:
            print('Try again')
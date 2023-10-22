while True:
    sayi = int(input('sayı: '))

    if sayi == 'q':
        break

    asalmi = True

    if sayi == 1:
        asalmi = False

    for i in range(2, sayi):
        if (sayi % i == 0):
            asalmi = False
            break
    if asalmi:
        print('sayı asaldır.')
    else:
        print('sayı asal değildir.')

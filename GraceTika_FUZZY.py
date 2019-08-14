import csv

def importdata():
    with open('dataset2.csv', 'rb') as f:
        reader = csv.reader(f,delimiter=';')
        data = list(reader)
    return data

class Emosi(object):
    def __init__(self, x):
        self.x = x

    def sedikit(self):
        if self.x <= 0:
            return 1
        elif 0 < self.x < 44:
            return (44 - self.x) / (44 - 0)
        else:
            return 0

    def cukup(self):
        if 35 < self.x < 45:
            return (self.x - 35) / (45 - 35)
        elif self.x == 45:
            return 1
        elif 45 < self.x < 69:
            return (69 - self.x) / (69 - 45)
        else:
            return 0

    def banyak(self):
        if 65 < self.x < 70:
            return (self.x - 65) / (70 - 65)
        elif self.x == 70:
            return 1
        elif 70 < self.x < 85:
            return (85 - self.x) / (85 - 70)
        else:
            return 0

    def sangat_banyak(self):
        if 80 < self.x < 100:
            return (self.x - 80) / (100 - 80)
        elif self.x >= 100:
            return 1
        else:
            return 0

class Provokasi(object):
    def __init__(self, x):
        self.x = x

    def kecil(self):
        if self.x <= 0:
            return 1
        elif 0 < self.x < 49:
            return (49 - self.x)/(49 - 0)
        else:
            return 0

    def sedang(self):
        if 45 < self.x < 50:
            return (self.x - 45)/(50 - 45)
        elif self.x == 50:
            return 1
        elif 50 < self.x < 69:
            return (69 - self.x)/(69 - 50)
        else:
            return 0

    def tinggi(self):
        if 65 < self.x < 70:
            return (self.x - 65)/(70 - 65)
        elif self.x == 70:
            return 1
        elif 70 < self.x < 89:
            return (89 - self.x)/(89 - 70)
        else:
            return 0

    def sangat_tinggi(self):
        if 80 < self.x < 100:
            return (self.x - 80)/(100 - 80)
        elif self.x >= 100:
            return 1
        else:
            return 0

if __name__ == '__main__':

    data = importdata()
    i = 0
    print '    Y_output asli_hasil fuzzy'
    print
    for i in range(len(data)):
        e = Emosi(float(data[i][0]))
        p = Provokasi(float(data[i][1]))

        # TIDAK
        a1 = min(e.sedikit(), p.kecil())
        a2 = min(e.sedikit(), p.sedang())
        a3 = min(e.cukup(), p.kecil())
        a4 = min(e.cukup(), p.sedang())
        a5 = min(e.cukup(), p.tinggi())
        a6 = min(e.banyak(), p.kecil())
        a7 = min(e.sangat_banyak(), p.kecil())

        a = max(a1, a1, a3, a4, a5, a6, a7)

        # YA
        b1 = min(e.sedikit(), p.tinggi())
        b2 = min(e.sedikit(), p.sangat_tinggi())
        b3 = min(e.cukup(), p.sangat_tinggi())
        b4 = min(e.banyak(), p.sedang())
        b5 = min(e.banyak(), p.tinggi())
        b6 = min(e.banyak(), p.sangat_tinggi())
        b7 = min(e.sangat_banyak(), p.sedang())
        b8 = min(e.sangat_banyak(), p.tinggi())
        b9 = min(e.sangat_banyak(), p.sangat_tinggi())

        b = max(b1, b2, b3, b4, b5, b6, b7, b8, b9)

        #defuzzification
        y = round((a*50)+(b*70)/(a+b))
        j = i+1

        if y > 49.99:
            print j,'.',y,'Ya',
        else:
            print j,'.',y,'Tidak',
        print data[i][2]


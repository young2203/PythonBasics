from gcd import gcd
class Fraction:
    '''
        This is a class used to define fraction object
    and all the operations related with it
    '''
    def __init__(self,num,den):
        if num * den <0 :
            num = -abs(num)
            den =  abs(den)
        self.top = num
        self.bottom = den

    def __add__(self, other):
        upper = self.top * other.bottom + self.bottom * other.top
        lower = self.bottom * other.bottom
        return Fraction(upper, lower).pretty()

    def __sub__(self, other):
        upper = self.top * other.bottom - self.bottom * other.top
        lower = self.bottom * other.bottom
        return Fraction(upper, lower).pretty()

    def __eq__(self, other):
        fac1=self.pretty()
        fac2=other.pretty()
        top_eql= fac1.top == fac2.top
        bottom_eql = fac1.bottom == fac2.bottom
        return top_eql and bottom_eql

    def __lt__(self, other):
        diff = self - other
        if diff.top < 0:
            return True
        else:
            return False

    def __gt__(self, other):
        diff = self - other
        if diff.top > 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.top)+'/'+str(self.bottom)

    def pretty(self):
        factor = gcd(self.top, self.bottom)
        prettyFac = Fraction(int(self.top/factor),int(self.bottom/factor))
        return prettyFac

    def show(self):
        print(str(self.top)+'/'+str(self.bottom))
'''
def gcd(m, n):
    # Get maximum factor
    while n != 0:
        m , n = n, m%n
    return abs(m)
'''
if __name__ == '__main__':
    myFrac_1 = Fraction(1,5)
    myFrac_2 = Fraction(2,5)
    ans=myFrac_1+myFrac_2
    print(ans)
    print(type(ans))
    #ans.show()
    #Fraction(3,5)==Fraction(6,10)

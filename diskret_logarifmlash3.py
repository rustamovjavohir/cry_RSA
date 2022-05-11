import math


class DiskretLog:
    def __init__(self, a, b, p) -> None:
        self.a = a
        self.b = b
        self.p = p
           
    def func(self):
        """
        Berilgan funksiyani togriligini tekshirish
        """

        is_true = input(f'{self.a}^x={self.b}mod{self.p} it is true? n/y')
        if 'y' in is_true:
            return self.a, self.b, self.p
        return self.func

    def find_H(self,):
        """
        H ni qiymatini hisoblash
        """
        H = math.ceil(math.sqrt(self.p))
        return H

    def find_C(self):
        """
        C ni qiymatini hisoblash
        """
        C = math.pow(self.a, self.find_H()) % self.p
        return C
    
    def list_u(self):
        """
        u, 1 <= u <= H sonli qiymatlari uchun C^u(mod p) jadval tuzib. Bu qiymatlarni tartiblab chiqish
        """
        u_list = []
        H = self.find_H()
        C = self.find_C()
        for i in range(1, H + 1):
            u_list.append(math.pow(C, i) % self.p)
        
        return u_list

    def list_v(self):
        """
        v, 0 <= v <= H sonli qiymatlari uchun b*a^v(mod p) jadval tuzib. Bu qiymatlarni tartiblab chiqish
        """
        v_list = []
        H = self.find_H()
        for i in range(1, H + 1):
            v_list.append(self.b * math.pow(self.a, i) % self.p)
        
        return v_list
        
    def find_u_v(self):
        """
        u va v jadvalaridagi bir xil qiymatlar inteksini qaytarish
        """
        u_list = self.list_u()
        v_list = self.list_v()

        for i, u in enumerate(u_list):
            for j, v in enumerate(v_list):
                if u == v:
                    return i+1, j+1
    
    def find_X(self):
        """
        X qiymatni topish
        """
        u, v = self.find_u_v()
        x = (self.find_H() * u - v) % (self.p - 1)
        return x

obj = DiskretLog(19,32,53)
print(f"X = {obj.find_X()}")

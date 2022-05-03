import numpy as np
class cnpj:
    def __init__(self, cnpj):
        self.cnpj_input = cnpj
        self.cnpj = self._clear_cnpj()
        self.cnpj_itens = self.cnpj[:12]
        self.cnpj_cod_in = self.cnpj[12:14]
        self.cnpj_output = self._calc_cnpj_out()
        self.cnpj_cod_out = self.cnpj_output[12:14]

    def _clear_cnpj(self):
        num = ''
        for n in self.cnpj_input:
            if n in ('0','1','2','3','4','5','6','7','8','9'):
                num += n

        return num

    def _cod_test(self,num_value):
        nr = num_value%11
        if nr <=1:
            nt = '0'
        else:
            nt = 11 - nr

        return int(nt)

    def _calc_cnpj_out(self):
        #cnpj
        inv_cnpj = self.cnpj_itens[::-1]
        list_vector = [2,3,4,5,6,7,8,9,2,3,4,5]

        while len(inv_cnpj) < 14:
            #itens_sum = 0.0
            mult_vector = np.array(list_vector, np.int32)

            mult_cnpj = np.array(list(inv_cnpj), np.int32)

            mult = np.sum(mult_vector * mult_cnpj)
            c1 = self._cod_test(mult)
            inv_cnpj = str(c1) + str(inv_cnpj)
            list_vector += [6]

        return inv_cnpj[::-1]

    def cnpj_status(self):
        if self.cnpj == self.cnpj_output:
            return True
        else:
            return False

if __name__ == '__main__':
    tc = cnpj('11.222.333/0001-33')
    print(tc.cnpj_status())
    print(tc.cnpj_input)
    print(tc.cnpj_output)
    print(tc.cnpj_cod_in)
    print(tc.cnpj_cod_out)

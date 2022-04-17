#input_number = input('Informe o número do doc:')
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

        while len(inv_cnpj) < 14:
            itens_sum = 0.0
            k = 2
            for i in inv_cnpj:
                itens_sum += (int(i) * k)
                k+=1

            c1 = self._cod_test(itens_sum)
            inv_cnpj = str(c1) + str(inv_cnpj)

        return inv_cnpj[::-1]

    def cnpj_entrada(self):

        return self.cnpj

    def cnpj_retorno(self):

        return self.cnpj_output

    def cnpj_verificador_entrada(self):

        return self.cnpj_cod_in

    def cnpj_verificador_retorno(self):

        return self.cnpj_cod_out

    def cnpj_status(self):
        if self.cnpj == self.cnpj_output:
            return True
        else:
            return False

if __name__ == '__main__':
    tc = cnpj('06.990.590/0001-23')
    print(tc.cnpj_status())
    print(tc.cnpj_entrada())
    print(tc.cnpj_retorno())
    print(tc.cnpj_verificador_entrada())
    print(tc.cnpj_verificador_retorno())

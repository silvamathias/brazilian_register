#input_number = input('Informe o número do doc:')
class cpf:
    def __init__(self, cpf):
        self.cpf_input = cpf
        self.cpf = self._clear_cpf()
        self.cpf_itens = self.cpf[:9]
        self.cpf_cod_in = self.cpf[9:11]
        self.cpf_output = self._calc_cpf_out()
        self.cpf_cod_out = self.cpf_output[9:11]

    def _clear_cpf(self):
        num = ''
        for n in self.cpf_input:
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

    def _calc_cpf_out(self):
        #cpf
        inv_cpf = self.cpf_itens[::-1]
        while len(inv_cpf) < 11:
            itens_sum = 0.0
            k = 2
            for i in inv_cpf:
                itens_sum += (int(i) * k)
                k+=1

            c1 = self._cod_test(itens_sum)
            inv_cpf = str(c1) + str(inv_cpf)

        return inv_cpf[::-1]

    def cpf_entrada(self):

        return self.cpf

    def cpf_retorno(self):

        return self.cpf_output

    def cpf_verificador_entrada(self):

        return self.cpf_cod_in

    def cpf_verificador_retorno(self):

        return self.cpf_cod_out

    def cpf_status(self):
        if self.cpf == self.cpf_output:
            return True
        else:
            return False

if __name__ == '__main__':
    tc = cpf('111.222.333-96')
    print(tc.cpf_status())
    print(tc.cpf_entrada())
    print(tc.cpf_retorno())
    print(tc.cpf_verificador_entrada())
    print(tc.cpf_verificador_retorno())

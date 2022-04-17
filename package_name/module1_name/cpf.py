input_number = input('Informe o número do doc:')
def clear_number(text_number):
    num = ''
    for n in text_number:
        if n in ('0','1','2','3','4','5','6','7','8','9'):
            num += n

    return num

def cpf_test(num_value):
    nr = num_value%11
    if nr <=1:
        nt = '0'
    else:
        nt = 11 - nr

    return int(nt)

doc = clear_number(input_number)
#cpf
if len(doc) == 11:
    doc_input = doc[:9]
    inv_doc = doc_input[::-1]
    while len(inv_doc) < 11:
        vl_sum = 0.0
        k = 2
        for i in inv_doc:
            vl_sum += (int(i) * k)
            k+=1

        c1 = cpf_test(vl_sum)
        inv_doc = str(c1) + str(inv_doc)

new_doc = inv_doc[::-1]
print(doc)
print(new_doc)

# brazilian_register

Description.
The package brazilian_register is used to:
	- Check brazilian Natural Persons Register number (Cadastro de Pessoa Física - CPF).
	- Check brazilian National Registry of Legal Entities (Cadastro Nacional da Pessoa Jurídica - CNPJ).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install brazilian_register

```bash
pip install brazilian_register
```


## Usage

```python
import brazilian_register as br
```


### To Check a cpf document number.

```python
cpf = br.cpf('cpf number')
print(cpf.cpf_status())
```
True if the verification code is correct or False if not.


#### To get document input.

```python
# as was informed
print(cpf.cpf_input)

# only numbers
print(cpf.cpf)
```


#### To get verification code input.

```python
print(cpf.cpf_cod_in)
```


#### To get number output.

```python
print(cpf.cpf_output)
```


#### To get verification code output.

```python
print(cpf.cpf_cod_out)
```

### To Check a cnpj document number.

```python
cnpj = br.cnpj('cnpj number')
print(cnpj.cnpj_status())
```
True if the verification code is correct or False if not.


#### To get document input.

```python
# as was informed
print(cnpj.cnpj_input)

# only numbers
print(cnpj.cnpj)
```


#### To get verification code input.

```python
print(cnpj.cnpj_cod_in)
```


#### To get number output.

```python
print(cnpj.cnpj_output)
```


#### To get verification code output.

```python
print(cnpj.cnpj_cod_out)
```


## Author

Phelipe Mathias


## License

[MIT](https://choosealicense.com/licenses/mit/)

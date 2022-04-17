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
from brazilian_register.cnpj import cnpj_tools
cnpj_tools.cnpj('cnpj number')
```
```python
from brazilian_register.cpf import cpf_tools
cpf_tools.cpf('cpf number')
```

To Check document number.

```python
check = cpf('cpf number')
print(check.cpf_status())
```
True if the verification code is correct or False if not.

To get number input.

```python
print(check.cpf_entrada())

```

To get verification code input.

```python
print(check.cpf_verificador_entrada())
```
To get number output.

```python
print(check.cpf_retorno())
```
To get verification code output.

```python
print(check.cpf_verificador_retorno())
```

## Author
Phelipe Mathias

## License
[MIT](https://choosealicense.com/licenses/mit/)

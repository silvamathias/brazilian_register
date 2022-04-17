from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="brazilian_register",
    version="0.0.1",
    author="Phelipe Mathias",
    author_email="silvamathias@gmail.com",
    description="Tools to test brazilian register numbers (CPF or CNPJ)",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/silvamathias/dio_desafio_ciacao_pacote_python"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)

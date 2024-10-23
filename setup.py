# setup.py
from setuptools import setup, find_packages

setup(
    name='prime_package',  # Название вашего пакета
    version='0.1',  # Версия пакета
    packages=find_packages(),  # Автоматически находит пакеты
    description='A package for generating prime numbers',  # Описание пакета
    author='inishevv',  # Ваше имя
    author_email='einishev@bk.ru',  # Ваш email
    url='https://github.com/inishevv/primelist.git',  # URL вашего репозитория
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Минимальная версия Python
)
from setuptools import setup, find_packages

setup(
    name="math_graphics",
    version="0.1.0",
    packages=find_packages(include=['math_graphics', 'math_graphics.*']),
    install_requires=[],
    author="Jean kronabuer de moura",
    description="Biblioteca profissional de matemática para computação gráfica",
    python_requires=">=3.7",
)
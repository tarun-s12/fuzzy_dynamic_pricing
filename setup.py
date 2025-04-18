from setuptools import setup, find_packages

setup(
    name="fuzzy_pricing",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-fuzzy",
        "matplotlib",
    ],
    description="Dynamic pricing system using fuzzy logic",
    author="Developer",
    python_requires=">=3.6",
) 
from setuptools import setup, find_packages

setup(
        name='analysisutils',
        version='1.0',
        packages=find_packages(),
        install_requires=[
            'pandas',
            'psutil',
            'plotly',
            'scikit-learn',
            'cloudpickle'
            ],
        )

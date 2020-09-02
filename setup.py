from setuptools import setup, find_packages
requirements = [
    'celery-4.4.7',
    'requests-2.24.0'
]
# need to hanlde other paramers of setup() method
setup(
    name="fes",
    version="1.0",
    packages=find_packages(),
    install_requires=requirements
)

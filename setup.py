from setuptools import setup, find_packages

setup(
    name='FakeFECProject',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Flask==2.1.0',
        'psycopg2==2.9.3',
        'requests==2.26.0',
        'PyCryptodome==3.11.0',
        'SQLAlchemy==1.4.25'
    ],
    entry_points={
        'console_scripts': [
            'run_app = app:main'
        ]
    }
)

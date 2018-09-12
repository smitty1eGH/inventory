from setuptools import setup

setup(
    name='inventory',
    version='3.0.2',
    description='A basic inventory management web app',
    url='https://github.com/williamjacksn/inventory',
    author='William Jackson',
    author_email='william@subtlecoolness.com',
    install_requires=['Flask', 'Flask-OAuth2-Login', 'Flask-SSLify', 'psycopg2', 'waitress'],
    packages=['inventory'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'inventory = inventory.inventory:main'
        ]
    }
)

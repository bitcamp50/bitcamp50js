from setuptools import setup

setup(
    name='check50_custom_js',
    version='0.1.0',
    description='Custom JavaScript extension for check50.',
    author='Giorgi Tarsaidze',
    author_email='tarsaidzeg@gmail.com',
    url='https://github.com/bitcamp50/bitcamp50js',
    install_requires=[
        'python-bond>=1.4,<2',
        'check50>=3,<4'
    ],
    py_modules=['check50_custom_js'],
    classifiers=[
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Utilities'
    ],
    python_requires='>=3.6',
)

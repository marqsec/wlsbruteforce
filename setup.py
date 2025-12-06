from setuptools import setup, find_packages

setup(
    name='wlsbruteforce',
    version='0.1.0',
    packages=find_packages(),
    description='A simple, educational Python module for demonstrating password generation via bruteforce.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='marqsec',
    author_email='marqlinux@gmail.com',
    url='https://github.com/marqsec/wlsbruteforce', 
    install_requires=[
        
    ],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
)

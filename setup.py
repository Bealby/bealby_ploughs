from setuptools import setup, find_packages

setup(
    name='bealby_ploughs',  # Replace with your package name
    version='1.0.0',  # Initial version
    author='Murray Bealby',  # Your name
    author_email='bealbyploughs@gmail.com',  # Your email
    description='Bealby Ploughs',  # Short description
    long_description=open('README.md').read(),  # Read long description from README
    long_description_content_type='text/markdown',  # Format of the long description
    url='https://github.com/bealby/bealby_ploughs',  # URL to your project
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[  # List of dependencies
        'numpy',  # Example dependency
    ],
    classifiers=[  # Classifiers for the package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
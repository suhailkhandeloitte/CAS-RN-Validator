from setuptools import setup, find_packages

setup(
    name='casrnvalidator',
    version='0.1.0',
    description='A Python package for validating CAS Registry Numbers',
    long_description=open('README.md').read(),  # Read the README file for long description
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/CAS_RN_Validator',  # URL to your package repository
    packages=find_packages(where='src'),  # Look for packages under the 'src' directory
    package_dir={'': 'src'},  # Specify the root package directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Define Python version requirement
    install_requires=['pandas'],  # Add any dependencies your package needs
    package_data={'cas_rn_validator': ['data/*.csv']},
    include_package_data=True,
)

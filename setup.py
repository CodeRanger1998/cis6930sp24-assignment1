from setuptools import setup, find_packages

setup(
	name='assignment1',
	version='1.0',
	author='Pranil Ingle',
	authour_email='inglepranil@ufl.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
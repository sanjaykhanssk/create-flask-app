from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='create-flask-app',
  version='0.0.1',
  description=' A handy tool to start your flask project in 0 time ',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Sanjay Khan ssk',
  author_email='sanjaykhanssk@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['flask','flask-app','create-flask-app'],
  packages=find_packages(),
  install_requires=[''] 
)

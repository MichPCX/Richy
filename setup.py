from setuptools import setup

setup(name='richy',
      version='0.50beta',
      description='Richy - command line personal assistant for GNU/Linux.',
      url='https://github.com/michpcx/Richy',
      author='michpcx',
      author_email='michpcx@protonmail.ch',
      license='GNU',
      py_modules=['richy_main'],
      entry_points={
               'console_scripts': ['richy=richy_main:main'],
           },
      install_requires=[
          'guessit<2',
          'terminaltables',
          'tqdm',
          'colorama',
	  'lxml',
	  'docopt',
	  'unipath',
	  'configparser',
	      'wikipedia'
      ],
      keywords=['richy', 'WolframAlpha', 'command', 'line', 'linux', 'python'],
      classifiers=[
          'Environment :: Console',
          'License :: GNU License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],)

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='pro_clash',
      version='0.1',
      description='Processing PRO-CLASH experiments results',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Biology :: RNA-seq',
      ],
      scripts=[
        'bin/map_chimeric_fragments.py', 'bin/map_single_fragments.py',
        'bin/pro_clash_significant_regions.py'],
      url='http://github.com/asafpr/pro_clash',
      author='Asaf Peer',
      author_email='asafpr@gmail.com',
      license='MIT',
      packages=['pro_clash'],
      install_requires=[
        'scipy', 'numpy'],
      include_package_data=True,
      zip_safe=False)

from distutils.core import setup

# Set doc for package
with open("README.md", "r") as fh:
    long_description = fh.read()

# Set package version
version = '1.0.0'

setup(name='MMLL',
      version=version,
      description='MMLL API',
      long_description=long_description,
      author='Treelogic',
      author_email='jose.fernandez@treelogic.com',
      url='https://github.com/Musketeer-H2020/MMLL-Robust',
      packages=setuptools.find_packages(),
      install_requires=['pandas==1.1.4',
                        'seaborn==0.10.1',
                        'gmpy2==2.0.8',
                        'onnxruntime==1.7.0',
                        'tqdm==4.61.0',
                        'sklearn==0.0',
                        'skl2onnx==1.8.0',
                        'sklearn2pmml==0.71.1',
                        'boto3==1.17.92',
                        'paramiko==2.7.2',
                        'pympler',
                        'dill',
                        'phe',
                        'graphviz',
                        'tensorflow==2.4.1',
                        'tf2onnx'],
      dependency_links=['http://github.com/IBM/pycloudmessenger/archive/v0.7.1.tar.gz']
      )

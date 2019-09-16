from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pysubmarine',  
     version='0.1',
     packages=find_packages(exclude=['tests', 'tests.*']),
     install_requires=[
        'six>=1.10.0',
        'waitress; platform_system == "Windows"',
        'gunicorn; platform_system != "Windows"',
        'numpy',
        'pandas',
        'sqlparse',
        'sqlalchemy',
    ],
     scripts=['pysubmarine'] ,
     description="A SDK for submarine",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='Apache License 2.0',
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
     url="https://github.com/hadoopsubmarine/submarine"
 )

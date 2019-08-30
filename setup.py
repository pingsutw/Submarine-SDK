import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='pysubmarine',  
     version='0.1',
     scripts=['pysubmarine'] ,
     author="Kevin Su",
     author_email="pingsutw@gmail.com",
     description="A SDK for submarine",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/hadoopsubmarine/submarine",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
 )

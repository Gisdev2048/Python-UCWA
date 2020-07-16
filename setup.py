import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-ucwa",
    version="1.0.0",
    author="jnlasher",
    description="Files for connecting to the REST API of Skype for Business",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gisdev2048/Python-UCWA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
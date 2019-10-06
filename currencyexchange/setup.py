import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="currencyexchange-pkg-surajkarki66",
    version="0.0.1",
    author="Suraj Karki",
    author_email="suraj.karki500@gmail.com",
    description="This is a simple python package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/surajkarki66/Python-Advance/tree/master/APIs%20in%20Python/libs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
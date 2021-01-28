import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matHandler-HiroMiyawaki", # Replace with your own username
    version="0.1.0",
    author="Hiro Miyawak at Osaka City Univ",
    author_email="miyawaki625@gmail.com",
    description="A simplemodule to read matlab files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HiroMiyawaki/matHandler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
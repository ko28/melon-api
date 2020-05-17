import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="melonapi", 
    version="0.0.1",
    author="Daniel Ko",
    author_email="danielhbko@gmailc.om",
    description="A small Melon api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ko28/melonApi/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="melonapi", 
    version="0.0.2",
    author="Daniel Ko",
    author_email="danielhbko@gmail.com",
    description="A small Melon api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ko28/melon-api/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=['Flask', 'requests', 'lxml', 'beautifulsoup4'],
    python_requires='>=3.6',
)

import setuptools
with open ("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "Rock_Paper_Scissors-arivvid27",
	version = "0.0.1",
	author = "arivvid27",
	author_email = "arivvid27@outlook.com",
	description = "A 'Rock Paper Scissors' game.",
	long_description = long_description,
	long_description_content_type="text/markdown",
	url = "https://github.com/arivvid27/Rock-Paper-Scissors",
	packages = setuptools.find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	],
	python_requires = '>=3.6',
)
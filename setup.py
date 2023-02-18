from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gpt_mirror",
    version="0.1.0",
    author='lightblue',
    author_email='lbcoder@hotmail.com',
    description='a tiny chatgpt mirror site',
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/weilancys/gpt_mirror",
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.7.1',
    install_requires = [
        'flask',
        'openai',
        'waitress',
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
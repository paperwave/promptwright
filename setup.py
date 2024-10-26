from setuptools import find_packages, setup

setup(
    name="promptsmith",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "requests==2.32.3",
        "tqdm==4.66.5",
        "urllib3==2.2.3",
    ],
    author="Luke Hinds",
    author_email="luke@stacklok.com",
    description="LLM based Synthetic Data Generation",
    long_description=open("README.md").read(),  # noqa: SIM115
    long_description_content_type="text/markdown",
    url="https://github.com/StacklokLabs/promptsmith",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
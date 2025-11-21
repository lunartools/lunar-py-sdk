from setuptools import setup, find_packages

setup(
    name="lunartools-sdk",
    version="1.0.1",
    description="Official SDK for Lunar Tools API",
    author="Lunar Tools",
    author_email="support@lunartools.co",
    url="https://github.com/lunartools/lunartools-python-sdk",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="lunar tools sdk api inventory orders",
)
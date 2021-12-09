from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-charts-plugin",
    version="0.0.3",
    description="MkDocs plugin to add charts from data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs plugin",
    url="https://github.com/timvink/mkdocs-charts-plugin",
    author="Tim Vink",
    author_email="vinktim@gmail.com",
    license="MIT",
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["mkdocs>=1.1", "pymdown-extensions>=9.1"],
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": ["charts = mkdocs_charts_plugin.plugin:ChartsPlugin"]
    },
)

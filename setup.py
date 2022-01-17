from setuptools import setup, find_packages
from pathlib import Path


version = 0.3
with Path('README.md').open() as readme:
    readme = readme.read()


setup(
    name='pretty-doc',
    version=version if isinstance(version, str) else str(version),
    keywords="pretty print, doc object, composable text objects", # keywords of your project that separated by comma ","
    description="A simple document rendering system in Python", # a concise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3.6.0',
    url='https://github.com/thautwarm/pretty-doc',
    author='thautwarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    install_requires=[
        "dataclasses ; python_version < '3.7'"
    ], # dependencies
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    zip_safe=False,
)



"""Setup för RightsGuide."""

from setuptools import setup, find_packages

setup(
    name="rightsguide",
    version="1.0.0",
    description="Guide till LSS, assistansersättning och vårdstöd",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="RightsGuide",
    license="GPL-3.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "PyGObject>=3.42",
    ],
    entry_points={
        "console_scripts": [
            "rightsguide=rightsguide.app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Natural Language :: Swedish",
    ],
)

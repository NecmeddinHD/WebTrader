from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as f:
    descript=f.read()
setup(
    name="WebTrader",
    version="1.1.0",
    packages=find_packages(),
    install_requires=["pyperclip", "requests"],
    description="You can quickly open websites from your computer on your phone or tablet.",
    entry_points={
         "console_scripts": [
              "webtrader = webtrader:main" 
        ]
    },
    long_description=descript,
    long_description_content_type="text/markdown",
    author="NecmeddinHD",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Topic :: Communications :: Chat",
    "Intended Audience :: Developers",
    "Development Status :: 4 - Beta",
    "Framework :: AsyncIO",
    "Environment :: Console",
],
keywords="telegram bot share link device transfer",
)
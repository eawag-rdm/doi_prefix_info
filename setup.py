import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='doi_prefix_info',
    description=("Returns information about registartion agency / datacenter "
                 + "for Datacite prefixes"),
    url="",
    install_requires=[
        'requests>=2.22.0',
        'docopt>=0.6.2'],
    entry_points={
      'console_scripts': [
        'doi_prefix_info=doi_prefix_info.doi_prefix_info:main'
      ]
    },
    python_requires='>=3',
    version="1.0.0",
    author="Harald von Waldow",
    author_email="harald.vonwaldow@eawag.ch",
    #long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
    ],
)




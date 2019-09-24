from setuptools import setup
requirements = [
"aiohttp",
]

setup(
    name='soks5-parser',
    version='2.0',
    description=" Python aioparser",
    author="dark0ghost",
    url='https://github.com/dark0ghost/AioCentralBankRuApi',
    packages=[
        'AioCentralBankRuApi',
    ],
    package_dir={'AioCentralBankRuApi':
                     'AioCentralBankRuApi'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT License",
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)

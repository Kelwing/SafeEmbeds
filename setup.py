from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()

setup(
    name='SafeEmbeds',
    version='0.1dev',
    author='Kelwing',
    packages=['safeembeds',],
    license='GPLv3',
    description='A monkey patcher that makes embeds in Discord.py safe at runtime.',
    url='https://github.com/kelwing/SafeEmbeds',
    python_requires='>=3.6.6',
    install_requires=['discord.py'],
    long_description=readme,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)

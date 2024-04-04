from setuptools import setup

setup(
    name='django-auto-timestamps-model',
    version='1.0.0',
    license='MIT',
    description='Django model for adding automatic timestamps in models.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Santiago',
    url='https://github.com/santiagopuerta/django-auto-timestamps-model',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
    packages=["django_auto_timestamps_model"],
    include_package_data=True,
    install_requires=["Django>=1.4"],
)
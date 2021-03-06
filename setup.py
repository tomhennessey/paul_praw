import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="subredditscraper_tomhennessey",
        version="0.0.1",
        author="Tom Hennessey",
        author_email="tomahennessey@gmail.com",
        description="A small subreddit scraper",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/tomhennessey/Subreddit-Scraper",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        entry_points={
            'console_scripts': [
                'subredditscraper=subredditscraper.scrape:main'
            ]
        },
        python_requires='>=3.6',
)

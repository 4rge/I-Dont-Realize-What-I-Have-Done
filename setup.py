from setuptools import setup, find_packages

setup(
    name='mind_model_chatbot',
    version='0.1.0',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A simple chatbot model using local GPT with memory management.',
    long_description=open('README.md').read(),  # Ensure you create a README.md file in your project
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mind_model',  # Replace with your repository URL
    packages=find_packages(),  # Automatically find and include all packages in the project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update as necessary
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify your required Python version
    install_requires=[
        'torch>=1.7.0',  # Specify the version of PyTorch compatible with your environment
        'transformers>=4.0.0',  # Specify version compatibility for Hugging Face Transformers
    ],
    entry_points={
        'console_scripts': [
            'mind_model=mind_model.main:run_chatbot',  # Points to the main function for launching the chatbot
        ],
    },
)

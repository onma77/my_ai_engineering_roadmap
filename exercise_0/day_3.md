## gpu setup and cloud
* its purpose is to understand how computers perform AI calculation and how to access additional computing power.

- GPU: the processor well suited to parallel calculation.
- CPU: the computer's general purpose processor.
- CUDA: NVIDIA's platform for GPU computing.
- PyTorch: a python library for machine learning.
- Cloud GPUs: remote computing resources you can rent or access online.

## API and  Keys
* its purpose is to learn how to communicate with external services, including AI models.

- an API(application programming interface) allows one spoftware application to request services or data from another.

# docker for AI
+ its purpose is to package application and their dependencies into containers

- Docker helps solve this problem by packaging an application and its required components into a container.

- Docker: A platform for building and running containers.
- Dockerfile: Instructions for creating a container image.
- Image: A package containing the application and its required environment.
- Container: A running instance of an image.
- Docker Compose: A tool for configuring applications with multiple services.

# data management
* its purpose is to learn how to load, process, and manage datasets efficiently.

- CSV and JSON: Common formats for storing structured data.
- Loading: Reading data into your application.
- Streaming: Processing data incrementally rather than loading everything into memory.
- Caching: Keeping frequently used data available to reduce repeated work.
- Hugging Face Datasets: A library for working with datasets used in machine learning.

# terminal and shell
* its purpose it to control your computer and process information using command linne tool.

- the terminal allows you to interact with your operating system by entering commands instead of relying entirely on graphical interfaces.

- pwd — Display your current directory.
- ls — List files and directories.
- cd — Change directories.
- grep — Search text for matching patterns.
- |— Pass one command's output into another command.
- (>— Redirect output into a file.)
- (>>— Append output to a file.)

# linux for AI
* understanding the linux operating system and perform essential file operations.

- linux is widely used  for servers, cloud computing,AI infrastructure and software deployment.
* understanding linux makes it easier to work with servers, cloud environnments, and AI development tools.

# debugging and profiling 
its Purpose Learn how to identify errors, investigate incorrect results, and measure program performance.

- Debugging helps you discover why something is wrong. 
- Profiling helps you understand where your program spends time or memory.

- Breakpoints: Pause execution at a particular line.
- breakpoint(): Enter Python's interactive debugger.
- Logging and debug output: Inspect values while your program runs.
- Profiling: Measure execution time and resource usage.
- Tensor shapes and data types: Check that AI operations receive the expected inputs.
for example:

def calculate_total(price, quantity):
    breakpoint()
    return price * quantity

print(calculate_total(100, 3))

- When execution reaches breakpoint(), Python pauses so you can inspect variables and investigate the program's behavior.
- Don't assume your program is correct just because it runs. Verify its results and investigate unexpected behavior.

# python for AI engineering 

* Strong Python fundamentals help you write AI code that is more reliable, reproducible, and easier to maintain.

- Collections: Lists, tuples, dictionaries, and sets.
- Functions and classes: Organizing reusable code.
- Type hints: Communicating the expected types of values.
- List comprehensions and generators: Processing collections efficiently.
- Dataclasses: Defining structured records.
- CSV and JSON: Loading and saving datasets.
- Random seeds: Making randomized experiments reproducible.
- NumPy: Performing numerical operations efficiently.
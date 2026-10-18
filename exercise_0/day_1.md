## lesson for the day.
# dev environment.
1. system foundation and setup.
System foundation is the process of preparing your computer with the operating system and essential tools required for software development.
* installation of operating system, for ubuntu(sudo apt update && sudo apt install -y build-essential git curl wget unzip).

## What is Ubuntu?
Ubuntu is a Linux-based operating system commonly used for backend development, AI, cybersecurity, and cloud computing.

Purpose of each tool:
- apt: Installs and manages Ubuntu packages.
- build-essential: Provides essential compilation tools.
- git: Tracks code changes and supports collaboration.
- curl: Transfers data and makes HTTP requests.
- wget: Downloads files.
- unzip: Extracts ZIP archives.

* Key terms:
- Terminal: Interface for entering commands.
- Shell: Program that interprets commands.
- Operating system: Software that manages computer hardware and applications.

2. python with Uv.
* we use UV, it is more faster than 
Uv refers to a fast, all in one python package and project manager written in rust

* to verify.
import sys
print(f"Python {sys.version}")

  import numpy as np
  print(f"NumPy {np.__version__}")
  a = np.array([1, 2, 3])
  print(f"Vector: {a}, dot product with itself: {np.dot(a, a)}")

* Key terms:
- Package: Reusable code that can be installed.
- Virtual environment: An isolated environment for project dependencies.
- NumPy: A Python library for numerical computing and arrays.  

3. node.js with PNPM : it represents one of the most efficient setup for modern javascript and typescript development(Node.js is a JavaScript runtime that allows JavaScript to run outside a web browser. It is commonly used for backend development and AI applications.)

* Key terms:
- Node.js: Runs JavaScript outside browsers.
- PNPM: Manages JavaScript and TypeScript dependencies.
- TypeScript: JavaScript with static typing.
- MCP: Model Context Protocol, which enables compatible AI applications to interact with external tools and data sources.
* for typescript lessons (agent, mcp servers, web apps)

   curl -fsSL https://fnm.vercel.app/install | bash
   fnm install 22
   fnm use 22

   npm install -g pnpm

   node -e "console.log('Node', process.version)"

 * + fnm stands for FAST NODE MANAGER.

 * + the fnm installer checks for unzip and exists with not installing fnm due to missing dependencies

4. rust
for performance-critical lessons, memory safety, and reliable software.
It is useful for performance-sensitive applications, systems programming, and developer tools. (inference, system)

   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

   rustc --version
   cargo --version

Key terms:
- rustc: Rust compiler.
- Cargo: Rust's package manager and build tool.
- Ownership: A Rust mechanism for managing memory safely.   

5. julia 
used for math-heavy lessons where julia shines. julia is a programming language designed for high performance numerical and scientific computing.
curl -fsSL https://install.julialang.org | sh

   julia -e 'println("Julia ", VERSION)'

6. GPU setup(linux/windows)
   A Graphics Processing Unit (GPU) performs many operations in parallel. GPUs are commonly used for AI training, deep learning, and other computationally intensive tasks.

   A Graphics Processing Unit (GPU) performs many operations in parallel. GPUs are commonly used for AI training, deep learning, and other computationally intensive tasks.

   nvidia-smi
   uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

   Key terms:
- GPU: Processor suited to many parallel computations.
- CUDA: NVIDIA GPU computing platform.
- PyTorch: Machine learning framework.
- Inference: Using a trained model to generate predictions or outputs.
A GPU is not required for every AI application. Many beginner lessons work on a CPU.

7. verifying the route i want to start.
it means verifying the route that my computer has the tools and version required for my choosen lesson.
# PromptSmith - Large Dataset Generation

[![Tests](https://github.com/StacklokLabs/promptsmith/actions/workflows/test.yml/badge.svg)](https://github.com/StacklokLabs/promptsmith/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/StacklokLabs/promptsmith/branch/main/graph/badge.svg)](https://codecov.io/gh/StacklokLabs/promptsmith)
[![Python Version](https://img.shields.io/pypi/pyversions/promptsmith.svg)](https://pypi.org/project/promptsmith/)


<img src="image.png" width="350" height="350">


PromptSmith is a Python library from [Stacklok](https://stacklok.com) designed for generating large datasets using a local LLM via Ollama. The library offers a flexible and easy-to-use interface to
enabling users the ability to generate structured datasets.

This was inspired by the [redotvideo/pluto](https://github.com/redotvideo/pluto),
in fact it started as fork, but ended up largley being a re-write, but with a
focus on generating large datasets against a local LLM model, as opposed to OpenAI 
where costs can be prohibitivly expensive.

## Features

- **Local LLM Client Integration**: interact with Ollama models using the `LocalDataEngine`.
- **Test and Validate Connections**: Verify a connection with the LLM and ensure models are operational available before generating datasets.
- **Configurable Instructions and Prompts**: Define custom instructions and system prompts to fine-tune the behavior of the LLM.
- **Push to Hugging Face**: Push the generated dataset to Hugging Face in parquet
format.

## Model Compatibility

The library should work with most LLM models. It has been tested with the
following models so far:

- **LLaMA3**: The library is designed to work with the LLaMA model, specifically the `llama3:latest` model.
- **Mistral**: The library is compatible with the Mistral model, which is a fork of the GPT-3 model.

## Getting Started

### Prerequisites

- Python 3.8+
- `promptsmith` library installed
- Ollama CLI installed and running
- Model `llama3:latest` downloaded via Ollama

### Installation

To install the prerequisites, you can use the following commands:

```bash
pip install promptsmith
ollama serve
ollama pull llama3:latest
```

### Example Usage

There are a few examples in the `examples` directory that demonstrate how to use
the library to generate different topic based datasets.

### Running the Example

To run the example:

1. Ensure you have started Ollama by running `ollama serve`.
2. Verify that the required model is downloaded (e.g. `llama3.2:latest`).
3. Execute one of the available examples:

   ```bash
   python example/creative_writing.py
   ```

### Prompt Output Examples

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are tasked with designing an immersive virtual reality experience that transports users to a fantastical world of wonder."
    },
    {
      "role": "user",
      "content": "Create a descriptive passage about a character discovering their hidden talents."
    },
    {
      "role": "assistant",
      "content": "As she stared at the canvas, Emma's fingers hovered above the paintbrushes, as if hesitant to unleash the colors that had been locked within her. The strokes began with bold abandon, swirling blues and greens merging into a mesmerizing dance of light and shadow. With each passing moment, she felt herself becoming the art – her very essence seeping onto the canvas like watercolors in a spring storm. The world around her melted away, leaving only the vibrant symphony of color and creation."
    }
  ]
}
```

### Library Overview

#### Classes

- **Dataset**: A class for managing generated datasets.
- **LocalDataEngine**: The main engine responsible for interacting with the LLM client and generating datasets.
- **LocalEngineArguments**: A configuration class that defines the instructions, system prompt, model name temperature, retries, and prompt templates used for generating data.
- **OllamaClient**: A client class for interacting with the Ollama API.
- **HFUploader**: A utility class for uploading datasets to Hugging Face.

#### Methods

- **`list_local_models()`**: Lists all available models in your local Ollama instance.
- **`create_data()`**: Generates data based on the provided configuration and parameters such as `num_steps` and `batch_size`.
- **`save(filename)`**: Saves the generated dataset to a JSONL file.

### Troubleshooting

If you encounter any errors while running the script, here are a few common troubleshooting steps:

1. **Restart Ollama**:  
   ```bash
   killall ollama && ollama serve
   ```

2. **Verify Model Installation**:  
   ```bash
   ollama pull {model_name}
   ```

3. **Check Ollama Logs**:  
   Inspect the logs for any error messages that might provide more context on
   what went wrong, these can be found in the `~/.ollama/logs` directory.

### Contributing

If something here could be improved, please open an issue or submit a pull request.

### License

This project is licensed under the Apache 2 License. See the `LICENSE` file for more details.
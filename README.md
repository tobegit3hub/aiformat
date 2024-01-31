# AI Format

The powerful "Swiss Army Knife" which leverages LLM models and prompt engineering to format anything.

There are common scenarios to use [aiformat](https://github.com/tobegit3hub/aiformat):

* Format source code like [yapf](https://github.com/google/yapf) but for all programming languages.
* Quickly translate text in command-line for English, Chinese or other natural languages.
* Correct spelling and grammar for all documents in entire project.
* Generate international documents in different languages with one command.

## Install

```
pip install aiformat
```

## Usage

Set `OPENAI_API_KEY` environment variable for ChatGPT models.

```
export OPENAI_API_KEY=sk-xxx
```

Run `aiformat` in command-line.

```
$ aiformat --help
Usage: aiformat [OPTIONS] FILE_OR_TEXT

Options:
  -d, --diff           Print the diff for the fixed source.
  -i, --inplace        Make changes to files in place.
  -r, --recursive      Run recursively over directories.
  -vv, --verbose       Print out file names while processing.
  -c, --command TEXT   Use the command, pass -vv to check supported commands.
  --model TEXT         Use the LLM model(gpt-3.5-turbo or gpt-4-1106-preview).
  --temperature FLOAT  Set temperature for the LLM model.
  --help               Show this message and exit.
```

You can translate text or format source code easily.

```
# Use "chat" command to do anything
aiformat "implmenet a python script to format python code"

# Use "-r" to format all source files in subdirectories
aiformat -c format_code -r ./aiformat --diff --inplace

# Use "to_chinese" to translate text in command-line
aiformat -c to_chinese "hello world"

# Use "--diff" and "--inplace" to view diff and make changes inplace
aiformat -c correct_spelling ./README.md --diff --inplace
```

## Built-in Commands

| Command | Description |
| ------- | ----------- |
| chat | Chat with LLM models like ChatGPT. |
| format_code | Format the source code according to its programming language. |
| format_doc | Format the document with common best practices. |
| to_chinese | Translate the text into Chinese and maintain the formatting. |
| to_english | Translate the text into English and maintain the formatting. |
| explain_code | Explain the source code in simple terms. |
| gen_ut | Generate the source code of unit test for input file. |
| correct_spelling | Correct the spelling errors for input file. |
| optimize_code | Use the best practices to optimize the source code. |

The built-in commands are defined in [commands.yaml](./aiformat/prompt/commands.yaml). You can extend new command and prompt in local `~/.aiformat/commands.yaml`.
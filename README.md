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
aiformat -c to_chinese "hello world"

aiformat -c format_code -r ./aiformat --diff --inplace

aiformat -c correct_spelling ./README.md --diff --inplace
```

## Built-in Commands

| Command | Description |
| ------- | ----------- |
| format_content | Format arbitary content by LLM models. |
| format_code | Format the source code according to its programming language. |
| format_doc | Format document |
| format_doc | Format document |
| format_doc | Format document |
| format_doc | Format document |
| format_doc | Format document |
| format_doc | Format document |

The built-in commands are define in [commands.yaml](./aiformat/prompt/commands.yaml). You can extend new command and prompt in local `~/.aiformat/commands.yaml`.
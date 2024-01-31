# AIFormat

The AI Formatter which leverages LLM models for source code and documents.

## Install

```
pip install aiformat
```

## Usage

Set `OPENAI_API_KEY` environment variable to use the LLM models.

```
export OPENAI_API_KEY=sk-xxxxxx
```

Use `aiformat` command and update prompt in `~/.aiformat/commands.yaml` if needed.

```
Usage: aiformat [OPTIONS] FILE_OR_TEXT

Options:
  -d, --diff           Print the diff for the fixed source.
  -i, --inplace        Make changes to files in place.
  -r, --recursive      Run recursively over directories.
  -vv, --verbose       Print out file names while processing.
  -c, --command TEXT   Use the command to exceute, use -vv to check supported commands.
  --model TEXT         Use the LLM model, could be gpt-3.5-turbo or gpt-4-1106-preview.
  --temperature FLOAT  Set temperature for the LLM model.
  --help               Show this message and exit.
```

## Commands

| Command | Description |
| --------- | ------------- |
| format_doc | Format document |


## Examples

### Format code

```
aiformat ./main.py
```

### Format document

```
aiformat --command format_doc ./README.md
```

### Translate document to Chinese

```
aiformat --command translate_to_chinese ./README.md
```

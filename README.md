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

Use `aiformat` command and update prompt in `aiformat_commands.yaml` if needed.

```
Usage: aiformat [OPTIONS] FILES

Options:
  -d, --diff          print the diff for the fixed source
  -i, --inplace       make changes to files in place
  -r, --recursive     run recursively over directories
  -p, --parallel      run in parallel when formatting multiple files
  -vv, --verbose      print out file names while processing
  -c, --command TEXT  use the command to exceute, check commands in yaml file
  -m, --model TEXT    use the LLM model, default is gpt-3.5-turbo
  --help              Show this message and exit.
```

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

# AIFormat

The AI Formatter with LLM models for code and documents.

## Install

```
pip install aiformat
```

## Usage

```
Usage: aiformat.py [OPTIONS] FILES

Options:
  -d, --diff          print the diff for the fixed source
  -i, --inplace       make changes to files in place
  -r, --recursive     run recursively over directories
  -p, --parallel      run in parallel when formatting multiple files
  -vv, --verbose      print out file names while processing
  -c, --command TEXT  use the command to exceute, check commands in yaml file
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

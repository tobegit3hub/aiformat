# AI Format

* [英文](./README.md)
* [中文](./README_zh.md)

## 简介

这是一个强大的“瑞士军刀”，利用LLM模型和提示工程来格式化任何内容。

使用 [aiformat](https://github.com/tobegit3hub/aiformat) 的常见场景包括：

* 像 [yapf](https://github.com/google/yapf) 一样为所有编程语言格式化源代码。
* 快速在命令行中翻译英文、中文或其他自然语言的文本。
* 为整个项目中的所有文档纠正拼写和语法错误。
* 用一条命令生成不同语言的国际文档。

## 安装

```
pip install aiformat
```

## 使用方法

为ChatGPT模型设置`OPENAI_API_KEY`环境变量。

```
export OPENAI_API_KEY=sk-xxx
```

在命令行中运行`aiformat`。

```
$ aiformat --help
用法: aiformat [OPTIONS] COMMAND FILE_OR_TEXT

选项:
  -d, --diff           打印修复后源代码的差异。
  -i, --inplace        直接修改文件。
  -r, --recursive      递归运行目录下的文件。
  -vv, --verbose       处理时打印文件名。
  --model TEXT         使用LLM模型(gpt-3.5-turbo或gpt-4-1106-preview)。
  --temperature FLOAT  设置LLM模型的温度。
  --help               显示此帮助信息并退出。
```

您可以轻松地翻译文本或格式化源代码。

```
# 使用“-r”来格式化子目录中的所有源文件
aiformat format_code -r ./aiformat --diff --inplace

# 使用“to_chinese”在命令行中翻译文本
aiformat to_chinese "hello world"

# 使用“--diff”和“--inplace”查看差异并直接进行更改
aiformat correct_spelling ./README.md --diff --inplace
```

## 内置命令

| 命令 | 描述 |
| ------- | ----------- |
| chat | 与LLM模型（如ChatGPT）聊天。 |
| format_code | 根据编程语言格式化源代码。 |
| format_doc | 使用常见的最佳实践格式化文档。 |
| to_chinese | 将文本翻译为中文并保持格式。 |
| to_english | 将文本翻译为英文并保持格式。 |
| explain_code | 用简单的术语解释源代码。 |
| gen_ut | 为输入文件生成单元测试的源代码。 |
| correct_spelling | 为输入文件纠正拼写错误。 |
| optimize_code | 使用最佳实践优化源代码。 |

运行以下命令以查看所有内置命令。

```
aiformat commands ''
```

内置命令在 [commands.yaml](./aiformat/prompt/commands.yaml) 中定义。您可以在本地的 `~/.aiformat/commands.yaml` 中扩展新的命令和提示。
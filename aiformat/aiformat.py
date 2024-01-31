#!/usr/bin/env python3

import os
import shutil
import click
import yaml
from jinja2 import Template

from . import chatgpt_util
from . import diff_util
from .print_util import system_print


@click.command()
@click.argument('file_or_text', required=True)
@click.option('-d', '--diff', is_flag=True, help='Print the diff for the fixed source.')
@click.option('-i', '--inplace', is_flag=True, help='Make changes to files in place.')
@click.option('-r', '--recursive', is_flag=True, help='Run recursively over directories.')
@click.option('-vv', '--verbose', is_flag=True, help='Print out file names while processing.')
@click.option('-c', '--command', type=click.STRING, default="chat", help='Use the command, pass -vv to check supported commands.')
@click.option('--model', type=click.STRING, default="gpt-3.5-turbo", help='Use the LLM model(gpt-3.5-turbo or gpt-4-1106-preview).')
@click.option('--temperature', type=click.FLOAT, default=0, help='Set temperature for the LLM model.')
#@click.option('-p', '--parallel', is_flag=True, help='Run in parallel when formatting multiple files.')
def main(file_or_text, diff, inplace, recursive, verbose, command, model, temperature):
    # Print parameter
    if verbose:
        system_print('Command-line options:')
        for param in click.get_current_context().params:
            print(f'{param}: {click.get_current_context().params[param]}')

    # Read yaml config
    aiformat_commands = {}

    config_dir = os.path.expanduser("~/.aiformat")
    config_file_path = os.path.join(config_dir, 'commands.yaml')

    os.makedirs(config_dir, exist_ok=True)

    if not os.path.exists(config_file_path):
        # Create yaml file from package yaml file
        pkg_resource_path = pkg_resources.resource_filename("aiformat", "prompt/commands.yaml")
        shutil.copy(pkg_resource_path, config_file_path)
        system_print(f"Generate yaml config file in {config_file_path}")

    with open(config_file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        aiformat_commands = yaml_data.get('aiformat_commands', {})

    if verbose:
        system_print(f"Read config file in {config_file_path}:")
        for current_command, prompt in aiformat_commands.items():
            print(f'Supported command: {current_command}')

    # Read input which may be a string, a file or a directory
    content_list = []
    file_name_list = []

    if recursive:  # If pass recursive parameter
        for root, dirs, files in os.walk(file_or_text):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    # TODO: Ignore the non source code for commands of code and doc
                    if "code" in command:
                        if not is_source_code_file(file_path):
                            if verbose:
                                system_print(f"Ignore non source code file {file_path}")
                            continue
                    elif "doc" in command:
                        if not is_document_file(file_path):
                            if verbose:
                                system_print(f"Ignore non document file {file_path}")
                            continue
                    if verbose:
                        system_print(f"Read input file {file_path}")
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        content_list.append(content)
                        file_name_list.append(file_path)

    else:  # If handle as single file
        if os.path.exists(file_or_text) and os.path.isfile(file_or_text):  # If it is file
            with open(file_or_text, 'r', encoding='utf-8') as file:
                if verbose:
                    system_print(f"Read input file {file_or_text}")
                content = file.read()
                content_list.append(content)
                file_name_list.append(file_or_text)
        else:  # If it is string
            if verbose:
                system_print(f"Read input string: {file_or_text}")
            content_list.append(file_or_text)

    # Construct prompt
    if command not in aiformat_commands:
        print(f"Fail to get command from config file: {command}")
        return
    command_prompt = aiformat_commands[command]
    template = Template(command_prompt)

    for index, input_content in enumerate(content_list):
        prompt = template.render(text=input_content)
        if verbose:
            system_print("Generate final prompt:")
            print(prompt)

        llm_model = chatgpt_util.LlmModel(model=model, temperature=temperature)
        output_content = llm_model.execute(prompt)

        if diff:
            system_print("Diff of input and output:")
            diff_util.print_diff_with_highlight(input_content, output_content)
        if inplace:
            input_file_name = file_name_list[index]
            try:
                with open(input_file_name, 'w', encoding='utf-8') as file:
                    system_print(f"Try to write formatted content in {input_file_name}:")
                    file.write(output_content)
                    print(output_content)
            except IOError as e:
                print(f"An error occurred while writing to the file: {e}")
        if not diff and not inplace:
            if verbose:
                system_print("Output of LLM model:")
            print(output_content)


def is_source_code_file(file_name):
    # Get the file extension
    _, file_extension = os.path.splitext(file_name)

    # Check if the file extension corresponds to a source code file
    extensions = ['.cpp', '.java', '.py', '.lua', '.c', '.h',
                  '.js', '.html', '.css', '.php', '.sql', '.json',
                  '.xml', '.cc', '.rb', '.swift']
    return file_extension.lower() in extensions


def is_document_file(file_name):
    _, file_extension = os.path.splitext(file_name)

    extensions = ['.md', '.txt', '.log', '']
    return file_extension.lower() in extensions


if __name__ == '__main__':
    main()
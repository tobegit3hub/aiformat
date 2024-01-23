#!/usr/bin/env python3

import click
import yaml

import chatgpt_util
import diff_util

def system_print(text):
   click.secho(text, bg='blue', fg='white')

@click.command()
@click.argument('files')
@click.option('-d', '--diff', is_flag=True, help='print the diff for the fixed source')
@click.option('-i', '--inplace', is_flag=True, help='make changes to files in place')
@click.option('-r', '--recursive', is_flag=True, help='run recursively over directories')
@click.option('-p', '--parallel', is_flag=True, help='run in parallel when formatting multiple files')
@click.option('-vv', '--verbose', is_flag=True, help='print out file names while processing')
@click.option('-c', '--command', type=click.STRING, default="format_code", help='use the command to exceute, check commands in yaml file')
def main(files, diff, inplace, recursive, parallel, verbose, command):

    # Print parameter
    if verbose:
      system_print("Read command-line parameters:")
      click.echo(f"Parameter file: {files}, diff: {diff}, inplace: {inplace}, recursive: {recursive}, parallel: {parallel}, verbose: {verbose}, command: {command}.")

    # Read yaml config
    command_yaml_file = 'aiformat_commands.yaml'
    with open(command_yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)
    aiformat_commands = yaml_data.get('aiformat_commands', {})
    if verbose:
      system_print("Read aiformat_commands.yaml and get commands:")
      for command, prompt in aiformat_commands.items():
        print(f'Command: {command}\nPrompt: {prompt}\n')

    
    # Read input file
    input_file_path = files
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            input_file_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {input_file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    # Construct prompt
    command_prompt = aiformat_commands[command]
    prompt = command_prompt + "\n" + input_file_content
    if verbose:
      system_print("Generate final prompt:")
      print(prompt)

    output_content = execute_format(prompt)
    if verbose:
      system_print("LLM model output:")
      print(output_content)

    if diff:
        system_print("Diff of input and output:")
        diff_util.print_diff(input_file_content, output_content)
    elif inplace:
        try:
            with open(input_file_path, 'w', encoding='utf-8') as file:
                system_print(f"Try to write formated content in {input_file_content}")
                file.write(output_content)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
    else:
       system_print("Output of LLM model:")
       print(output_content)
    

def execute_format(prompt):
    # Request ChatGPT
    chatgpt_output = chatgpt_util.request_chatgpt(prompt)

    # remove triple backticks
    prefix = "```"
    if chatgpt_output.startswith(prefix) and chatgpt_output.endswith(prefix):
        return chatgpt_output[len(prefix):-len(prefix)]
    return chatgpt_output


if __name__ == '__main__':
    main()

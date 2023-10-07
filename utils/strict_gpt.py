import os
import openai
import json
import re
import random



openai.api_key= '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'
def strict_output(system_prompt, user_prompt, output_format, default_category = "", output_value_only = False,
model="gpt-3.5-turbo",temperature = 0, num_tries = 3, verbose = False):


    list_input = isinstance(user_prompt, list)
    dynamic_elements = '<' in str(output_format)
    list_output = '[' in str(output_format)
    
    error_msg = ''
    output=[]
    
    for i in range(num_tries):
        
        output_format_prompt = f'''\nYou are to output the following in json format: {output_format}. 
Do not put quotation marks or escape character \ in the output fields.'''
        
        if list_output:
            output_format_prompt += f'''\nIf output field is a list, classify output into the best element of the list.'''
        
        if dynamic_elements: 
            output_format_prompt += f'''
Any text enclosed by < and > indicates you must generate content to replace it. Example input: Go to <location>, Example output: Go to the garden
Any output key containing < and > indicates you must generate the key name to replace it. Example input: {{'<location>': 'description of location'}}, Example output: {{school: a place for education}}'''

        if list_input:
            output_format_prompt += '''\nGenerate a list of json, one json for each input element.'''
        
        response = openai.ChatCompletion.create(
          temperature = temperature,
          model=model,
          messages=[
            {"role": "system", "content": system_prompt + output_format_prompt + error_msg},
            {"role": "user", "content": str(user_prompt)}
          ]
        )

        res = response['choices'][0]['message']['content'].replace('\'', '"')
        
        res = re.sub(r"(\w)\"(\w)", r"\1'\2", res)

        if verbose:
            print('System prompt:', system_prompt + output_format_prompt + error_msg)
            print('\nUser prompt:', str(user_prompt))
            print('\nGPT response:', res)

            output = json.loads(res)

            output = [output]
                
            for index in range(len(output)):
                for key in output_format.keys():
                    if '<' in key or '>' in key: continue
                    if isinstance(output_format[key], list):
                        choices = output_format[key]
                        if isinstance(output[index][key], list):
                            output[index][key] = output[index][key][0]
                        if output[index][key] not in choices and default_category:
                            output[index][key] = default_category
                        if ':' in output[index][key]:
                            output[index][key] = output[index][key].split(':')[0]
                            
                if output_value_only:
                    output[index] = [value for value in output[index].values()]
                    if len(output[index]) == 1:
                        output[index] = output[index][0]
                    
            return output if list_input else output[0]

      
         
    return res



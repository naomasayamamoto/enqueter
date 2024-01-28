"""Utils for displaying to user"""
import os
import string

import termcolor


def get_template(template_file_name, color=None):
    """Return the path of template.
    
    Args:
        template_file_name(str): template file name
        color(str): Color formatting for termcolor pkg
        
    Returns:
        Template(str): templates text
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(base_dir, 'templates')
    template = os.path.join(templates_dir, template_file_name)
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = termcolor.colored(contents, color)
        return string.Template(contents)
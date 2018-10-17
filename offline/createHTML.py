import os
import datetime
from jinja2 import Environment, FileSystemLoader
 

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'template')),
    trim_blocks=False)
 

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
"""
template: string of the file name under jinja2 template folder. i.e. 'index.html'
output: string of the output file name. i.e. 'output.html'
content: data which is passed to jinja tempalte. plotly charts will be passed through here.
"""
def create_html(template, output, context):
    with open('output/' + output, 'w', encoding='utf-8') as f:
        html = render_template(template, context)
        f.write(html)

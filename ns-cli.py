import typer

cli = typer.Typer()

import os 
import shutil
from distutils.dir_util import copy_tree


EXE_URL = os.path.dirname(os.path.abspath(__file__))
BASE_URL = os.path.dirname(os.path.dirname(EXE_URL))

@cli.command()
def new(project_name: str = typer.Argument(...)):
    shutil.copytree(f"{BASE_URL}/resource", f"./{project_name}")
    with open(f'./{project_name}/.env', 'a') as f:
        f.write(f'\n\nPROJECT_NAME=\"{project_name}\"\n')

@cli.command()
def init():
    current_dir = os.path.basename(os.getcwd())
    copy_tree(f"{BASE_URL}/resource", f"../{current_dir}")
    with open(f'../{current_dir}/.env', 'a') as f:
        f.write(f'\n\nPROJECT_NAME=\"{current_dir}\"\n')

if __name__ == '__main__':
    cli()
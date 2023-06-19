import os
import shutil
import subprocess
import fire
import json

class CLI:

    def __init__(self):
        pass

    def git_config(self):
        subprocess.call(['git', 'init'])

    def create_project_json_file(self, project):
        project = {
            'name': project['name'],
            'description': project['description'],
            'version': project['version'],
            'author': project['author'],
            'git_repository': project['git_repository'],
            'virtual_environment': project['virtual_environment'],
            'requirements': project['requirements'],
            'scripts': {
                'run': 'python app.py'
            },
        }
        with open('project_config.json', 'w') as f:
            json.dump(project, f, ensure_ascii=False, indent=4)
        
    
    def create_virtual_environment(self, settings):
        subprocess.call(['python', '-m', 'venv', settings['name']])

    def start(self):
        project_name = input('Enter the name of the project: ')
        project_description = input('Enter the description of the project: ')
        project_version = input('Enter the version of the project: ')
        project_author = input('Enter the author of the project: ')
        project_git_repository = input('Enter the git repository of the project: ')
        project_virtual_environment = input('Enter the virtual environment of the project: ')
        project_python_version = input('Enter the python version of the project: ')
        project_settings = {
            'name': project_name,
            'description': project_description,
            'version': project_version,
            'author': project_author,
            'git_repository': project_git_repository,
            'virtual_environment': 
                {
                    'name': project_virtual_environment,
                    'python_version': project_python_version,
                },
            'scripts': {
                'run': 'python app.py'
            },
            'requirements': '',
        }
        self.create_project_folder(project_name)
        self.create_project_structure()
        self.create_project_json_file(project_settings)
        self.git_config()
        self.create_virtual_environment(project_settings['virtual_environment'])

    def create_project_folder(self, project_name):
        os.makedirs(project_name, exist_ok=True)
        os.chdir(project_name)

    def create_project_structure(self):
        folders = ['src', 'doc', 'data', 'scripts']
        files = {
            'readme.md': '# Project Name\n\n## Description\n\n## Getting Started\n\n## Usage\n\n## License\n\n## Author\n\n',
            'requirements.txt': '',
            '.gitignore': '.env\n__pycache__/\n*.pyc\n',
            '.env': '',
        }

        for folder in folders:
            os.makedirs(folder, exist_ok=True)

        for file, content in files.items():
            with open(file, 'w') as f:
                f.write(content)

    def create_entity(self, entity_name, module=None):
        if module:
            entity_folder = os.path.join('src', module, 'entity')
        else:
            entity_folder = os.path.join('src', 'entity')
        os.makedirs(entity_folder, exist_ok=True)

        entity_file = os.path.join(entity_folder, entity_name + '.py')
        init_file = os.path.join(entity_folder, '__init__.py')
        
        with open(init_file, 'w') as f:
            f.write('')

        with open(entity_file, 'w') as f:
            f.write(f"from dataclasses import dataclass\n\n\n@dataclass\nclass {entity_name.title()}:\n    pass\n")

    def ent(self, entity_name, module=None):
        self.create_entity(entity_name, module)

    def create_dto(self, entity_name, module=None):
        if module:
            dto_folder = os.path.join('src', module, 'dto')
        else:
            dto_folder = os.path.join('src', 'dto')
        os.makedirs(dto_folder, exist_ok=True)

        dto_file = os.path.join(dto_folder, entity_name + 'DTO.py')

        with open(dto_file, 'w') as f:
            f.write(f"from dataclasses import dataclass\n\n\n@dataclass\nclass {entity_name.title()}DTO:\n    pass\n")

    def dto(self, entity_name, module=None):
        self.create_dto(entity_name, module)

    def create_module(self, module_name):
        module_folder = os.path.join('src', module_name)
        os.makedirs(module_folder, exist_ok=True)

        module_init_file = os.path.join(module_folder, '__init__.py')
        module_file = os.path.join(module_folder, module_name + '.py')

        for file in [module_init_file, module_file]:
            open(file, 'a').close()

    def mod(self, module_name):
        self.create_module(module_name)

    def create_submodule(self, module_name, submodule_name):
        submodule_folder = os.path.join('src', module_name, submodule_name)
        os.makedirs(submodule_folder, exist_ok=True)

        submodule_init_file = os.path.join(submodule_folder, '__init__.py')
        submodule_file = os.path.join(submodule_folder, submodule_name + '.py')

        for file in [submodule_init_file, submodule_file]:
            open(file, 'a').close()

    def sub(self, module_name, submodule_name):
        self.create_submodule(module_name, submodule_name)
                              

    def help(self):
        print("*"*50)
        print("FASTER - Fast Python Project Generator")
        print("*"*50)
        print("AVAILABLE COMMANDS:")
        print("  start - Start a new project")
        print("  ent <entity_name> - CREATE AN ENTITY")
        print("  dto <entity_name> - CREATE A DTO ")
        print("  mod <module_name> - CREATE A MODULE ")
        print("  sub <module_name> <submodule_name> - CREATE A SUBMODULE ")
        print("  act - ACTIVATE THE VIRTUAL ENVIRONMENT")
        print("  git - CONFIGURE THE GIT REPOSITORY ")
        print("  run - RUN A SCRIPT ")
        print("  help - SHOW THIS MESSAGE")

    def read_project_json_file(self):
        with open('project_config.json', 'r') as f:
            project = json.load(f)
        return project
    
    def create_file_on_righ_place(self):
        project_folder = self.read_project_json_file()['name']
        os.chdir(project_folder)

    def activate_virtual_environment(self):
        virtual_environment = self.read_project_json_file()['virtual_environment']['name']

        if os.name == 'posix':  # Linux ou MacOS
            activate_script = 'activate'
        else:  # Windows
            activate_script = 'activate.bat'

        activate_path = os.path.join(virtual_environment, 'Scripts', activate_script)
        subprocess.run(f'call "{activate_path}"', shell=True, stdout=subprocess.PIPE, text=True)

    def act(self):
        self.activate_virtual_environment()

    def install_library(self, library_name):
        virtual_environment = self.read_project_json_file()['virtual_environment']['name']
        subprocess.run([virtual_environment + '/Scripts/activate'],shell=True, stdout=subprocess.PIPE, text=True)
        subprocess.run(['python', '-m', 'pip', 'install', library_name], shell=True)
        subprocess.run(['pip', 'freeze', '>', 'requeriments.txt'], shell=True, stdout=subprocess.PIPE, text=True)

    def i(self, library_name):
        self.install_library(library_name)

    def run(self, script_name):
        self.activate_virtual_environment()
        scripts = self.read_project_json_file()['scripts']
        for script, command in scripts.items():
            if script == script_name:
                subprocess.run(command, shell=True)


def main():
    cli = CLI()
    fire.Fire(cli)


if __name__ == '__main__':
    main()

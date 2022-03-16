from configparser import ConfigParser

import sys

project_path = sys.argv[1]
project_path_friendly = "--".join(project_path.split('/'))

config_path = "./.tx/config"

config = ConfigParser()
config.read(config_path)


for section_title in config.sections():
    if config.has_option(section_title, 'source_file'):
        source_file_path = config.get(section_title, 'source_file')
        if source_file_path[:len(project_path)] == project_path:
            split_section_title = section_title.split('.')
            split_section_title[1] = project_path_friendly + split_section_title[1]
            new_section_title = ".".join(split_section_title)
            config.add_section(new_section_title)
            for option_name in config.options(section_title):
                config.set(new_section_title, option_name, config[section_title][option_name])
            config.remove_section(section_title)

with open(config_path, 'w') as file:
    config.write(file)

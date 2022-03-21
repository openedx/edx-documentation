"""
This script changes the section titles of the tx config file to be more unique based on
the directory of the file that is used to make the original section title.

The script loops through the sections of the tx config and changes the sections that
match the project_path argument variable. The script then adds a delimited version of the
directory to the section title making the title more unique. These section titles become
the file names on Transifex, and if they are not unique, they overwrite eachother.

example:
If we had a file "example/index.rst" that we wanted to translate, in tx config we would
have a section with the title [index] and the source_file: "example/index.rst". But this
filename is common in Sphinx Projects. This script would rename the section title to be
[example--title], keeping all other values under it untouched.
"""
import sys
from configparser import ConfigParser

project_path = sys.argv[1]
project_path_friendly = "--".join(project_path.split("/"))

config_path = "./.tx/config"

config = ConfigParser()
config.read(config_path)


for section_title in config.sections():
    if config.has_option(section_title, "source_file"):
        source_file_path = config.get(section_title, "source_file")
        if source_file_path[: len(project_path)] == project_path:
            split_section_title = section_title.split(".")
            split_section_title[1] = project_path_friendly + split_section_title[1]
            new_section_title = ".".join(split_section_title)
            config.add_section(new_section_title)
            for option_name in config.options(section_title):
                config.set(
                    new_section_title, option_name, config[section_title][option_name]
                )
            config.remove_section(section_title)

with open(config_path, "w") as file:
    config.write(file)

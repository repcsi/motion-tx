import yaml
from os import listdir
from os.path import join, isfile

with open("motion-tx.yaml", 'r') as yamlfile:
    try:
        config = yaml.safe_load(yamlfile);
    except yaml.YAMLError as exc:
        print(exc)

print("Config dump: ")
for section in config:
    print(section + ":" + str(config[section]))

filestocheck = listdir(config['video_directory'])

for files in filestocheck:
    #print(files)
    #print(join(config['video_directory'],files))
    if (isfile(join(config['video_directory'],files))):
        print(files + " is a file")

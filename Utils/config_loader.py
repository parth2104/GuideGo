import yaml

def load_config(file_path:str=r"config\config.yaml"):
    with open(file_path,"r") as file:
        data=yaml.safe_load(file)
    return data
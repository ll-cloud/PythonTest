import yaml
with open('./add.yaml','rb') as f:
    result=yaml.safe_load(f)

print(result)
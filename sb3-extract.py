import sys
from json import loads
from zipfile import ZipFile
from pathlib import Path

def Validate(filename):
    return filename.replace(":", "colon")

def ExtractAssets(assetType):
    for asset in sprite[assetType]:
        targetFile = Validate(asset['name'] + '.' + asset['dataFormat'])
        zipFile.extract(asset['assetId'] + '.' + asset['dataFormat'], sb3Dir / targetFolder / targetFile)

if len(sys.argv) != 2:
    sys.exit("Syntax: sb3-extract <file.sb3>")

sb3Path = Path(sys.argv[1])
if not sb3Path.is_file():
    sys.exit("File \"" + sb3Path.name + "\" does not exist")
sb3Dir = sb3Path.parent

with ZipFile(sb3Path, 'r') as zipFile:
    sb3Data = loads(zipFile.read("project.json", ))

    for sprite in sb3Data['targets']:
        targetFolder = Validate(sprite['name'])
        ExtractAssets("costumes")
        ExtractAssets("sounds")

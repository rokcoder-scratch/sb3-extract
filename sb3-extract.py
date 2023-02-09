import sys
from json import loads
from zipfile import ZipFile
from pathlib import Path

def Validate(filename):
    return filename.replace(":", "colon")

def ExtractAssets(assetType):
    for asset in sprite[assetType]:
        assetFile = Validate(asset['md5ext'])
        targetFile = Validate(asset['name'] + '.' + asset['dataFormat'])
        zipFile.extract(asset['assetId'] + '.' + asset['dataFormat'], sb3Dir / targetFolder)
        Path(sb3Dir / targetFolder / assetFile).replace(sb3Dir / targetFolder / targetFile)

if len(sys.argv) != 2:
    sb3File = input("Enter sb3 file's path:")
else:
    sb3File = sys.argv[1]

sb3Path = Path(sb3File)
if not sb3Path.is_file():
    sys.exit("File \"" + sb3Path.name + "\" does not exist")
sb3Dir = sb3Path.parent

with ZipFile(sb3Path, 'r') as zipFile:
    sb3Data = loads(zipFile.read("project.json", ))

    for sprite in sb3Data['targets']:
        targetFolder = Validate(sprite['name'])
        ExtractAssets("costumes")
        ExtractAssets("sounds")

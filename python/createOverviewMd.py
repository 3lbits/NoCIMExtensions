import os

class General():

    def getProfileName(self):
        
        for dirs in os.walk('docs'):
            docsProfilePaths = dirs[1]
            break

        for files in os.walk('schemas/yaml'):
            filesProfilePaths = []
            for file in files[2]:
                fileName = file.split('.')[0]
                fileName = ''.join(word.capitalize() for word in fileName.split('_'))
                filesProfilePaths.append(fileName)
            break
        
        profileNames = []

        for docsProfilePath in docsProfilePaths:
            if docsProfilePath in filesProfilePaths:
                profileNames.append(docsProfilePath)

        return profileNames

class CreateMarkdown():

    def create_markdown_file(self):
        title = f'Overview'
        description = f'This document provides an overview of the profiles in the Norwegian CIM National Profiles.'
        ProfileListDescription = f'Currently documented here are the following profiles (click on each to learn more).'

        profileNames = General().getProfileName()

        profileNamesMdString = ''

        for profileName in profileNames:
            profileNamesMdString += f'- [{profileName}](./{profileName}/index.md)\n'

        with open(f'{docFilePath}', 'w') as file:
            file.write(f"# {title}\n\n")
            file.write(f'{description}\n\n')
            file.write(f'{ProfileListDescription}\n\n')
            file.write(f'Profiles:\n\n')
            file.write(f'{profileNamesMdString}')

class CreaeOverviewMdController():

    def main(self):
        docName = 'index.md'

        global docFilePath
        docFilePath = f"docs/{docName}"

        CreateMarkdown().create_markdown_file()

if __name__ == "__main__":
    CreaeOverviewMdController().main()
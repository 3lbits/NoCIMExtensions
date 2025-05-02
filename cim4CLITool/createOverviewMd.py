import os

class General():

    def getProfileName(self):
        
        for dirs in os.walk('docs/Models/Profiles'):
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
        title = f'Welcome to CIM for Norway'
        description = f'Welcome to our website, your go-to resource for all things related to digital information exchange within the (Norwegian) grid sector. Whether you\'re a seasoned professional or new to the field, we aim to make this platform designed to provide you with the latest insights and resources to help you navigate and excel in the utilization of CIM (Common Information Model). \n## What You Can Expect: \n### CIM Profile Documentation \nAccess comprehensive documentation on CIM profiles and their usage, helping you understand and implement these standards effectively.'
        ProfileListDescription = f'#### Currently documented profiles (click on each to learn more): \nTo access examples of how to use these profiles, please visit our [GitHub repository](https://github.com/3lbits/NoCIMExtensions) and navigate to the folder **data**.'

        profileNames = General().getProfileName()

        profileNamesMdString = ''

        for profileName in profileNames:
            profileNamesMdString += f'- [{profileName}](/Models/Profiles/{profileName}/)\n'

        with open(f'{docFilePath}', 'w') as file:
            file.write(f"# {title}\n\n")
            file.write(f'{description}\n\n')
            file.write(f'{ProfileListDescription}\n\n')
            file.write(f'Profiles:\n\n')
            file.write(f'{profileNamesMdString}')

class CreateOverviewMdController():

    def main(self):
        docName = 'index.md'

        global docFilePath
        docFilePath = f"docs/{docName}"

        CreateMarkdown().create_markdown_file()

if __name__ == "__main__":
    CreateOverviewMdController().main()
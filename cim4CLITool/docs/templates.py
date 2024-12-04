from jinja2 import Environment, FileSystemLoader
import yaml
from cim4CLITool.docs.configs.mkdocs_config import MkDocsConfig

import os

class General:

    def write_file(output_path, data):
        with open(output_path, 'w') as f:
            f.write(data)

    def read_file(input_path):
        with open(input_path, 'r') as f:
            data = f.read()
        return data

    def contains_key(_list, key):
        for item in _list:
            if key in item:  # Check if key exists in the dictionary
                return True
        return False

class TemplateClass:

    def render_template(data, template):
        rendered_data = template.render(data)
        return rendered_data

    def open_template(template_name):
        env = Environment(loader=FileSystemLoader(os.path.join("cim4CLITool", "docs", "_templates")))
        template = env.get_template(template_name)
        return template
    
    def controller(template_name, data, output_path, write_file=True):
        template = TemplateClass.open_template(template_name)
        rendered_data = TemplateClass.render_template(data, template)
        if write_file:
            General.write_file(output_path, rendered_data)
        else:
            return rendered_data

class EditMkDocsYaml:

    # mkdocs.yaml has a syntax error when mermaid is enabled that python cannot read into dictionary
    def replace_mermaid_format():
        mkdocs_yaml_file = General.read_file(file_path)
        mkdocs_yaml_file = mkdocs_yaml_file.replace('format: !!python/name:pymdownx.superfences.fence_code_format', 'format: temporary replaced')
        mkdocs_dict_file = yaml.load(mkdocs_yaml_file, Loader=yaml.FullLoader)
        return mkdocs_dict_file
    
    def add_mermaid_format_back_in():
        mkdocs_yaml_file = General.read_file(file_path)
        mkdocs_yaml_file = mkdocs_yaml_file.replace('format: temporary replaced', 'format: !!python/name:pymdownx.superfences.fence_code_format')
        return mkdocs_yaml_file

    def traverse_navDict(_list, navKey):

        for object in _list:
            for key in object:
                if key == navKey:
                    if object[navKey] != None and object[navKey] != []:
                        exist = True
                        return exist, object[navKey]
 
    def remove_object_from_list(_list, key):
        for item in _list:
            if key in item:
                _list.remove(item)
                break

    def add_profile_to_nav(nav_profile):

        mkdocs_dict_file = EditMkDocsYaml.replace_mermaid_format()

        # Validate if nav is correct. If not, rebuild the hole thing

        resettedNav = [{'Home': 'index.md'}, {'Models': [{'Profiles': [{'Overview': 'Models/Profiles/index.md'}, nav_profile]}]}]

        if 'nav' not in mkdocs_dict_file:
            mkdocs_dict_file['nav'] = resettedNav
        
        if mkdocs_dict_file['nav'] == None:
            mkdocs_dict_file.pop('nav')
            mkdocs_dict_file['nav'] = resettedNav

        navList = mkdocs_dict_file["nav"]

        existModels = False
        modelList = None
        existProfiles = False

        checkModels = EditMkDocsYaml.traverse_navDict(navList, 'Models')

        if checkModels != None:
            existModels = checkModels[0]
            modelList = checkModels[1]

        if modelList != None:

            checkProfiles = EditMkDocsYaml.traverse_navDict(modelList, 'Profiles')
            if checkProfiles != None:
                existProfiles = checkProfiles[0]
                profileList = checkProfiles[1]

        if existModels == False or existProfiles == False:
            mkdocs_dict_file.pop('nav')
            mkdocs_dict_file['nav'] = resettedNav

        # End Validation

        # Check if the profile already exists in the nav

        navList = mkdocs_dict_file["nav"]
        modelList = EditMkDocsYaml.traverse_navDict(navList, 'Models')[1]
        profileList = EditMkDocsYaml.traverse_navDict(modelList, 'Profiles')[1]
        profileName = list(nav_profile.keys())[0]

        # Remove the Overview if it already exists
        EditMkDocsYaml.remove_object_from_list(profileList, 'Overview')

        # Remove the profile if it already exists
        EditMkDocsYaml.remove_object_from_list(profileList, profileName)

        # Add the profile and Overview if validation is okay
        profileList.append({'Overview': 'Models/Profiles/index.md'})
        profileList.append(nav_profile)

        # Sort the nav with Overview first and then the rest of the profiles alphabetically
        profileList.sort(key=lambda x: (list(x.keys())[0] != 'Overview', list(x.keys())[0]))
        return mkdocs_dict_file

    def controller(path, nav_profile):
        
        global file_path
        file_path = path

        mkdocs_dict_file = EditMkDocsYaml.add_profile_to_nav(nav_profile)
        General.write_file(path, yaml.dump(mkdocs_dict_file, sort_keys=False))
        mkdocs_dict_file = EditMkDocsYaml.add_mermaid_format_back_in()
        General.write_file(path, mkdocs_dict_file)

if __name__ == "__main__": # For testing purposes
    outputpath = os.path.join("cim4CLITool", "docs", "output_test", "mkdocs.yaml")
    config='elbits' # 'elbits', 'default'
    add_profile = {'AviationObstacle': [{'Overview': 'Model/Profiles/AviationObstacle/index.md'}, {'Abstract Classes': [{'IdentifiedObject': 'Model/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject.md'}]}, {'Concrete Classes': [{'Feeder': 'Model/Profiles/AviationObstacle/ConcreteClasses/Feeder.md'}]}, {'Enumerations': [{'TimeSeriesInterpolationKind': 'Model/Profiles/AviationObstacle/Enumerations/TimeSeriesInterpolationKind.md'}]}, {'Types': [{'DateTime': 'Model/Profiles/AviationObstacle/Types/DateTime.md'}]}]}
    nav_profiles = {'WattApp': [{'Overview': 'Models/Profiles/WattApp/index.md'}, {'Abstract Classes': [{'IdentifiedObject': 'Models/Profiles/WattApp/AbstractClasses/IdentifiedObject.md'}, {'PowerSystemResource': 'Models/Profiles/WattApp/AbstractClasses/PowerSystemResource.md'}, {'ConnectivityNodeContainer': 'Models/Profiles/WattApp/AbstractClasses/ConnectivityNodeContainer.md'}, {'EquipmentContainer': 'Models/Profiles/WattApp/AbstractClasses/EquipmentContainer.md'}, {'BaseTimeSeries': 'Models/Profiles/WattApp/AbstractClasses/BaseTimeSeries.md'}, {'BaseIrregularTimeSeries': 'Models/Profiles/WattApp/AbstractClasses/BaseIrregularTimeSeries.md'}]}, {'Concrete Classes': [{'LanguageObject': 'Models/Profiles/WattApp/ConcreteClasses/LanguageObject.md'}, {'SpatialObject': 'Models/Profiles/WattApp/ConcreteClasses/SpatialObject.md'}, {'Feature': 'Models/Profiles/WattApp/ConcreteClasses/Feature.md'}, {'Geometry': 'Models/Profiles/WattApp/ConcreteClasses/Geometry.md'}, {'GeometryObject': 'Models/Profiles/WattApp/ConcreteClasses/GeometryObject.md'}, {'Feeder': 'Models/Profiles/WattApp/ConcreteClasses/Feeder.md'}, {'CapacitySchedule': 'Models/Profiles/WattApp/ConcreteClasses/CapacitySchedule.md'}, {'CapacityTimePoint': 'Models/Profiles/WattApp/ConcreteClasses/CapacityTimePoint.md'}, {'Container': 'Models/Profiles/WattApp/ConcreteClasses/Container.md'}]}, {'Enumerations': [{'TimeSeriesInterpolationKind': 'Models/Profiles/WattApp/Enumerations/TimeSeriesInterpolationKind.md'}, {'BaseTimeSeriesKind': 'Models/Profiles/WattApp/Enumerations/BaseTimeSeriesKind.md'}]}, {'Types': [{'DateTime': 'Models/Profiles/WattApp/Types/DateTime.md'}, {'ActivePower': 'Models/Profiles/WattApp/Types/ActivePower.md'}, {'ReactivePower': 'Models/Profiles/WattApp/Types/ReactivePower.md'}]}]}

    if config == 'default':
        config = MkDocsConfig.default()
    elif config == 'elbits':
        config = MkDocsConfig.elbits(nav_profiles)

    TemplateClass.controller("mkdocs.yaml", config, outputpath) # If not exist: This one is for creating the mkdocs.yaml file without navigation
    EditMkDocsYaml.controller(outputpath, nav_profiles) # Always: This one is for adding a profile to the navigation
    EditMkDocsYaml.controller(outputpath, add_profile) # Always: This one is for adding a second profile to the navigation

    

import json
import yaml
import os

def convert_jsonld_to_yaml(jsonld_file_path, yaml_file_path):
    """
    Converts a JSON-LD file to a YAML file.

    :param jsonld_file_path: Path to the input JSON-LD file.
    :param yaml_file_path: Path to the output YAML file.
    """
    try:
        # Read the JSON-LD file
        with open(jsonld_file_path, 'r', encoding='utf-8') as jsonld_file:
            jsonld_data = json.load(jsonld_file)
        
        graph = extract_graph(jsonld_data)

        # Clean the graph object
        graph = clean_graph_objects(graph)

        # Create a dictionary to hold the graph objects by type
        graph = same_type_objects_containment(graph)

        # Write the data to a YAML file
        with open(yaml_file_path, 'w', encoding='utf-8') as yaml_file:
            yaml.dump(graph, yaml_file, default_flow_style=False, allow_unicode=True, sort_keys=False)

        print(f"Successfully converted {jsonld_file_path} to {yaml_file_path}")

    except Exception as e:
        print(f"Error during conversion: {e}")

def extract_graph(jsonld_data):
    """
    Extracts the 'graph' from JSON-LD data.
    Cleans values and namespace and attribute inheritance from keys.
    """
    if isinstance(jsonld_data, dict) and '@graph' in jsonld_data:
        jsonld_graph = jsonld_data['@graph']

        for i in jsonld_graph:
            if '@type' in i and isinstance(i['@type'], list): # if @type is a list, set the first item as the main type
                i['@type'] = i['@type'][0]
            
            keys = list(i.keys())

            for k in keys: # remove namespace and attribute inheritance from keys
                temp = k.split(":")[-1].split(".")[-1]
                i[temp] = i.pop(k)         

    return jsonld_graph

def clean_graph_objects(jsonld_graph): #remove information that is not needed for the YAML file
    for o in jsonld_graph: # for each object in graph
        for p in o: # for each property in object
            if isinstance(o[p], list):
                for l in o[p]: #for each list item
                    if isinstance(l,dict): # if list item is a dict, change the key frm @id to mRID
                        l["mRID"] = l.pop("@id").split(":")[-1]
            
            elif isinstance(o[p], dict):
                if len(o[p]) == 1 and "@id" in o[p]: #if true assume reference is an enumeration and remove all superflous details about relation
                    temp = o[p]["@id"].split(":")[-1].split(".")[-1]
                    o[p] = temp
                
                elif len(o[p]) > 1 and isinstance(o[p], dict): #if true proceed to clean dictionaries within

                    keys_l2 = list(o[p].keys())
                   
                    for s in keys_l2:
                        if isinstance(o[p][s], dict): #remove "@" from key names within dictionary
                           
                           keys_l3 = list(o[p][s].keys())
                           
                           for k in keys_l3: 
                            temp = k.strip("@")
                            o[p][s][temp] = o[p][s].pop(k)
                        
                        if ":" in s: #remove namespace from key names
                            temp = s.split(":")[-1].split(".")[-1]
                            o[p][temp] = o[p].pop(s)
        
        o.pop('@id')

    return jsonld_graph

def same_type_objects_containment(jsonld_graph):
    """
    Creates a key based on types and puts objects of the same type in the JSON-LD graph as values of relevant key.
    """
    #merged_graph = []
    type_dict = {}

    for obj in jsonld_graph:
        obj_type = obj.get('@type')
        obj_type = obj_type.split(":")[-1]
        if obj_type not in type_dict:
            type_dict[obj_type] = []

        type_dict[obj_type].append(obj)

        obj.pop('@type')
   
    return type_dict

if __name__ == "__main__": # needs to be updated !NB
    # Input JSON-LD file path 
    jsonld_file_path = f"data\Telemark-120\jsonld\grid\Telemark-120-LV1_EQ.jsonld"
    
    # Output YAML file path
    yaml_file_path = f"data\Telemark-120\yaml\grid\{jsonld_file_path.split("\\")[-1].split(".")[0] + ".yaml"}"

    # Convert JSON-LD to YAML
    convert_jsonld_to_yaml(jsonld_file_path, yaml_file_path)
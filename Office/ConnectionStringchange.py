import xml.etree.ElementTree as ET

def update_config_values(file_path,new_values):

    # Load and parse the XML configuration file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Update <connectionStrings> based on new_values["connectionStrings"]
    connection_strings = root.find('connectionStrings')
    if connection_strings is not None and "connectionStrings" in new_values:
        for conn in connection_strings.findall('add'):
            name = conn.get('name')
            if name in new_values["connectionStrings"]:
                conn.set('connectionString', new_values["connectionStrings"][name])

    # Update <appSettings> for other values in new_values
    app_settings = root.find('appSettings')
    if app_settings is not None:
        for setting in app_settings.findall('add'):
            key = setting.get('key')
            if key in new_values:
                setting.set('value', new_values[key])

    # Save the updated XML to the file
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
    print("Configuration updated successfully.")




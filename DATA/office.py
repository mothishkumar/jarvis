# Configuration paths
path = {
    "mdms": r"D:\Esyasoft\mdms_web_new\mdmsweb\MDMSWeb\Web.config",  # Make sure this is correctly set
    "wfm": ""  # Add other paths as needed
}

# bhopal_prod configuration
bhopal_prod = {
    "connectionStrings": {
        "CPConnectionString": "Data Source=new_data_source;User ID=new_user;Password=new_password;Initial Catalog=new_catalog;",
        "IntegrationConnectionString": "Data Source=another_data_source;User ID=another_user;Password=another_password;Initial Catalog=another_catalog;",
        "MDMSConnectionString": "Data Source=third_data_source;User ID=third_user;Password=third_password;Initial Catalog=third_catalog;",
    },
    "TokenURL": "https://new.token.url",
    "TokenIP": "new.token.ip.address"
}
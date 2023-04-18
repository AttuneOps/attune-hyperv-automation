from datetime import date
import dropbox
import re

dropbox_access_token = "${dropboxAccessToken.password}"
dropbox_app_key = "${dropboxAppKey.password}"
dropbox_refresh_token = "${dropboxRefreshToken.password}"
dropbox_app_secret = "${dropboxAppSecret.password}"

today = date.today()
date = today.strftime("%Y%m%d")
dropbox_path = "/Product Releases/Attune/" + date + "_tmp.txt"

computer_path = "C:/Users/Public/Downloads/tmp.txt"

print("dropbox_path=[%s], computer_path=[%s]" % (dropbox_path, computer_path
))

authorization_bearer = "Bearer " + dropbox_access_token

def getRootNamespaceId( \
    authorization_bearer,
    dropbox_access_token,
    dropbox_refresh_token,
    dropbox_app_key,
    dropbox_app_secret):
        
    headers = {
        "Authorization": authorization_bearer,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    dbx = dropbox.Dropbox( \
        oauth2_access_token=dropbox_access_token,
        headers=headers,
        oauth2_refresh_token=dropbox_refresh_token,
        app_key=dropbox_app_key,
        app_secret=dropbox_app_secret)
        
    # dbx.users_get_current_account() returns a non string
    # so call str() to get a string for use with re.
    users_string = str(dbx.users_get_current_account())
    
    # Use Regex with a capturing group to capture the numbers
    # In the root_namespace_id field.
    re_result = re.search("root_namespace_id='(\d+)'", users_string)

    return re_result.group(1)

def uploadFile( \
    authorization_bearer,
    root_namespace_id,
    dropbox_access_token,
    dropbox_refresh_token,
    dropbox_app_key,
    dropbox_app_secret):
        
    dropbox_api_path_root = '{".tag": "root", "root": "' + \
        root_namespace_id + '"}'
        
    headers = {
        "Authorization": authorization_bearer,
        "Content-Type": "application/x-www-form-urlencoded",
        "Dropbox-API-Path-Root": dropbox_api_path_root
    }
    dbx = dropbox.Dropbox(
        oauth2_access_token=dropbox_access_token,
        headers=headers,
        oauth2_refresh_token=dropbox_refresh_token,
        app_key=dropbox_app_key,
        app_secret=dropbox_app_secret)
    
    file = open(computer_path, "rb")
    
    dbx.files_upload(file.read(), dropbox_path)
    print("[UPLOADED] {} to Dropbox {}".format(computer_path, dropbox_path))
    
    file.close()
    
root_namespace_id = getRootNamespaceId( \
    authorization_bearer,
    dropbox_access_token,
    dropbox_refresh_token,
    dropbox_app_key,
    dropbox_app_secret)

print("root_namespace_id=%s" % root_namespace_id)

uploadFile( \
    authorization_bearer,
    root_namespace_id,
    dropbox_access_token,
    dropbox_refresh_token,
    dropbox_app_key,
    dropbox_app_secret)


from datetime import date
import dropbox
import os
import re

dropbox_access_token = "${dropboxAccessToken.password}"
dropbox_app_key = "${dropboxAppKey.password}"
dropbox_refresh_token = "${dropboxRefreshToken.password}"
dropbox_app_secret = "${dropboxAppSecret.password}"

today = date.today()
date = today.strftime("%Y%m%d")
dropbox_path = "/Product Releases/Peek/peek_" + \
    "${exportPeekVersion}_" + date + "_hyperv.zip"

computer_path = "${hypervExportDirectory}/${targetServer.name}.zip"
computer_path = computer_path.replace(os.sep, '/')

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
    
def uploadBigFile( \
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
    file_size = os.path.getsize(computer_path)
    print("file_size = %s" % file_size)
    
    # 4 MB
    CHUNK_SIZE = 4 * 1024 * 1024
    
    if file_size <= CHUNK_SIZE:
    
        prin(dbx.files_upload(file.read(), dropbox_path))
    
    else:
    
        upload_session_start_result = dbx.files_upload_session_start(\
          file.read(CHUNK_SIZE))
    
        cursor = dropbox.files.UploadSessionCursor(\
            session_id=upload_session_start_result.session_id,
            offset=file.tell())
    
        commit = dropbox.files.CommitInfo(path=dropbox_path)
    
        while file.tell() < file_size:
            if ((file_size - file.tell()) <= CHUNK_SIZE):
                print(dbx.files_upload_session_finish(\
                    file.read(CHUNK_SIZE),
                    cursor,
                    commit))
            else:
                dbx.files_upload_session_append(\
                    file.read(CHUNK_SIZE),
                    cursor.session_id,
                    cursor.offset)
                    
                cursor.offset = file.tell()
    
    file.close()
    
root_namespace_id = getRootNamespaceId( \
    authorization_bearer,
    dropbox_access_token,
    dropbox_refresh_token,
    dropbox_app_key,
    dropbox_app_secret)

print("root_namespace_id=%s" % root_namespace_id)

uploadBigFile( \
    authorization_bearer,
    root_namespace_id,
    dropbox_access_token,
    dropbox_refresh_token,
    dropbox_app_key,
    dropbox_app_secret)
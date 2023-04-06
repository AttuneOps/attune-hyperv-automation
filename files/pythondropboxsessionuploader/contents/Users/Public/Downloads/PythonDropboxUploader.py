import dropbox
import os

dropbox_access_token = "${dropboxAccessToken.password}"
dropbox_app_key = "${dropboxAppKey.password}"
dropbox_refresh_token = "${dropboxRefreshToken.password}"
dropbox_app_secret = "${dropboxAppSecret.password}"

dropbox_path = "/Kean Ooi/${targetServer.name}.zip"
computer_path = "${hypervExportDirectory}/${targetServer.name}.zip"
computer_path = computer_path.replace(os.sep, '/')

print("yo4 dropbox_path=[%s], computer_path=[%s]" % (dropbox_path, computer_path
))

authorization_bearer = "Bearer " + dropbox_access_token

headers = {
    "Authorization": authorization_bearer,
    "Content-Type": "application/x-www-form-urlencoded"
}

print("headers")
print(headers)

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
import dropbox

dropbox_access_token = "${dropboxAccessToken.password}"
dropbox_app_key = "${dropboxAppKey.password}"
dropbox_refresh_token = "${dropboxRefreshToken.password}"
dropbox_app_secret = "${dropboxAppSecret.password}"

dropbox_path = "/Kean Ooi/tmp"
computer_path = "C:/Users/Public/Downloads/tmp.txt"

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
    
print("[SUCCESS] dropbox account linked")

print(dbx.users_get_current_account())

# dbx.files_upload(open(computer_path, "rb").read(), dropbox_path)
# print("[UPLOADED] {}".format(computer_path))
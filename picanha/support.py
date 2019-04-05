from api_access import acceso

dbx = acceso.dbx.files_list_folder('/AAA_Webseiten/255_deutschland-spielt.de').entries
for basura in dbx:
    print(basura.name)

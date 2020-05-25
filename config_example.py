#postgres database credentials
DB_PARAMS={"host":"host"
    , "port":"port"
    , "user":"user"
    , "password":"password"
    , "default_database":"default_database" #default database to connect to create the 'database'
    , "database":"data_database"} #data database to load

#sourcefile name and location
SOURCE_FILE_NAME='xxxxxxxxx.json'
SOURCE_FILE_URL='https://xxxxxxxxxxxxxxxxxx/xxxxxxx.json'

#path to store the file locally
LOCAL_FILE_PATH="sourceData"

#create database flag. if false will skip creating the database
CREATE_DATABASE_OBJECTS_FLAG=True

#log configuration
LOG_LEVEL="INFO"
LOG_FILE_NAME="handleDataPipeline.log"

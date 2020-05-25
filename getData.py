import config
import requests
import os
import logging

def create_local_directory():
    try:
        if os.path.isdir(config.LOCAL_FILE_PATH):
            logging.info("Directory already exists %s " % config.LOCAL_FILE_PATH)
        else:
            os.mkdir(config.LOCAL_FILE_PATH)
            logging.info("Successfully created the directory %s " % config.LOCAL_FILE_PATH)
    except OSError:
        logging.error("Creation of the directory %s failed" % config.LOCAL_FILE_PATH)


def download_data():
    create_local_directory()
    open(os.path.join(config.LOCAL_FILE_PATH, config.SOURCE_FILE_NAME), 'wb').write(requests.get(config.SOURCE_FILE_URL).content)
    logging.info("Successfully downloaded file %s" % config.SOURCE_FILE_URL)


def main():
    logging.basicConfig(level=logging.DEBUG)
    download_data()

if __name__ == "__main__":
    main()
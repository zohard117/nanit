import config
import getData
import databaseUtils
import prepareData
import logging

#configure logger
def getLogger():
    logging.basicConfig(
        level=config.LOG_LEVEL,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(config.LOG_FILE_NAME),
            logging.StreamHandler()
        ]
    )


# run main etl process
#   create databse objects
#   download data
#   prepare data to load
#   load data
def main():
    getLogger()
    logging.info("start ETL process")
    if config.CREATE_DATABASE_OBJECTS_FLAG:
        logging.info("create DB")
        databaseUtils.main()
    logging.info("download data")
    getData.main()
    logging.info("prepare data")
    shipping_lines_data=prepareData.get_shipping_lines_data()
    logging.info("load data")
    databaseUtils.load_shipping_lines_table(shipping_lines_data)
    logging.info("end ETL process")

if __name__ == "__main__":
    main()
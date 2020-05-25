import json
import config
from datetime import datetime
import os
import psycopg2.extras

def get_shipping_lines_data():
    all_shipment_lines = []
    all_products = set()
    def get_utc_object(p_date_string):
        return datetime.strptime(p_date_string, '%Y-%m-%dT%H:%M:%S') #2020-02-10T12:35:15

    with open(os.path.join(config.LOCAL_FILE_PATH, config.SOURCE_FILE_NAME)) as f:
        data= json.load(f)
        for one_order in data["Order"]:
            one_order_dispatches= one_order.get("Dispatches")
            if one_order_dispatches is not None:
                current_shipment_row = {"order_source": one_order.get("OrderSource").lower(),
                                        "order_id":one_order.get("OrderNumber")
                                        }

                for dispatch_num, one_dispatch in enumerate(one_order_dispatches):
                    current_shipment_row.update({
                        "shipment_id": one_dispatch.get("DispatchReference"),
                        "shipment_date": get_utc_object(one_dispatch.get("DispatchDate"))
                    })
                    for dispatch_line_num, one_dispatch_line in enumerate(one_dispatch.get("DispatchedLines")):
                        current_shipment_row.update({
                                                    "product_code":one_dispatch_line.get("ProductCode").upper(),
                                                    "product_quantity":one_dispatch_line.get("Quantity")
                                                    })
                all_shipment_lines.append(current_shipment_row)
    return all_shipment_lines


def main():
    get_shipping_lines_data()

if __name__ == "__main__":
    main()
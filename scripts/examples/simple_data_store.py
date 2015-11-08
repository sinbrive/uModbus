#!/usr/bin/env python
# scripts/examples/simple_data_store.py
from umodbus import get_server
from collections import defaultdict

# A very simple data store which maps addresss against their values.
data_store = defaultdict(int)

app = get_server('localhost', 502)


@app.route(slave_ids=[1], function_codes=[3, 4], addresses=list(range(0, 10)))
def read_data_store(slave_id, address):
    """" Return value of address. """
    return data_store[address]


@app.route(slave_ids=[1], function_codes=[6, 16], addresses=list(range(0, 10)))
def write_data_store(slave_id, address, value):
    """" Set value for address. """
    data_store[address] = value

if __name__ == '__main__':
    try:
        app.serve_forever()
    finally:
        app.stop()

import os

from featuretools import dfs
from featuretools.demo import load_mock_customer, load_retail
from featuretools.demo.retail import make_retail_pathname


def test_load_retail_save():
    nrows = 10
    load_retail(nrows=nrows)
    assert os.path.isfile(make_retail_pathname(nrows))
    assert os.path.getsize(make_retail_pathname(nrows)) < 45580670
    os.remove(make_retail_pathname(nrows))


def test_load_retail_diff():
    nrows = 10
    es_first = load_retail(nrows=nrows)
    assert os.path.isfile(make_retail_pathname(nrows))
    assert es_first['order_products'].df.shape[0] == nrows

    nrows_second = 11
    es_second = load_retail(nrows=nrows_second)
    assert os.path.isfile(make_retail_pathname(nrows_second))
    assert es_second['order_products'].df.shape[0] == nrows_second
    os.remove(make_retail_pathname(nrows))
    os.remove(make_retail_pathname(nrows_second))


def test_load_mock_customer_dfs():
    es = load_mock_customer(return_entityset=True)
    dfs(entityset=es,
        target_entity="sessions",
        agg_primitives=["mean", "sum", "mode"],
        trans_primitives=["month", "hour"],
        max_depth=2)

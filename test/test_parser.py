from app.parser import parse_query

def test_parse_query_price():
    pred = parse_query("price > 100")
    assert pred({"price": 150})
    assert not pred({"price": 50})

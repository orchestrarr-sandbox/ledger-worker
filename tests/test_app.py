import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app as ledger


def client():
    ledger.ENTRIES.clear()
    return ledger.app.test_client()


def test_health():
    res = client().get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_add_and_list():
    c = client()
    assert c.post("/entries", json={"amount": 5, "kind": "credit"}).status_code == 201
    assert c.post("/entries", json={"amount": 2, "kind": "debit"}).status_code == 201
    assert len(c.get("/entries").get_json()) == 2
    assert len(c.get("/entries?kind=debit").get_json()) == 1


def test_refuses_an_incomplete_entry():
    assert client().post("/entries", json={"amount": 5}).status_code == 400


def test_import_valid_yaml():
    c = client()
    res = c.post("/import", data="- {amount: 3, kind: credit}\n")
    assert res.status_code == 201
    assert len(c.get("/entries").get_json()) == 1


def test_import_refuses_python_tag():
    c = client()
    payload = "!!python/object/apply:os.system ['echo pwned']"
    assert c.post("/import", data=payload).status_code >= 400
    assert c.get("/entries").get_json() == []

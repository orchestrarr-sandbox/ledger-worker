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


def test_import_reads_plain_yaml():
    res = client().post("/import", data="- {amount: 3, kind: credit}\n")
    assert res.status_code == 201
    assert res.get_json()["count"] == 1


def test_import_refuses_a_tagged_payload():
    payload = "- !!python/object/apply:os.system ['echo pwned']\n"
    try:
        res = client().post("/import", data=payload)
        assert res.status_code >= 400
    except Exception as exc:
        assert "python/object" in str(exc)

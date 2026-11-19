"""Offline tests for apkpure.py -- no network, no token.

The fixture HTML mimics the real APKPure search page structure
(verified live 2026-11-19: search results link as /slug/package,
e.g. /facebook-lite/com.facebook.lite, first result "Facebook Lite").
Run:  python test_apkpure.py
"""

from apkpure import parse_detail_html, parse_search_html

SEARCH_FIXTURE = """
<html><body>
<div class="search-result">
  <a href="/facebook-lite/com.facebook.lite" title="Facebook Lite">Facebook Lite</a>
  <a href="/messenger-lite/com.facebook.mlite" title="Messenger Lite">Messenger Lite</a>
  <a href="/facebook/com.facebook.katana" title="Facebook">Facebook</a>
  <a href="/search?q=facebook+lite">Search again</a>
</div>
</body></html>
"""

DETAIL_FIXTURE = """
<html><head><title>Facebook Lite APK for Android Download</title></head>
<body>
<div>Latest Version 539.0.0.7.106</div>
<div>File Size 3.6 MB</div>
</body></html>
"""


def test_search():
    results = parse_search_html(SEARCH_FIXTURE, limit=5)
    assert len(results) == 3, results
    assert results[0]["name"] == "Facebook Lite", results[0]
    assert results[0]["package"] == "com.facebook.lite", results[0]
    assert results[0]["slug"] == "facebook-lite", results[0]
    assert results[0]["detail_url"] == (
        "https://apkpure.com/facebook-lite/com.facebook.lite"
    )
    assert results[1]["package"] == "com.facebook.mlite"
    assert results[2]["package"] == "com.facebook.katana"
    print("test_search OK:", [(r["name"], r["package"]) for r in results])


def test_search_empty():
    assert parse_search_html("<html><body>No results</body></html>") == []
    print("test_search_empty OK")


def test_detail():
    d = parse_detail_html(DETAIL_FIXTURE, "facebook-lite", "com.facebook.lite")
    assert d["name"] == "Facebook Lite", d
    assert d["version"] == "539.0.0.7.106", d
    assert d["size"] == "3.6 MB", d
    assert d["download_url"] == (
        "https://apkpure.com/facebook-lite/com.facebook.lite/download"
    )
    assert d["detail_url"] == (
        "https://apkpure.com/facebook-lite/com.facebook.lite"
    )
    print("test_detail OK:", d)


if __name__ == "__main__":
    test_search()
    test_search_empty()
    test_detail()
    print("All offline tests passed.")

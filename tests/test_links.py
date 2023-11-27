import crawler.links

def test_get_all_links_from_page():
    tested = crawler.links.Links(HTML1)
    assert tested.all() == [
                    "a.txt",
                    "b.txt",
                    "one/",
                    "three/",
                    "two/",
            ]


HTML1 = """
<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href="a.txt">a.txt</a></li>
<li><a href="b.txt">b.txt</a></li>
<li><a href="one/">one/</a></li>
<li><a href="three/">three/</a></li>
<li><a href="two/">two/</a></li>
</ul>
<hr>
</body>
</html>
"""

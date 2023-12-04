class Crawl:
    def __init__(self, root_url, *, find_links):
        self._root_url = root_url

        result = [[root_url]]
        to_visit = [root_url]
        while len(to_visit) > 0:
            url = to_visit.pop(0)
            links = find_links(url)
            if len(links) == 0:
                continue
            to_visit += links
            result.append(links)

        self._result = result


    def web_of_links(self):
        return self._result

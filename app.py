import requests


class PoeItemCrawler(object):
    def __init__(self, apiid):
        self.requested_data = requests.get('http://api.pathofexile.com/public-stash-tabs/?id={}'.format(apiid)).json()

    def item_reader(self):
        item_list = []
        for item in self.requested_data["stashes"]:
            for itemlist in item["items"]:
                if itemlist["ilvl"]!= 0:
                    item_list.append(itemlist["ilvl"])
        return item_list

    def item_properties(self):
        item_dict = {}
        for item in self.requested_data["stashes"]:
            for itemdata in item["items"]:
                try:
                    item_dict[itemdata["explicitMods"]] = itemdata["properties"]
                except KeyError:
                    continue

    def average_of_list(self, list_of_items):
        avg = sum(list_of_items) / float(len(list_of_items))
        return avg


def main():
    poe = PoeItemCrawler('23')
    print(poe.average_of_list(poe.item_reader()))
    print(poe.item_properties())

if __name__ == '__main__':
    main()


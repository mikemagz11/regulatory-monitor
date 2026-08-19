import yaml


def load_watchlist(path="config/watchlist.yml"):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data["watchlists"]


def filter_records(records, watchlists):

    matches = []

    for record in records:

        searchable = " ".join([
            record.get("applicant", ""),
            record.get("entity", "")
        ]).lower()

        for company, aliases in watchlists.items():

            for alias in aliases:

                if alias.lower() in searchable:

                    match = record.copy()
                    match["watchlist"] = company
                    matches.append(match)
                    break

    return matches
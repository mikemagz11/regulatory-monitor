import yaml


with open("config/watchlist.yml", "r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)

ALIASES = CONFIG["hard_rock_aliases"]


def find_matches(records):

    matches = []

    for record in records:

        searchable = (
            f"{record.get('entity', '')} "
            f"{record.get('applicant', '')}"
        ).lower()

        for alias in ALIASES:

            if alias.lower() in searchable:

                match = record.copy()
                match["matched_alias"] = alias

                matches.append(match)

                break

    return matches
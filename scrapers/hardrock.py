HARD_ROCK_ALIASES = [
    "Seminole Hard Rock Digital, LLC",
    "Hard Rock Interactive",
    "Hard Rock Digital",
    "Seminole Hard Rock",
    "Seminole Gaming",
    "Seminole Tribe",
    "Hard Rock",
]


def find_matches(records):
    matches = []

    for record in records:

        searchable = (
            f"{record.get('entity', '')} "
            f"{record.get('applicant', '')}"
        ).lower()

        for alias in HARD_ROCK_ALIASES:

            if alias.lower() in searchable:

                match = record.copy()
                match["matched_alias"] = alias

                matches.append(match)

                break

    return matches
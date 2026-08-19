import json
import os


def load_snapshot(filename):

    if not os.path.exists(filename):
        return []

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def compare_snapshots(old_records, new_records):

    old_lookup = {
        (
            r["applicant"],
            r["section"],
            r["entity"],
        ): r
        for r in old_records
    }

    new_lookup = {
        (
            r["applicant"],
            r["section"],
            r["entity"],
        ): r
        for r in new_records
    }

    new_items = []
    removed_items = []
    changed_items = []

    #
    # Find NEW
    #
    for key, record in new_lookup.items():

        if key not in old_lookup:
            new_items.append(record)

    #
    # Find REMOVED
    #
    for key, record in old_lookup.items():

        if key not in new_lookup:
            removed_items.append(record)

    #
    # Find UPDATED
    #
    for key in old_lookup.keys():

        if key not in new_lookup:
            continue

        old = old_lookup[key]
        new = new_lookup[key]

        if (
            old["status"] != new["status"]
            or old["status_date"] != new["status_date"]
            or old["expiration_date"] != new["expiration_date"]
        ):

            changed_items.append(
                {
                    "before": old,
                    "after": new,
                }
            )

    return new_items, removed_items, changed_items
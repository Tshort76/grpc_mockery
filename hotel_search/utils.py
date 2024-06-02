import json
import os
import toolz as tz

with open(os.path.join("resources", "hotel_search_mocks.json"), "r") as fp:
    MOCK_DATA = json.load(fp)


def mock_lookup_key(request: dict) -> str:
    id_fields = [
        tz.get_in(["user_session", "session_id"], request),
        tz.get_in(["check_in_date", "year"], request),
        tz.get_in(["check_in_date", "month"], request),
        tz.get_in(["check_in_date", "day"], request),
    ]
    return "::".join(map(str, id_fields))

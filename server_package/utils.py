from datetime import datetime, timezone


class Utils:
    @staticmethod
    def convertToUTC(date):
        if date:
            print(date)
            return datetime.fromisoformat(date).replace(tzinfo=timezone.utc)

        return None

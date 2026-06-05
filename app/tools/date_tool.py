from datetime import datetime


class DateTool:

    def get_today(self):

        return datetime.now().strftime(
            "%Y-%m-%d"
        )


date_tool = DateTool()
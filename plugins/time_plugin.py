class TimePlugin:
    def get_current_date(self):
        from datetime import date
        return str(date.today())

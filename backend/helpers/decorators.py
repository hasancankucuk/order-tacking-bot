def with_validated_db(func):
    def wrapper(self, dispatcher, tracker, domain):
        from backend.helpers.path_checker import get_validated_db_path

        db_path = get_validated_db_path(dispatcher)
        if not db_path:
            return []
        return func(self, dispatcher, tracker, domain, db_path)
    return wrapper
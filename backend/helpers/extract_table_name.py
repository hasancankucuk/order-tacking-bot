from sql_metadata import Parser # type: ignore

def extract_table_name(query: str) -> str:
    if query:
        parser = Parser(query)
        tables = parser.tables
        if tables:
            return tables[0]
    
    return ""
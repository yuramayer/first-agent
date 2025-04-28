import pandas as pd
import io


class TableManager:
    def __init__(self):
        self.df = None

    def load_table_from_text(self, text: str) -> str:
        try:
            self.df = pd.read_csv(io.StringIO(text))
            return  f"Таблица успешно загружена! Колонки: \
                {', '.join(self.df.columns)}"
        except Exception as err:
            return f'Ошибка при загрузке таблицы: {str(err)}'
    
    def find_most_frequent(self, column: str) -> str:
        if self.df is None:
            return 'Таблица не загружена'
        if column not in self.df.columns:
            return f"Колонка '{column} не найдена"
        most_common = self.df[column].value_counts().head(5)
        return most_common.to_string()



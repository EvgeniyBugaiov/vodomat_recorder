from pathlib import Path
from datetime import date, timedelta
from zipfile import ZipFile


class Recorder:
    def __init__(self, work_dir: str,
                 report_type: str,
                 archive_dir: str = 'archive'):
        self.report_path = Path(work_dir) / report_type
        self.archive_path = self.report_path / archive_dir
        self.archive_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def created_date(file: Path) -> date:
        date_str = file.stem.split('_')[1]
        return date(int(date_str[:4]), int(date_str[4:6]), int(date_str[6:]))

    def add_to_archive(self, days: int = 1):
        for file in self.report_path.glob('*.xml'):
            file_created_date = self.created_date(file)
            if file_created_date < (date.today() - timedelta(days=days)):
                year, month = file_created_date.year, file_created_date.month
                week = file_created_date.isocalendar()[1]
                zip_file = f'{year}-{month} ({week}).zip'
                zip_file_path = self.archive_path / zip_file
                with ZipFile(zip_file_path, 'a') as week_archive:
                    week_archive.write(file, file.name)
                file.unlink()

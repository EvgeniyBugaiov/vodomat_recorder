from recorder import Recorder

work_dir = '/mnt/recorder/data'
o_reports = Recorder(work_dir, 'O')
z_reports = Recorder(work_dir, 'Z')
x_reports = Recorder(work_dir, 'X')

if __name__ == '__main__':
    o_reports.add_to_archive()
    z_reports.add_to_archive()
    x_reports.add_to_archive()

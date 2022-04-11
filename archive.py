from recorder import Recorder

rec = Recorder('/mnt/recorder/data', 'O')

if __name__ == '__main__':
    rec.add_to_archive()

import os 

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = ROOT_DIR + '/data'

inputs = dict(
    data = dict(
        filename = '01_raw.csv',
        filedir  = DATA_DIR,
        fullpath = DATA_DIR + '/01_raw.csv'
    ),
    rules = dict(
        filename = '01_service_rules.csv',
        filedir  = DATA_DIR,
        fullpath = DATA_DIR + '/service_rules.csv'
    ),
    signals = dict(
        signup = ['coming', 'back', 'signup', 'signing', 'joining', 'welcome'],
        cancellation = ['cancelled', 'cancel']
    ),
    allowed_services = [
        'Netflix', 'CBS All Access', 'Hulu', 'Starz', 'Showtime'
    ]
)

from git import Repo
repo = Repo(ROOT_DIR)

if repo.active_branch.name == 'development':
    outputs = dict(
        local = dict(
            filedir = 'data',
            filename = 'dev-processed_data.csv',
            fullpath = DATA_DIR + '/dev-processed_data.csv'
        ),
        cloud = dict(
            bucket_name = 'antenna-task'
        )
    )
<<<<<<< HEAD
else:
    outputs = dict(
        local = dict(
            filedir = 'data',
            filename = 'processed_data.csv',
            fullpath = DATA_DIR + '/processed_data.csv'
        ),
        cloud = dict(
            bucket_name = 'antenna-task'
        )
    )
=======
)
>>>>>>> development

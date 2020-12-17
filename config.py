import os 


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

inputs = dict(
    data = dict(
        filename = '01_raw.csv',
        filedir  = ROOT_DIR + '/data',
        fullpath = ROOT_DIR + '/data/01_raw.csv'
    ),
    rules = dict(
        filename = '01_service_rules.csv',
        filedir  = ROOT_DIR + '/data',
        fullpath = ROOT_DIR + '/data/service_rules.csv'
    ),
    signals = dict(
        signup = ['coming', 'back', 'signup', 'signing', 'joining', 'welcome'],
        cancellation = ['cancelled', 'cancel']
    ),
    allowed_services = [
        'Netflix', 'CBS All Access', 'Hulu', 'Starz', 'Showtime'
    ]
)

outputs = dict(
    local = dict(
        filedir = 'data',
        filename = 'processed_data.csv',
        fullpath = ROOT_DIR + '/data/processed_data.csv'
    ),
    cloud = dict(
        bucket_name = 'antenna-task'
    )
)

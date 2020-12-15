import os 


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

files = dict(
    raw = ROOT_DIR + '/data/01_raw.csv',
    processed = ROOT_DIR + '/data/02_processed.csv',
    service_rules = ROOT_DIR + '/data/01_service_rules.csv'
)

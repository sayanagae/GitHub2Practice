def load_data():
    print('Loading raw dataset...')
def parse_data(raw_data):
    print('Parsing and cleaning records...')
def validate_inputs(data):
    if not data: raise ValueError('Empty dataset provided')
def export_results(cleaned_data):
    print('Exporting cleaned dataset to output format...')
if __name__ == '__main__':
    print('Running capstone data pipeline...')

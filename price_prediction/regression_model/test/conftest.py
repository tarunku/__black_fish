import pytest


from regression_model.config.core import get_Config
from regression_model.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    #config = create_and_validate_config()
    return load_dataset(file_name= get_Config().app_config.test_data_file)
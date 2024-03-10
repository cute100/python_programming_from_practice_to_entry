
from city_country import get_city_country

def test_first_last_name():
    """能够正确处理像 Santiago Chile这样的国家城市名吗？"""
    formatted_name=get_city_country('santiago','chile')
    assert formatted_name=='Santiago Chile'

def test_first_last_middle_name():
    """能够正确处理像Santiago Chile Population=50000这样的吗？"""
    formatted_name=get_city_country('santiago','chile','50000')
    assert formatted_name=='Santiago Chile-Population=50000'


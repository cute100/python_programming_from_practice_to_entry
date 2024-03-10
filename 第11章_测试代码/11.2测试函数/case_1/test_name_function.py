
from Python编程从入门到实践.第11章_测试代码.case_1.name_function import get_formatted_name

def test_first_last_name():
    """能够正确处理像 Janis Joplin这样的姓名吗？"""
    formatted_name=get_formatted_name('janis','joplin')
    assert formatted_name=='Janis Joplin'

def test_first_last_middle_name():
    """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
    formatted_name=get_formatted_name('wolfgang','mozart','amadues')
    assert formatted_name=='Wolfgang Amadues Mozart'


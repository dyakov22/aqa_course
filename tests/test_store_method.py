import pytest


@pytest.mark.parametrize('store', [('iPhone', 1), ('Pixel', 2)], indirect=True)
def test_possibility_to_get_catalog_with_parametrize(store):
    store, phone_info = store
    result = store.show_catalog()
    assert result
    assert isinstance(result, list)
    assert phone_info == str(result[0])


@pytest.mark.phone_info({'phone': 'iPhone', 'price': 1000})
@pytest.mark.skip('Reason')
def test_possibility_to_get_catalog(store):
    result = store.show_catalog()
    assert result
    assert isinstance(result, list)
    assert 'iPhone at 1000' == str(result[0])


@pytest.mark.skip('Reason')
def test_possibility_to_get_catalog_skip(store):
    result = store.show_catalog()
    assert not result
    assert isinstance(result, list)


def test_possibility_to_get_catalog_with_fin(store_fin):
    result = store_fin.show_catalog()
    assert not result
    assert isinstance(result, list)

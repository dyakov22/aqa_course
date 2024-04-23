import pytest

from python.lesson_15_16.src.store.store_facade import StoreFacade


@pytest.fixture(name='store')
def store_facade(request):
    print('Init Store Facade in fixture')
    store = StoreFacade()
    phone_info = request.param
    if phone_info:
        store.add_phone_to_catalog(*phone_info)

    yield store, str(store.show_catalog()[0])

    print('Clean up Store Facade in fixture')

    del store.catalog.phones


@pytest.fixture(name='store_fin')
def store_facade_with_fin(request):
    print('Init Store Facade in fixture')
    store = StoreFacade()

    def teardown():
        print('Clean up Store Facade in fixture')

        del store.catalog.phones

    request.addfinalizer(teardown)

    return store

# @pytest.fixture(name='store')
# def store_facade(request):
#     print('Init Store Facade in fixture')
#     store = StoreFacade()
#     phone_info = request.node.get_closest_marker('phone_info')
#     if phone_info:
#         store.add_phone_to_catalog(*phone_info.args[0].values())
#
#     yield store
#
#     print('Clean up Store Facade in fixture')
#
#     del store.catalog.phones

#
# @pytest.fixture(name='store', params=[('iPhone', 1), ('Pixel', 2)])
# def store_facade(request):
#     print('Init Store Facade in fixture')
#     phone_model, price = request.param
#     store = StoreFacade()
#     store.add_phone_to_catalog(phone_model, price)
#
#     yield store
#
#     print('Clean up Store Facade in fixture')
#
#     del store.catalog.phones


#
# @pytest.fixture(name='store')
# def store_facade():
#     print('Init Store Facade in fixture')
#
#     store = StoreFacade()
#
#     yield store
#
#     print('Clean up Store Facade in fixture')
#
#     del store.catalog.phones

# @pytest.fixture(autouse=True, scope='class')
# def store_facade_cls(request):
#     print('Init Store Facade in fixture')
#
#     store = StoreFacade()
#     request.cls.store = store
#     yield
#
#     print('Clean up Store Facade in fixture')
#
#     del store.catalog.phones


# @pytest.fixture(scope='package', autouse=True)
# def fix_package():
#     print('From package')
#     yield
#     print('From package, teardown')

#
# @pytest.fixture(scope='module', autouse=True)
# def fix_module():
#     print('From module')
#     yield
#     print('From module, teardown')

# @pytest.fixture(scope="class")
# def setup_class_fixture():
#     print(f'Setup class from conftest')
#     yield
#     print(f'Teardown class from conftest')
#
#
# @pytest.fixture(scope='function')
# def setup_method_fixture():
#     print(f'Setup method from conftest')
#     yield
#     print(f'Teardown method from conftest')

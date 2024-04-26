


def driver_config(platform: str):
    android_config = {'platform': 'android'}
    ios_config = {'platform': 'ios'}
    return android_config if platform.lower() == 'android' else ios_config

    # return config_parser

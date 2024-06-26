"""Врапперы для работы с selenium"""

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge

from library.test_utils.browser_data import BrowserData


def init_chrome(browser_data: BrowserData) -> Chrome:
    """Инициализация веб-драйвера Chrome"""
    options = ChromeOptions()
    options.browser_version = browser_data.version
    for pref in browser_data.prefs:
        options.add_experimental_option('prefs', pref)
    for arg in browser_data.cli_args:
        options.add_argument(arg)
    return Chrome(options=options)


def init_firefox(browser_data: BrowserData) -> Firefox:
    """Инициализация веб-драйвера Firefox"""
    options = FirefoxOptions()
    options.browser_version = browser_data.version
    for pref in browser_data.prefs:
        for name, value in pref.items():
            options.set_preference(name, value)
    for arg in browser_data.cli_args:
        options.add_argument(arg)
    return Firefox(options=options)


def init_edge(browser_data: BrowserData) -> Edge:
    """Инициализация веб-драйвера Edge"""
    options = EdgeOptions()
    options.browser_version = browser_data.version
    for pref in browser_data.prefs:
        options.add_experimental_option('prefs', pref)
    for arg in browser_data.cli_args:
        options.add_argument(arg)
    return Edge(options=options)

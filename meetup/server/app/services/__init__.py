import logging
import pathlib
import importlib
from typing import Callable, Generator
from types import ModuleType

from fastapi import APIRouter


def find_all_modules_path_in_services_by_name(module_name: str) -> Generator[pathlib.Path]:
    services_path = pathlib.Path(__file__).parent.resolve()
    modules_paths = services_path.glob(f"**/{module_name}.py")
    return modules_paths


def get_module_relative_path_by_absolute_path(module_path: pathlib.Path) -> str:
    module_name = module_path.stem
    parent_module_name = module_path.parent.stem
    module_relative_path = f".{parent_module_name}.{module_name}"
    return module_relative_path


def get_and_import_valid_modules(module_name: str, *, validator: Callable[[ModuleType], bool] = None
                                 ) -> Generator[ModuleType]:
    if not module_name.isidentifier():
        raise ValueError(f"Invalid {module_name=}")
    modules_paths = find_all_modules_path_in_services_by_name(module_name)
    for module_path in modules_paths:
        module_relative_path = get_module_relative_path_by_absolute_path(module_path)
        try:
            module = importlib.import_module(module_relative_path, __package__)
        except ImportError:
            logging.error(f"Failed to import module from {module_relative_path}")
            continue
        if not isinstance(validator, Callable) or validator(module):
            yield module


routers = get_and_import_valid_modules("api", validator=(
    lambda module: hasattr(module, "router") and isinstance(module.router, APIRouter)))
signals = get_and_import_valid_modules("signals")

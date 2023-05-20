import pathlib
import importlib

from fastapi import APIRouter


def get_all_valid_routers_from_services():
    modules_path = pathlib.Path(__file__).parent.resolve()
    modules = modules_path.glob("**/api.py")
    for module_path in modules:
        parent_module_name = module_path.parent.stem
        module_name = module_path.stem
        module = importlib.import_module(f".{parent_module_name}.{module_name}", __package__)
        if hasattr(module, "router") and isinstance(module.router, APIRouter):
            yield module


def get_all_valid_signals_from_services():
    modules_path = pathlib.Path(__file__).parent.parent.resolve()
    modules = modules_path.glob("**/signals.py")
    for module_path in modules:
        parent_module_name = module_path.parent.stem
        module_name = module_path.stem
        module = importlib.import_module(f".{parent_module_name}.{module_name}", __package__)
        yield module


routers = [router_module for router_module in get_all_valid_routers_from_services()]
signals = [signal for signal in get_all_valid_signals_from_services()]

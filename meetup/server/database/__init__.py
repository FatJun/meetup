import pathlib


DATABASE_MODULE_PATH = "database"


def get_all_valid_models_from_services():
    modules_path = pathlib.Path(__file__).parent.resolve()
    modules = modules_path.glob("**/models.py")
    for module_path in modules:
        parent_module_name = module_path.parent.stem
        module_name = module_path.stem
        module_dotted_path = f"{DATABASE_MODULE_PATH}.{parent_module_name}.{module_name}"
        yield module_dotted_path


models = [model_dotted_path for model_dotted_path in get_all_valid_models_from_services()]

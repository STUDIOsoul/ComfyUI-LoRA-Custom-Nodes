from ..custom_node_base import SimpleNode

class Dataset_Loader(SimpleNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "dataset_path": ("STRING", {"default": "/content/ComfyUI/dataset/"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_dataset"

    def load_dataset(self, dataset_path):
        return (f"[Dataset Loader]: Loaded from {dataset_path}",)

NODE_CLASS_MAPPINGS = {
    "Dataset_Loader": Dataset_Loader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Dataset_Loader": "Dataset: Loader"
}

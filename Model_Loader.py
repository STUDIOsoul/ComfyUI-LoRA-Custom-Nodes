from ..custom_node_base import SimpleNode

class Model_Loader(SimpleNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_path": ("STRING", {"default": "/content/ComfyUI/models/checkpoints/"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_model"

    def load_model(self, model_path):
        return (f"[Model Loader]: Loaded from {model_path}",)

NODE_CLASS_MAPPINGS = {
    "Model_Loader": Model_Loader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Model_Loader": "Model: Loader"
}

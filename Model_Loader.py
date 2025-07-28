class Model_Loader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "Hola desde Model_Loader!"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "output_text"

    def output_text(self, text):
        return (f"[Model Loader]: {text}",)

NODE_CLASS_MAPPINGS = {
    "Model_Loader": Model_Loader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Model_Loader": "Model Loader"
}

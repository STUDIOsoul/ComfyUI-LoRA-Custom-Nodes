class Dataset_Loader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "Hola desde Dataset_Loader!"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "output_text"

    def output_text(self, text):
        return (f"[Dataset Loader]: {text}",)

NODE_CLASS_MAPPINGS = {
    "Dataset_Loader": Dataset_Loader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Dataset_Loader": "Dataset Loader"
}

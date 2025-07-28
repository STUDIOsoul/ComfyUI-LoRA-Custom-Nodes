class LoRA_Loader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "Hola desde LoRA_Loader!"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "output_text"

    def output_text(self, text):
        return (f"[LoRA Loader]: {text}",)

NODE_CLASS_MAPPINGS = {
    "LoRA_Loader": LoRA_Loader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoRA_Loader": "LoRA Loader"
}

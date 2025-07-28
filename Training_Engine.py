class Training_Engine:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "Hola desde Training_Engine!"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "output_text"

    def output_text(self, text):
        return (f"[Training Engine]: {text}",)

NODE_CLASS_MAPPINGS = {
    "Training_Engine": Training_Engine
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Training_Engine": "Training Engine"
}

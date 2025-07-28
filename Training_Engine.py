from ..custom_node_base import SimpleNode

class Training_Engine(SimpleNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "epochs": ("INT", {"default": 10}),
                "learning_rate": ("FLOAT", {"default": 0.0001}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "train_model"

    def train_model(self, epochs, learning_rate):
        return (f"[Training Engine]: Training for {epochs} epochs with lr={learning_rate}",)

NODE_CLASS_MAPPINGS = {
    "Training_Engine": Training_Engine
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Training_Engine": "Training: Engine"
}

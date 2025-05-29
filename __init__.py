
# wildcard trick is taken from pythongossss's
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_typ = AnyType("*")

class SwapAndScale:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "IN_Height": ("INT", ),
                "IN_Width": ("INT", ),
                "Swap_Width_Height": ("BOOLEAN", {"default": False}),
                "factor_32px": ("BOOLEAN", {"default": True}),
                "Limit_1MP": ("BOOLEAN", {"default": True})
            }
        }
    def adjust_x32(value):
        """Lower value to closest number in factor of 32."""
        return value if value % 32 == 0 else value - (value % 32)

    def scale_values(IN_Height, IN_Width, max_product):
        """Scale IN_Height and IN_Width proportional"""
        factor = (max_product / (IN_Height * IN_Width)) ** 0.5
        new_h = int(IN_Height * factor)
        new_b = int(IN_Width * factor)

        return adjust_x32(new_h), adjust_x32(new_b)

    def process_inputs(IN_Height, IN_Width, IN_swap, factor_32px, Limit_1MP):
        """check inputs and do processing"""
    
        # Step 1: adjust to 32px format if selected
        if factor_32px:
            IN_Height = adjust_x32(IN_Height)
            IN_Width = adjust_x32(IN_Width)

        # Step 2: Check if 1MP is set and adjust
        if Limit_1MP and (IN_Height * IN_Width > 1024000):
            IN_Height, IN_Width = scale_values(IN_Height, IN_Width, 1024000)

        # Step 3: Swap IN_Height and IN_Width if selected
        if IN_swap:
            IN_Height, IN_Width = IN_Width, IN_Height

        return IN_Height, IN_Width

    RETURN_TYPES = ("INT",)
    OUTPUT_NODE = True
    CATEGORY = "Image"
    FUNCTION = "swap_and_scale"

    def swap_and_scale(
        self,
        IN_Height,
        IN_Width,
        Swap_Width_Heightt:False,
        factor_32px:True,
        Limit_1MP:True,
    ):
        process_inputs(IN_Height, IN_Width, IN_swap, factor_32px, Limit_1MP)

        return ("Uploading Completed",)


NODE_CLASS_MAPPINGS = {
    "SwapAndScale": SwapAndScale,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SwapAndScale": "Swap width/height and/ or Scale image",
}
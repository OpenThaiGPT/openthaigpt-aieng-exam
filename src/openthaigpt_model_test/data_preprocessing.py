from .constants import TEXT_COLUMN, IMAGE_COLUMN


def dataset_tokenization(batch_input, processor):
    """
    Description: Tokenize `text` and `image` column with processor
    Args:
        batch_input: Batch columns contains `text` and `image`
        processor: CLIP processor
    Returns:
        batch_output: Batch columns contains `input_ids`, `attention_mask` 
            and `pixel_values`
    """
    return

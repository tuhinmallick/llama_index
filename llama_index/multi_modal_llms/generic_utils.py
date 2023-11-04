from llama_index.schema import ImageDocument


def load_image_urls(image_urls: list[str]) -> list[ImageDocument]:
    # load remote image urls into image documents
    image_documents = []
    for image_url in image_urls:
        new_image_document = ImageDocument()
        new_image_document.metadata["image_url"] = image_url
        image_documents.append(new_image_document)
    return image_documents

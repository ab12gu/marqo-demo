# input images from wiki

import marqo

mq = marqo.Client(url="http://localhost:8882")

settings = {
    "treat_urls_and_pointers_as_images": True,  # allows us to find an image file and index it
    "model": "open_clip/ViT-B-32/laion2b_s34b_b79k",
}
response = mq.create_index("my-multimodal-index", **settings)


response = mq.index("my-multimodal-index").add_documents(
    [
        {
            "My_Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Hipop%C3%B3tamo_%28Hippopotamus_amphibius%29%2C_parque_nacional_de_Chobe%2C_Botsuana%2C_2018-07-28%2C_DD_82.jpg/640px-Hipop%C3%B3tamo_%28Hippopotamus_amphibius%29%2C_parque_nacional_de_Chobe%2C_Botsuana%2C_2018-07-28%2C_DD_82.jpg",
            "Description": "The hippopotamus, also called the common hippopotamus or river hippopotamus, is a large semiaquatic mammal native to sub-Saharan Africa",
            "_id": "hippo-facts",
        }
    ],
    tensor_fields=["My_Image"],
)


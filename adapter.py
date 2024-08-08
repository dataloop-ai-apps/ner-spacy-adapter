import spacy
import dtlpy as dl


class Adapter(dl.BaseModelAdapter):
    def load(self, local_path, **kwargs):
        model_name = self.configuration.get('model_name', "en_core_web_sm")
        self.nlp = spacy.load(model_name)

    def prepare_item_func(self, item: dl.Item):
        buffer = item.download(save_locally=False)
        text = buffer.read().decode()
        return text

    def predict(self, batch, **kwargs):
        batch_annotations = list()
        for text in batch:
            doc = self.nlp(text)
            collection = dl.AnnotationCollection()
            for entity in doc.ents:
                collection.add(dl.Text(text_type='block',
                                       label=entity.label_,
                                       start=entity.start_char,
                                       end=entity.end_char),
                               model_info={'name': self.model_entity.name,
                                           'confidence': 1.})
            batch_annotations.append(collection)
        return batch_annotations


if __name__ == "__main__":
    adapter = Adapter()
    # adapter.predict_items(items=["66b4856680ee7d69c26cd4e8"])
    adapter.load(None)
    doc = adapter.nlp(
        "On April 2, 2023, Apple IncInc., a leading technology company, announced the launch of its newest smartphone, the iPhone 14 Pro MaMax. The device features a groundbreaking new camera system and a powerful A16 Bionic chip. It will be available for pre-order on April 9, 2023, and in stores starting April 16, 2023. The price for the base model starts at $999. Meanwhile, in the realm of politics, US President Joe Biden is scheduled to visit France on May 15, 2023, for a summit with French President Emmanuel Macron to discuss climate change and global security. The meeting is expected to be held at the Élysée Palace in")
    for entity in doc.ents:
        print(entity.label_)
        print(entity.text)
        print(entity.start_char)
        print(entity.end_char)

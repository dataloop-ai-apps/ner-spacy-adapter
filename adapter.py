import spacy
import dtlpy as dl


class Adapter(dl.BaseModelAdapter):
    def load(self, local_path, **kwargs):
        model_name = self.configuration.get('model_name', 'en_core_web_sm')
        self.nlp = spacy.load(model_name)

    def prepare_item_func(self, item: dl.Item):
        buffer = item.download(save_locally=False)
        text = buffer.read().decode()
        return text

    def predict(self, batch, **kwargs):
        batch_annotations = list()
        split_str = ". "
        for text in batch:
            offset = 0
            collection = dl.AnnotationCollection()
            # split by ". " and keep the same char in the chunks
            sentences = text.split(split_str)
            for sentence in sentences:
                sentence += split_str
                results = self.nlp(sentence)
                for entity in results.ents:
                    collection.add(dl.Text(text_type='block',
                                           label=entity.label_,
                                           start=entity.start_char + offset,
                                           end=entity.end_char + offset
                                           ),
                                   model_info={'name': self.model_entity.name,
                                               'confidence': 1.})
                offset += len(sentence)
            batch_annotations.append(collection)
        return batch_annotations

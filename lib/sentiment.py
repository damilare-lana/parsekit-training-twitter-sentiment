import parsekit
from parsekit.schema import DecimalField
from textblob import TextBlob


class AddSentiment(parsekit.Step):

    def run(self, record, metadata):
        schema = metadata.get_closest('schema')
        field_idx = schema.field_index(self.options.field)
        field_val = record[field_idx]
        analyzer = TextBlob(field_val)
        record.append(analyzer.polarity)
        schema.append_field(DecimalField('sentiment_score'))
        metadata['schema'] = schema
        return record, metadata

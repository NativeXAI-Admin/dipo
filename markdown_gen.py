import pandas as pd
import json

class Markdown():
    
    def markdown_table_output(self, data_option_json):
        data = data_option_json
        df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
        markdown_table = df.to_markdown()
        return markdown_table
        

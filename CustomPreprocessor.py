from nbconvert.preprocessors import Preprocessor
import re

# Adapted from https://stackoverflow.com/questions/42255564/how-to-export-and-preserve-linked-jupyter-notebooks/42279992#42279992
class CustomPreprocessor(Preprocessor):

    def preprocess_cell(self, cell, resources, index):
        if 'source' in cell and cell.cell_type == "markdown":
            #print( "BEFORE:" + cell.source )
            cell.source = re.sub(r"\[([^]]*)\]\(([^)]*)\.ipynb\)",r"[\1](\2.html)",cell.source)
            #print( "AFTER:" + cell.source )

        return cell, resources

c = get_config() 
c.HTMLExporter.preprocessors = ['CustomPreprocessor.CustomPreprocessor']
c.FilesWriter.build_directory = './docs'

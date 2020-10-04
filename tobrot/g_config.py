from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1308800587:AAFY0X528VUH41VxHtHXVqaJfyDwzTrB2Kw"
    APP_ID = 1963772
    API_HASH = "698ee5bfa035f3547dda04a847921380"
    OWNER_ID = 1014172906
    AUTH_CHANNEL = [-1001317020794]
    DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"{"access_token":"ya29.a0AfH6SMBg0WF1Hw89Htqw1-IgYGCUceFa3hjw6wo1_czmD-anezT44_b0uCuvQ_IWpLfI6RMhgL8OeJiIEwcLMgQ75ldu-nIaSpFy-984PXWpIDbfATq1z51IPhRo0hTGLz3o2QuKn3ftQ4KHd1ddTI_ZhwYj5gdBn7Y","token_type":"Bearer","refresh_token":"1//0gub1LJLlp9UhCgYIARAAGBASNwF-L9IrEBF9LrOW6uN9tiM8pIuTfPLcNYreQZ_MvgbmIhMc6GqbznOVFwm5Ruz25NIEeZJb5TU","expiry":"2020-10-04T14:13:39.4709345+05:30"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 

class MediaFile:
    def __init__(self,name,size,file_type):
        self.name = name
        self.size = size
        self.file_type = file_type
    def save(self):
        '''
        The method saves file
        :return:
        '''
        pass

    def delete(self):
        pass

    def convert(self,target_format:str):
        pass
class Audio(MediaFile):
    def __init__(self,name,size,file_type,duration):
        super().__init__(name,size,file_type)
        self.duration = duration

class Video(MediaFile):
    def __init__(self,name,size,file_type,resolution):
        super().__init__(name,size,file_type)
        self.resolution = resolution

class Photo(MediaFile):
    def __init__(self,name,size,file_type,picture_resolution):
        super().__init__(name,size,file_type)
        self.picture_resolution = picture_resolution



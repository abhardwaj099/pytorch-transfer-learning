from torch.utils.data import Dataset
from utils import getFiles, getLabel 
import cv2

class ImagesDataset(Dataset):
    """Images Dataset"""
    def __init__(self, dir, transform=None):
      self.dir = dir 
      self.paths = []
      for file in getFiles(dir):
          self.paths.append(file)
      self.transform = transform
    
    def __len__(self):

        return len(self.paths)
    
    def __getitem__(self, index):
    
        sample_path = self.paths[index]
        # sample_path = str(sample_path.resolve())
        im = cv2.imread(str(sample_path.absolute()))

        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

        if self.transform is not None:
            im = self.transform(im)
        label = getLabel(sample_path)
        
        return (im, label)
        

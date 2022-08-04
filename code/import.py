import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

! pip install opendatasets --quiet
import opendatasets as od 
od.download('https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps/download?datasetVersionNumber=7')

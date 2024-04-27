""""
Created on 4/22/2024
by UgoTheAnalyst

"""
# 1. Import package
from pydantic import BaseModel

# 2.Class which describes bank note measurement
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
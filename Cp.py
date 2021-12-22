import plotly_express as px
import csv
import numpy as np

def get_data_source(data_path):
    student = []
    marks = []
    with open(data_path)as f:
        df = csv.DictReader(f)
        for row in df :
            student.append(float(row["Number of days present"]))
            marks.append(float(row["MArks"]))
    return {"x":student,"y":marks}

def find_correlation(data_source):
    re = np.corrcoef(data_source["x"],data_source["y"])
    print("The Correlation is ", re[0,1])
    
def main():
    data_path = "SMDP.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

main()

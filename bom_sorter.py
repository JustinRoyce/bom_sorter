import pandas as pd
import os


SCRIPT_PATH = __file__
SCRIPT_NAME = os.path.basename(SCRIPT_PATH)
ROOT_PATH = os.path.dirname(SCRIPT_PATH)
BOM_PATH = os.path.join(ROOT_PATH,"bom")
CSV_HEADERS = ['Ref',
    'Qnty',
    'Value',
    'Cmp name',
    'Footprint',
    'Description',	
    'Manufacturer',	
    'MPN',	
    'Package',	
    'Rating',
    "PCB"]
CSV_HEADER_SIZE = 11

PASSIVE_C_CMP_NAME = "C"
PASSIVE_R_CMP_NAME = "R_US"

def append_BOM_data():
    frames = []
    csv_fpaths_list = []
    csv_names_list = []
    csv_files = os.listdir(BOM_PATH)
    df = pd.DataFrame()
 
    for csv_file in csv_files:

        csv_fpath = os.path.join(BOM_PATH,csv_file)
        csv_fpaths_list.append(csv_fpath)
        csv_name = csv_file.replace(".csv","")
        
        csv_names_list.append(csv_names_list)
        
        tmp = pd.read_csv(csv_fpath)
        tmp_shape = tmp.shape

        row = tmp_shape[0]
        col = tmp_shape[1]
        PCB_list = []
        for i in range(0,row):
            PCB_list.append(csv_name)

        #print("row:" + str(row))
        #print("col:" + str(col))
        tmp['PCB'] = PCB_list
        frames.append(tmp)
       
    result = pd.concat(frames)
    
    #remove garbage from headers
    frames_cols = list(result.columns.values)
    frames_col_len = len(frames_cols)
   
    if (frames_col_len !=  CSV_HEADER_SIZE):
        for n in range(CSV_HEADER_SIZE,frames_col_len,1):
            trash_header = frames_cols[n]
            #print(str(n)+":" + trash_header)
            result.pop(trash_header)

    return result


if __name__ == "__main__":
    
    BOM_Data = append_BOM_data()

    print("The column headers :")
    print(list(BOM_Data.columns.values))

    #PASSIVE COMPONENT NAMES:
    # Cmp name: C
    # Cmp name: R_US
    # Cmp name: LED

    # CONNECTORS AND SOCKETS:
    # Ref:P*
    # Ref:J*

    # HOLES AND TESTPOINTS:
    # Ref: J*
    # Ref: T*

    # ACTIVE PARTS
    #
    # all other parts
import time
import pandas as pd

from evaluation_diff_quantity import DiffInput, DiffSolution

def load_solution(path):
    # Loads a solution from a json file to a pandas DataFrame.
    df = pd.read_json(path, orient='records')
    # 转换合适的列为 category 类型以优化内存使用
    df['datacenter_id'] = df['datacenter_id'].astype('category')
    df['server_generation'] = df['server_generation'].astype('category')
    df['action'] = df['action'].astype('category')
    
    return df

solution = load_solution('./output/quantity_2663_8.96212e+08.json')
S = DiffSolution(seed=2663, verbose=True)

input:DiffInput = DiffInput(is_new=True, step=1, diff_solution=solution)

score = S.SA_evaluation_function(input)
print(f'Solution score: {score}')

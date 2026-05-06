# USD ONLY FOR TEST
import sys
import json
import talib
import numpy as np

exec_globals = {
    "talib": talib,
    "numpy": np,
    "result": None
}

for line in sys.stdin:
    try:
        data = json.loads(line)
        script_str = data.get("script", "")

        exec(script_str, exec_globals)

        output = exec_globals.get("result")
        print(output)
        
    except Exception as e:
        print(e)
    
    sys.stdout.flush()
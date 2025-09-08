# eval_robustness_reasoning_wrapper.py
import sys
import json
try:
  from control.femformal.eval_robustness_reasoning import eval_robustness as femformal_eval_robustness
except ImportError:
    import sys
    import os
    sys.path.append(os.path.abspath('/localhome/mms43/scratch/mathcoder2/MathCoder2'))
    from control.femformal.eval_robustness_reasoning import eval_robustness as femformal_eval_robustness


def main():
    llm_anchor_output = sys.argv[1]
    llm_interm_output = sys.argv[2]
    robustness, runtime = femformal_eval_robustness(llm_anchor_output, llm_interm_output)
    # Note that this code should not print anything else to stdout or it will screw with the evaluation
    print(json.dumps({
        "robustness": robustness,
        "runtime": runtime
        }))

if __name__ == "__main__":
    main()

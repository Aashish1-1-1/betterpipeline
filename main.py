import numpy as np
from onnxruntime import InferenceSession

if __name__ == "__main__":
    # Load the ONNX model
    sess = InferenceSession("util/spamweb.onnx", providers=["CPUExecutionProvider"])

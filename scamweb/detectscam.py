import numpy as np


def detect(x: str, sess):
    a = len(x)
    b = 1 if "subscribe" in x else 0
    c = 1 if "#" in x else 0
    d = sum(1 for i in x if i.isnumeric())
    e = 0 if "https" in x else 1
    f = len(x.split("/"))

    input_dict = {
        "len_url": np.array([[a]], dtype=np.float32),
        "contains_subscribe": np.array([[b]], dtype=np.float32),
        "contains_hash": np.array([[c]], dtype=np.float32),
        "num_digits": np.array([[d]], dtype=np.float32),
        "non_https": np.array([[e]], dtype=np.float32),
        "num_words": np.array([[f]], dtype=np.float32),
    }

    # Predict
    pred_ort = sess.run(None, input_dict)
    print(pred_ort)
    return pred_ort

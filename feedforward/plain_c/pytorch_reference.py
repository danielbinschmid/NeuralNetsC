import torch
torch.manual_seed(42)
import torch.nn as nn

def run():
    IN_FEATS=5
    OUT_FEATS=6

    ff = nn.Linear(
        in_features=IN_FEATS,
        out_features=OUT_FEATS,
        bias=True,
        dtype=torch.float32
    )

    dummy_tensor = torch.randn([1, IN_FEATS])

    result = ff.forward(
        input=dummy_tensor
    ) 

    print("Input: ", dummy_tensor)
    print("Weights: ", ff.weight.T)
    print("Bias: ", ff.bias)
    print("Output: ", result)

if __name__ == "__main__":
    run()
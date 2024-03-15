# NeuralNetsC

This repository contains C or C++ code for a collection of neural networks. The design goal is to provide dependency-free C/C++ code that can be used by ASIP simulator tools such as Synopsis or Chipyard.

## Collection

|Name of NN|Source|Language|Supports|
|-|-|-|-|
|[LeNet5](./codegen/lenet5/)|[CodeGen, Apache TVM]((https://github.com/danielbinschmid/C-CodeGen-NN))|Dependency-free C|Baremetal RISC-V compiler|
|[MNIST CNN](./codegen/mnist_cnn/)|[CodeGen, Apache TVM]((https://github.com/danielbinschmid/C-CodeGen-NN))|Dependency-free C|Baremetal RISC-V compiler|
|[Transformer Encoder Layer](./codegen/transformer_enc_layer/)|[CodeGen, Apache TVM]((https://github.com/danielbinschmid/C-CodeGen-NN))|Dependency-free C|Baremetal RISC-V compiler|
|[Linear Layer](./feedforward/plain_c/)|Handwritten|Dependency-free C|Standard GCC|

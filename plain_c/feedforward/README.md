# LinearLayerC

## Pytorch

0. Virtual environment with python version 3.10.13.
1. torch 2.2.1, CPU version is sufficient, [install instructions](https://download.pytorch.org/whl/cpu).
2. `pip install -r requirements.txt`

## C Code

```s
$ cd c_code
```

1. Build SML (Small Matrix Library).

```s
$ cd lib/sml
$ make
$ cd ../../
```

2. Build executable

```s
$ cd src
$ make
```

3. Run executable

```s
$ ./linear
```

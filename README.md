# ManiCM

## environment
```bash
$ mamba env create -f conda_environment.yaml
$ conda activate consistency-policy
```


## train Teacher Model
choose GPU number in `train_DPTeacher.sh`
```bash
$ cd ManiCM
$ bash train_DPTeacher.sh
```

## train Student Model
choose GPU number in `train_DPStudent.sh`
```bash
$ cd ManiCM
$ bash train_DPStudent.sh
```


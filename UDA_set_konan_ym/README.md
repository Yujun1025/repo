# Unsupervised Domain Adaptation (충분한 Unlabeled Target Data 가정)

## 추가 계획
### - 데이터셋 추가 예정 (HUST 다른 Load, PU, MFPT, JNU 등)
### - Train,val,test 분리 수정 예정
### - Hyperparmeter Tuning 예정 
### - [최신 UDA 코드 추가 예정][https://github.com/zhaoxin94/awesome-domain-adaptation]
### - 인풋 형태 변경 코드 추가 예정 (Spectrogram 등)

## Competing Methods (Signal Size 2048)
### DA모델 11개, DG모델 2개

### Domain Adaptation Models
- **CNN** - Base
- **ACDANN** - Integrating expert knowledge with domain adaptation for unsupervised fault diagnosis. [Published in TIM 2021](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9612159) | [View Code](/models/ACDANN.py)
- **ADACL** - Adversarial domain adaptation with classifier alignment for cross-domain intelligent fault diagnosis of multiple source domains. [Published in Measurement Science and Technology 2020](https://iopscience.iop.org/article/10.1088/1361-6501/abcad4/pdf) | [View Code](/models/ADACL.py)
- **BSP** - Transferability vs. discriminability: Batch spectral penalization for adversarial domain adaptation. [Published in ICML 2019](http://proceedings.mlr.press/v97/chen19i/chen19i.pdf) | [View Code](/models/BSP.py) 
- **CDAN** - Conditional adversarial domain adaptation. [Published in NIPS 2018](http://papers.nips.cc/paper/7436-conditional-adversarial-domain-adaptation) | [View Code](/models/CDAN.py) 
- **CORAL** - Deep coral: Correlation alignment for deep domain adaptation. [Published in ECCV 2016](https://arxiv.org/abs/1607.01719) | [View Code](/models/CORAL.py)
- **DAN** - Learning transferable features with deep adaptation networks. [Published in ICML 2015](http://ise.thss.tsinghua.edu.cn/~mlong/doc/deep-adaptation-networks-icml15.pdf) | [View Code](/models/DAN.py)
- **DANN** - Unsupervised domain adaptation by backpropagation. [Published in ICML 2015](http://proceedings.mlr.press/v37/ganin15.pdf) | [View Code](/models/DANN.py)
- **MCD** - Maximum classifier discrepancy for unsupervised domain adaptation. [Published in CVPR 2018](http://openaccess.thecvf.com/content_cvpr_2018/papers/Saito_Maximum_Classifier_Discrepancy_CVPR_2018_paper.pdf) | [View Code](/models/MCD.py)

- **MFSAN** - Aligning domain-specific distribution and classifier for cross-domain classification from multiple sources. [Published in AAAI 2019](https://ojs.aaai.org/index.php/AAAI/article/view/4551) | [View Code](/models/MFSAN.py) 
- **MSSA** - A multi-source information transfer learning method with subdomain adaptation for cross-domain fault diagnosis. [Published in Knowledge-Based Systems 2022](https://reader.elsevier.com/reader/sd/pii/S0950705122001927?token=03BD384CA5D6E0E7E029B23C739C629913DE8F8BB37F6331F7D233FB6C57599BFFC86609EE63BE2F9FC43871D96A2F61&originRegion=us-east-1&originCreation=20230324021230) | [View Code](/models/MSSA.py)


### Domain Generalization Models
- **IRM** - Invariant risk minimization. [Published in ArXiv 2019](https://arxiv.org/abs/1907.02893) | [View Code](/models/IRM.py)
- **IBN** - Two at once: Enhancing learning and generalization capacities via IBN-Net. [Published in ECCV 2018](https://openaccess.thecvf.com/content_ECCV_2018/papers/Xingang_Pan_Two_at_Once_ECCV_2018_paper.pdf) | [View Code](/models/IBN.py)


## Getting Started
### Requirements
Our code runs fine with the following prerequisites:
*  Python 3 (>=3.8)
*  Pytorch (>=1.10)
*  Numpy (>=1.21.2)
*  Pandas (>=1.5.3)
*  tqdm (>=4.46.1)
*  Scipy (>=1.10)

Example folder structure for HUST dataset:
```
.
└── datasets
    └── HUST
        ├── condition_0
        │   ├── ball
        │   │   └── B504_sim.mat
        │   ├── inner
        │   │   └── I504_sim.mat
        │   ...
        ├── condition_1
        │   ├── ball
        │   │   └── B504.mat
        │   ...
        ├── condition_2
        ...
```


#### One-to-One Transfer
Example: Transfer from CWRU operation condition 0 to condition 1. (1730 -> 1750)
```shell
python train.py --model_name DANN --source CWRU_0 --target CWRU_1 --train_mode single_source --cuda_device 0
```

Example: Transfer from HUST operation condition 0 to condition 1. (504_Simulation-> 504_Real)
```shell
python train.py --model_name DANN --source HUST_0 --target HUST_1 --train_mode single_source --cuda_device 0
```

# 전체 모델 성능 비교
```shell
bash HUST_train.sh
```

```shell
bash CWRU_train.sh
```

## Citation
Your support in citing our project when used in your research is highly appreciated. It helps in the recognition and dissemination of our work. Please use the following citation format:
```latex
@misc{TL-Bearing-Fault-Diagnosis,
    author = {Jinyuan Zhang},
    title = {TL-Bearing-Fault-Diagnosis},
    year = {2022},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/Feaxure-fresh/TL-Bearing-Fault-Diagnosis}}
}

```


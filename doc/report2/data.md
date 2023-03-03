# 实验报告

数据

MF



## Embedding

|               | 多任务方式                                                   | 迭代优化方式*                                                |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 相加 & TransR | Precision [0.2922, 0.2548]<br/>Recall [0.0655, 0.1105]<br/>NDCG [0.3063, 0.2818] | Precision [0.2859, 0.2539]<br/>Recall [0.0652, 0.1121]<br/>NDCG [0.2986, 0.2793] |
| 相乘 & TransR | Precision [0.1195, 0.1020]<br/>Recall [0.0240, 0.0396]<br/>NDCG [0.1294, 0.1156] | Precision [0.1110, 0.0886]<br/>Recall [0.0221, 0.0358]<br/>NDCG [0.1241, 0.1057] |
| 拼接 & TransR | Precision [0.2926, 0.2550]<br/>Recall [0.0657, 0.1107]<br/>NDCG [0.3065, 0.2820] | Precision [0.2864, 0.2541]<br/>Recall [0.0652, 0.1121]<br/>NDCG [0.2988, 0.2795] |
| 相加 & TransE | Precision [0.2890, 0.2508]<br/>Recall [0.0658, 0.1093]<br/>NDCG [0.3040, 0.2796] | Precision [0.2890, 0.2445]<br/>Recall [0.0671, 0.1089]<br/>NDCG [0.2996, 0.2724] |
| 相乘 & TransE | Precision [0.1767, 0.1600]<br/>Recall [0.0372, 0.0658]<br/>NDCG [0.1783, 0.1694] | Precision [0.1378, 0.1114]<br/>Recall [0.0286, 0.0442]<br/>NDCG [0.1564, 0.1339] |
| 拼接 & TransE | Precision [0.2890, 0.2508]<br/>Recall [0.0658, 0.1093]<br/>NDCG [0.3039, 0.2796] | Precision [0.2890, 0.2447]<br/>Recall [0.0671, 0.1090]<br/>NDCG [0.2995, 0.2724] |

```
多任务方式

TransR & 相加
Precision [0.2922, 0.2548]
Recall [0.0655, 0.1105]
NDCG [0.3063, 0.2818]

TransR & 相乘
Precision [0.1195, 0.1020]
Recall [0.0240, 0.0396]
NDCG [0.1294, 0.1156]

TransR & 拼接
Precision [0.2926, 0.2550]
Recall [0.0657, 0.1107]
NDCG [0.3065, 0.2820]

TransE & 相加
Precision [0.2890, 0.2508]
Recall [0.0658, 0.1093]
NDCG [0.3040, 0.2796]

TransE & 相乘
Precision [0.1767, 0.1600]
Recall [0.0372, 0.0658]
NDCG [0.1783, 0.1694]

TransE & 拼接
Precision [0.2890, 0.2508]
Recall [0.0658, 0.1093]
NDCG [0.3039, 0.2796]
```

```
迭代优化方式

相加 & TransR
Precision [0.2859, 0.2539]
Recall [0.0652, 0.1121]
NDCG [0.2986, 0.2793]

相乘 & TransR
Precision [0.1110, 0.0886]
Recall [0.0221, 0.0358]
NDCG [0.1241, 0.1057]

拼接 & TransR
Precision [0.2864, 0.2541]
Recall [0.0652, 0.1121]
NDCG [0.2988, 0.2795]

相加 & TransE
Precision [0.2890, 0.2445]
Recall [0.0671, 0.1089]
NDCG [0.2996, 0.2724]

相乘 & TransE
Precision [0.1378, 0.1114]
Recall [0.0286, 0.0442]
NDCG [0.1564, 0.1339]

拼接 & TransE
Precision [0.2890, 0.2447]
Recall [0.0671, 0.1090]
NDCG [0.2995, 0.2724]
```



## GNN

| n_layer2          | 多任务方式 *                                                 | 迭代优化方式                                                 |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| gcn & TranR       | Precision [0.3096, 0.2714]<br/>Recall [0.0732, 0.1225]<br/>NDCG [0.3276, 0.3035] | Precision [0.3096, 0.2705]<br/>Recall [0.0733, 0.1222]<br/>NDCG [0.3257, 0.3008] |
| graphsage & TranR | Precision [0.3092, 0.2658]<br/>Recall [0.0732, 0.1224]<br/>NDCG [0.3198, 0.2951] | Precision [0.3051, 0.2707]<br/>Recall [0.0742, 0.1241]<br/>NDCG [0.3140, 0.2961] |
| lightgcn & TranR  | Precision [0.3074, 0.2678]<br/>Recall [0.0748, 0.1263]<br/>NDCG [0.3200, 0.2977] | Precision [0.3163, 0.2711]<br/>Recall [0.0767, 0.1241]<br/>NDCG [0.3332, 0.3050] |
| gcn & TranE       | Precision [0.3248, 0.2740]<br/>Recall [0.0757, 0.1250]<br/>NDCG [0.3369, 0.3066] | Precision [0.2989, 0.2566]<br/>Recall [0.0732, 0.1160]<br/>NDCG [0.3088, 0.2838] |
| graphsage & TranE | Precision [0.3123, 0.2696]<br/>Recall [0.0721, 0.1200]<br/>NDCG [0.3225, 0.2965] | Precision [0.3154, 0.2617]<br/>Recall [0.0738, 0.1207]<br/>NDCG [0.3284, 0.2951] |
| lightgcn & TranE  | Precision [0.3195, 0.2691]<br/>Recall [0.0756, 0.1273]<br/>NDCG [0.3339, 0.3036] | Precision [0.3226, 0.2801]<br/>Recall [0.0767, 0.1290]<br/>NDCG [0.3365, 0.3117] |

```
迭代优化方式

transE & graphsage
Precision [0.3154, 0.2617]
Recall [0.0738, 0.1207]
NDCG [0.3284, 0.2951]

transE & lightgcn
Precision [0.3226, 0.2801]
Recall [0.0767, 0.1290]
NDCG [0.3365, 0.3117]

transE & gcn
Precision [0.2989, 0.2566]
Recall [0.0732, 0.1160]
NDCG [0.3088, 0.2838]

transR & gcn
Precision [0.3096, 0.2705]
Recall [0.0733, 0.1222]
NDCG [0.3257, 0.3008]

transR & graphsage
Precision [0.3051, 0.2707]
Recall [0.0742, 0.1241]
NDCG [0.3140, 0.2961]
```

```
多任务优化方式

gcn & TranR
Precision [0.3096, 0.2714]
Recall [0.0732, 0.1225]
NDCG [0.3276, 0.3035]

graphsage & TranR
Precision [0.3092, 0.2658]
Recall [0.0732, 0.1224]
NDCG [0.3198, 0.2951]

lightgcn & TranR
Precision [0.3074, 0.2678]
Recall [0.0748, 0.1263]
NDCG [0.3200, 0.2977]

gcn & TranE
Precision [0.3248, 0.2740]
Recall [0.0757, 0.1250]
NDCG [0.3369, 0.3066]

graphsage & TranE
Precision [0.3123, 0.2696]
Recall [0.0721, 0.1200]
NDCG [0.3225, 0.2965]

lightgcn & TranE
Precision [0.3195, 0.2691]
Recall [0.0756, 0.1273]
NDCG [0.3339, 0.3036]
```




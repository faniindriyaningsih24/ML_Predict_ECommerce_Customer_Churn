# **E-commerce Customer Churn Prediction**
**by : Fani Indriyaningsih**

---
# Business Problem Understanding

## Context
Sebuah perusahaan ritel online (E-commerce) berusaha untuk mengidentifikasi pelanggan yang kemungkinan besar akan berhenti menggunakan layanan mereka, atau yang dikenal dengan istilah "churn." Dengan memprediksi pelanggan yang berpotensi beralih ini, perusahaan dapat mengambil langkah proaktif untuk mempertahankan mereka, seperti menawarkan promosi khusus, diskon, atau insentif lainnya. Tujuan utamanya adalah untuk meningkatkan loyalitas pelanggan dan mengurangi tingkat churn, yang pada akhirnya akan mendukung operational cost dalam meminimalisir cost promosi.

Target :<br>
0 = No Churn<br>
1 = Churn

## Problem Statement
Dalam domain e-commerce, mendapatkan pelanggan baru umumnya lebih mahal daripada mempertahankan pelanggan yang sudah ada. Pelanggan biasanya pergi jika mereka tidak mendapatkan insentif yang baik. Oleh karena itu, perusahaan ingin memprediksi customer churn agar meminimalisir biaya promosi.

## Goals
Perusahaan mampu memprediksi e-commerce customer yang akan churn

## Analytic Approach
Membangun model klasifikasi yang akan membantu perusahaan untuk dapat memprediksi pelanggan yang terindikasi akan churn atau no churn pada e-commerce tersebut.

True Positive (TP)  : Predict No Churn Actual No Churn
False Positive (FP) : Predict No Churn Actual Churn
True Negative (TN)  : Prediect Churn Actual Churn
False Negative (FN) : Predict Churn Actual No Churn
Focus :
- FP
  <br>Dampak : Provit perusahaan kecil karna predict No churn , Actual Churn
- FN
  <br>Dampak : Biaya promosi besar yang telah dikeluarkan karna predict churn, Actual No Churn

Matrix Evaluation menggunakan F1 - Score
<br>F1 - Score digunakan karena pada case ini akan berfocus pada permasalahan FP dan 

---
# Data Understanding
## Features
| No. | Attribute | Description |
| --- | --- | --- |
|1.|Tenure|Masa customer berlangganan pada e-commerce|
|2.|WarehouseToHome|Jarak antara gudang dengan rumah customer|
|3.|NumberOfDeviceRegistered|Jumlah perangkat yang didaftarkan pada satu akun customer tertentu|
|4.|PreferedOrderCat|Kategori yang dipesan dalam satu bulan terakhir|
|5.|SatisfactionScore|Nilai kepuasan pelanggan terhadap layanan|
|6.|MaritalStatus|Status pernikahan customer|
|7.|NumberOfAddress|Jumlah alamat yang ditambahkan customer pada ecommerce|
|8.|Complaint|Keluhan yang diajukan dalam satu bulan terakhir|
|9.|DaySinceLastOrder|Hari terakhir pemesanan pada e-commerce|
|10.|CashbackAmount|Jumlah rata-rata cashback dalam satu bulan terakhir|
|11.|Churn|Tanda customer teridentifikasi churn atau tidak churn, <br> 0 = No Churn, 1 = Churn|

## Data Info
Jumlah baris dan kolom di dataframe df adalah (3941, 11)
Data columns (total 11 columns):
|    | Column                   | Non-Null Count|  Dtype  |
|--- | ------------------------ | --------------|  -----  |
| 0  | Tenure                   | 3747 non-null |  float64|
| 1  | WarehouseToHome          | 3772 non-null |  float64|
| 2  | NumberOfDeviceRegistered | 3941 non-null |  int64  |
| 3  | PreferedOrderCat         | 3941 non-null |  object |
| 4  | SatisfactionScore        | 3941 non-null |  int64  |
| 5  | MaritalStatus            | 3941 non-null |  object |
| 6  | NumberOfAddress          | 3941 non-null |  int64  |
| 7  | Complain                 | 3941 non-null |  int64  |
| 8  | DaySinceLastOrder        | 3728 non-null |  float64|
| 9  | CashbackAmount           | 3941 non-null |  float64|
| 10 | Churn                    | 3941 non-null |  int64  |

## Unique Values & Missing Values
| 	|dataFeatures	          |dataType	    |null   |null% 	|unique|unique sample|
|---|-------------------------|-------------|-------|-------|------|-------------|
| 0	|Tenure                   |float64	    |194	|4.92	|36	   |[17.0, 10.0] |
| 1	|WarehouseToHome	      |float64	    |169	|4.29	|33	   |[25.0, 6.0]  |
| 2	|NumberOfDeviceRegistered |int64	    |0	    |0.00	|6	   |[6, 4]       |
| 3	|PreferedOrderCat	      |object	    |0	    |0.00	|6	   |[Others, Laptop&Accessory]|
| 4	|SatisfactionScore	      |int64	    |0	    |0.00	|5	   |[3, 5]       |
| 5	|MaritalStatus	          |object	    |0	    |0.00	|3	   |[Single, Divorced]|
| 6	|NumberOfAddress	      |int64	    |0	    |0.00	|14	   |[1, 7]|
| 7	|Complain	              |int64	    |0	    |0.00	|2	   |[1, 0]|
| 8	|DaySinceLastOrder	      |float64	    |213	|5.40	|22	   |[15.0, 10.0]|
| 9	|CashbackAmount	          |float64	    |0	    |0.00	|2335	[151.3, 126.22]|
| 10|Churn	                  |int64	    |0	    |0.00	|2	   |[1, 0]|

## Duplicate Data
Total number of duplicate rows: 671 atau 17.026135498604415

## Inconsisten Data
Feature ***PreferedOrderCat***	terdapat inconsisten data yaitu pada value Mobile dan Mobile Phone. Terdapat value yang memiliki arti sama namun beda penulisan, values yang digunakan tidak konsisten.

## Outliers
    - data Tenure memiliki outliers 4
    - data WarehouseToHome memiliki outliers 1
    - data NumberOfDeviceRegistered memiliki outliers 271
    - data SatisfactionScore memiliki outliers 0
    - data NumberOfAddress memiliki outliers 3
    - data Complain memiliki outliers 0
    - data DaySinceLastOrder memiliki outliers 43
    - data CashbackAmount memiliki outliers 316
    - data Churn memiliki outliers 674
---
# Data Cleaning
## Handling Missing Values
Handling missing values diisi dengan nilai median , dikarenakan data berdistribusi tidak normal.
serta Handling missing values diisi dengan nilai median atau cara simple, tanpa menggunakan KNNImputer atau ML karena percentage data missing values masih relatih kecil, hanya sebesar 5%.

## Handling Duplicate Data
Handling duplicate data pada case ini yaitu menghapus data duplicate, karena agar data tidak bias dan diasumsikan data duplicate ini bersumber dari CustomerID yang sama.

## Handling Inconsisten Data
Pada feature **PreferedOrderCat** terdapat nilai **Mobile Phone** dan **Mobile**. Terdapat ketidak konsistenan data. Maka nilai **Mobile** akan di ubah menjadi **Mobile Phone**.

## Handling Outliers
    Outliers tidak akan dihapus karena outliers masih masuk akal dan masih relevan dengan data lainnya.
---
# Data Preprocessing & Feature Engineering
## Column Transformer
- Feature **PreferedOrderCat** dan **MaritalStatus** ditransform menggunakan **One Hot Encoding**
- Feature **Tenure**, **WarehouseToHome**, **NumberOfDeviceRegistered**, **SatisfactionScore**, **NumberOfAddress**, **Complain**, **DaySinceLastOrder**, **CashbackAmount** ditransform menggunakan **Robust Scaler** karena data yang digunakan mengandung banyak outliers dan berdistribusi tidak normal.

|No| Attribute               | Data Type | Encoder |Scaler     |
|--|-------------------------|-----------|---------|-----------|
|1 |Tenure                   |float	     |         |Robust     |
|2 |WarehouseToHome          |float      |         |Robust     |
|3 |NumberOfDeviceRegistered |int	     |         |Robust     |
|4 |PreferedOrderCat         |str	     |One Hot  |           |
|5 |SatisfactionScore 	     |int	     |         |Robust     |
|6 |MaritalStatus	         |str	     |One Hot  |           |
|7 |NumberOfAddress	         |int	     |         |Robust     |
|8 |Complain	             |int	     |         |Robust     |
|9 |DaySinceLastOrder 	     |float	     |         |Robust     |
|10|CashbackAmount 	         |float	     |         |Robust     |

## Split Data
Pembagian data train dan data test yaitu 80 : 20 karena salah satu praktik umum dalam machine learning

## Check Imbalance & Resampling Benchmarking
Check Imbalance
|     |Value Counts|Percentage|
|-----|------------|----------|
|Churn|            |          | 
|0    |2188        |83.671128 |
|1    |427         |16.328872 |


Result Resampling Benchmarking
RandomUnderSampler: 0.6345
RandomOverSampler: 0.7415
SMOTE: 0.6791
NearMiss: 0.3818

Berdasarkan plot diatas feature CHurn (Target) ternyata imbalance, setelah dilakukan resampling benchmarking metode RandomOverSampler memiliki score tertinggi sebesar 0.7415. Maka pada case ini resampling menggunakan RandomOverSampler.

# Benchmark Modeling
Dilakukan benchmark modelling dengan metode sebagai berikut :
- Random Forest
- Gradient Boost
- Support Vector Classifier (SVC)
- K-Nearest Neighbors (KNN)
- Logistic Regression

Model - model tersebut dipilih karena cocok untuk data yang memiliki banyak outliers dan jumlah data relatif sedikit.
Result Benchmark Modeling
|     |Model	           |Mean F1 Score (Train)|STD (Train)|Mean F1 Score (Test)|
|-----|--------------------|---------------------|-----------|--------------------|
|0	  |Random Forest	   |0.719871	         |0.019393	 |0.758294            |     
|1	  |GBoost	           |0.662947	         |0.014074	 |0.689394            |
|2	  |SVM	               |0.618487	         |0.014491	 |0.654545            |
|4	  |Logistic Regression |0.568795	         |0.009256	 |0.544892            |
|3 	  |KNN	               |0.553871	         |0.018476	 |0.550523            |

- Di dapat 2 Model terbaik yaitu Random Forest dengan Mean F1 Score (Train) sebesar 0.719871 dan GBoost dengan Mean F1 Score (Train) sebesar 0.662947.  

# Hyperparameter Tuning
Result hyperparameter tuning :

<br>**Random Forest**
- Best parameters: {'rdf__max_depth': 20, 'rdf__min_samples_leaf': 2, 'rdf__min_samples_split': 5, 'rdf__n_estimators': 200}
- Best cross-validated F1 score: 0.7319782857060783

<br>**Gradient Boost**
- Best parameters: {'gboost__learning_rate': 0.05, 'gboost__max_depth': 5, 'gboost__max_features': 'sqrt', 'gboost__min_samples_leaf': 1, 'gboost__min_samples_split': 5, 'gboost__n_estimators': 100, 'gboost__subsample': 0.6}
- Best cross-validated F1 score: 0.6863124653615971

Setelah dilakukan hyperparameter tuning. Didapat performa yang baik yaitu Random Forest dengan Best parameters: {'rdf__max_depth': 20, 'rdf__min_samples_leaf': 2, 'rdf__min_samples_split': 5, 'rdf__n_estimators': 200}
dan Best cross-validated F1 score: 0.7319782857060783.
Maka pada case ini Machine Learning akan dideploy menggunakan model RandomForest

Random Forest adalah salah satu metode ensemble learning yang menggunakan banyak pohon keputusan (decision trees) untuk melakukan klasifikasi atau regresi. Cara Kerja Random Forest :
1. Pembuatan Banyak Pohon Keputusan: Random Forest membangun banyak pohon keputusan (biasanya ratusan atau ribuan) dari subset data pelatihan yang berbeda. Setiap pohon dibangun menggunakan sampel acak dari data pelatihan dengan penggantian (bootstrap sampling).
2. Random Feature Selection: Untuk setiap split di setiap pohon, hanya subset acak dari fitur yang dipertimbangkan. Ini membantu mengurangi korelasi antara pohon-pohon dan meningkatkan keragaman model.
3. Voting atau Averaging: Untuk klasifikasi, hasil akhir diputuskan berdasarkan voting mayoritas dari semua pohon. Untuk regresi, hasil akhir adalah rata-rata dari semua prediksi pohon.

Random Forest efektif dalam menghadapi dataset dengan banyak outlier dan jumlah data yang kecil karena:
- Menggunakan banyak pohon untuk mengurangi overfitting.
- Robust terhadap outlier karena teknik bagging dan random feature selection.
- Optimalisasi parameter melalui cross-validation untuk mendapatkan performa terbaik dalam hal F1 score.

Dengan pendekatan ini, Random Forest dapat menjadi model yang kuat dan stabil meskipun bekerja dengan data yang kecil.

# Final Model
Model klasifikasi churn menunjukkan kinerja yang sangat baik dalam memprediksi customer yang berpotensi churn. Dengan F1-Score 0.67 dan akurasi 90.67% serta dengan precision 79% dan recall 58%, model ini mampu mengidentifikasi customer yang tidak churn dengan sangat akurat, serta memprediksi customer yang churn dengan tingkat keberhasilan yang cukup tinggi. Dengan demikian, model ini dapat membantu perusahaan mengurangi risiko kehilangan customer dan meningkatkan loyalitas customer.

Hal ini dapat dilihat dari confusion matrix dimana model memprediksi 531 customer tidak churn dengan benar (TP), 16 customer tidak churn salah prediksi sebagai churn (FN), 45 customer churn salah prediksi sebagai tidak churn (FP), dan 62 customer churn diprediksi dengan benar (TN).

# Model Evaluation
model memiliki performa yang cukup baik dengan nilai F1 score yang semakin tinggi seiring dengan bertambahnya jumlah training examples. Terlihat juga bahwa nilai F1 score pada data training dan data test tidak terlalu jauh berbeda, hal ini menunjukkan bahwa model tidak mengalami overfitting.

# Feature Importance
<br>- Tenure adalah fitur yang paling signifikan dalam mempengaruhi prediksi model. Menunjukkan bahwa ia dapat memiliki dampak besar baik positif maupun negatif pada prediksi.
<br>- CashbackAmount, Jumlah cashback memiliki dampak yang signifikan terhadap prediksi. Menunjukkan bahwa cashback yang lebih tinggi cenderung berkontribusi pada prediksi.
<br>- WarehouseToHome, Jarak atau waktu dari gudang ke rumah memiliki pengaruh moderat terhadap prediksi.
<br>- Complain memiliki pengaruh yang terhadap prediksi. Dapat dilihat bahwa adanya keluhan cenderung memberikan dampak pada prediksi customer churn.
<br>- NumberOfAddress, Jumlah alamat yang terdaftar juga merupakan fitur penting. Menunjukkan bahwa memiliki pengaruh besar baik positif maupun negatif.
<br>- DaySinceLastOrder, Hari sejak pesanan terakhir memiliki pengaruh yang cukup signifikan. Menunjukkan bahwa memiliki pengaruh besar baik positif maupun negatif.
<br>- SatisfactionScore, Skor kepuasan pelanggan memiliki dampak yang signifikan, di mana skor yang lebih tinggi cenderung memberikan dampak positif pada prediksi.
<br>- NumberOfDeviceRegistered, Jumlah perangkat yang terdaftar juga berpengaruh pada prediksi, dengan distribusi yang lebih lebar menunjukkan dampak yang cukup signifikan.
<br>- PreferedOrderCat_Mobile Phone, preferensi untuk memesan kategori mobile phone juga mempengaruhi prediksi model, tetapi dengan dampak yang lebih terfokus pada sisi negatif.
<br>- MaritalStatus_Single, juga mempengaruhi prediksi model, tetapi dengan dampak yang lebih terfokus pada sisi negatif.
<br>- MaritalStatus_Married, PreferedOrderCat_Laptop&Accessory, PreferedOrderCat_Grocery, PreferedOrderCat_Others memiliki pengaruh yang lebih kecil dibandingkan fitur-fitur lainnya.

# Conclusion & Recommendation
**Conclusion Model**
1. Model dapat melakukan prediksi customer churn, sehingga promosi dapat tepat sasaran.
   - Best model Random Forest dalam memprediksi customer churn
      |F1-Score|akurasi|precision|recall|
      |---------|-------|---------|-------|
      |0.67    |90.67% |79%      |58%   | 
2. Model dapat membantu meningkatkan customer retention rate.

**Recommendation Model**
1. Penambahan kolom seperti PreferredPaymentMode, HourSpendOnApp atau OrderCount agar dapat membantu mengurangi bias model dengan memasukkan informasi yang lebih lengkap dan akurat tentang data.
2. Menambahkan CustomerID untuk memastikan data dan sebagai pendukung langkah handling data duplicate.
3. Meningkatkan jumlah data agar hasil tidak mengarah ke overfitting.

**Conclusion Bisnis**
1. Model dapat melakukan prediksi terhadap customer yang terindikasi churn
   - Dilihat dari confusion matrix dimana model memprediksi 531 customer tidak churn dengan benar (TP), 16 customer tidak churn salah prediksi sebagai churn (FN), 45 customer churn salah prediksi sebagai tidak churn (FP), dan 62 customer churn diprediksi dengan benar (TN).
2. Terdapat 5 faktor yang mempengaruhi prediksi
<br>- Tenure adalah fitur yang paling signifikan dalam mempengaruhi prediksi model. Menunjukkan bahwa ia dapat memiliki dampak besar baik positif maupun negatif pada prediksi.
<br>- CashbackAmount, Jumlah cashback memiliki dampak yang signifikan terhadap prediksi. Menunjukkan bahwa cashback yang lebih tinggi cenderung berkontribusi pada prediksi.
<br>- WarehouseToHome, Jarak atau waktu dari gudang ke rumah memiliki pengaruh moderat terhadap prediksi.
<br>- Complain memiliki pengaruh yang terhadap prediksi. Dapat dilihat bahwa adanya keluhan cenderung memberikan dampak pada prediksi customer churn.
<br>- NumberOfAddress, Jumlah alamat yang terdaftar juga merupakan fitur penting. Menunjukkan bahwa memiliki pengaruh besar baik positif maupun negatif.

**Recommendation Bisnis**
1. Perusahaan membuat program loyalitas terhadap customer dengan tenure yang lama agar customer merasa dihargai oleh e-commerce.
2. Pemberian promo dalam bentuk cashback agar customer sering menggunakan e-commerce.
3. Meningkatkan proses penanganan complain dengan menyediakan fitur komunikasi yang mudah diakses atau perusahaan perlu mengevaluasi layanan terhadap penanganan complain agar jumlah complain berkurang dan mengurangi risiko churn.
4. Penyesuaian strategi promosi dengan memahami WarehouseToHome dan NumberOfAddress.

## Estimasi Keuntungan Bisnis
Berdasarkan hasil classification report dari model Random Forest model dapat memprediksi customer churn dengan akurasi 90.67% ,precision 79% dan recall 58%.

Biaya Promosi dengan Menggunakan Model
- Biaya promosi per customer = 20 USD
- Keuntungan yang diperoleh setiap kali customer yang dipromosikan no churn = 40 USD

1. Menghitung Biaya Promosi Berdasarkan Prediksi Model:
    - Biaya per promosi = 20 USD
    - Jumlah customer yang diprediksi churn = 107
    - Total biaya promosi = 107×20 USD = 2140 USD

2.	Menghitung Total Biaya Promosi Tanpa Model:
    - Jumlah total customer = 654
    - Biaya per promosi = 20 USD
    - Total biaya promosi = 654×20 USD = 13080 USD
    
Ringkasan Perbandingan Biaya Promosi
    - Dengan Model:
      <br>Total biaya promosi = 2140 USD
      <br>Promosi hanya diberikan kepada 107 customer yang diprediksi churn.
    - Tanpa Model:
      <br>Total biaya promosi = 13080 USD
      <br>Promosi diberikan kepada semua customer dengan total 654 customer tanpa mempertimbangkan kemungkinan churn.

Dengan menggunakan model, perusahaan dapat menghemat biaya promosi secara signifikan. Dalam contoh ini, penghematan yang diperoleh dengan menggunakan model adalah:
Penghematan = 13080 USD − 2140 USD = 10940 USD
Ini menunjukkan bahwa penggunaan model Random Forest tidak hanya efektif dalam memprediksi churn tetapi juga efisien dalam mengurangi biaya promosi yang dikeluarkan perusahaan.

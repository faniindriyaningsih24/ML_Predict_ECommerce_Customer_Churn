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
# Data Undersatanding
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
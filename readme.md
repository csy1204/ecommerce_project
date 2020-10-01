# [WP] E-commerce Project

> SKKU WP 2019-FALL Team Project

## 1. Pre-requisite

- python 3.7 이상
- django 2.2 이상
- DB: Sqlite3


## 2. 페이지 구성도

![KakaoTalk_Photo_2019-11-29-23-42-26](https://user-images.githubusercontent.com/18041103/69876176-45cac380-1302-11ea-9208-35e9193af422.jpeg)


## 3. 모델 구성도
![KakaoTalk_Photo_2019-11-29-23-42-29](https://user-images.githubusercontent.com/18041103/69876181-495e4a80-1302-11ea-8291-2b58e8b08ee7.jpeg)

## 4. Requirements

### Administrator Login
- [x]  1. Member List: Student ID, Password, Name, Classification (Buyer or Seller)
- [x] 2. Member Modification / Delete 

### When Seller Login
- [x] Product Registration: Product name, Price, trading place, phone number, status `/product/create`
- [x] status will be (auction / purchased completed / purchased in progress)
- [x] Seller can also go to the auction without setting a price.
- [x] **Product Modification / Product Canceled (Such as auction Closing)**
- [x] **Seller’s Product list**
- [x] Product name, number of wish applicants,
- [x] **(Auction) History of auction price and bidder**

### When buyer Login
- [x] **Product list: Seller name, Product name, Price, trading place, phone number, status**
- [x] **Product search : Search by Seller name, Product name, hope price, Multiple conditions must be combined to enable searching** `/product`
- [x] **Wish List** [GET] `/product/wish`
- [x] Product buy:  The status of the product should change when you click Buy
- [x] **(Auction) Must bid more than current price and submit**
- [x] **Shopping list: If the auction you bid is over, the amount must also be included**

### Common Page
- [x] 1. Login Page
- [x] 2. Registration Page (with user input validation)
- [x] 3. Product Page



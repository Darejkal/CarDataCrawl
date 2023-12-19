# Car price prediction
## Abstract
<!-- The recent market witnessed an increasing demand for pre-owned cars due to high inflation. People are seeing used automobiles as a viable options in terms of cost and quality. However, there are a diverse selections of brands and models for the prospect buyers to choose from that hinders their ability to make a timely and decisive decision. Meanwhile, it is a demanding task to find and select the suitable model that within the budget. Consequently, buyers need the advent of new tools to help them estimate possible price of car based on known contexts. This reports present analysis steps on car data and provide solutions for car price prediction.  -->

## Introduction
<!-- Car price prediction is an example of multivariate regression problem where several context is examined to produce an estimate of the car monetary value. -->
Lạm phát trong những năm gần đây thúc đẩy việc tiêu dùng xe ô tô đã qua sử dụng. Xe ô tô đã qua sử dụng có thể coi là 1 lựa chọn an toàn và tiết kiệm cho người mua xe, với sự lựa chọn đa dạng và phong phú. Tuy nhiên, chính sự đa dạng đó đã đặt ra thách thức trong việc định giá các sản phẩm ô tô mới, khi mà việc định giá thủ công đắt đỏ và khó có thể đáp ứng được so với nguồn cung và cầu. Về phía người tiêu dùng, nhu cầu có một hệ thống định giá xe tự động cũng rất lớn, khi mà lựa chọn đa dạng tuy nhiên ngân sách hạn chế. Nhóm đi vào tìm hiểu và phân tích các dữ liệu về xe ô tô và đưa ra mô hình định giá xe hiệu quả.
## Methodology
Nhóm tiếp cận vấn đề theo 4 bước: 

1. Thu thập dữ liệu
2. Phân tích dữ liệu
3. Xây dựng mô hình
4. Kiểm thử, xây dựng hệ thống, kết luận

## Data preparation
### Data Collection
<!-- We have collected data from online car listings Autolist and Carconnection. Our data is based on the available inventory during the period of 12/12/2023 to 14/12/2023. The data includes:
'Price', 'Trim', 'Transmission', 'Engine', 'Drivetrain', 'VIN',
'Fuel Type', 'Exterior Color', 'Interior Color', 'Condition', 'Mileage',
'Gas Mileage', 'Body Style', 'Doors', 'Cabin', 'Bed', 'Rear Wheel',
'Title' -->
Dữ liệu bao gồm data lấy từ trang web Autolist và Carconnection. Dữ liệu về 1 xe là 1 vector đa chiều bao gồm các trường:

-Price: Giá xe
-Trim: Mẫu xe
-Transmission: Hộp số
-Engine: Động cơ
-Drivetrain: Hệ thống truyền động
<!-- -VIN: ID của xe -->
-Fuel Type: Loại nguyên liệu tiêu thụ
-Exterior Color: Màu ngoại thất
-Interior Color: Màu nội thất
-Condition: Tình trạng
-Mileage: Quãng đường đã đi
-Gas Mileage: Hiệu suất gas tiêu thụ
-Body Style: Kiểu thân xe
-Doors: Số cửa xe
-Cabin: 
-Bed:
-Rear Wheel: 
-Title: Tên xe

### Data Analysis
### Feature Engineering
### Feature Selection
## Models and results analysis
## Conclusion

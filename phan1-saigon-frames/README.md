# Saigon Frames – Sổ ảnh kiến trúc Sài Gòn

Phần 1 của WDLab03: cá nhân hóa ứng dụng mẫu **PhotoNest** thành sổ ảnh kiến trúc Sài Gòn.

- Mở `index.html` bằng trình duyệt (chạy offline được, không cần server) hoặc qua XAMPP: `http://localhost/WD-Lab03/phan1-saigon-frames/`.
- Chỉ dùng HTML5 + CSS: lọc nhóm bằng radio `:checked`, thẻ chi tiết bằng `:target`, form kiểm tra bằng thuộc tính HTML rồi chuyển tới `form-result.html`.
- Form **không lưu** dữ liệu, không thêm ảnh vào thư viện.

## Cấu trúc

```
phan1-saigon-frames/
├── index.html          # header, hero, thư viện 12 ảnh, dòng thời gian, form gửi ảnh, 12 lightbox
├── form-result.html    # trang xác nhận tĩnh
├── styles.css          # toàn bộ giao diện + responsive
└── assets/
    ├── logo.svg
    └── photos/         # 12 ảnh minh họa SVG tự vẽ bằng code (tools/gen_photos.py)
```

Ảnh là hình minh họa phẳng tự vẽ, lấy cảm hứng từ các công trình ở TP.HCM; không phải ảnh chụp thật.

# Prompt tạo ảnh cho WD-Lab03

Ảnh hiện tại là **SVG tự vẽ bằng code** (`tools/gen_photos.py`): hình khối phẳng, nhìn hơi "clip-art". File này có prompt để bạn tự tạo lại ảnh bằng phần mềm (Midjourney, Firefly, DALL·E, Ideogram, Leonardo…).

Prompt viết bằng tiếng Anh vì các công cụ tạo ảnh hiểu tiếng Anh tốt nhất.

---

## 0. Quy tắc chung (đọc trước)

| Mục | Khuyến nghị |
|---|---|
| Tỉ lệ | **4:3** cho cả 12 ảnh Saigon Frames (ví dụ 1600×1200). Lightbox hiện ảnh nguyên khung, còn ô lưới sẽ **cắt bớt** (`object-fit: cover`), nên đặt chủ thể **ở giữa khung**. |
| Ô lưới | Ô *rộng* cắt thành dải ngang khoảng 2.4:1, ô *cao* cắt thành dải dọc khoảng 0.6:1. Ảnh nào là ô rộng hay ô cao được ghi ở từng prompt. |
| Định dạng | Xuất **.webp** hoặc **.jpg**, mỗi ảnh ≤ 300 KB. Giữ nguyên tên file, chỉ đổi đuôi (ví dụ `buu-dien.webp`). |
| Đồng bộ | Dùng **cùng một khối STYLE** cho cả 12 ảnh, chỉ đổi phần SUBJECT. Nếu công cụ có *seed* hoặc *style reference* thì khóa lại sau ảnh đầu tiên. |
| Cấm | Thêm vào negative prompt (hoặc cuối prompt): `no text, no letters, no watermark, no signature, no logo, no frame border`. |
| Trung thực | Ghi vào README và report: *"Ảnh minh họa tạo bằng <tên phần mềm> ngày …, prompt trong WD-Lab03-image-prompts.md; không phải ảnh chụp thật."* Đề Lab03 yêu cầu asset phải "tự tạo hoặc có nguồn rõ". |

Sau khi có ảnh, chép vào `phan1-saigon-frames/assets/photos/` và báo mình. Mình sẽ đổi toàn bộ `src`, link tải và chữ "Tải SVG" trong `index.html`.

---

## 1. Saigon Frames: chọn MỘT phong cách

Giao diện mới dùng bảng màu **Kanagawa**: nền mực tối, giấy ngà `#f2ecbc`, đỏ đèn phòng tối `#c34043`, vàng `#dca561`, xanh ngọc `#7aa89f`, xanh sóng `#223249`. Hai phong cách dưới đây đều hợp với giao diện này.

### STYLE A: Tranh khắc gỗ / risograph *(lạ mắt nhất, khớp Kanagawa vì Kanagawa lấy cảm hứng từ tranh khắc gỗ Hokusai)*

```
STYLE: Japanese ukiyo-e woodblock print meets risograph poster, limited palette of
deep ink #1f1f28, aged ivory paper #f2ecbc, muted vermilion #c34043, ochre #dca561,
sea-glass teal #7aa89f and indigo #223249. Visible paper grain, slight ink
misregistration, flat color areas with fine carved line work, calm composition,
architectural illustration, no people in focus.
```

### STYLE B: Ảnh phim 35 mm *(khớp concept "phòng tối tráng phim")*

```
STYLE: 35mm analog film photograph, Kodak Portra 400 look, soft natural grain,
gentle halation around lights, warm muted colors leaning ochre and teal, slight
vignette, documentary architectural photography, eye-level, realistic but
not hyper-sharp.
```

> Nếu chọn B, ảnh trông như ảnh chụp thật nên **bắt buộc** ghi rõ là ảnh tạo bằng AI. Ngoài ra AI có thể vẽ sai chi tiết công trình. Vì vậy prompt bên dưới chỉ mô tả "lấy cảm hứng từ", đúng như cột "Cảm hứng" trong site.

### SUBJECT cho 12 ảnh (ghép sau khối STYLE)

| # | File | Ô lưới | SUBJECT |
|---|---|---|---|
| 01 | `buu-dien` | rộng | `SUBJECT: symmetrical front facade of a French-colonial post office in Saigon, ochre-yellow walls, a row of tall arched windows, a round clock at the center of the pediment, midday sun 11:40, straight-on 24mm view.` |
| 02 | `hai-thap-chuong` | **cao** | `SUBJECT: red-brick neo-Romanesque cathedral with two slender pointed bell towers, early morning light 06:30, low camera angle so the towers soar upward, vertical composition, subject centered.` |
| 03 | `nha-hat` | thường | `SUBJECT: French-colonial municipal opera house, cream facade with a large central arched entrance glowing warm yellow, wide front steps leading the eye in, sky turning orange at 17:20.` |
| 04 | `cong-cho` | thường | `SUBJECT: old market gate with a square clock tower, morning traffic of motorbikes passing in soft motion blur at 07:15, everyday life around a 1914 landmark.` |
| 05 | `chung-cu-ca-phe` | **cao** | `SUBJECT: 1960s apartment block where every balcony is a tiny café with colorful hand-painted signboards (no readable text), repetitive floors seen straight-on, 08:00 light, vertical framing.` |
| 06 | `ban-cong-xanh` | thường | `SUBJECT: weathered 1970s canal-side apartment building, grey-green walls, plants and vines spilling from every old balcony, soft 10:10 light, calm and lived-in.` |
| 07 | `cau-thang-xoan` | **cao** | `SUBJECT: looking straight up a spiral staircase inside an old Cholon apartment light well, curved concrete steps forming rhythmic rings like wood grain, 16mm wide angle, skylight at center.` |
| 08 | `thap-ben-song` | rộng | `SUBJECT: modern glass skyscraper on a riverbank at blue hour 18:10, lit windows reflected as long streaks on the Saigon river, a small boat crossing.` *(ảnh này cũng là "Ảnh của tuần" ở hero)* |
| 09 | `thap-bup-sen` | thường | `SUBJECT: tall tower shaped like a lotus bud, tapering upward, a helipad jutting out near the top like a petal, clear noon sky 12:00, 35mm view from street level.` |
| 10 | `cau-day-vang` | rộng | `SUBJECT: single-pylon cable-stayed bridge at night 20:30, cables fanning out like a harp, bridge lights printing golden dots on dark water, wide 24mm.` |
| 11 | `hem-chieu` | rộng | `SUBJECT: narrow Saigon alley at 16:45, red paper lanterns, tangled overhead electrical wires, one motorbike passing across the frame, warm late-afternoon light.` *(cũng dùng ở cột "Mẹo chụp")* |
| 12 | `pho-di-bo` | rộng | `SUBJECT: wide pedestrian boulevard at night 21:00 leading toward an old colonial building, tiny strolling figures under street lamps, long leading lines.` |

Ví dụ một prompt hoàn chỉnh (Style A + ảnh 01):

```
Japanese ukiyo-e woodblock print meets risograph poster, limited palette of deep ink #1f1f28,
aged ivory paper #f2ecbc, muted vermilion #c34043, ochre #dca561, sea-glass teal #7aa89f and
indigo #223249. Visible paper grain, slight ink misregistration, flat color areas with fine
carved line work, calm composition, architectural illustration. Symmetrical front facade of a
French-colonial post office in Saigon, ochre-yellow walls, a row of tall arched windows, a round
clock at the center of the pediment, midday sun, straight-on view. 4:3, no text, no watermark,
no logo, no frame border.
```

Thêm tham số theo công cụ, ví dụ Midjourney: `--ar 4:3 --style raw --seed 2026`.

---

## 2. StudyDesk (concept bullet journal, bảng màu Rosé Pine Dawn)

Màu: giấy `#faf4ed`, mực `#464261`, xanh pine `#286983` (Toán), hồng love `#b4637a` (Tin), vàng gold `#ea9d34` (Đại cương), hồng nhạt `#ebbcba`.

### `desk` (ảnh hero trang tổng quan và khung "Chưa chọn học phần"): 4:3, xuất 1260×900

```
Top-down flat lay of an open dotted bullet-journal notebook on a warm cream desk #faf4ed,
weekly spread with hand-drawn boxes, washi tape strips in dusty pink #ebbcba and teal #286983,
a highlighter in amber #ea9d34, a small laptop corner, a mug, sticky notes, soft daylight,
cozy minimal illustration in gouache texture, muted palette #464261 #b4637a #286983 #ea9d34,
lots of empty space, no readable text, no watermark.
```

### Ba "sticker" biểu tượng nhóm (hình vuông 1:1, nền trong suốt, xuất PNG 256×256)

Dùng chung STYLE:
```
STYLE: die-cut journal sticker, hand-drawn doodle with slightly wobbly ink outline #464261,
flat fill, white sticker border, transparent background, centered, no text.
```

| File | SUBJECT |
|---|---|
| `toan` | `SUBJECT: a sigma symbol and a small graph curve on grid paper, main color teal #286983.` |
| `tin` | `SUBJECT: a tiny laptop showing angle brackets </>, main color dusty rose #b4637a.` |
| `dai-cuong` | `SUBJECT: a stack of two books with a bookmark ribbon, main color amber #ea9d34.` |

> `logo.svg` nên **giữ nguyên SVG**: logo cần nét gọn ở 36 px, mà ảnh AI thu nhỏ cỡ đó sẽ bị nhòe.

---

## 3. Kiểm tra sau khi thay ảnh

- [ ] Mỗi ảnh ≤ 300 KB, tổng cả thư mục photos ≤ 4 MB (site còn chạy offline và push GitHub nhẹ).
- [ ] Ô *rộng* và ô *cao* không bị cắt mất chủ thể ở 1280 px và 390 px.
- [ ] `alt` vẫn mô tả đúng ảnh mới. Sửa câu `alt` nếu bố cục khác hẳn.
- [ ] Ghi nguồn ảnh vào README và report (mục "Nội dung & assets" và Self-assessment).

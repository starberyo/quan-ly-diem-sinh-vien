import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Hiển thị tiêu đề ứng dụng web
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Chuẩn bị dữ liệu 10 sinh viên, tính điểm tổng kết và xếp loại
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [9.0, 8.5, 7.0, 9.5, 8.0, 6.0, 8.5, 7.5, 8.0, 9.0],
    'Giữa kỳ': [8.0, 7.5, 6.5, 9.0, 7.0, 5.5, 8.0, 6.0, 7.0, 9.5],
    'Cuối kỳ': [8.5, 8.0, 6.0, 8.5, 6.5, 5.0, 7.5, 6.5, 7.0, 9.0]
}
df = pd.DataFrame(data)

# Công thức tính điểm tổng kết
df['Tong_ket'] = 0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']

# Quy định xếp loại
def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 2. Hiển thị bảng điểm của 10 sinh viên (Họ tên, Chuyên cần, Giữa kỳ, Cuối kỳ, Tổng kết, Xếp loại)
st.subheader("Bảng điểm chi tiết 10 sinh viên")
st.dataframe(df)

# 3. Hiển thị điểm trung bình của lớp
st.subheader("Thống kê chung của lớp")
st.write(f"- Điểm tổng kết trung bình của lớp: **{df['Tong_ket'].mean():.2f}**")

# 4. Hiển thị sinh viên có điểm cao nhất và thấp nhất
max_score = df['Tong_ket'].max()
min_score = df['Tong_ket'].min()
sv_max = ", ".join(df[df['Tong_ket'] == max_score]['Họ và tên'].tolist())
sv_min = ", ".join(df[df['Tong_ket'] == min_score]['Họ và tên'].tolist())

st.write(f"- Sinh viên có điểm tổng kết cao nhất ({max_score:.2f}): **{sv_max}**")
st.write(f"- Sinh viên có điểm tổng kết thấp nhất ({min_score:.2f}): **{sv_min}**")

# 5. Hiển thị số sinh viên đạt (điểm tổng kết >= 5.0)
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()
st.write(f"- Số sinh viên đạt (điểm tổng kết >= 5.0): **{so_sv_dat}**")

# 6. Tạo danh sách xổ xuống (Selectbox) chọn một sinh viên
st.subheader("Tra cứu thông tin chi tiết từng sinh viên")
selected_student = st.selectbox("Chọn sinh viên muốn xem:", df['Họ và tên'])

# 7. Khi chọn sinh viên, hiển thị điểm Chuyên cần, Giữa kỳ, Cuối kỳ, Tổng kết và Xếp loại của sinh viên đó
student_info = df[df['Họ và tên'] == selected_student].iloc[0]
st.info(f"""
- **Họ và tên:** {student_info['Họ và tên']}
- **Điểm Chuyên cần:** {student_info['Chuyên cần']}
- **Điểm Giữa kỳ:** {student_info['Giữa kỳ']}
- **Điểm Cuối kỳ:** {student_info['Cuối kỳ']}
- **Điểm Tổng kết:** {student_info['Tong_ket']:.2f}
- **Xếp loại:** {student_info['Xep_loai']}
""")

# 8. Hiển thị biểu đồ cột điểm tổng kết của 10 sinh viên
st.subheader("Biểu đồ cột điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Họ và tên'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Họ và tên')
ax.set_xlim(0, 10)
st.pyplot(fig)

# 9. Hiển thị họ tên và MSSV ở cuối trang Web App với kích thước chữ nhỏ (Nhớ thay thông tin của bạn vào đây)
st.markdown("---")
st.caption("Người thực hiện: Trần Minh Hằng - MSSV: 036308013108")

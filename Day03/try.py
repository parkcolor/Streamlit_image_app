import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
from datetime import datetime
import os


def load_image(image_file): #이미지 파일 불러오기
    img = Image.open(image_file)
    return img

# 디렉토리와 이미지을 주면, 해당 디렉토리에 이 이미지을 저장하는 함수
def save_uploaded_file(directory, img):
    if not os.path.exists(directory) :    
        os.makedirs(directory)
 
   # 2. 디렉토리가 원래 있거나 생겼으므로, 이미지를 저장
    filename = datetime.now().isoformat().replace(':','-').replace('.','-')
    img.save(directory + '/' + filename + '.jpg')
    return st.success('Saved image : {} in {}'.format(filename+'.jpg', directory))
 
 
def main():
    
    image_file_list = st.file_uploader('이미지 파일들 업로드', type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
    cnt=0

    if image_file_list is not None :
        # 2.  각 파일을 이미지로 바꿔줘야 한다
        image_list = []

        #2-1. 모든 파일이 image_list에 이미지로 저장됨
        for image_file in image_file_list :
            img = load_image(image_file)
            image_list.append(img)

        # 3. 이미지를 화면에 출력해본다
        for img in image_list :
            st.image(img)

        option_list = ['Show Image', 'Rotate Image', 'Create Thumbnail',
                    'Crop Image', 'Merge Image', 'Flip Image', 'Black & White',
                    'Filters - Sharpen', 'Filter - Edge Enhance', 'Contrast Image']

        option = st.selectbox('옵션을 선택하세요', option_list)

        # 하드코딩을 소프트 코딩으로 바꿔주자
        if option == 'Show Image':
            for img in image_list:
                st.image(img)

            directory = st.text_input('파일경로 입력')
            if st.button('파일 저장'):
                for img in image_list:
                    save_uploaded_file(directory,img)
                
        elif option == 'Rotate Image':
            #1. 유저가 입력
            rot_size = st.number_input('각도 입력(1 ~ 360)', 0, 360)
            #2. 모든 이미지를 돌린다
            transformed_img_list = []
            for img in image_list:
                rotated_img = img.rotate(rot_size)
                st.image(rotated_img)
                transformed_img_list.append(rotated_img)

            directory = st.text_input('파일경로 입력')
            if st.button('파일 저장'):
                #3. 파일저장.
                for img in transformed_img_list :
                    save_uploaded_file(directory,img)
            
        elif option == 'Create Thumbnail':
            #1. 이미지 사이즈를 확인한다
            width = st.number_input('x축 크기 입력', 1,)
            height = st.number_input('y축 크기 입력', 1,)

            size=(width, height)

            transformed_img_list = []

            for img in image_list :
                thumb_img = img.thumbnail(size)
                st.image(img)
                transformed_img_list.append(img)
                        
            directory = st.text_input('파일경로 입력')
            if st.button('파일 저장'):
                for img in transformed_img_list:
                    save_uploaded_file(directory,img)

#         elif option == 'Crop Image':
#             save_button = st.button('저장하시겠습니까?', key=cnt)
#             cnt = cnt + 1

#             x_start = st.number_input('시작 x값 입력', 0, img.size[0])
#             y_start = st.number_input('시작 y값 입력', 0, img.size[1])
#             x_last = st.number_input('x 사이즈 입력', 1, img.size[0])
#             y_last = st.number_input('y 사이즈 입력', 1, img.size[1])

#             max_width = img.size[0] - x_start
#             max_height = img.size[1] - y_start  
 
#             if max_width > 0 and max_height > 0 :
#                 box = (x_start,y_start,x_last,y_last)

#                 for img_file in uploaded_files:
#                     st.write(img.size)
#                     img = Image.open(img_file)
#                     cropped_img = img.crop(box)
#                     st.image(cropped_img)                

#                     if save_button :
#                         save_uploaded_file('Processed images', img_file)

#         elif option == 'Merge Image':
#             merge_file = st.file_uploader('Upload merge image',
#                                              type=['png', 'jpg', 'jpeg'], key='merge')

#             if merge_file is not None:
#                 new_img = Image.open(merge_file)
#                 st.write(img.size)
#                 st.write(new_img.size)

#                 x_start = st.number_input('시작 x값 입력', 0, img.size[0])
#                 y_start = st.number_input('시작 y값 입력', 0, img.size[1])
#                 position = ( x_start, y_start )
#                 img.paste(new_img, position)
#                 st.image(img)

        elif option == 'Flip Image':                
            flip_list = ['FLIP_LEFT_RIGHT', 'FLIP_TOP_BOTTOM']
            flip_sel = st.radio('플립 선택', flip_list)
            # flip_sel = st.selectbox('옵션을 선택하세요', flip_list)

            if flip_sel == 'FLIP_LEFT_RIGHT':
                transformed_img_list = []
                for img in image_list:
                    flipped_img = img.transpose( Image.FLIP_LEFT_RIGHT )
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)

            elif flip_sel == 'FLIP_TOP_BOTTOM':
                transformed_img_list = []
                for img in image_list:
                    flipped_img = img.transpose( Image.FLIP_TOP_BOTTOM )
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)
            
            directory = st.text_input('파일경로 입력')
            if st.button('파일 저장'):
                for img in transformed_img_list:
                    save_uploaded_file(directory,img)

#         elif option == 'Change Color':
#             color_list = ['Black & White', 'Gray', 'Color']
#             status = st.radio('옵션을 선택하세요', color_list)
#             if status == 'Black & White':
#                 color = '1'
#             elif status == 'Gray':
#                 color = 'L'
#             elif status == 'Color':
#                 color = 'RGB'
#             color_img = img.convert(color)
#             st.image(color_img)

#         elif option == 'Filters - Sharpen':
#             sharp_img = img.filter(ImageFilter.SHARPEN)
#             st.image(sharp_img)

#         elif option == 'Filter - Edge Enhance':
#             edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
#             st.image(edge_img)

#         elif option == 'Contrast Image':
#             contrast_img = ImageEnhance.Contrast(img).enhance(2)
#             st.image(contrast_img)


# # 이미지를 선택해서 올리기. 1장. (여러장은 다음에.)

# # rotate image를 할 경우 숫자 입력창 나와서 값 입력하도록. 그에맞게 rotate.

# # 썸네일 크기도 지정하기! 이미지 사이즈 보여주기 -> 입력값 4개 받기.

# # black white도 그레이컬러, bw, 등.

# # -> 하드코딩된 코드를, 유저에게 입력받아 처리할 수 있도록 만든다.

 

# # 여러파일을 변환할 수 있도록 수정.

# # 각 옵션마다 저장하기버튼이 있어서, 버튼 누르면 저장하도록.

# # 저장시에는 디렉토리 이름을 유저가 직접 입력해서 저장. (이름이 없으면 만들어서 하기?)

 

if __name__ == '__main__':

    main()
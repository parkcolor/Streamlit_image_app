import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import pandas as pd
from PyPDF2 import PdfFileReader # pdf파일 읽어오는 라이브러리
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') #서버에서 화면에 표시하기 위해서 필요
import seaborn as sns

# 깃연동



def main():
    
    img = st.file_uploader('Upload Image', type=['png','jpg','jpeg'])
    
    if img is not None :
        img = Image.open(img)
        st.image(img)
        option_list = ['-------------','Show Image','Rotate Image',
        'Create Thumbnail','Crop Image','Merge Images',
        'Flip Image','Change Color','Filters -Sharpen','Filters - Edge Enhance',
        'Contrast Image']
        option = st.selectbox('옵션을 선택하세요',option_list)

        if option == 'Show Image' :
            st.image(img)
    
        elif option == 'Rotate Image' :
            user_input = st.number_input('회전각도 입력 : ',1,360)
            rotated_img = img.rotate(user_input)
            st.image(rotated_img)
    
        elif option == 'Create Thumbnail' :
            width = st.number_input('가로사이즈 입력',1,640)
            height = st.number_input('세로사이즈 입력',1,427)
            size = (width, height)
            img.thumbnail(size)
            # img.save('data/thumb.jpg')
            st.image(img)

        elif option == 'Crop Image':
            #좌측상단부터 너비와 깊이만큼 자른다
            #좌측상단 좌표(50 ,100)
            #너비 x축, 깊이 y축(200,200)
            start_x = st.number_input('가로 시작값',0,img.size[0]-1)
            start_y = st.number_input('세로 시작값',0,img.size[1]-1)

            max_width = img.size[0] - start_x
            max_height = img.size[1] - start_y

            width = st.number_input('가로 크기',1,max_width)
            height = st.number_input('세로 크기',1,max_height)

            box = (start_x , start_y , start_x + width , start_y + height)
            cropped_img = img.crop(box)
            # cropped_img.save('data/crop.png')
            if (start_x * start_y * width * height) >1 :
                st.image(cropped_img)
        
        elif option == 'Merge Images':
            merge_file = st.file_uploader('Upload Image', type=['png','jpg','jpeg'],key='merge')
            
            if merge_file is not None :

                merge_img = Image.open(merge_file)

                start_x = st.number_input('x값',0,img.size[0]-1)
                start_y = st.number_input('y값',0,img.size[1]-1)

                position = (start_x,start_y)
                img.paste(merge_img,position)
                st.image(img)

        elif option == 'Flip Image':
            status = st.radio('정렬을 선택하세요', ['좌우반전','상하반전'])
            if status == '좌우반전':
                flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                st.image(flipped_img)
            else :
                flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
                st.image(flipped_img)
            

        elif option == 'Change Color':
            
            if st.checkbox('흑백적용'):
                bw = img.convert('L')
                st.image(bw)
            else :
                st.image(img)    

        elif option == 'Filters -Sharpen':
            sharp_img = img.filter(ImageFilter.SHARPEN)
            st.image(sharp_img)
        
        elif option == 'Filters - Edge Enhance':
            edg_img = img.filter(ImageFilter.EDGE_ENHANCE)
            st.image(edg_img)
        
        elif option == 'Contrast Image':
            user_input = st.number_input('콘트라스트값 입력',0,)
            con_img = ImageEnhance.Contrast(img).enhance(user_input)
            st.image(con_img)

        # 1. 이미지를 탑재할 수 있도록 한다
        # 2. rotate 이미지를 유저가 원하는대로 설정하라
        # 3. 썸네일 사이즈를 원하는대로 설정가능토록 코딩



if __name__ == '__main__':
    main()
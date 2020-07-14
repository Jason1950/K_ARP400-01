def gamma_trans(img, gamma):  # gamma函数处理
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img, gamma_table) 

def feature_gamma_fix_byqq(img, gamma_val):
    image_gamma_correct = gamma_trans(img, gamma_val)   # gamma变换
    return image_gamma_correct

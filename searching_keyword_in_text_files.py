import os



def text_file_split_lo_list_function(inp_file_linc:str) -> list:
    """ 
    Функція перетворення вхідного файлу на список \n
    param: `inp_lists_file_linc` \n
    Читає файл, та перетворює його на список. 
    """
    try:
        with open(inp_file_linc, "r", encoding="utf-8") as file1:
            read_file = str("".join(file1.read())).split("\n")
            res_read_f = []
            for split_nline in read_file:
                spl_lis_word = split_nline.split(" ")
                
                for sp_lw in spl_lis_word:
                    sp_lw = sp_lw.strip(",.:;()= \n\t").lower()
                    res_read_f.append(sp_lw)
            
            return res_read_f
        
    except: return f"Невірний шлях до файлу"




def read_contents_directory(directory:str, extension=".txt") -> list:
    """
    Читає вміст папки та повертає список файлів з вказаним розширенням.
    param: `directory` Шлях до папки.
    param: `extension` Розширення файлу (наприклад, ".txt").
    """
    if not os.path.isdir(directory):
        print("Вказана папка не існує.")
        return []
    
    res_ls_files = []
    for fls in os.listdir(directory):
        if not fls.endswith(extension):
            pass
        else:
            res_ls_files.append(directory+"\\"+fls)
    
    if not res_ls_files:
        print(f"Файли з розширенням {extension} відсутні")
        return []
    else: return res_ls_files



def func_found_in_match(inp_path_directory:str, inp_list_keywords:list[str]) -> dict:
    """ 
    Шукає співпадіння в файлах папки яку вказано, \n
    зі списком ключових слів. \n
    param: `inp_path_directory` Вхідна папка з файлами .txt \n
    param: `inp_list_keywords` Список слів для пошуку в файлах \n
    Повертає словник з всіма співпадіннями в файлах.
    """
    res_dict = {}
    files_list = read_contents_directory(inp_path_directory)
    
    for fl_ls in files_list:
        ls_buf = []
        list_words = text_file_split_lo_list_function(fl_ls)
        for key_wd in list_words:
            for sea_w in inp_list_keywords:
                if sea_w == key_wd:
                    ls_buf.append(key_wd)
        res_dict[fl_ls] = ls_buf
        
    return res_dict



from collections import Counter
def func_search_coincid_words_with_count(path_directory:str, list_keywords:list[str]) -> str:
    dict_coincidence = func_found_in_match(path_directory, list_keywords)
    if not dict_coincidence:
        return "Невірний шлях до папки"
    elif dict_coincidence: 
        retr_search = ""
        retr_search += f"Список слів для пошуку: {str(list_keywords)} \n"
        retr_search += f"Папка для пошуку: {path_directory} \n"
        
        for d_cons in dict_coincidence:
            count_rs = dict(Counter(dict_coincidence[d_cons]))
            retr_search += d_cons + ": "
            
            for rfs in count_rs:
                retr_search += f"({rfs}, {str(count_rs[rfs])}) "
            
            retr_search += "\n"
        return retr_search

# list_keyw = ["цифра", "програми", "windows", "python"] # Ключові слова для пошуку
# print(func_search_coincid_words_with_count("C:\\Users\\A1\\Desktop\\WOOLF\\Computer_Systems_and_Their_Fundamentals\\HomeWork\\cs-hw-04\\Files2", list_keyw))



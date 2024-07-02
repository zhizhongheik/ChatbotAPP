# ChatbotAPP
A chatbot trained with tensorflow, easy to install and operate. Artificial Intelligence Application
based on Generative Language Model.

## Introduction
In this project, I will introduce the chatbot, including how to install it, how to use it, and the problems you may encounter and their solutions. The software I use is Anaconda, and most of the libraries are installed using conda. Of course, you can also use pip, which is fine.

##  Use and Install

After downloading all the files, open the local cmd, use the cd command to adjust to the folder, then open the chatbot_main file to change the intents file path, and then install the libraries included in the requirements (pip install -r requirements.txt), run the run.py file, and see if it can run. If it can run, use pyinstaller to package the run.spec file (pyinstaller run.spec), and then you can find the run.exe file in the generated dist file to run the application.

## Problems

1. nltk : 
No model "nltk" , but you use conda or pip to confirm that it has been installed. The solution is as follows: Go to (https://github.com/nltk/nltk_data) to download the packages file. There are ten files in this package,
<img width="678" alt="c96251376ca67bba07f89fbceaf291e" src="https://github.com/zhizhongheik/ChatbotAPP/assets/136669816/5c45e515-c233-4bc7-aad4-13edb203972b">

each of which has an unzip package. Unzip them all. Here, take one of the files as an example: <img width="351" alt="ebe86969883c1969a8a0c999f619538" src="https://github.com/zhizhongheik/ChatbotAPP/assets/136669816/45e71e47-cb4c-48e0-9fe9-4fb843d1c11f">

After all the compressed packages are unzipped, return to the packages folder, select all the files (a total of ten) and put them into the nltk file. Here, take conda as an example. The general path is YOUR_Env\.conda\Lib\site-packages\nltk. So far, you may have solved the problem. (In China, you can use `pip install nltk -i https://pypi.tuna.tsinghua.edu.cn/simple` to download very quickly).

2. numpy ：
In this project, I use Python 3.8. If your numpy version is too high, you will get an error because some parts of the code use np.object to call numpy, but numpy has deleted this method in versions 1.20 and later. So make sure that the numpy version is below 1.20. Here I use numpy==1.18.5

3. pyinstaller : 
After you call this function and package the project, if you click on the exe file in dist and it fails to run, you can try to run it as an administrator. Of course, this is my solution. 
If you have other problems, you might as well try these: Make sure your parent and child files do not have the same name, and there are functions in the .py file that are not used. Check if there is a problem with the data. You can use the local cmd to run this file to view the cause of the error.

## References

Valderrama Jonatan, Aguilar-Alonso Igor, Creation Of A ChatBot Based On Natural Language Proccesing For Whatsapp, (URL: https://arxiv.org/abs/2310.10675)

Canziani A. , Paszke A. , Culurciello E. , “an Analysis of Deep Neural Network Models for Practical Applications” (URL: https://arxiv.org/abs/1605.07678)


The following references are in no particular order, if my description of some problem was not clear enough I will also put the reference where I found the solution to the problem：

Kanisa7, chat, https://github.com/Kanisa7/Chat/blob/main/chatbot.ipynb

yezhizhenya, Problems encountered when installing nltk, https://www.cnblogs.com/liweikuan/p/13898893.html (chinese)

wskuge, Manually install Python NLTK language package, https://blog.csdn.net/wskuge/article/details/103287044?utm_source=app (chinese)

Mohdsanadzakirizvi, Build your own Language Model in Python, https://medium.com/analytics-vidhya/how-to-build-your-first-desktop-application-in-python-7568c7d74311

Ampofo Amoh - Gyebi, How to build your first Desktop Application in Python, https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-language-model-nlp-python-code/

moxinggeiwopaoqilaiya, [Bug修改]‘NoneType’ object has no attribute ‘flush‘, https://blog.csdn.net/2301_79656701/article/details/139096545(chinese)

nengbianshoudemoqiaoli, python使用Pyinstaller打包整个项目, https://blog.csdn.net/Rebacca122222/article/details/124440089?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-124440089-blog-137784557.235^v43^pc_blog_bottom_relevance_base2&spm=1001.2101.3001.4242.2&utm_relevant_index=2(chinese)

qketanghentian, pyinstaller工具打包python项目详细教程, https://blog.csdn.net/weixin_45863084/article/details/137784557(chinese)

## nltk download link 

https://github.com/nltk/nltk_data

https://github.com/nltk/nltk/tree/develop

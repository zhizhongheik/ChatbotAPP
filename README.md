# ChatbotAPP
A chatbot trained with tensorflow, easy to install and operate. Artificial Intelligence Application
based on Generative Language Model.

## Introduction
In this project, I will introduce the chatbot, including how to install it, how to use it, and the problems you may encounter and their solutions. The software I use is Anaconda, and most of the libraries are installed using conda. Of course, you can also use pip, which is fine.

##  Use and Install

Click the chatbot_main.exe file in the dist file to use it.
If you want to learn how to create this application, you can follow these steps: First you can use the command `pip install -r requirements.txt` to install the required libraries.(If you have problems at this step, you may be able to find solutions from the following Problems.) And download .zip file unzip it. After you need to change your pth address to correspond to the address of the intents.json file. Because the pyinstaller file is already in the requirements.txt file, you can directly use the command `pyinstaller -F chatbot_main.ipynb` to package this project. Please make sure that you have installed this library. You can use conda list or pip list to check.

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

Valderrama Jonatan, Aguilar-Alonso Igor, Creation Of A ChatBot Based On Natural Language Proccesing For Whatsapp, [https://www.researchgate.net/publication/333253943_Simultaneous_skin_friction_and_velocity_measurements_in_high_Reynolds_number_pipe_and_boundary_layer_flows](https://arxiv.org/abs/2310.10675)

The following references are in no particular order, if my description of some problem was not clear enough I will also put the reference where I found the solution to the problem：

Kanisa7, chat, https://github.com/Kanisa7/Chat/blob/main/chatbot.ipynb

yezhizhenya, Problems encountered when installing nltk, https://www.cnblogs.com/liweikuan/p/13898893.html (chinese)

wskuge, Manually install Python NLTK language package, https://blog.csdn.net/wskuge/article/details/103287044?utm_source=app (chinese)

Mohdsanadzakirizvi, Build your own Language Model in Python, https://medium.com/analytics-vidhya/how-to-build-your-first-desktop-application-in-python-7568c7d74311

Ampofo Amoh - Gyebi, How to build your first Desktop Application in Python, https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-language-model-nlp-python-code/

## nltk download link 

https://github.com/nltk/nltk_data

https://github.com/nltk/nltk/tree/develop

                                                       MULTIPLE IMPUTATION USING DENOISING AUTOENCODERS:
there are 3 types of datasets: numerical, categorical and, numerical+categorical.
each of the dataset is preinduced with missingness. the project is to impute missing values in the data and make a comparision with original data(completed

Procedure to install all the necessary softwares/packages to run the code successfully:

			Prerequisites (Windows/Mac):

1.	Anaconda Navigator (version)
2.	Jupyter Notebook(version)
3.	Python (version)
4.	Libraries (pandas, Tensorflow, MIDASpy, math, numpy, sklearn)


			Installation process:

1.	Install the Anaconda Navigator for Windows/Mac from the official website [https://docs.anaconda.com/anaconda/navigator/index.html]
2.	In the Anaconda Navigator, install Jupyter Notebook (it should be preinstalled with the Anaconda Navigator. If not, click on the install Jupyter Notebook)
3.	Python (version 3.8) installation ( Python gets installed along with the Anaconda Navigator)
4.	In the jupyter notebook, install the necessary libraries (pandas, Tensorflow, MIDASpy, math, numpy, sklearn, matplotlib) using “pip” function

			Library packages installations:

Use the following commands on the Jupter notebook or in the CMD.exe Prompt from the Anaconda Navigator
1. 	pandas: pip install pandas
2. 	Tensorflow: !pip(or pip) install tensorflow 
3. 	sklearn: pip install scikit-learn
4. 	numpy, math: will be installed witht he python
5. 	matplotlib: pip install matplotlib
6.	statmodels" pip install statsmodels
7.	scipy: pip install scipy
8.	MIDASpy: pip install MIDASpy

Note: If you are using anaconda navigator's CMD.exe prompt, then use 'conda' instead of 'pip' in the above commands (recommended for ease of installation).


Note: Import all the aforementioned libraries in the jupyter notebook using ‘import’ statement. MIDASpy package is the heart of the project

Note: This zip file contains this readme.txt file along with the program codes for EACH dataset in different folders. There is no need to edit any hyperparameters from the program.
          You HAVE TO edit the root location of the dataset (for the incomplete dataset as well the complete dataset) in the program instead of the one already present in the code. 
          There are two lines in the code where you should edit this (one for incomplete and another for complete dataset)

Note: Incase you cannot open the .IPYNB file(the Jupyter Notebook program code) directly, open the Anaconda Navigator (in Windows OS, use the search icon in the taskbar and type 
          Anaconda Navigator) and then hover over to Jupyter Notebook and click it. You will be redirected to the Notebook home page. 
          Click on the upload button and browse for the .IPYNB and upload it. On the home page, you will find the .IPYNB file, double click it to opn the program code.

Note: To run the whole code, hover to 'Cells', and click on 'Run All'. To run each line, click on the first line of the code and press SHIFT+ENTER at the same time to run the respective line of the code.    
      

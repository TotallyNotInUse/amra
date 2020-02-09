from imageai.Prediction.Custom import CustomImagePrediction
import os, fnmatch, re, sys
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as msgbox

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

execution_path = os.getcwd()
prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(resource_path("recogModel_v3_92.h5"))
prediction.setJsonPath(resource_path("model_class.json"))
prediction.loadModel(num_objects=5)

def idenDir():
	msgbox.showinfo("Prompt", "Currently not available.")
	'''imgFiles = fnmatch.filter(os.listdir('.'), '*.jpg')
	identifiedFiles = []
	for file in imgFiles:
		predictions, probabilities = prediction.predictImage(filename, result_count=3)
		print("---------------------------------------")
		identifiedFiles.append("-------------------------------------------")
		print(filename)
		identifiedFiles.append(filename)
		for eachPrediction, eachProbability in zip(predictions, probabilities):
			print(eachPrediction , " : " , eachProbability)
			identifiedFiles.append(eachPrediction , ":" , eachProbability)'''

def idenImage():
	fileOut.config(state="normal")
	perOut.config(state="normal")
	verdictOut.config(state="normal")
	fileOut.delete(0, 	END)
	perOut.delete(0, END)
	verdictOut.delete(0, END)
	fileOut.config(state="readonly")
	perOut.config(state="readonly")
	verdictOut.config(state="readonly")
	file = askopenfilename()
	predictions, probabilities = prediction.predictImage(file, result_count=2)
	fileOut.config(state="normal")
	fileOut.insert(0 ,file)
	fileOut.config(state="readonly")
	print("---------------------------------------")
	print(file)
	listd = []
	for eachPrediction, eachProbability in zip(predictions, probabilities):
		listd.append(eachPrediction)
		perOut.config(state="normal")
		perOut.insert(0 ,(eachPrediction , ":" , eachProbability))
		perOut.config(state="readonly")
		print(eachPrediction , ":" , eachProbability)
	verdictOut.config(state="normal")
	verdictOut.insert(0, ("This is a "+listd[0]))
	verdictOut.config(state="readonly")



root = Tk()
root.geometry("420x300")
root.title("A.M.R.A.")
Label(root, text="AI Meme Recognition Algorithm", font=30, bg="green", fg="white").pack(fill="both")
Label(root, text="Made by TotallyNotInUse").pack()
lf = LabelFrame(root, text="Output values")
lf.pack(fill="both", expand="yes")
Label(lf, text="File:").pack()
fileOut = Entry(lf, width=60, state="readonly")
fileOut.pack()
Label(lf, text="Percentages:").pack()
perOut = Entry(lf, width=60, state="readonly")
perOut.pack()
Label(lf, text="Verdict:").pack()
verdictOut = Entry(lf, width=60, state="readonly")
verdictOut.pack()
Button(text="Identify current directory", command=idenDir).pack(side="bottom", fill="both")
Button(text="Identify image", command=idenImage).pack(side="bottom", fill="both")
Label(text="Version: 1.0, Datamodel: recogModel_v3_92").pack()
#root.withdraw()
root.mainloop()


'''

'''

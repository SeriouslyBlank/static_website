import os 
import shutil




def source_dir_to_desig_dir():
	if os.path.exists("public"):
		shutil.rmtree("public")
		os.mkdir("public")
	else:
		os.mkdir("public")

	static_dir = [f for f in os.listdir(".") if not f.startswith(".")]
	static_dir.remove("public")

	for item in static_dir:
		if os.path.isdir(item) == True:
			os.mkdir(f"public/{item}")
			item_dir = [f for f in os.listdir(item) if not f.startswith("__")]
			for item_2 in item_dir:
				if os.path.isdir(f"{item}/{item_2}"):
					os.mkdir(f"public/{item}/{item_2}")
				else:
					shutil.copy(f"{item}/{item_2}", f"public/{item}/")

		else:
			shutil.copy(f"{item}", f"public/")


	


source_dir_to_desig_dir()
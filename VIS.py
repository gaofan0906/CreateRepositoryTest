import h2o
import subprocess
from IPython.display import Image

h2o.init()

# df = h2o.import_file('https://raw.githubusercontent.com/h2oai/sparkling-water/master/examples/smalldata/prostate.csv')
df = h2o.load_dataset("prostate.csv")
y = 'CAPSULE'
x = df.col_names
x.remove(y)

df[y] = df[y].asfactor()
train, valid, test = df.split_frame(ratios=[.8, .1])



from h2o.estimators.gbm import H2OGradientBoostingEstimator

gbm_cv3 = H2OGradientBoostingEstimator(nfolds=3)
gbm_cv3.train(x=x, y=y, training_frame=train)
## Getting all cross validated models
all_models = gbm_cv3.cross_validation_models()
print("Total cross validation models: " + str(len(all_models)))

mojo_file_name = "./my_gbm_mojo.zip"

h2o_jar_path = '/Users/gaofan/Desktop/7-8/h2o_test/h2o.jar'

mojo_full_path = mojo_file_name
gv_file_path = "./my_gbm_graph.gv"

image_file_name = "./my_gbm_tree"

gbm_cv3.download_mojo(mojo_file_name)


def generateTree(h2o_jar_path, mojo_full_path, gv_file_path, image_file_path, tree_id=0):
    image_file_path = image_file_path + "_" + str(tree_id) + ".png"
    result = subprocess.call(
        ["java", "-cp", h2o_jar_path, "hex.genmodel.tools.PrintMojo", "--tree", str(tree_id), "-i", mojo_full_path,
         "-o", gv_file_path], shell=False)
    result = subprocess.call(["ls", gv_file_path], shell=False)
    if result is 0:
        print("Success: Graphviz file " + gv_file_path + " is generated.")
    else:
        print("Error: Graphviz file " + gv_file_path + " could not be generated.")


def generateTreeImage(gv_file_path, image_file_path, tree_id):
    image_file_path = image_file_path + "_" + str(tree_id) + ".png"
    result = subprocess.call(["dot", "-Tpng", gv_file_path, "-o", image_file_path], shell=False)
    result = subprocess.call(["ls", image_file_path], shell=False)
    if result is 0:
        print("Success: Image File " + image_file_path + " is generated.")
        print("Now you can execute the follow line as-it-is to see the tree graph:")
        print("Image(filename='" + image_file_path + "\')")
    else:
        print("Error: Image file " + image_file_path + " could not be generated.")


#Just change the tree id in the function below to get which particular tree you want
generateTree(h2o_jar_path, mojo_full_path, gv_file_path, image_file_name, 3)


generateTreeImage(gv_file_path, image_file_name, 0)
# Note: If this step hangs, you can look at "dot" active process in osx and try killing it


# Just pass the Tree Image file name depending on your tree
# Image(filename='./my_gbm_tree_0.png')


# Just pass the Tree Image file name depending on your tree
# Image(filename='./my_gbm_tree_3.png')

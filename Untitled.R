library(h2o)
h2o.init(nthreads=-1)
path <- system.file("extdata", "prostate.csv", package="h2o")
h2o_df <- h2o.importFile(path)
h2o_df$CAPSULE <- as.factor(h2o_df$CAPSULE)
model <- h2o.gbm(y="CAPSULE",
                 x=c("AGE", "RACE", "PSA", "GLEASON"),
                 training_frame=h2o_df,
                 distribution="bernoulli",
                 ntrees=100,
                 max_depth=4,
                 learn_rate=0.1)
modelfile <- h2o.download_mojo(model, path="./experiments/", get_genmodel_jar=TRUE)
print("Model saved to " + modelfile)